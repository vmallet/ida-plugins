"""
Couple of utilities to read/(maybe write) the plugin list from/to
JS files.
"""

import re
from typing import Dict, List

import demjson

__author__ = "https://github.com/vmallet"

JS_VAR = re.compile("^var [^=]*= *(.*);$", re.DOTALL)


def load_plugins(js_file: str) -> List[Dict[str, str]]:
    """Parse the JS structure into an array of dicts, one dict per plugin."""
    with open(js_file, "rt", encoding="UTF-8") as f:
        content = f.read().strip()
        m = JS_VAR.match(content)
        if not m:
            raise Exception("Unable to parse js data definiton from: {}".format(js_file))
        plugins = demjson.decode(m.group(1))

    return plugins

