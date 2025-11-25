# Add a Calendar

To add a Calendar, click the **Add New Calendar** button. This can be found on the **Calendars** page of the admin interface, or at the top of the **Dashboard**.&#x20;

If you can't see the **Add New Calendar** button, you may not have the correct account permissions. &#x20;

If you think you should have different account permissions, get in touch with the Organiser of your PlaceCal site (contact information can be found on the homepage of your PlaceCal site) or [contact the PlaceCal team](mailto:support@placecal.org).&#x20;

When you click **Add New Calendar** you will be brought to the **Create a new Calendar** page. This is where you can configure the calendar as well as associate it with an existing Partner. It is mandatory to associate a Calendar with a Partner, so you might need to [add a Partner](add-a-partner.md) first.&#x20;

## Details

### Partner Organiser

Choose a Partner from the dropdown list to associate with this Calendar. This Calendar will then be used as a source of information for the selected Partner's PlaceCal events. &#x20;

Partners can have multiple associated Calendars.&#x20;

### Name

This should be a human-readable name which accurately describes this Calendar. This is most useful for differentiating between Calendars where a partner has more than one source of event information, for example both Eventbrite and Google Calendar.&#x20;

### URL

This is where to put the URL of the calendar feed you'd like PlaceCal to import. [PlaceCal supports a number of different types of calendars and calendar feeds](../reference/supported-calendar-sources/). PlaceCal will periodically check for new events on the source calendar located at this URL and import them to PlaceCal.&#x20;

Each Calendar can only have one URL.&#x20;

### Importer mode

The Importer mode tells PlaceCal how to handle the URL you've given it. For most cases it'll do a good enough job working this out on its own—but if you get an error this is a good place to check.&#x20;

If you're using an .ics feed from a source that we don't specifically list, make sure you choose **Generic iCal / .ics** from the dropdown.&#x20;

## Location

### Default location

Set the default location for this Calendar here, by choosing a Partner from the dropdown. Note that only Partners with a set street address will appear in this list.&#x20;

### Where should location information for this Calendar come from?&#x20;

This determines how the location information for each event is handled by PlaceCal. You should choose the option which most closely reflects how the Calendar is used by the Partner—for example a Calendar which never usually has address information because all of the events happen in the same place should be set to either **Default location** or **Event where possible**. A Calendar for a Partner which never operates from the same place twice should be set to **Event**. &#x20;

* **Event where possible**: Use the address from each event. If the address is invalid or it doesn't have one, use the calendar's default location.
* **Event**: Use the address from each event. If an address is invalid or it doesn't have one, the event will import with no location.
* **Default location**: Always use the calendar's default location.
* **Room number**: Get a room number from the event's address, and overwrite the rest of the address with the calendar's default location.
* **No location**: Discard any address information.
* **Online only**: Discard any address information but retain web links.

## Public Contact Information

This information is used on the _public_ event listing pages in the "Problem with this listing? Let us know." contact link at the bottom of the show event page. Providing this information isn't compulsory.

## What next?

When you've filled out all of the relevant fields click **Create Calendar** to queue the Calendar for creation. If there are any errors or missing information you will be prompted to correct these fields, after which you'll need to click **Create Calendar** again to save the Calendar.&#x20;

Once the Calendar has been successfully created PlaceCal will queue it for import. Events might take a few minutes to show on the associated Partner's page, and only events in the future will be imported by PlaceCal.&#x20;
