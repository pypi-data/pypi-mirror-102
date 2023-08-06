# anenvconf

A python3 module for defining a config schema and importing it from environment variables.

## Install

```shell
python3 -m pip install anenvconf
```

## Usage

Import the modules key classes, define the config schema and create a Config object with the schema.

```python
from anenvconf import Config, ConfigValueType
config_schema = {
  'jsonvar1': {
    'type': ConfigValueType.JSON,
    'required_key': 'important_key'
  },
  'stringvar1': {},
  'stringvar2': {
    'default': "Default value in case setting this variable is not mandatory"
  },
  'boolvar1': {
    'type': ConfigValueType.BOOL,
    'default': True
  }
}

config = None

try:
  config = Config(config_schema)

except anenvconf.exceptions.InvalidValueException as e:
  print("Got an invalid value: ", e.text)

except anenvconf.exceptions.EnvironmentVarMissingException as e:
  print("A required environment variable is missing: ", e.text)

except anenvconf.exceptions.RequiredVarMissingException as e:
  print("A required value inside a variable is missing: ", e.text)

if config is not None:
  print(config.get_value("stringvar2"))
```

## Schema

The schema is given as a dict, where the keys are the environment variables to read, and each of
their values is an another dict that defines details about how to handle that variable. The dict that
defines the handling can have the following keys:

`type` is the data type of the variable value, defined as `ConfigValueType`. Supported types are `str` (default),
`bool`, `int`and `json`.

`default` is the default value of the variable. If `default`is not set, the environment variable is treated
as mandatory. If you want to have optional variables, you can for example set `default` to `None`.

`required_key` defines a key that is required in the keys of a `json` type of value. If the key is not found, an exception is raised.

Example:

```python
example_config_schema = {
  # Use "type" to define ConfigValueType, string is assumed by default.
  'env_variable_name1': {
    'type': ConfigValueType.JSON
  },

   # Default data type is string
  'env_variable_name2': {},

  # If default value exists, value from environment variable is not required.
  # Otherwise the key-value pair is expected to be found in the env variables.
  'env_variable_name3': {
    'type': ConfigValueType.JSON,
    'default': '{}'
  }
}
```
