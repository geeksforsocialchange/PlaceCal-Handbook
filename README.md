# PlaceCal Handbook

This [PlaceCal Handbook](https://handbook.placecal.org) is a collection of documentation for [PlaceCal](https://placecal.org)

The rest of this page covers how to edit the handbook, see the above link to the handbook itself if you need documentation about PlaceCal

## Local Development

This handbook is built using [Zensical](https://zensical.org/docs/get-started/), a Python application for building project documentation. Follow the instructions they provide to install Zensical if you want to build this handbook locally

GitHub Actions uses Zensical to build and serve the site, and will serve all Markdown files from the docs directory

The tables on the supported calendar sources page come from PlaceCal's own list of sources. Run `python scripts/sources_table.py` before building to fill them in, and don't commit the filled-in page. Set `SOURCES_URL` to read the list from somewhere other than placecal.org.

See the Zensical [setup](https://zensical.org/docs/setup/basics/) pages for how to configure Zensical
