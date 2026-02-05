# TicketSource

> 🥉 **Bronze Integration** - This is a [fragile integration](README.md#-bronze---fragile) that scrapes data from web pages. It may break if TicketSource changes their website structure.

PlaceCal can import events from TicketSource venue pages. TicketSource is a UK-based ticketing platform used by many theatres, arts centres, and community venues.

## How to import from TicketSource

To import events from TicketSource, you need the URL of your **venue page** (not individual event pages). This is typically in the format:

* `https://www.ticketsource.co.uk/your-venue-name`

Simply paste this URL into the calendar field when [adding a calendar](../../how-to/add-a-calendar.md). PlaceCal will automatically detect it as a TicketSource source and import all upcoming events from that venue.

## Information PlaceCal imports from TicketSource

PlaceCal pulls the following from TicketSource events:

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
