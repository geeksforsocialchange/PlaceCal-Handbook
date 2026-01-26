# Supported Calendar Sources

PlaceCal can import events from a variety of calendar and ticketing platforms. Our integrations are categorised into three tiers based on their stability and reliability.

## Integration Tiers

### 🥇 Gold - Stable

Gold integrations use official APIs or standard formats (iCal, RSS, JSON-LD). These are the most reliable and unlikely to break.

### 🥈 Silver - Semi-stable

Silver integrations use structured data but may occasionally require maintenance. They have some official support or use stable data formats embedded in pages.

### 🥉 Bronze - Fragile

Bronze integrations scrape data from web pages without an official API or feed. These may break if the platform changes their website structure. We maintain these for community organisations who have limited ability to migrate platforms, but recommend Gold or Silver sources where possible.

---

## List of Supported Sources

### 🥇 Gold - Stable

| Source | Format | Notes |
|--------|--------|-------|
| [iCal/ICS (generic)](ical-generic.md) | iCal standard | Universal calendar format |
| [Google Calendar](google-calendar.md) | iCal | Widely used, reliable |
| [iCloud Calendar](icloud-calendar.md) | iCal | Apple calendar service |
| [Outlook 365](outlook-365.md) | iCal | Microsoft calendar service |
| [Airtable](airtable.md) | iCal | Database with calendar export |

### 🥈 Silver - Semi-stable

| Source | Format | Notes |
|--------|--------|-------|
| [JSON-LD (generic)](json-ld-generic.md) | JSON-LD | Structured data in web pages |
| [Eventbrite](eventbrite.md) | JSON-LD | Popular ticketing platform |
| [Meetup](meetup.md) | JSON-LD | Community events platform |
| [Dice.fm](dice.fm.md) | JSON-LD | Music events platform |
| [OutSavvy](outsavvy.md) | JSON-LD | Ticketing platform |
| [Ticketsolve](ticketsolve.md) | JSON-LD | Legacy, limited testing |

### 🥉 Bronze - Fragile

| Source | Method | Notes |
|--------|--------|-------|
| [TicketSource](ticketsource.md) | Web scraping | UK ticketing platform |
| [Squarespace](squarespace.md) | Web scraping | Website builder |
| [Resident Advisor](resident-advisor-ra.md) | Web scraping | Music events platform |
| [Wix](wix.md) | Web scraping | ⚠️ [BDS listed](https://boycottwix.org/) - see page for details |

---

## Sources PlaceCal Does Not Support

### Google Sheets

We cannot meaningfully import [unstructured data](../../explanation/structured-and-unstructured-data.md). There are various Google Sheets to iCal integrations which you are welcome to try but we cannot offer specific support as they are constantly changing.

### Facebook

Facebook have closed their APIs and make it practically impossible to scrape public data. If you are extremely brave you can try to improve our abandoned [faceloader Facebook scraping app](https://github.com/geeksforsocialchange/faceloader) but again, we cannot support with this.

### Fatsoma

Fatsoma do not provide a suitable API or metadata output.

## Sources PlaceCal Could Support With Additional Resources

### TicketTailor

TicketTailor have an API PlaceCal could use, with support to develop the importer.
