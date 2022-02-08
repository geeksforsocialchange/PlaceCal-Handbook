# Developer Guide

```{toctree}
:hidden: true

glossary
developers/user-access
developers/roadmap
developers/data-structures
experimental/routing
```

## Getting started

Read the {doc}`Glossary <glossary>`.

### Tools

We use:

- [Trello for project
  management](https://trello.com/b/mA4Rwzum/dev-backlog)
- Sketch + Dropbox for UI files (get Kim to set you up).
- [GitHub for
  code](https://github.com/geeksforsocialchange/PlaceCal)
- Rollbar for error reporting
- [Sign up on PlaceCal](https://placecal.org/users) and get Kim to
  make you an admin.

### Hosting / Environment

- Rails 5 / Ruby 2.4 / postgresql
- `rails db:setup db:migrate seed:migrate`
- `rails import:all_events`
- To log in you need to go to `/users` and then `/superadmin` (for
  now!)
- Prod server is a [Digital Ocean box running this
  setup](https://gist.github.com/kimadactyl/5c277d2698f754edf3daa5fd84488851)
- `master` branch auto-deploys to our staging server
  <http://placecal-staging.org>. `production` branch deploys manually
  to the production server.

### Notes

We’re using the [Mountain
View](https://github.com/devnacho/mountain_view) gem for frontend
components. Anything and everything reusable should be encapsulated in a
component and given some mocks to test it. Components are at
<https://placecal.org/styleguide>. For each component add a line to
`test/controllers/components_test.rb`: easy tests!

Important information should be added in a [seed
migration](https://github.com/harrystech/seed_migration).

Ideally the Sketch art should export directly into our repo file
structure somehow, so if we can work towards having a master Sketch file
for anything live then take the time to do it.

## User access

See the {doc}`User Access Guide </developers/user-access>`.

## Roadmap

See the current {doc}`Roadmap <developers/roadmap>`.

## Getting API access

This is still in development. Drop us an email to have a chat about it.
