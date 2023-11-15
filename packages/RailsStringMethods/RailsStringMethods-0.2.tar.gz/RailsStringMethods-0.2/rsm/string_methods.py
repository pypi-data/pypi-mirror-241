# string_methods.py

import re
import inflect

p = inflect.engine()

def pluralize(s):
    return p.plural(s)

def singularize(s):
    return p.singular_noun(s) or s

def truncate(s, length, ending='...'):
    return s if len(s) <= length else s[:length] + ending

def upcase(s):
    return s.upper()

def downcase(s):
    return s.lower()

def titleize(s):
    return ' '.join(word[0].upper() + word[1:].lower() for word in s.split())

def camelize(s, uppercase_first_letter=True):
    words = s.split('_')
    if not uppercase_first_letter:
        words[0] = words[0].lower()
    return ''.join(word.capitalize() for word in words)

def dasherize(s):
    return s.replace('_', '-')

def underscore(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def humanize(s):
    return s.replace('_', ' ').capitalize()

def tableize(s):
    return pluralize(underscore(s))

def parameterize(s, separator='-'):
    return re.sub(r'\W+', separator, s).lower()

def classify(s):
    return camelize(singularize(s))
