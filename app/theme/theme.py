from importlib import import_module
import app.config.theme as theme

target_theme = import_module('app.theme.{t}'.format(t=theme.target_theme))
