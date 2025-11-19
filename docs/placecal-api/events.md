# Events

## Show

```javascript
let queryString = `
  query Event($id: ID!) { 
    event(id: $id) { 
      id
      name
      summary
      description
      startDate
      endDate
      address {
        streetAddress
        postalCode
        addressLocality
        addressRegion
      }
      organizer {
        id
        name
      }
    }
  }`;

query(queryString, { id: 2 })
  .then( (response) => {
    console.log(JSON.stringify(response, null, 2));
  });

/* response */

{
  "data": {
    "event": {
      "id": "2",
      "name": "event 0: A summary of an event",
      "summary": "event 0: A summary of an event",
      "description": "A longer description of this event",
      "startDate": "2022-02-10 00:00:00 +0000",
      "endDate": null,
      "address": {
        "streetAddress": "123 A Street, A place",
        "postalCode": "SE2 0QG",
        "addressLocality": "Belvedere",
        "addressRegion": "London (region)"
      },
      "organizer": null
    }
  }
}
```

## Index

Shows a set of events in manageable chunks. Can be used to load events on demand for pagination/infinite scroll. There is an explanation of how connections work in comments.

```javascript
let queryString = `
  query EventConnection($first: Int, $after: String) { 
    eventConnection(first: $first, after: $after) {
      pageInfo {
        hasNextPage
				endCursor
      }
      edges {
        cursor
        node {
          id
          name
          summary
          description
          startDate
          endDate
          address {
            streetAddress
            postalCode
            addressLocality
            addressRegion
          }
          organizer {
            id
            name
          }
        }
      }
    }
  }`;

/* return the first block of events */
query(queryString, {first: 5})
  .then( (response) => {
    console.log(JSON.stringify(response, null, 2));
  });

/* first response */
"data": {
    "eventConnection": {
      "pageInfo": {
        "hasNextPage": true
      },
      "edges": [
        {
          "cursor": "MQ",
          "node": {
            "id": "2",
            "name": "event 0: A summary of an event",
            "summary": "event 0: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        },
        {
          "cursor": "Mg",
          "node": {
            "id": "3",
            "name": "event 1: A summary of an event",
            "summary": "event 1: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        },
        {
          "cursor": "Mw",
          "node": {
            "id": "4",
            "name": "event 2: A summary of an event",
            "summary": "event 2: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        },
        {
          "cursor": "NA",
          "node": {
            "id": "5",
            "name": "event 3: A summary of an event",
            "summary": "event 3: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        },
        {
          "cursor": "NQ",
          "node": {
            "id": "6",
            "name": "event 4: A summary of an event",
            "summary": "event 4: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        }
      ]
    }
  }
}

/*
Notes on connection pagination:
Cursors are GraphQL's way of identifying a record in a connection.
They act like IDs but are more complicated for reasons.

Input parameters
  first: limit the number of records to return
  after: only fetch records that follow on from this cursor

In the response each record is wrapped in an 'edge' that contains 
the GQL cursor identifier.

pageInfo:
  hasNextPage: (boolean) there are records that follow from this block
  endCursor: (string) the cursor of the last record retrieved 
*/

/* then to get the next block of events */
query(queryString, {first: 5, after: "NQ"})
  .then( (response) => {
    console.log(JSON.stringify(response, null, 2));
  });

/* second response */
{
  "data": {
    "eventConnection": {
      "pageInfo": {
        "hasNextPage": true
      },
      "edges": [
        {
          "cursor": "Ng",
          "node": {
            "id": "7",
            "name": "event 5: A summary of an event",
            "summary": "event 5: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        },
        {
          "cursor": "Nw",
          "node": {
            "id": "8",
            "name": "event 6: A summary of an event",
            "summary": "event 6: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        },
        {
          "cursor": "OA",
          "node": {
            "id": "9",
            "name": "event 7: A summary of an event",
            "summary": "event 7: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        },
        {
          "cursor": "OQ",
          "node": {
            "id": "10",
            "name": "event 8: A summary of an event",
            "summary": "event 8: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        },
        {
          "cursor": "MTA",
          "node": {
            "id": "11",
            "name": "event 9: A summary of an event",
            "summary": "event 9: A summary of an event",
            "description": "A longer description of this event",
            "startDate": "2022-02-10 00:00:00 +0000",
            "endDate": null,
            "address": {
              "streetAddress": "123 A Street, A place",
              "postalCode": "SE2 0QG",
              "addressLocality": "Belvedere",
              "addressRegion": "London (region)"
            },
            "organizer": null
          }
        }
      ]
    }
  }
}
```

## Filter

Events can be filtered by date range, neighbourhood or tag. All events are returned in ascending order of start date.

```javascript
let queryString = `
  query EventsByFilter(
    $fromDate: String, 
    $toDate: String, 
    $neighbourhoodId: Int, 
    $tagId: Int) 
  {

    eventsByFilter(
      fromDate: $fromDate, 
      toDate: $toDate, 
      neighbourhoodId: $neighbourhoodId, 
      tagId: $tagId) 
    { 
      id
      name
      summary
      description
      startDate
      endDate
      address {
        streetAddress
        postalCode
        addressLocality
        addressRegion
      }
      organizer {
        id
        name
      }
    }
  }`;

/* 
notes on event filter
The filter has the following parameters:
  fromDate: the initial start point. defaults to 
	  date request was made. can be in the past.
    format is YYYY-MM-DD HH:MM
  toDate: the end limit of query. must be after fromDate
  neighbourhoodId: scope events to be in a 
    neighbourhood. returns events in BOTH
    the address and service area.
  tagId: scope events to only one tag
*/

query(queryString)
  .then( (response) => {
    console.log(JSON.stringify(response, null, 2));
  });

/* response */
{
  "data": {
    "eventsByFilter": []
  }
}
```

Some sample GQL queries that show the various input fields. The fields can be combined in one query.

```graphql

# default query with no args
query {
	eventsByFilter {
	   id
	   name
	   startDate
	}

# query with fromDate
query {
	eventsByFilter(fromDate: "1985-01-01 00:00") {
	   id
	   name
	   startDate
	}

# query with fromDate and toDate
query {
	eventsByFilter(fromDate: "1990-01-01 00:00", toDate: "1990-03-01 00:00") {
	  id
	  name
	  startDate
	}

# query with neighbourhoodId
query {
  eventsByFilter(neighbourhoodId: 123) {
    id
    name
  }
}

# query with tagId
query {
  eventsByFilter(tagId: #{have_tag.id}) {
    id
    name
  }
}
```
