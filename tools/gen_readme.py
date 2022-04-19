"""
Quick tool to generate the static list of plugins in README.md from
the JS data (in data.js)

Dependencies: demjson (in order to parse the JS data structure
directly) (License: LGPL3)
https://github.com/dmeranda/demjson
"""

import sys

__author__ = "https://github.com/vmallet"

import jsstore

SKIP_MARKER = "__SKIP__"
GEN_MARKER = "__GENERATED_LIST__"


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
    plugins = jsstore.load_plugins(js_path)

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
