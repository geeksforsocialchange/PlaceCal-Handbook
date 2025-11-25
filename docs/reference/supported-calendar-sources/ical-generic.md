# iCal (generic)

iCal is a widely-used standard for publishing calendar and event data which PlaceCal can use as a source. We provide instructions on connecting [Google](google-calendar.md), [Outlook 365](outlook-365.md), [iCloud](icloud-calendar.md) and [Airtable](airtable.md) calendars, but you might have iCal data from another source which PlaceCal can still read!&#x20;

To identify an iCal source look for the .ics file extension. This will appear at the end of any iCal file, which means it will also show up in valid iCal URLs. &#x20;

Most calendar software will support exporting an .ics file of a given calendar. This file can then be hosted online. As long as it's hosted somewhere where the URL isn't going to change (meaning whenever it's updated, it needs to be replaced with a file of exactly the same name with the same path to get to it) you can use this URL as a source for PlaceCal when [adding a Calendar](../../how-to/add-a-calendar.md).&#x20;

We provide information about common services which handle this part for you because for most people this will be the easiest and most convenient way to host an .ics file, but you're free to use whichever hosting works for you.&#x20;

## Information PlaceCal imports from iCal sources

* Unique ID
* Event title
* Description
* Start date and time
* End date and time
* Address
* URL
* Online address (if an online event)&#x20;
