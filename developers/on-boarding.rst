On Boarding
===========

PlaceCal has a lot of moving parts to line up before it can be worked on locally by a developer.

Prerequisites

- ruby
- rbenv
  - rbenv-ruby
  - ruby-gemset (hopefully at some point)
- postgresql
  + dev libraries
- node.js
  (for rails webpacker to work)
  + yarn

Steps taken

- install correct ruby for rbenv
- clone repo
- cd into dir
- bundle
- set up environment
    - pick a postgres user, host and password
    - put in an environment shell script
- create a user in postgres and a database with correct permissions
- source your environment
- run npm install yarn
- run yarn?
- run rails db:migrate
- run it again?
- run rails db:seed (and other scripts for importing base data)
- now run tests to check its okay

setting up admin
placecal employs some funky routing based on the URL domain
add `lvh.me` and `admin.lvh.me` to your hosts file
Now pop open a console and create a user
visit lvh.me:3000/sign_in and log in
you should be redirected to `admin.lvh.me` and see the admin dashboard

