# Getting started

For a very basic test the following code will ping the server:

```sh
curl -v -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "query { ping }" }' \
  https://placecal.org/api/v1/graphql
```

The response will look something like:

```
// Some code< HTTP/2 200 
< server: nginx
< date: Thu, 17 Mar 2022 11:18:53 GMT
< content-type: application/json; charset=utf-8
< vary: Accept-Encoding
< x-frame-options: SAMEORIGIN
< x-xss-protection: 1; mode=block
< x-content-type-options: nosniff
< x-download-options: noopen
< x-permitted-cross-domain-policies: none
< referrer-policy: strict-origin-when-cross-origin
< vary: Accept, Origin
< etag: W/"4034a5865f578ab82fb98f15f75daaae"
< cache-control: max-age=0, private, must-revalidate
< x-request-id: 5fd1e66a-bbf9-4d13-a721-71d79824f78b
< x-runtime: 1.296813
< strict-transport-security: max-age=15724800; includeSubdomains
< 
* Connection #0 to host placecal-staging.org left intact
{"data":{"ping":"Hello World! The time is 2022-03-17 11:18:53 +0000"}}
```

## Getting a list of Partners

A more useful example may be getting a list of partners:

```sh
curl -v -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "query { partnerConnection { edges { node { id summary } } } }" }' \
  https://placecal.org/api/v1/graphql
```

At its heart the query looks like this. `node` lists the set of fields you want returned.

```graphql
query { 
  partnerConnection { 
    edges { 
      node { 
        id 
        summary 
      } 
    } 
  } 
}
```

Response should be:

```json
{
   "data":{
      "partnerConnection":{
         "edges":[
            {
               "node":{
                  "id":"123",
                  "summary":"Gendered Intelligence, established in 2008, is a registered charity that exists to increase understandings of gender diversity and improve trans people's quality of life."
               }
            },
            {
               "node":{
                  "id":"137",
                  "summary":"The Outside Project is an LGBTIQ+ Community Shelter, Centre and Domestic Abuse Refuge in response to those within the LGBTIQ+ community who feel endangered."
               }
            },
            {
               "node":{
                  "id":"145",
                  "summary":"Marvellous Mossley celebrates our town and lets people know about all the community activity happening here."
               }
            },
            {
               "node":{
                  "id":"146",
                  "summary":"Sibyls is a nationwide group for Christian transgender, non-binary and intersex people, partners and allies."
               }
            },
            {
               "node":{
                  "id":"148",
                  "summary":"Drab Drink is a monthly event for anyone on the trans* spectrum, their friends and allies. There is no dress code and most people do not present/dress."
               }
            },
            {
               "node":{
                  "id":"124",
                  "summary":"Distinction is a support organisation which is aimed at helping people who want to or who are supporting their partner that is Transgender, Non Binary or Gender Fluid"
               }
            }
         ]
			}
	}
}
```
