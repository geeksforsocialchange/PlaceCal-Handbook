# Wix Events

> ⚠️ **BDS Warning**: Wix is on the [BDS (Boycott, Divestment and Sanctions) list](https://boycottwix.org/) due to its ties to the Israeli government and military. We support this importer because many community organisations already use Wix and have limited technical capacity to migrate. **We recommend using alternative platforms where possible**, such as [iCal-compatible calendars](ical-generic.md), [Eventbrite](eventbrite.md), or self-hosted solutions.

PlaceCal can import events from Wix websites that use the Wix Events feature. Wix has [official documentation on adding events to your Wix site](https://support.wix.com/en/article/wix-events-adding-and-setting-up-events).

## How to import from Wix

### Wixsite.com URLs

If your site uses a wixsite.com URL (e.g., https://yourname.wixsite.com/mysite/events), simply paste the events page URL into the calendar field when adding a calendar. PlaceCal will automatically detect it as a Wix source.

### Custom domain URLs

If your Wix site uses a custom domain (e.g., https://www.myorganisation.com/events), you will need to:

1. Paste the events page URL into the calendar field
2. Set the **Importer mode** to "Wix" in the calendar settings

## Information PlaceCal imports from Wix

PlaceCal pulls the following from Wix events:

* Unique ID
* Event title
* Description
* Start date and time
* End date and time
* Location name and address
* URL
* Event image

## Important notes

### Fragile importer

Unlike standard calendar formats (iCal, RSS), Wix does not expose a public events feed. PlaceCal extracts event data from the page internal JSON structure. This means:

* The importer may require updates if Wix changes their internal data format
* If your events stop importing, please contact us so we can investigate

### Finding your events page URL

Your events page URL should be the page that shows a list of upcoming events. This is typically something like:

* https://yourname.wixsite.com/mysite/events
* https://yourname.wixsite.com/mysite/event-list
* https://www.yourcustomdomain.com/events

The URL should show multiple events in a list view, not a single event page.
