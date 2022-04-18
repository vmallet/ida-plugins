"""
A quickly hacked-together converter to parse the plugin list in
README.md and produce a more-or-less usable JS datastructure.
"""

import re
import sys

__author__ = "https://github.com/vmallet"

ENTRY_HEADER = \
    re.compile("^\\* \\[(?P<name>[^]]*)\\]\\((?P<url>[^)]+)\\):? ?(?P<desc>.*)\n")
"""regex to match:  * [plugin-name](plugin-url): plugin-desc"""


class Entry(object):
    def __init__(self, name, url, desc1):
        self.name = name
        self.url = url
        self.desc = [ desc1 ]

    def append(self, desc):
        self.desc.append(desc)

    def emit(self):
        print("{{name: \"{}\", ".format(self.name))
        print(" url: \"{}\",".format(self.url))
        print(" desc: \"{}\"}},".format(
            "\\n".join(desc.replace('"', '\\"') for desc in self.desc)))
        print()


def produce_js(filename: str):
    print("var tabledata = [")
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
                    entry.emit()
                entry = Entry(name, url, desc)
                continue

            line = line.strip()

            if entry and line:
                entry.append(line)
    if entry:
        entry.emit()
    print("];")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: {} path-to-readme.md".format(sys.argv[0]))
        exit(1)

    produce_js(sys.argv[1])
