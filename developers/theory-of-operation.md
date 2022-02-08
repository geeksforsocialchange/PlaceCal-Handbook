# Theory of Operation

Theory of how it works, yo

Here are the basic data structures driving PlaceCal

## Users

Basic user holding. has a type field that is set to either 'citizen\` or 'root'. root is admin.

## Geography

How locations are stored.

### Sites

A marker for defining a particular local to organise events within.

### Neighbourhoods

Is a self referential tree allowing strata of zones to be contained within zones within zones.
In the UK this takes the form of Country->Region->County->District->Ward. Country being largest and Ward being smallest.

### SiteNeighbourhoods

A join table linking sites >-\< neighbourhoods. The

Baiscally this:
neighbourhoods are imported from a dataset stored in repo
placecal admins can create themselves from the console.
they can also create each other (as either global or site-scoped)
site admins create partner and partner-admins

casual users can browse the events in their area
they can also sign up some how? and register interest? no?

partner admins can configure their organisations
they can also post new events
they can also import events from pre-existing calendars
