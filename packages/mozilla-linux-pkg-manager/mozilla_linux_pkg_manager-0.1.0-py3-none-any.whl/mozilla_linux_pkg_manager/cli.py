import argparse
import asyncio
import logging
from datetime import datetime, timedelta
from pprint import pformat
from urllib.parse import urljoin

import aiohttp
import yaml
from mozilla_version.gecko import GeckoVersion

logging.basicConfig(
    format="%(asctime)s - mozilla-linux-pkg-manager - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch data: HTTP Status {response.status}")

            content = await response.text()
            return content


def parse_key_value_block(block):
    package = {}
    for line in block.split("\n"):
        if line:
            key, value = line.split(": ", 1)
            package[key.strip()] = value.strip()
            if key == "Version":
                version, postfix = value.split("~")
                package["Gecko-Version"] = GeckoVersion.parse(version)
                if package["Gecko-Version"].is_nightly:
                    package["Build-ID"] = postfix
                    package["Moz-Build-Date"] = datetime.strptime(
                        package["Build-ID"], "%Y%m%d%H%M%S"
                    )
                else:
                    package["Build-Number"] = postfix[len("build") :]
    return package


async def delete_nightly_versions(retention_days):
    url = "https://packages.mozilla.org/apt/dists/mozilla"
    normalized_url = f"{url}/" if not url.endswith("/") else url
    release_url = urljoin(normalized_url, "Release")
    try:
        raw_release_data = await fetch_url(release_url)
        parsed_release_data = yaml.safe_load(raw_release_data)
        logging.info(f"parsed_release_data:\n{pformat(parsed_release_data)}")
        architectures = parsed_release_data["Architectures"].split()
        package_data_promises = []
        for architecture in architectures:
            pkg_url = f"{normalized_url}main/binary-{architecture}/Packages"
            package_data_promises.append(fetch_url(pkg_url))
        package_data_results = await asyncio.gather(*package_data_promises)
        package_data = []
        for architecture, package_data_result in zip(
            architectures, package_data_results
        ):
            parsed_package_data = [
                parse_key_value_block(raw_package_data)
                for raw_package_data in package_data_result.split("\n\n")
            ]
            package_data.extend(parsed_package_data)
        nightly_package_data = [
            package for package in package_data if package["Gecko-Version"].is_nightly
        ]
        now = datetime.now()
        expired_nightly_packages = [
            package
            for package in nightly_package_data
            if now - package["Moz-Build-Date"] > timedelta(days=retention_days)
        ]
        logging.info(
            f"Found {format(len(expired_nightly_packages), ',')} expired nightly packages. Keeping {format(len(nightly_package_data) - len(expired_nightly_packages), ',')} nightly packages created < {retention_days} days ago"
        )
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="mozilla-linux-pkg-manager")
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help='Sub-commands (currently only "clean-up" is supported)',
    )

    # Subparser for the 'clean-up' command
    clean_up_parser = subparsers.add_parser(
        "clean-up", help="Clean up package versions."
    )
    clean_up_parser.add_argument(
        "--product",
        type=str,
        help="Product in the packages (i.e. firefox)",
        required=True,
    )
    clean_up_parser.add_argument(
        "--channel",
        type=str,
        help="Channel of the packages (e.g. nightly, release, beta)",
        required=True,
    )
    clean_up_parser.add_argument(
        "--retention-days",
        type=int,
        help="Retention period in days for packages in the nightly channel",
    )

    args = parser.parse_args()

    if args.command == "clean-up":
        if args.product != "firefox":
            raise ValueError("firefox is the only supported product")
        if args.channel == "nightly":
            if args.retention_days is None:
                raise ValueError(
                    "Retention days must be specified for the nightly channel"
                )
            asyncio.run(delete_nightly_versions(args.retention_days))
        else:
            raise ValueError("Only the nightly channel is supported")
