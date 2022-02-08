# Database structures

This page covers the high level relationships as described by the database schema. These schema were mainly derived from following the core actions in the PlaceCal application and discerning how the data is gathered before being sent to the user.

## Sites

Sites represent the entry point for users to see what is going on in their local area. It is derived from the url domain so `hulme.placecal.org` has the site of `hulme`.

![Image of Site relationship](/assets/developers/db-sites.png "Image of Site relationship")

Sites have a primary neighbourhood indicated by a field on one of the SiteNeighbourhood records. I don't think there is any logic stopping more than one site_neighbourhood from being flagged at a time.

Neighbourhoods are recursively self-referential: this is how areas can contain areas like regions having many post-codes.

The hierarchy of the unit field in the Neighbourhood model is: country->region->county->district->ward.

## Users

Users come in two varieties: `root` and `citizen` where root is an application wide administrator of PlaceCal itself and citizen users exist to administer a given partner or site.

![User data structures](/assets/developers/db-users.png "User data structures")

Not sure if Tags is used? (See Tags section below)

## Events

Events are the core resource that has the most utility for the end-users: people who are looking for things to do near them.

![Event data Diagram](/assets/developers/db-events-overview.png "Event data Diagram")

### via path

Events as described by the `/events` action.

![Event via Site](/assets/developers/db-event-via-site.png "Event via Site")

This is one of the primary paths that events are returned to the user. It is tied to Site, which in turn is derived from the domain (see above).

## Partners

Partners are the entities that actually host the event. So a coding challenge (the event) will be hosted on a college campus (the partner).

![Partner relationship structure](/assets/developers/db-partner.png "Partner relationship structure")

(More description of partner)

### via path

End users can also access Partners via the action `/partners`. Has the same pattern as Event above.

![Partner via Site](/assets/developers/db-partner-via-site.png "Partner via Site")

## Calendars

Calendars are created by Partner admins to import events in bulk from an online calendar service.

![Calendar data structures](/assets/developers/db-calendar.png "Calendar data structures")

## Collections

(TBD)

## Tags

*(currently non-functional)*

Tags allow Site admins (coordinators) to associate a Partner with a set of properties.
