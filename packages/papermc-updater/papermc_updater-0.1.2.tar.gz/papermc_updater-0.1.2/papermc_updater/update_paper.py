from argparse import ArgumentParser
import json
import os
from sys import argv
import urllib.request
import urllib.error

MC_VERSION = "1.20.2"


def parse_args() -> dict:
    """ parse_args: parse command line arguments in form:

    update-papermc $PATH --version $VERSION

    Args:
        None

    Returns:
        dict: {'jar_path': $PATH, 'version': $VERSION}
    """

    ap = ArgumentParser(prog="update-papermc")
    ap.add_argument(
        "jar_path",
        type=str,
        help="Path to PaperMC .jar file to update"
    )
    ap.add_argument(
        "--version",
        type=str,
        default=MC_VERSION,
        help=f"MC version (default: {MC_VERSION})"
    )
    return vars(ap.parse_args(argv[1:]))


def get_latest_paper_build(version: str) -> int:
    """ get_latest_paper_build: obtain the latest PaperMC build (integer
    number) from api.papermc.io

    Args:
        version (str): MC version (e.g., "1.20.1")

    Returns:
        int: latest build of PaperMC
    """

    response = urllib.request.urlopen(
        f"https://api.papermc.io/v2/projects/paper/versions/{version}/builds/"
    )
    content = json.loads(response.read().decode("utf-8"))
    latest_build = max(b["build"] for b in content["builds"])
    return latest_build


def update_paper_to_latest(jar_path: str, version: str) -> None:
    """ update_paper_to_latest: update PaperMC server .jar file (in-place) to
    the latest build

    Args:
        jar_path (str): path to existing PaperMC server .jar file (will be
            replaced!)
        version (str): desired MC version (e.g., "1.20.1")

    Returns:
        None
    """

    if not os.path.exists(jar_path):
        raise FileNotFoundError(
            f"Existing PaperMC .jar file not found: {jar_path}"
        )
    latest_build = get_latest_paper_build(version)
    paper_url = "".join([
        f"https://api.papermc.io/v2/projects/paper/versions/{version}/",
        f"builds/{latest_build}/downloads/paper-{version}-{latest_build}.jar"
    ])
    try:
        os.remove(jar_path)
        filename, _ = urllib.request.urlretrieve(paper_url, jar_path)
    except urllib.error.URLError as ex:
        raise ex
    except Exception as ex:
        raise ex
    if not os.path.exists(filename):
        raise RuntimeError("Error finding new .jar file")


def cmd_line() -> None:
    """ command line tool """

    args = parse_args()
    update_paper_to_latest(args["jar_path"], args["version"])
