# Squarespace

PlaceCal can import events created using the default Squarespace events block. Squarespace has [official documentation on adding events to your Squarespace site](https://support.squarespace.com/hc/en-us/articles/206543837-Events-pages).&#x20;

PlaceCal can import events using the default Squarespace URL of sites which have an events block. If you're using the default Squarespace URL, simply navigate to your events page and copy the page URL. You should then enter this URL in the URL field when [adding a Calendar](../../how-to/add-a-calendar.md) to PlaceCal.&#x20;

Custom domain names **do not work** with PlaceCal. If you have a custom domain associated with your Squarespace site, you can still import your events by using the slug from your site in combination with your default Squarespace URL.&#x20;

The slug is the part of a URL after and including the `/`.&#x20;

To import events from a Squarespace site using a custom domain, navigate to the events page of your site and copy the slug (usually something like `/events`). Paste this somewhere you can refer to it later. Then find the default Squarespace site URL (usually something like `https://bumblebee-raspberry-5hgh.squarespace.com`). You now want to combine the two to make one URL by putting the slug at the end of your default Squarespace site URL (in this example, making `https://bumblebee-raspberry-5hgh.squarespace.com/events`). You should enter this combined URL in the URL field when [adding a Calendar](../../how-to/add-a-calendar.md) to PlaceCal.&#x20;

## Information PlaceCal imports from Squarespace

* Unique ID
* Event title
* Description
* Start date and time
* End date and time&#x20;
* URL

### A note on how Squarespace handles location information&#x20;

Squarespace stores location information as latitude and longitude rather than as a street address, which means that **this isn't able to be understood and matched to a street address by the PlaceCal importer**. If you want to use Squarespace as a source, you will need to use **Default location**, **No location** or **Online only** [when setting up the Calendar](../../how-to/add-a-calendar.md#where-should-location-information-for-this-calendar-come-from). This means Squarespace isn't a suitable source for a Partner which operates out of multiple physical locations, and we would recommend using an[ iCal source](ical-generic.md) instead.&#x20;
