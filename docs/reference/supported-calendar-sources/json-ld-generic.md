# JSON-LD (generic)

JSON-LD (sometimes referred to as Linked Data) is a way of conveying [computer-readable information](../../explanation/structured-and-unstructured-data.md) which many ticketing and events platforms use on their websites. [Google looks for JSON-LD to pull events through to Search and Maps](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data), and PlaceCal can use it to import events.&#x20;

To find if a site is using JSON-LD:

1. Navigate to a source you'd like to import into PlaceCal
2. Open the Inspector to view the webpage's code
3. Search for the string `ld+json`&#x20;

If `ld+json` is present, it means there is structured data on the site which PlaceCal should be able to read (provided they're using the right fields, see below).

## Information PlaceCal imports from JSON-LD sources

See [what each source imports](README.md#what-each-source-imports) for the information PlaceCal takes from JSON-LD sources. The event image comes from the event's `image`.
