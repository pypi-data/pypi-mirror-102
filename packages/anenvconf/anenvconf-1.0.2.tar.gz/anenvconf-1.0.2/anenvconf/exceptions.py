class ConfigException(Exception):
  def __init__(self, text, trace=None):
    super().__init__(text)
    self.text = text
    self.trace = trace


class InvalidValueException(ConfigException):
  pass


class EnvironmentVarMissingException(ConfigException):
  pass


class RequiredVarMissingException(ConfigException):
  pass
