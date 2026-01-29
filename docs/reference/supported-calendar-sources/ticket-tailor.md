# Ticket Tailor

PlaceCal can import events from a [Ticket Tailor](https://www.tickettailor.com/) box office page. Unlike most other importers, Ticket Tailor requires an API key to access your events.

## Setup

### 1. Get your API key

1. Log in to your Ticket Tailor account
2. Go to **Box Office > API Keys**
3. Create a new API key with **read** permission on **Events** only
4. Copy the key (it starts with `sk_`)

### 2. Add the calendar in PlaceCal

1. [Add a calendar](../../how-to/add-a-calendar.md) using your Ticket Tailor box office URL as the source, e.g. `https://www.tickettailor.com/events/yourorganisation`
2. PlaceCal will detect it as a Ticket Tailor feed and ask for your API key
3. Paste your API key into the field provided

PlaceCal will then import your published events automatically.

## Information PlaceCal imports from Ticket Tailor

* Unique ID
* Event title
* Description
* Start date and time
* End date and time
* Venue name and postcode
* Event URL

## Notes

* Only **published** events are imported. Draft or archived events are skipped.
* Your API key is stored securely and is only used to fetch your event listings.
* If your API key expires or is revoked, you can update it on the calendar settings page in PlaceCal.
