# Meetup

PlaceCal supports importing events directly from Meetup URLs.

Meetup have recently changed their format so our current importer is temporarily broken. In the meantime you can load it via the iCal importer

Sample group URL: `https://www.meetup.com/london-bisexual-women-games-wine-group`

To get the iCal feed just add on `/events/ical` to the end, so e.g:

`https://www.meetup.com/london-bisexual-women-games-wine-group/events/ical`

We will update this page soon once the underlying issue is fixed.

See [adding a calendar](../../how-to/add-a-calendar.md) for the other steps.

## Information PlaceCal imports from Meetup

* Unique ID&#x20;
* Event title
* Description
* Start time and date
* End time and date (calculated by adding the event duration to the start date)&#x20;
* Address
* URL&#x20;
* Online address (if it's an online event)&#x20;
