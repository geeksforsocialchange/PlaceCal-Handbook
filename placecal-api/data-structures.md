# Data structures

Either specified by the query with these fields or returned from the server in this structure

```graphql
PingType: String


NeighbourhoodType {
  name: String
  abbreviatedName: String
  unit: String
  unitName: String
  unitCodeKey: String
  unitCodeValue: String
}

ContactType {
  name: String
  email: String
  telephone: String
}

OpeningHoursType {
  dayOfWeek: String
  opens: String
  closes: String
}

AddressType {
  streetAddress: String
  postalCode: String
  addressLocality: String
  addressRegion: String
  neighbourhood: NeighbourhoodType
}

PartnerType {
  id: ID
  name: String
  summary: String
  description: String
  accessibilitySummary: String
  logo: String
  url: String
  facebookUrl: String
  twitterUrl: String
  address: AddressType
  areasServed: [NeighbourhoodType]
  contact: ContactType
  openingHours: OpeningHoursType
	articles: [Article]
}

EventType {
  id: ID
  name: String
  summary: String
  description: String
  startDate: ISO88601Format
  endDate: ISO88601Format
  address: AddressType
  organizer: PartnerType
}

ArticleType {
  name: String
  headline: String
  text: String
  articleBody: String
  datePublished: ISO88601Format
  dateCreated: ISO88601Format
  dateUpdated: ISO88601Format
  providers: [Partners]
}
```
