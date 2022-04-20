"""
A quickly hacked-together converter to parse the plugin list in
README.md and produce a more-or-less usable JS datastructure.
"""

import re
import sys

from jsstore import print_plugins

__author__ = "https://github.com/vmallet"

ENTRY_HEADER = \
    re.compile("^\\* \\[(?P<name>[^]]*)]\\((?P<url>[^)]+)\\):? ?(?P<desc>.*)\n")
"""regex to match:  * [plugin-name](plugin-url): plugin-desc"""


class Entry(object):
    def __init__(self, name, url, desc1):
        self.attrs = {"name": name, "url": url}
        self.desc = [desc1]

    def append(self, desc):
        self.desc.append(desc)

    def to_attrs(self):
        """Get a 'info' compatible set of attributes for this entry."""
        attrs = dict(self.attrs)
        attrs["desc"] = "\n".join(desc for desc in self.desc)
        return attrs


def produce_js(filename: str):
    plugins = []
    entry = None
    with open(filename, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            m = ENTRY_HEADER.match(line)
            if m:
                name = m.group("name")
                url = m.group("url")
                desc = m.group("desc")
                if entry:
                    plugins.append(entry.to_attrs())
                entry = Entry(name, url, desc)
                continue

            line = line.strip()

            if entry and line:
                entry.append(line)
    if entry:
        plugins.append(entry.to_attrs())

    print_plugins(plugins)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: {} path-to-readme.md".format(sys.argv[0]))
        exit(1)

    produce_js(sys.argv[1])
