"""
Quick tool to generate the static list of plugins in README.md from
the JS data (in data.js)

Dependencies: demjson (in order to parse the JS data structure
directly) (License: LGPL3)
https://github.com/dmeranda/demjson
"""

import re
import sys
from typing import Dict, List

import demjson

__author__ = "https://github.com/vmallet"

JS_VAR = re.compile("^var [^=]*= *(.*);$", re.DOTALL)

SKIP_MARKER = "__SKIP__"
GEN_MARKER = "__GENERATED_LIST__"


def load_plugins(js_file: str) -> List[Dict[str, str]]:
    """Parse the JS structure into an array of dicts, one dict per plugin."""
    with open(js_file, "rt", encoding="UTF-8") as f:
        content = f.read().strip()
        m = JS_VAR.match(content)
        if not m:
            raise Exception("Unable to parse js data definiton from: {}".format(js_file))
        plugins = demjson.decode(m.group(1))

    return plugins


def desc_to_md(desc: str):
    """Parse a multiline description into multiple lines suitable for
    Markdown."""
    fixed = []
    for line in desc.split("\n"):
        line = line.strip()
        if line.startswith("*"):
            if not fixed:
                fixed.append("")
            # If we have bullet points, turn it into a nested list
            fixed.append("  " + line)
        else:
            fixed.append(line)

    return fixed


def output_plugins(plugins):
    """Print plugins in Markdown format to stdout."""
    for i, info in enumerate(plugins):
        name = info.get("name", None)
        url = info.get("url", None)
        desc = info.get("desc", None)

        if not (name and url and desc):
            print("Incomplete plugin, skipped: "
                  "index={}, name={}, url={}, desc={}".format(i, name, url, desc),
                  file=sys.stderr)
            continue

        md_desc = desc_to_md(desc)

        print("* [{}]({}): {}".format(name, url, md_desc[0]))
        for line in md_desc[1:]:
            print(line)
        print()


def gen_readme(template_path: str, js_path: str):
    """Produce a templated readme on stdout using the provided template
    and injecting the plugins definitions read from the JS data."""
    plugins = load_plugins(js_path)

    with open(template_path, "rt") as f:
        for line in f:
            line = line.strip()
            if SKIP_MARKER in line:
                continue
            if GEN_MARKER in line:
                print("{} plugins".format(len(plugins)))
                output_plugins(plugins)
            else:
                print(line)


if __name__ == "__main__":
    gen_readme("README-template.md", "data.js")
