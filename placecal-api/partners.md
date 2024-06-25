# Partners

## Show

```javascript
let queryString = `
query Partner($id: ID!) { 
  partner(id: $id) {
    id
    name
    summary
    description
    accessibilitySummary
    logo
    url
    facebookUrl
    twitterUrl
    address {
      streetAddress
      postalCode
      addressLocality
      addressRegion
      neighbourhood {
        name
        abbreviatedName
        unit
        unitName
        unitCodeKey
        unitCodeValue
      }
    }
    contact {
      name
      email
      telephone
    }
    openingHours {
      dayOfWeek
      opens
      closes
    }
    areasServed {
      name
      abbreviatedName
      unit
      unitName
      unitCodeKey
      unitCodeValue
    }
  }
}`;

query(queryString, { id: 10 })
  .then( (response) => {
    console.log(JSON.stringify(response, null, 2));
  });

/* typical response */
{
  "data": {
    "partner": {
      "id": "10",
      "name": "London Partner",
      "summary": "A Partner in London",
      "description": "Longer description of London Partner is here",
      "accessibilitySummary": "",
      "logo": "",
      "url": "",
      "facebookUrl": "",
      "twitterUrl": "https://twitter.com/",
      "address": null,
      "contact": {
        "name": "Me",
        "email": "me@example.com",
        "telephone": ""
      },
      "openingHours": [],
      "areasServed": [
        {
          "name": "London",
          "abbreviatedName": null,
          "unit": "region",
          "unitName": "London",
          "unitCodeKey": "RGN19CD",
          "unitCodeValue": "E12000007"
        }
      ]
    }
  }
}
```

## Index

Show a sample request returning all events for a given date range with a given partner and tag.

```javascript
let queryString = `
  query PartnerConnection($first: Int, $after: String) { 
    partnerConnection(first: $first, after: $after) {
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
          accessibilitySummary
          logo
          url
          facebookUrl
          twitterUrl
          address {
            streetAddress
            postalCode
            addressLocality
            addressRegion
            neighbourhood {
              name
              abbreviatedName
              unit
              unitName
              unitCodeKey
              unitCodeValue
            }
          }
          contact {
            name
            email
            telephone
          }
          openingHours {
            dayOfWeek
            opens
            closes
          }
          areasServed {
            name
            abbreviatedName
            unit
            unitName
            unitCodeKey
            unitCodeValue
          }
        }
      }
    }
  }`;

/* 
The partnerConnection pagination works the same as event pagination above
*/

/* return the first block of partners */
query(queryString, {first: 3})
  .then( (response) => {
    console.log(JSON.stringify(response, null, 2));
  })

/* response */
{
  "data": {
    "partnerConnection": {
      "pageInfo": {
        "hasNextPage": true,
        "endCursor": "Mw"
      },
      "edges": [
        {
          "cursor": "MQ",
          "node": {
            "id": "12",
            "name": "Service Area Partner",
            "summary": "",
            "description": "",
            "accessibilitySummary": "",
            "logo": "",
            "url": "",
            "facebookUrl": "",
            "twitterUrl": "https://twitter.com/",
            "address": null,
            "contact": {
              "name": "Me",
              "email": "me@example.com",
              "telephone": ""
            },
            "openingHours": [],
            "areasServed": [
              {
                "name": "London",
                "abbreviatedName": null,
                "unit": "region",
                "unitName": "London",
                "unitCodeKey": "RGN19CD",
                "unitCodeValue": "E12000007"
              }
            ]
          }
        },
        {
          "cursor": "Mg",
          "node": {
            "id": "10",
            "name": "London Partner",
            "summary": "A Partner in London",
            "description": "Longer description of London Partner is here",
            "accessibilitySummary": "",
            "logo": "",
            "url": "",
            "facebookUrl": "",
            "twitterUrl": "https://twitter.com/",
            "address": null,
            "contact": {
              "name": "Me",
              "email": "me@example.com",
              "telephone": ""
            },
            "openingHours": [],
            "areasServed": [
              {
                "name": "London",
                "abbreviatedName": null,
                "unit": "region",
                "unitName": "London",
                "unitCodeKey": "RGN19CD",
                "unitCodeValue": "E12000007"
              }
            ]
          }
        },
        {
          "cursor": "Mw",
          "node": {
            "id": "13",
            "name": "Inner London Partner",
            "summary": "Summary of outer london partner",
            "description": "",
            "accessibilitySummary": "",
            "logo": "",
            "url": "",
            "facebookUrl": "",
            "twitterUrl": "https://twitter.com/",
            "address": null,
            "contact": {
              "name": "",
              "email": "",
              "telephone": ""
            },
            "openingHours": [
              {
                "dayOfWeek": "Monday",
                "opens": "09:00:00",
                "closes": "17:00:00"
              },
              {
                "dayOfWeek": "Tuesday",
                "opens": "09:00:00",
                "closes": "17:00:00"
              },
              {
                "dayOfWeek": "Friday",
                "opens": "09:00:00",
                "closes": "17:00:00"
              }
            ],
            "areasServed": [
              {
                "name": "Inner London",
                "abbreviatedName": null,
                "unit": "county",
                "unitName": "Inner London",
                "unitCodeKey": "CTY19CD",
                "unitCodeValue": "E13000001"
              }
            ]
          }
        }
      ]
    }
  }
}
```
