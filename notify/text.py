#!/usr/bin/python

import sys
from twilio.rest import TwilioRestClient

def send_overview_message(body, number):
  ACCOUNT_SID = TWILIO_ACCOUNT_SID
  AUTH_TOKEN = "3651073f38f5c3411733f84e0e0d3adb"
  if ('TWILIO_ACCOUNT_SID' not in globals() or 'TWILIO_AUTH_TOKEN' not in globals() or 'TWILIO_FROM_NUMBER' not in globals()):
    raise NameError('Twilio settings not defined.')

  client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
  client.messages.create(
    to=number,
    from_=TWILIO_FROM_NUMBER,
    body=body,
  )

def main():
  if ('TWILIO_ACCOUNT_SID' not in globals()):
    raise NameError('To Number is not set.')
  print send_overview_message('Test Body', TWILIO_TO_NUMBER);

if __name__ == '__main__':
  # Include twilio settings in a settings.py file that will be included here.
  execfile('settings.py')
  main()
