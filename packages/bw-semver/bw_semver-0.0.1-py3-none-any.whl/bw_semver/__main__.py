import argparse
import os
from functools import cache
from pathlib import Path

import packaging
import tomllib
from packaging.version import Version
from pypi_simple import PyPISimple
from setuptools.build_meta import Distribution


@cache
def _resolve_version() -> Version:
    with Path("pyproject.toml").open("rb") as pyproject_file:
        pyproject_data = tomllib.load(pyproject_file)
        config = pyproject_data.get("tool", {}).get("bw-semver")
        if config is None:
            msg = "[tool.bw-semver] missing from pyproject.toml"
            raise RuntimeError(msg)

        minor_version = config.get("minor-version")
        if minor_version is None:
            msg = "minor-version missing from [tool.bw-semver]"
            raise RuntimeError(msg)

        target_file_name = config.get("target-file")
        if target_file_name is None:
            msg = "target-file missing from [tool.bw-semver]"
            raise RuntimeError(msg)

        pypi_endpoint = config.get("pypi-endpoint")
        if pypi_endpoint is None:
            msg = "pypi_endpoint missing from [tool.bw-semver]"
            raise RuntimeError(msg)

        project_name = pyproject_data.get("project", {}).get("name")
        if project_name is None:
            msg = "project name missing from pyproject.toml"
            raise RuntimeError(msg)

        print("[bw-semver] Project name:", project_name)
        print("[bw-semver] Configured minor version:", minor_version)
        print("[bw-semver] Querying from", pypi_endpoint)
        next_version = get_next_version(
            project=project_name,
            current_minor_version=minor_version,
            pypi_endpoint=pypi_endpoint,
            pre_releases_ok=os.getenv("BW_SEMVER_PRE_VERSION", "0") == "1",
        )
        print("[bw-semver] Next version:", next_version)
        Path(target_file_name).write_text(str(next_version))
        print("[bw-semver] Written to file:", target_file_name)
        return next_version


def get_next_version(
    project: str,
    current_minor_version: str,
    pypi_endpoint: str,
    pre_releases_ok: bool,  # noqa: FBT001
) -> Version:
    all_versions = _get_versions(
        project,
        pre_releases_ok=pre_releases_ok,
        pypi_endpoint=pypi_endpoint,
    )
    return _resolve_next_version(
        all_versions,
        Version(str(current_minor_version)),
        pre_releases_ok,
    )


def _get_versions(
    project: str,
    pre_releases_ok: bool,  # noqa: FBT001
    pypi_endpoint: str,
) -> list[Version]:
    with PyPISimple(pypi_endpoint) as client:
        if page := client.get_project_page(project):

            def _is_valid(version: Version) -> bool:
                return not version.is_prerelease or pre_releases_ok

            return [
                version
                for package in page.packages
                if _is_valid(version := packaging.version.parse(package.version))
            ]
        return []


def _resolve_next_version(
    all_versions: list[Version],
    minor_version: Version,
    pre_release: bool,  # noqa: FBT001
) -> Version:
    matching_versions = [
        version
        for version in all_versions
        if version.release[:2] == minor_version.release
        and "dev" not in str(version)
        and "post" not in str(version)
    ]
    if not matching_versions:
        print("[bw-semver] Latest matching version: None")
        digits = list(minor_version.release)
    else:
        last_version = sorted(matching_versions)[-1]
        print(f"[bw-semver] Latest matching version: {last_version}")
        digits = list(last_version.release)
        if len(digits) == 2:  # noqa: PLR2004
            digits.append(0)
        digits[2] += 1

    if pre_release:
        matching_pre_versions = [
            version
            for version in all_versions
            if list(version.release) == digits and "dev" in str(version)
        ]
        if matching_pre_versions:
            new_dev_version = max(version.dev for version in matching_pre_versions) + 1
        else:
            new_dev_version = 0
        digits.append(f"dev{new_dev_version}")

    return Version(".".join(str(digit) for digit in digits))


def set_metadata_version(distribution: Distribution) -> None:
    next_version = str(_resolve_version())
    distribution.metadata.version = next_version
    print("[bw-semver] Version resolved:", next_version)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["resolve"])
    parser.parse_args()
    _resolve_version()
