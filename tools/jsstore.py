"""
Couple of utilities to read/(maybe write) the plugin list from/to
JS files.
"""

import re
import sys
from typing import Dict, List

import demjson

__author__ = "https://github.com/vmallet"

# Attribute names used in plugin definition
ATTR_NAME = "name"
ATTR_URL = "url"
ATTR_SRC = "src"
ATTR_CATS = "cats"
ATTR_LAST = "last"
ATTR_VERS = "vers"
ATTR_DESC = "desc"

VALID_ATTRS = {
    ATTR_NAME, ATTR_URL, ATTR_SRC, ATTR_CATS, ATTR_LAST, ATTR_VERS, ATTR_DESC
}

JS_VAR = re.compile("^var [^=]*= *(.*);$", re.DOTALL)


class EntryFormatter(object):
    """Format a plugin entry in a consistent way for data.js"""
    def __init__(self, attrs):
        self.attrs = attrs

    def _emit_attr_maybe(self, name, out_name=None, prefix="", suffix="",
                         escape=False, end='\n', file=sys.stdout):
        attr = self.attrs.get(name, None)
        if attr is not None:
            if escape:
                attr = attr.replace("\n", "\\n").replace("\"", "\\\"")
            print("{}{}: \"{}\"{}".format(prefix, out_name or name, attr, suffix),
                  end=end, file=file)

    def emit(self, file=sys.stdout):
        print("{", end='', file=file)
        self._emit_attr_maybe(ATTR_NAME, suffix=",", file=file)
        self._emit_attr_maybe(ATTR_URL, prefix=" ", suffix=",", file=file)
        self._emit_attr_maybe(ATTR_SRC, prefix=" ", suffix=",", file=file)
        self._emit_attr_maybe(ATTR_CATS, prefix=" ", suffix=",", file=file)
        self._emit_attr_maybe(ATTR_LAST, prefix=" ", suffix=",", file=file)
        self._emit_attr_maybe(ATTR_VERS, prefix=" ", suffix=",", file=file)
        self._emit_attr_maybe(ATTR_DESC, prefix=" ", escape=True, end='', file=file)
        print("},", file=file)
        print(file=file)


def check_attrs(plugins):
    """Check for unknown attributes in plugins, raise if so."""
    for i, info in enumerate(plugins):
        keys = set(info.keys())
        if not keys.issubset(VALID_ATTRS):
            raise Exception("Unknown attribute, plugin entry {}: {}".format(
                i, keys - VALID_ATTRS))


def load_plugins(js_file: str, check_attributes=False) -> List[Dict[str, str]]:
    """Parse the JS structure into an array of dicts, one dict per plugin."""
    with open(js_file, "rt", encoding="UTF-8") as f:
        content = f.read().strip()
        m = JS_VAR.match(content)
        if not m:
            raise Exception("Unable to parse js data definiton from: {}".format(js_file))
        plugins = demjson.decode(m.group(1))

    if check_attributes:
        check_attrs(plugins)

    return plugins


def _info_key(info):
    """Return a midly-sanitized sorting key for the given plugin info."""
    # TODO: switch to using translate() instead of chaining replace()?
    return info.get("name", "").lower().replace(" ", "").replace("-", "").replace("_", "")


def print_plugins(plugins, file=sys.stdout):
    """Print plugins in the canonical order to a JS var definition."""
    plugins = sorted(plugins, key=_info_key)
    print("var tabledata = [", file=file)
    for info in plugins:
        EntryFormatter(info).emit(file=file)
    print("];", file=file)
