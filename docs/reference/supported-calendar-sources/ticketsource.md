# TicketSource

PlaceCal can import events from TicketSource using their REST API. TicketSource is a UK-based ticketing platform used by many theatres, arts centres, and community venues.

## How to import from TicketSource

You need two things to set up a TicketSource calendar in PlaceCal:

1. **Your venue page URL** (not individual event pages), in the format:
   * `https://www.ticketsource.co.uk/your-venue-name`
2. **A TicketSource API key**. You can find this in your TicketSource account settings under API Keys.

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
