# API Rest of Books

## Requirements

- flask
- flask-restful
- flask-sqlalchemist
- flask-marshmallow


## Migrate class

from app import db
db.create_all()

## Set Enviroment

### Windows
set CONFIGURATION_SETUP=config.DevelopmentConfig

### Linux MacOS

export CONFIGURATION_SETUP="config.DevelopmentConfig"