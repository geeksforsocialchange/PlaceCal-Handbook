# WordPress

There are many WordPress calendar plugins available. PlaceCal currently supports sites using [The Events Calendar](https://theeventscalendar.com/) plugin (also known as Tribe Events), which is one of the most popular options.

If you're using a different WordPress calendar plugin that provides an iCal feed, you may be able to use the [generic iCal importer](ical-generic.md) instead.

## The Events Calendar

To import events from a site using The Events Calendar, you need to find the iCal feed URL. Most sites expose this by adding `?ical=1` to the events page URL.

For example, if the events page is:

```
https://example.org/events/
```

The iCal feed URL would be:

```
https://example.org/events/?ical=1
```

Paste this URL into the calendar field when [adding a calendar](../../how-to/add-a-calendar.md) and you should be good to go!

### Finding the iCal feed

1. Navigate to the events listing page on the WordPress site
2. Add `?ical=1` to the end of the URL
3. If the feed works, your browser will either download a file or display calendar data
4. Use this URL as your PlaceCal calendar source

## Information PlaceCal imports from WordPress

* Unique ID
* Event title
* Description
* Start date and time
* End date and time
* Address
* URL
* Online address (if an online event)
