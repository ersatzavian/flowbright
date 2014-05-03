#!/usr/bin/python

# Create a message for mail or text.

import sys
import keen

def format_message():
  if ('KEEN_PROJECT_ID' not in globals() or 'KEEN_READ_KEY' not in globals()):
    raise NameError('Keen settings not set.')
  keen.project_id = KEEN_PROJECT_ID
  keen.read_key = KEEN_READ_KEY
  return keen.sum("purchase", target_property="price");

def main():
  print format_message()

if __name__ == '__main__':
  # Include mailgun settings in a settings.py file that will be included here.
  execfile('settings.py')
  main()