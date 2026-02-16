# TicketSource

PlaceCal can import events from TicketSource using their REST API. TicketSource is a UK-based ticketing platform used by many theatres, arts centres, and community venues.

## How to import from TicketSource

You need two things to set up a TicketSource calendar in PlaceCal:

1. **Your venue page URL** (not individual event pages), in the format:
   * `https://www.ticketsource.co.uk/your-venue-name`
2. **A TicketSource API key**. To find this:
   1. Log in to your [TicketSource](https://www.ticketsource.co.uk/) account
   2. Go to **Settings** > **API**
   3. Copy your API key using the copy button next to it

   See [TicketSource's API integration guide](https://help.ticketsource.com/en/article/api-integration-10o5gun/) for more details.

Paste the venue URL into the URL field and the API key into the API key field when [adding a calendar](../../how-to/add-a-calendar.md). PlaceCal will automatically detect it as a TicketSource source and import all upcoming events from that venue.

## Information PlaceCal imports from TicketSource

* Event title
* Description
* Start date and time
* End date and time
* Location/venue address
* Event URL

## Important notes

### Venue pages only

PlaceCal imports from venue pages, not individual event pages. Make sure you use the main venue URL (e.g., `https://www.ticketsource.co.uk/fairfield-house`) rather than a specific event or ticket URL.

### Multiple time slots

If an event has multiple performances or time slots, PlaceCal will import each one as a separate event with its own date and time.
