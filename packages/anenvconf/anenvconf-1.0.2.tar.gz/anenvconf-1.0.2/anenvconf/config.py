import json
import os
import traceback

from enum import Enum

from . import exceptions


class ConfigValueType(Enum):
  STR  = 0
  INT  = 1
  BOOL = 2
  JSON = 3


class Config(object):
  def __init__(self, config_schema_dict):
    self._schema = config_schema_dict
    self._config = self._get_values()


  @staticmethod
  def _get_env(key, default=None):
    return os.environ[key] if key in os.environ else default


  @classmethod
  def _require_env(cls, key):
    result = cls._get_env(key, default=None)

    if result is None:
      raise exceptions.EnvironmentVarMissingException(
        'Environment variable {} is not set'.format(key)
      )

    return result


  def _get_values(self):
    all_items_present = True

    _config = { **self._schema }

    for k, v in _config.items():
      required = not (isinstance(v, dict) and "default" in v)
      default = v["default"] if required is False else None

      if required is True:
        val = self._require_env(k)
      else:
        val = self._get_env(k, default)

      if isinstance(v, dict) and "type" in v:
        value_type = v["type"]

        try:
          if value_type is ConfigValueType.JSON:
            val = json.loads(val)

            if "required_key" in v and v["required_key"] not in val:
              # We are missing the required key, remove the value
              # so that it will result in a config error
              val = None

          elif value_type is ConfigValueType.BOOL:
            val = bool(val)
          elif value_type is ConfigValueType.INT:
            val = int(val)

        except Exception as e:
          raise exceptions.InvalidValueException(
            'Config item {} value "{}" is not valid for type {}'.format(
              k,
              val,
              value_type.name.lower()
            ),
            traceback.format_exc()
          ) from e

      if val is not None:
        _config[k]["value"] = val
      else:
        if value_type is ConfigValueType.JSON and default is not None:
          _config[k]["value"] = json.loads(default)
        else:
          _config[k]["value"] = default

      if required is True and val is None:
        all_items_present = False

    if all_items_present is False:
      raise exceptions.RequiredVarMissingException(
        "Missing required configuration variables"
      )

    return _config


  def get_config(self):
    return self._config


  def get_config_text(self):
    d = { **self._config }
    for k, v in d.items():
      for k2, v2 in v.items():
        if isinstance(v2, Enum):
          d[k][k2] = v2.name.lower()

    return json.dumps(d)


  def get_value(self, key):
    return self._config[key]['value']
