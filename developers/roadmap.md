# PlaceCal v0.2 Roadmap

## Overview

The goal for the the next round of development is to modularise
PlaceCal, creating separate sites (or sub-sites) that target each set of
capabilities.

The current site will be split into the following components:

- `placecal.org` becomes the hub for PlaceCal as a whole, aimed at
  potential partners, developers, etc. This then accepts all event data
  we can get our hands on.
- `admin.placecal.org` becomes a unified administration frontend for
  administrators and moderators.
- `hulme.placecal.org` will become aimed more directly at Hulme
  residents. (We’ve yet to resolve the “Hulme, Moss Side and Rusholme”
  mouthful issue.)

We can then start considering more subdomains for each of our Age
Friendly Neighbourhoods and other curious regions, based on a subset of
the PlaceCal.org database:

- `moston.placecal.org`
- `milesplatting.placecal.org`
- `burnage.placecal.org`
- `mossley.placecal.org`

Finally, we are beginning to consider interest-based platforms as well:

- `cycling.placecal.org` or cyclemcr.org (for example), showing cycle
  routes over a larger area
- `agefriendlyhulme.org` (for example), showing the Hulme data but
  restricted to age friendly data, with more information about the
  board and how to get involved.

As part of this work we will also consider the suggestions and feedback
to date.

## PlaceCal.org

### Audience

Neighbourhood leaders, health commissioners, city councils, interest
groups, local partnerships. Anyone looking to set up PlaceCal in their
area or for their interest.

### Objectives

- Explain what PlaceCal is and how it works
- Find local PlaceCal instances for your area or interest
- Create a directory of partners, regions and places that are on the
  platform
- Find out about how to develop websites or apps with PlaceCal data
  (inc API docs)
- Updates and news about the project as a whole

### Work to be done

- Update current promotion material (website, slidedeck etc) to be more
  generic (i.e., not tied to Hulme).
- Review website information architecture, probably removing the Events
  listings and replacing with a list of active PlaceCal instances
  (currently just Hulme).
- Provide clear link to admin resources
- Add a blog with project news and updates
- Create a report based on the first round of tech audits to inform and
  refine the above
- Begin a basic overview of developer documentation (probably a
  placeholder for now)

## Admin.PlaceCal.org

(audience-1)=

### Audience

Regional admins (secretaries) and potential or current partner admins.

(objectives-1)=

### Objectives

- Partners can add calendars and places
- Secretaries can add calendars, places and partners, and edit partners
  in their region
- Get help adding information to PlaceCal for partner admins (docs)
- Get help adding partners and calendars for secretaries (docs)
- Find out contact information for PlaceCal as a whole (technical
  support)
- Partners can find out what’s involved in PlaceCal as a whole
- Ensure compliance with new Data Protection rules, and create a clear
  onboarding process with identified people
- Give secretaries and partners automated updates about their event
  data to improve reliability and validity

(work-to-be-done-1)=

### Work to be done

- Train a new calendar secretary
- Create training materials and documentation for partners
- Begin creation of training materials and documentation for
  secretaries
- Create secretary user interface
- Create partner user interface
- Create comprehensive onboarding process considering GDPR
- Support more APIs that came up in the Hulme research (Jadu, Artifax,
  Tribal Calendar…)
- Create notification system for admins

## Hulme.PlaceCal.org

(audience-2)=

### Audience

Hulme residents, organisations, businesses, and partners.

Need to resolve what to call this – probably three aliased sites to
begin with \[hulme/moss-side/rusholme\] which all have the same data.

(objectives-2)=

### Objectives

- Single, joined-up source of all events, places and partners in the
  area
- Information about Hulme as an area and how to get involved in the
  neighbourhood partnership
- Promotion of Hulme-based activities as a whole
- Review user feedback to date

(work-to-be-done-2)=

### Work to be done

- Reconsider home page of Hulme site
- Resolve naming issues
- Address front end bugs and tweaks for Hulme site
- Complete onboarding all Hulme organisations as admins

(placecal-org-1)=

## \*.PlaceCal.org

(audience-3)=

### Audience

Future region or interest-based groups - cycling, yoga, age-friendly,
etc.

Objectives

Consider the costs and tech commitment in setting subsites up

Create one or more as a pilot

(work-to-be-done-3)=

### Work to be done

- Make sure the subsites are well documented
- Create a report on the commitment involved
