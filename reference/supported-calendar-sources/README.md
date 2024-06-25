# Supported Calendar sources

By default PlaceCal supports [iCal/.ics](ical-generic.md) and [JSON-LD](json-ld-generic.md) data sources. PlaceCal also supports specific ticketing and event platforms which provide an API for integrations. These are listed below. Instructions for setting up a calendar feed which PlaceCal can import can be found by clicking through on the source you would like to use.&#x20;

## List of supported sources

* [Airtable](airtable.md)
* [Dice.fm](dice.fm.md)
* [Eventbrite](eventbrite.md)
* [Google Calendar](google-calendar.md)
* [iCloud Calendar](icloud-calendar.md)
* [Meetup](meetup.md)
* [Outlook 365](outlook-365.md)
* [OutSavvy](outsavvy.md)
* [Squarespace](squarespace.md)
* [Ticketsolve](ticketsolve.md)

## Sources PlaceCal doesn't support

### Google Sheets

We can’t meaningfully import [unstructured data](../../explanation/structured-and-unstructured-data.md). There are various Google Sheets to iCal integrations which you're welcome to try but we can’t offer specific support to these as they are constant moving targets.

### Facebook

Facebook have closed their APIs and make it practically impossible to scrape public data. If you’re extremely brave you can try to improve our abandoned [faceloader Facebook scraping app](https://github.com/geeksforsocialchange/faceloader) but again, we can’t support with this.

### Fatsoma

Fatsoma don't provide a suitable API or metadata output.&#x20;

## Sources PlaceCal could support with additional resources&#x20;

### TicketTailor

TicketTailor have an API PlaceCal could use, with support to develop the importer.&#x20;
