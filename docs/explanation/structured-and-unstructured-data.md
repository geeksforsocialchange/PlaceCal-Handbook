# Structured and unstructured data

Structured data is information which is understandable by computers. This means it is consistent—it’s in the same format every time, and that each piece of information is labelled with metadata which tells the computer both what it is and how it should be used. Unstructured data isn't consistent and doesn't have metadata. This means it's difficult for computers to understand and it's not possible to apply processes to it in order to reliably collect and use the information for other purposes.&#x20;

We can conceptualise data in different dimensions, relating to how much structure it has (and how easy it is for both humans and computers to understand it):

### 1D data - Flyers, posters, and Instagram posts <a href="#block-9a569d575fe54b658671f0691914224a" id="block-9a569d575fe54b658671f0691914224a"></a>

1D data is data which is visually resolved, meaning you use visual information to pick up cues about how to use the data, for example an arrow on a map pointing to an address, or a transport icon next to the name of a station. It’s not standardised, and is often not searchable as text is baked into an image, or physically printed. Instagram posts are 1D data because they often use poster-style images with a lot of information in the image itself. 1D data is not easily usable – a human has to go through every piece of data individually and make it into a more computer-readable format to use it with a piece of software, like a calendar app.

### 2D data - Spreadsheets <a href="#block-489f3fc460c346f4a3d9742806907a47" id="block-489f3fc460c346f4a3d9742806907a47"></a>

2D data is visually resolved, but has some structure. Spreadsheets are 2D data because while you can apply formulas to them to get some functionality out of them, and they have column headings and titles telling you what each piece of data is, it’s down to a human to make sure all of the information in that column is appropriate and in the right format. It’s easy for spreadsheets to contain erroneous information, for example a date entered into a spreadsheet as 03/10 might be resolved as March 10th or October 3rd depending on how the spreadsheet is configured.

### 3D data - Database <a href="#block-a10c680d5d9a43f58e0f859c0d39380b" id="block-a10c680d5d9a43f58e0f859c0d39380b"></a>

3D data is able to be resolved visually and understood by a computer, meaning both humans and computers find it useful. 3D data is consistent and has checks stopping the wrong kind of information being entered. This is the most usable kind of data for working with software and integrating data into other places – it requires the least human oversight to work and keep working, and is least likely to introduce mistakes. This is the kind of data PlaceCal can work with!

## What does structured data allow us to do?

Because structured data is computer-readable, we can use it to automate the import of event listings into PlaceCal. This reduces the administrative burden on Partners by removing the need to manually update PlaceCal listings on top of their usual event planning process—many community calendars which don't use PlaceCal are manually updated, often requiring a great deal of labour to keep up to date. If Partners are already using tools which output structured data, they only need to connect this to PlaceCal once to have their events listed on the Site.&#x20;

PlaceCal also outputs structured data—each PlaceCal Site outputs an iCal feed which you can follow in any calendar software which allows you to subscribe to calendar feeds. [PlaceCal also has an API](broken-reference) which developers of other apps can use to integrate with information from PlaceCal.

Sites which use structured data (specifically JSON-LD) are also great for SEO—[Google uses JSON-LD to inform its Rich Results](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data), which is their term for the details they display about events in Search and Maps.&#x20;

## Popular formats&#x20;

[PlaceCal can read data from a variety of sources](../reference/supported-calendar-sources/). Some common formats of structured data are:

### iCal <a href="#block-d9cb8061f32542fbaeecba9f914fcb7e" id="block-d9cb8061f32542fbaeecba9f914fcb7e"></a>

iCal is a format for calendar events, which every reputable digital calendar is able to read and export. It outputs the data in a predictable way every time, which PlaceCal can read and use to output an events feed. It’s used by software like Microsoft Outlook and Google Calendar, so will probably be the type of feed a partner uses if the main way they keep track of their events is through a calendar software rather than a ticketing platform.

### JSON-LD <a href="#block-4ea22e00d40e46fd87617f3ae2048926" id="block-4ea22e00d40e46fd87617f3ae2048926"></a>

JSON-LD is another format for structured data, which can support event data. It’s often used by SaaS (Software as a Service) web platforms like Squarespace, and might be used by ticketing providers too. It’s useful on the web because it’s the format that Google and other search engines use to find event information on a web page and surface that in search results.

### APIs <a href="#block-be37ff0c44014dbaa64ec87fe005421f" id="block-be37ff0c44014dbaa64ec87fe005421f"></a>

These are custom ways of structuring data which are specified by the companies who make software. These are not standard across platforms, which means that to work with them you need to make your software understand the terms laid out by the API. Companies sometimes use an API if they want to restrict who can access their data – Facebook is a notable example. They have an API but restrict access, which means that independent software (like PlaceCal) can’t access their information, but big-budget companies like Ticketmaster can.
