"""Building the app and initializing all prerequisites."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

from cli import constants
from cli.utils import console


def initialize_requirements_txt(reflex_version: str):
    """Initialize the requirements.txt file.
    If absent, generate one for the user.
    If the requirements.txt does not have reflex as dependency,
    generate a requirement pinning current version and append to
    the requirements.txt file.

    Args:
        reflex_version: The current version of Reflex used in the app.
    """
    fp = Path(constants.RequirementsTxt.FILE)
    fp.touch(exist_ok=True)

    try:
        with open(fp, "r") as f:
            for req in f.readlines():
                # Check if we have a package name that is reflex
                if re.match(r"^reflex[^a-zA-Z0-9]", req):
                    console.debug(f"{fp} already has reflex as dependency.")
                    return
        with open(fp, "a") as f:
            f.write(f"\n{constants.RequirementsTxt.DEFAULTS_STUB}{reflex_version}\n")
    except Exception:
        console.info(f"Unable to check {fp} for reflex dependency.")


def generate_requirements():
    """Generate a requirements.txt file based on the current environment."""
    # Run the command and get the output
    result = subprocess.run(
        [sys.executable, "-m", "pipdeptree", "--warn", "silence"],
        capture_output=True,
        text=True,
    )

    # Filter the output lines using a regular expression
    lines = result.stdout.split("\n")
    filtered_lines = [line for line in lines if re.match(r"^\w+", line)]

    # Write the filtered lines to requirements.txt
    with open("requirements.txt", "w") as f:
        for line in filtered_lines:
            f.write(line + "\n")


def check_requirements():
    """Check if the requirements are installed."""
    if not os.path.exists(constants.RequirementsTxt.FILE):
        console.warn("It seems like there's no requirements.txt in your project.")
        response = console.ask(
            "Would you like us to auto-generate one based on your current environment?",
            choices=["y", "n"],
        )

        if response == "y":
            generate_requirements()
        else:
            console.error(
                "Please create a requirements.txt file in your project's root directory and try again."
            )
            exit()
