# Supported Calendar sources

By default PlaceCal supports [iCal/.ics](ical-generic.md) and [JSON-LD](json-ld-generic.md) data sources. PlaceCal also supports specific ticketing and event platforms which provide an API for integrations. These are listed below. Instructions for setting up a calendar feed which PlaceCal can import can be found by clicking through on the source you would like to use.&#x20;

## Supported sources

<!-- sources-table:start -->

This table is filled in from PlaceCal's own list of calendar sources when the handbook is built. See `scripts/sources_table.py`.

<!-- sources-table:end -->

## Setup guides

Each source in the tables links to its setup guide. These services publish their events in a standard format, so PlaceCal reads them with one of the generic sources:

* Read as [iCal](ical-generic.md): [Airtable](airtable.md), [Google Calendar](google-calendar.md), [iCloud Calendar](icloud-calendar.md), [Outlook 365](outlook-365.md), [WordPress](wordpress.md) (The Events Calendar plugin)
* Read as [JSON-LD](json-ld-generic.md): [Dice.fm](dice.fm.md)

## Sources PlaceCal doesn't support

### Google Sheets

We can’t meaningfully import [unstructured data](../../explanation/structured-and-unstructured-data.md). There are various Google Sheets to iCal integrations which you're welcome to try but we can’t offer specific support to these as they are constant moving targets.

### Facebook

Facebook have closed their APIs and make it practically impossible to scrape public data. If you’re extremely brave you can try to improve our abandoned [faceloader Facebook scraping app](https://github.com/geeksforsocialchange/faceloader) but again, we can’t support with this.

### Fatsoma

Fatsoma don't provide a suitable API or metadata output.&#x20;
