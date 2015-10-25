import yaml
import os
from ansible import errors

vars_path = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'vars',
        'main.yml',
    )
)

with open(vars_path, 'r') as f:
    contents = f.read()

vars = yaml.load(contents)

shortcuts = vars['OSX_SHORTCUTS']

def osx_hotkey(in_keys):
    translated_keys = []
    for in_key in in_keys:
        if shortcuts[in_key]:
            translated_keys.append(shortcuts[in_key])
        else:
            translated_keys.append(in_key)
    translated = ''.join(translated_keys)
    return translated

class FilterModule(object):
    '''nrser.osx jinja2 filters'''

    def filters(self):
        return {
            'osx_hotkey': osx_hotkey,
        }
