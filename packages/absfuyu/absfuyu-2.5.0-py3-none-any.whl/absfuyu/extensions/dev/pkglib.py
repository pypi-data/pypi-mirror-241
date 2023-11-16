from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from typing import Dict, List, Union

# json
__all_lib = {
    "native": [
        "os","random","string","subprocess","typing","hashlib",
        "datetime","json","sys","math","base64","codecs",
        "zlib","inspect","functools","tracemalloc", "re",
        "collections", "urllib", "time",
    ],
    "external": [
        "rich","click","colorama","requests","numpy","pandas",
        "matplotlib","LunarCalendar",
    ],
    "dev-only": [
        "twine", "virtualenv", "setuptools", "wheel",
        "autoimport", "black", "pytest", "tox", "build",
        "pipx",
    ],
    "unused": [
        "sortedcontainers", "tomli", "pyyaml",
    ],
    "future": [
        "scikit-learn", "opencv-python",
    ],
}

LibraryDict = Dict[str, List[str]]

def show_lib_from_json(
        lib_dict: LibraryDict,
        hidden: bool = False,
        to_json: bool = True
    ) -> str:
    """
    Show libraries
    
    lib_dict: a dict that converted from jso
    hidden: import as __[lib name]
    to_json: save as json format
    """

    catergory = [x for x in lib_dict.keys()] # get keys
    libs = [x for x in lib_dict.values()] # get values

    lib_import = [] # New list
    for lib_list in libs: # Take each lib list in a list of lib list
        temp = []
        for item in sorted(list(set(lib_list))):
            if hidden:
                hidden_text = f" as __{item}"
            else:
                hidden_text = ""
            temp.append(f"import {item}{hidden_text}")
        lib_import.append(temp)

    new_lib = dict(zip(catergory, lib_import))

    if to_json:
        import json
        return str(json.dumps(new_lib, indent=4))
    else:
        out_text = ""
        for idx, val in enumerate(catergory):
            out_text += f"# {val} libs\n"
            for x in lib_import[idx]:
                out_text += x+"\n"
            out_text += "\n"
        return out_text


# idk why i add arg parser here *shrug*
def get_parser(
        name: Union[str, None] = None,
        description: Union[str, None] = None,
        epilog: Union[str, None] = None,
        *,
        version: str = "",
        add_help: bool = True,
    ) -> ArgumentParser:
    arg_parser = ArgumentParser(
        prog=name,
        description=description,
        epilog=epilog,
        add_help=add_help,
        formatter_class=ArgumentDefaultsHelpFormatter,
        # allow_abbrev=False, # Disable long options recognize
        # exit_on_error=True
    )
    arg_parser.add_argument("--version", action="version",
                            version=f"%(prog)s {version}")
    _ll_val = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    arg_parser.add_argument(
        "--log-level",
        metavar="LOG_LEVEL",
        dest="log_level",
        choices=_ll_val,
        default="INFO",
        help=f"Log level: {_ll_val}"
    )
    return arg_parser