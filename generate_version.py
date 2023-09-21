import datetime
import subprocess
from typing import Optional


def generate_version(
    latest_version: Optional[str], utcnow: Optional[None] = None
) -> str:
    if not utcnow:
        utcnow = datetime.datetime.utcnow()
    calver = "{}.{}".format(utcnow.year % 100, utcnow.month)
    if latest_version and latest_version.startswith(calver + "."):
        build_number = int(latest_version.split(".")[-1]) + 1
    else:
        build_number = 0
    return f"{calver}.{build_number}"


def test():
    def gv(latest_version: Optional[str], year: int, month: int) -> str:
        return generate_version(
            latest_version, datetime.datetime(year=year, month=month, day=1)
        )

    assert gv("21.5.0", year=2021, month=5) == "21.5.1"
    assert gv("21.5.1", year=2021, month=5) == "21.5.2"
    assert gv("21.5.0", year=2021, month=12) == "21.12.0"
    assert gv("21.5.0", year=2022, month=1) == "22.1.0"
    assert gv("21.5.0", year=2022, month=5) == "22.5.0"
    assert gv("21.5.2", year=2021, month=12) == "21.12.0"
    assert gv(None, year=2021, month=12) == "21.12.0"


if __name__ == "__main__":
    existing_versions = subprocess.check_output(
        ["git", "tag", "--list", "--sort=-v:refname", "release/*"],
        text=True,
    )
    if existing_versions:
        latest_version = existing_versions[0].removeprefix("release/")
    else:
        latest_version = None
    print(generate_version(latest_version))
