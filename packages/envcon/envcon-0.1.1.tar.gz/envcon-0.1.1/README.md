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

Parse them with envcon...

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


## Handling prefixes

```python
TODO
```


For local development, use a `.env` file to override the default
configuration.

```bash
# .env
DEBUG=true
SECRET_KEY="not so secret"
```


## Why...?

### Why envvars?

See [The 12-factor App](http://12factor.net/config) section on
[configuration](http://12factor.net/config).

### Why not `os.environ`?

While `os.environ` is enough for simple use cases, a typical application
will need a way to manipulate and validate raw environment variables.
environs abstracts common tasks for handling environment variables.

environs will help you

- cast environment vars to the correct type
- specify required environment vars
- define default values
- parse list and dict values
- serialize your configuration

### Why use envcon?
TODO

## License

MIT licensed. 