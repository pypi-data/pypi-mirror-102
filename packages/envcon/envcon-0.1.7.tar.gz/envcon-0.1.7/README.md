# envcon: easy environment variables parsing


**Envcon** -  easy environment variables parsing.  
Envcon allows you to store configuration separated from your code, like 
[The Twelve-Factor App](https://12factor.net/config) suggests.  
Envcon heavily leaned on python type-hints and makes configuration simple and declerative. 

## Contents

- [Features](#features)
- [Install](#install)
- [Usage](#usage)
  - [Basic usage](#basic-usage)
  - [Prefix](#prefix)
  - [Optional](#optional)
  - [Another Source](#another-source)
- [Supported types](#supported-types)
  - [Casting](#casting)
- [Reading .env files](#reading-env-files)
- [Why...?](#why)
  - [Why environment variables?](#why-environment-variables)
  - [Why not os.environ?](#why-not-osenviron)
- [License](#license)

## Features

- Simple usage
- Type-casting
- Parse `.env` file as well as environment variables (`os.environ`)
- Default values
- Prefix

## Install

    pip install envcon

## Usage

Assuming these environment variables are set (or written in .env file)

```bash
export MONGO_USER=myMongoUser
export MONGO_PASSWORD=shh_its_a_secret
export SECRET_NUMBER=0.42
export ONE_TO_TEN=1,2,3,4,5,6,7,8,9,10
export IS_ENABLED=true
export URL=http://www.google.com
```

### Basic usage

```python3
from envcon import environment_configuration

@environment_configuration
class Configs:
    SECRET_NUMBER: float
    IS_ENABLED: bool
    ONE_TO_TEN: list[int] # on python 3.8 use List[int] (from typing import List) 

print(Configs.SECRET_NUMBER) # 0,42
print(type(Configs.SECRET_NUMBER)) # <class 'float'>
print(Configs.IS_ENABLED) # True
print(type(Configs.IS_ENABLED)) # <class 'bool'>
print(type(Configs.ONE_TO_TEN[0])) # <class 'int'> 
```

### Prefix

```python3
from envcon import environment_configuration

@environment_configuration(prefix="MONGO_")
class MongoConfiguration:
    USER: str
    PASSWORD: str

print(MongoConfiguration.USER) # myMongoUser
    
```

### Optional
All variables without default value are considered required.
Optional annotation suggests non-required variable and default set to `None`.

```python3
from typing import Optional
from envcon import environment_configuration

@environment_configuration(prefix="MONGO_")
class Configuration:
    NON_EXISTING_ENV_VER: Optional[int]

print(type(Configuration.NON_EXISTING_ENV_VER)) # <class 'NoneType'>
    
```

### Another Source
What if I want different source other than my `.env` file / `os.environ`? 
```python3
from envcon import configuration

my_config_dict = {
  "MONGO_USER": "myUser",
  "MONGO_PASSWORD": "myPassword",
}

@configuration(prefix="MONGO_", source=my_config_dict)
class MongoConfiguration:
    USER: str
    PASSWORD: str

print(MongoConfiguration.USER) # myUser
    
```

## Supported types

The following types hints are supported

Builtins and from `typing`:
- `str`
- `bool`
- `int`
- `float`
- `list`
- `list[T] # >= python 3.9. T = str/bool/int/float`
- `dict` 
- `List`
- `List[T]`
- `Dict`
- `Optional[T] # T = str/bool/int/float/dict/list/list[T]`

### Casting

#### int float
Simple casting. 
```python3
i, f = "42",  "4.2"
int(i)
float(i)
```

#### bool
The following case-insensitive strings are considered False, otherwise, True:
- "" (empty string)
- 0 
- n
- no
- ney 
- nan 
- null 
- not 
- false 
- off 
- ~

Its strongly suggested sticking with simple "false/true" and not Yaml/Java-Spring syntax (or more horrible fALsE).

#### list
List is parsed as comma separated values.  
If sub-type is provided (e.g. `list[int]`) each element will be converted as well.

#### dict
JSON string which loaded using json.loads()


## Reading `.env` files
By default, envcon will parse your `.env` file.
This feature is useful for local development.    
.env will not override your environment variables.  

You can turn this feature off:  
```python3
@environment_configuration(include_dot_env_file=False)
class MyConfigClass:
    ...
```


## Why...?

### Why environment variables?

See [The 12-factor App](http://12factor.net/config) section on
[configuration](http://12factor.net/config).

### Why not `os.environ`?
Basically, because this:
```python3
class Config:
    MAX_CONNECTION = int(os.environ.get("MAX_CONNECTION", "42"))
    TIMEOUT = float(os.environ.get("TIMEOUT", "4.2"))
    MY_PASSWORD = os.environ["MY_PASSWORD"] #required w/o default value
    OPTIONAL_URL = os.environ.get("OPTIONAL_URL", None)
    OPTIONAL_NUMBER = int(os.environ.get("OPTIONAL_NUMBER", "0")) or None
    NUMS_LIST = [int(i) for i in os.environ["NUMS_LIST"].splite(",")]
    NUMS_LIST_WITH_DEFAULT = [int(i) for i in os.environ.get("NUMS_LIST", "1,2,3").splite(",")]
```

will simply turn into this:
```python3
from typing import Optional, List

@environment_configuration
class Config:
    MAX_CONNECTION: int = 42
    TIMEOUT: float = 4.2
    MY_PASSWORD: str
    OPTIONAL_URL: Optional[str]
    OPTIONAL_NUMBER: Optional[int]
    NUMS_LIST: list[int] # in python 3.8 use List[int]
    NUMS_LIST_WITH_DEFAULT: list[int] = [1, 2, 3]
```

envcon will help you

- cast environment variables to the correct type
- specify required environment variables
- define default values
- parse list and dict

## License

MIT licensed.  