# Squarespace

PlaceCal can import events created using the default Squarespace events block. Squarespace has [official documentation on adding events to your Squarespace site](https://support.squarespace.com/hc/en-us/articles/206543837-Events-pages).&#x20;

To import events from Squarespace, find the listings view of your site. This looks something like [this](https://www.partisancollective.net/events/listing/) or [this](https://www.vfdalston.com/our-events) - the calendar grid view will not work.

Paste that URL into the calendar field and you should be good to go!

## Information PlaceCal imports from Squarespace

* Unique ID
* Event title
* Description
* Start date and time
* End date and time&#x20;
* URL

### A note on how Squarespace handles location information&#x20;

Squarespace stores location information as latitude and longitude rather than as a street address, which means that **this isn't able to be understood and matched to a street address by the PlaceCal importer**. If you want to use Squarespace as a source, you will need to use **Default location**, **No location** or **Online only** [when setting up the Calendar](../../how-to/add-a-calendar.md#where-should-location-information-for-this-calendar-come-from). This means Squarespace isn't a suitable source for a Partner which operates out of multiple physical locations, and we would recommend using an[ iCal source](ical-generic.md) instead.&#x20;
