# Questor
[![Build Status](https://travis-ci.com/gchilczuk/questor.svg?branch=develop)](https://travis-ci.com/gchilczuk/questor)

Questor is very simple application for simple Cicada-like games.
The game can be prepared only by the website administrator. There can be many players who, by inserting pass-codes, can get access to tasks and riddles.

### How to use it?
There is docker-compose file provided to easily run the application on your own

#### Deployment

##### Development
`docker-compose up --build`

#### Production
You need to specify a bunch of environemt variables

`DATABASE_URL` - according to [dj-database-url](https://github.com/kennethreitz/dj-database-url#url-schema)

`ALLOWED_HOSTS` - list of allowed hosts for application

`SECRET_KEY` - secret key for application

TBD

#### Game preparation
To be determined
