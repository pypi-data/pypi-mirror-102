# environs: simplified environment variable parsing


**envcon**. easy environment variables parsing.
envcon allows you to store configuration separated from your code, like 
[The Twelve-Factor App](https://12factor.net/config) suggests.

## Contents

- [Features](#features)
- [Install](#install)
- [Basic usage](#basic-usage)
- [Supported types](#supported-types)
- [Reading .env files](#reading-env-files)
  - [Reading a specific file](#reading-a-specific-file)
- [Handling prefixes](#handling-prefixes)
- [Variable expansion](#variable-expansion)
- [Validation](#validation)
- [Deferred validation](#deferred-validation)
- [Serialization](#serialization)
- [Defining custom parser behavior](#defining-custom-parser-behavior)
- [Usage with Flask](#usage-with-flask)
- [Usage with Django](#usage-with-django)
- [Why...?](#why)
  - [Why envvars?](#why-envvars)
  - [Why not os.environ?](#why-not-osenviron)
  - [Why another library?](#why-another-library)
- [License](#license)

## Features

- Type-casting
- Parse `.env` files as well as environment variables (`os.environ`) (useful for development)
- Validation
- Default values

## Install

    pip install envcon

## Basic usage

Assuming these environment variables are set (or written in .env file)

```bash
export MONGO_USER=myMongoUser
export MONGO_PASSWORD=shh_its_a_secret
export SECRET_NUMBER=0.42
export ONE_TO_TEN=1,2,3,4,5,6,7,8,9,10
export IS_ENABLED=true
export URL=http://www.google.com
```

Parse them with environs...

```python3
from envcon import environment_configuration

@environment_configuration
class Configs:
    SECRET_NUMBER: float
    IS_ENABLED: bool
    ONE_TO_TEN: list[int] # in python 3.8 use List[int] (from typing import List) 

print(Configs.SECRET_NUMBER) # 0,42
print(type(Configs.SECRET_NUMBER)) # <class 'float'>
print(Configs.IS_ENABLED) # True
print(type(Configs.IS_ENABLED)) # <class 'bool'>
print(type(Configs.ONE_TO_TEN[0])) # <class 'int'> 

@environment_configuration(prefix="MONGO_")
class MongoConfiguration:
    USER: str
    PASSWORD: str

print(MongoConfiguration.USER) # myMongoUser
    
```

## Supported types

The following types are supported in type-hinting

Builtins:
- `str`
- `bool`
- `int`
- `float`
- `list`
- `dict` 

From `typing`

## Reading `.env` files

```bash
# .env
DEBUG=true
PORT=4567
```

Call `Env.read_env` before parsing variables.

```python
from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()

env.bool("DEBUG")  # => True
env.int("PORT")  # => 4567
```

### Reading a specific file

By default, `Env.read_env` will look for a `.env` file in current
directory and (if no .env exists in the CWD) recurse
upwards until a `.env` file is found.

You can also read a specific file:

```python
from environs import Env

with open(".env.test", "w") as fobj:
    fobj.write("A=foo\n")
    fobj.write("B=123\n")

env = Env()
env.read_env(".env.test", recurse=False)

assert env("A") == "foo"
assert env.int("B") == 123
```

## Handling prefixes

```python
# export MYAPP_HOST=lolcathost
# export MYAPP_PORT=3000

with env.prefixed("MYAPP_"):
    host = env("HOST", "localhost")  # => 'lolcathost'
    port = env.int("PORT", 5000)  # => 3000

# nested prefixes are also supported:

# export MYAPP_DB_HOST=lolcathost
# export MYAPP_DB_PORT=10101

with env.prefixed("MYAPP_"):
    with env.prefixed("DB_"):
        db_host = env("HOST", "lolcathost")
        db_port = env.int("PORT", 10101)
```

## Variable expansion

```python
# export CONNECTION_URL=https://${USER:-sloria}:${PASSWORD}@${HOST:-localhost}/
# export PASSWORD=secret
# export YEAR=${CURRENT_YEAR:-2020}

from environs import Env

env = Env(expand_vars=True)

connection_url = env("CONNECTION_URL")  # =>'https://sloria:secret@localhost'
year = env.int("YEAR")  # =>2020
```


## Deferred validation

By default, a validation error is raised immediately upon calling a parser method for an invalid environment variable.
To defer validation and raise an exception with the combined error messages for all invalid variables, pass `eager=False` to `Env`.
Call `env.seal()` after all variables have been parsed.

```python
# export TTL=-2
# export NODE_ENV='invalid'
# export EMAIL='^_^'

from environs import Env
from marshmallow.validate import OneOf, Email, Length, Range

env = Env(eager=False)

TTL = env.int("TTL", validate=Range(min=0, max=100))
NODE_ENV = env.str(
    "NODE_ENV",
    validate=OneOf(
        ["production", "development"], error="NODE_ENV must be one of: {choices}"
    ),
)
EMAIL = env.str("EMAIL", validate=[Length(min=4), Email()])

env.seal()
# environs.EnvValidationError: Environment variables invalid: {'TTL': ['Must be greater than or equal to 0 and less than or equal to 100.'], 'NODE_ENV': ['NODE_ENV must be one of: production, development'], 'EMAIL': ['Shorter than minimum length 4.', 'Not a valid email address.']}
```

`env.seal()` validates all parsed variables and prevents further parsing (calling a parser method will raise an error).


## Usage with Flask

```python
# myapp/settings.py

from environs import Env

env = Env()
env.read_env()

# Override in .env for local development
DEBUG = env.bool("FLASK_DEBUG", default=False)
# SECRET_KEY is required
SECRET_KEY = env.str("SECRET_KEY")
```

Load the configuration after you initialize your app.

```python
# myapp/app.py

from flask import Flask

app = Flask(__name__)
app.config.from_object("myapp.settings")
```

For local development, use a `.env` file to override the default
configuration.

```bash
# .env
DEBUG=true
SECRET_KEY="not so secret"
```

Note: Because environs depends on [python-dotenv](https://github.com/theskumar/python-dotenv),
the `flask` CLI will automatically read .env and .flaskenv files.


## Why...?

### Why envvars?

See [The 12-factor App](http://12factor.net/config) section on
[configuration](http://12factor.net/config).

### Why not `os.environ`?

While `os.environ` is enough for simple use cases, a typical application
will need a way to manipulate and validate raw environment variables.
environs abstracts common tasks for handling environment variables.

environs will help you

- cast envvars to the correct type
- specify required envvars
- define default values
- validate envvars
- parse list and dict values
- parse dates, datetimes, and timedeltas
- parse expanded variables
- serialize your configuration to JSON, YAML, etc.

### Why use envcon?


## License

MIT licensed. 