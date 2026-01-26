# Supported Calendar Sources

PlaceCal can import events from a variety of calendar and ticketing platforms. Our integrations are categorised into three tiers based on their stability and reliability.

## Integration Tiers

### 🥇 Gold - Stable

Gold integrations use official APIs or standard formats (iCal, JSON-LD). These are the most reliable and unlikely to break.

### 🥈 Silver - Semi-stable

Silver integrations use structured data from platforms that embed standard formats, but the way we access them may occasionally require maintenance.

### 🥉 Bronze - Fragile

Bronze integrations scrape data from web pages without an official API or standard feed. These may break if the platform changes their website structure. We maintain these for community organisations who have limited ability to migrate platforms, but recommend Gold or Silver sources where possible.

---

## List of Supported Sources

| Source | Tier | Format | Notes |
|--------|------|--------|-------|
| [Airtable](airtable.md) | 🥇 Gold | iCal | Database with calendar export |
| [Dice.fm](dice.fm.md) | 🥈 Silver | JSON-LD | Music events platform |
| [Eventbrite](eventbrite.md) | 🥈 Silver | JSON-LD | Popular ticketing platform |
| [Google Calendar](google-calendar.md) | 🥇 Gold | iCal | Widely used, reliable |
| [iCal/ICS (generic)](ical-generic.md) | 🥇 Gold | iCal | Universal calendar format |
| [iCloud Calendar](icloud-calendar.md) | 🥇 Gold | iCal | Apple calendar service |
| [JSON-LD (generic)](json-ld-generic.md) | 🥇 Gold | JSON-LD | Structured data in web pages |
| [Meetup](meetup.md) | 🥈 Silver | JSON-LD | Community events platform |
| [Outlook 365](outlook-365.md) | 🥇 Gold | iCal | Microsoft calendar service |
| [OutSavvy](outsavvy.md) | 🥈 Silver | JSON-LD | Ticketing platform |
| [Resident Advisor](resident-advisor-ra.md) | 🥉 Bronze | Web scraping | Music events platform |
| [Squarespace](squarespace.md) | 🥉 Bronze | Web scraping | Website builder |
| [TicketSource](ticketsource.md) | 🥉 Bronze | Web scraping | UK ticketing platform |
| [Ticketsolve](ticketsolve.md) | 🥈 Silver | JSON-LD | Legacy, limited testing |
| [Wix](wix.md) | 🥉 Bronze | Web scraping | ⚠️ [BDS listed](https://boycottwix.org/) |

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
