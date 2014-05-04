#!/usr/bin/python

# Create a message for mail or text.

import sys
import keen
from pprint import pprint
from math import ceil
import dateutil.parser
from datetime import date
execfile('settings.py')

def format_message():
  if ('KEEN_PROJECT_ID' not in globals() or 'KEEN_READ_KEY' not in globals()):
    raise NameError('Keen settings not set.')
  keen.project_id = KEEN_PROJECT_ID
  keen.read_key = KEEN_READ_KEY
  usageSum = keen.sum("flow", "volume", "previous_7_days", None, "daily", [{'property_name':'volume', "operator":"gt", "property_value":"0"}])
  totalUsage = 0;
  for usage in usageSum:
    totalUsage += usage['value']

  output = ''
  for usage in usageSum:
    repeat = int(ceil(10 * (float(usage['value']) / totalUsage)))
    start = dateutil.parser.parse(usage['timeframe']['start'])
    usage_value = str(usage['value'])
    usage_bar = ('=' * repeat).ljust(10)
    output += '\n{}: {} {}'.format(start.strftime('%A'), usage_bar, usage['value'])
  return output;

def main():
  print format_message()

if __name__ == '__main__':
  # Include mailgun settings in a settings.py file that will be included here.
  main()