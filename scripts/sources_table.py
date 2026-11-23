#!/usr/bin/env python3
"""Fill the supported sources table from PlaceCal's public list of calendar sources."""

import json
import os
import pathlib
import sys
import urllib.request

SOURCES_URL = os.environ.get("SOURCES_URL", "https://placecal.org/api/v1/calendar_sources")
PAGE = pathlib.Path(__file__).parent.parent / "docs/reference/supported-calendar-sources/README.md"
START = "<!-- sources-table:start -->"
END = "<!-- sources-table:end -->"
SCHEMA_VERSION = 1


def fetch():
    request = urllib.request.Request(SOURCES_URL, headers={"User-Agent": "PlaceCal-Handbook-build"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.load(response)
    except (OSError, ValueError) as error:
        sys.exit(f"Could not read {SOURCES_URL}: {error}")
    if data.get("version") != SCHEMA_VERSION:
        sys.exit(f"{SOURCES_URL} has schema version {data.get('version')}, this script reads {SCHEMA_VERSION}")
    return data


def yes_no(value):
    return "Yes" if value else "No"


def table(headings, rows):
    lines = ["| " + " | ".join(headings) + " |", "| " + " | ".join("---" for _ in headings) + " |"]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(lines)


def sentence_list(items):
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def link(source):
    return f"[{source['name']}]({source['handbook_page']}.md)" if source["handbook_page"] else source["name"]


def render(data):
    sources = data["sources"]
    tiers = {tier["key"]: tier for tier in data["tiers"]}
    shared = [field for field in data["fields"] if all(field["key"] in source["imports"] for source in sources)]
    varying = [field for field in data["fields"] if field not in shared]

    about = table(
        ["Source", "Tier", "Needs an API key", "Ticketing platform"],
        [[link(s), tiers[s["tier"]]["label"], yes_no(s["requires_api_token"]), yes_no(s["ticketing"])] for s in sources],
    )
    imports = table(
        ["Source"] + [field["label"] for field in varying],
        [[link(s)] + [yes_no(field["key"] in s["imports"]) for field in varying] for s in sources],
    )
    tier_notes = "\n".join(f"- **{tier['label']}.** {tier['description']}" for tier in data["tiers"])
    shared_labels = sentence_list([field["label"].lower() for field in shared])

    return "\n\n".join(
        [
            about,
            "Tiers say how open the source's format is:",
            tier_notes,
            "An event from a ticketing platform has a **Book tickets** button that goes to its page there.",
            "## What each source imports",
            f"Every source gives PlaceCal each event's {shared_labels}. The table shows what else each one brings.",
            imports,
        ]
    )


def main():
    page = PAGE.read_text()
    if START not in page or END not in page:
        sys.exit(f"{PAGE} has no {START} and {END} markers")
    before, rest = page.split(START, 1)
    after = rest.split(END, 1)[1]
    PAGE.write_text(f"{before}{START}\n\n{render(fetch())}\n\n{END}{after}")


if __name__ == "__main__":
    main()
