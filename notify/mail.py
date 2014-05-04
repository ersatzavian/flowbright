#!/usr/bin/python

import sys
import requests
import message

def send_overview_mail(subject, body, email):
  if ('MAILGUN_REST_URL' not in globals() or 'MAILGUN_API_KEY' not in globals()):
    raise NameError('Mailgun settings not set..')
  return requests.post(
    MAILGUN_REST_URL,
    auth=("api", MAILGUN_API_KEY),
    data={"from": "FlowBright <me@samples.mailgun.org>",
        "to": [email],
        "subject":subject,
        "text": body})

def main():
  if ('MAILGUN_TEST_MAIL' not in globals()):
    raise NameError('Test mail is not set.')
  print send_overview_mail('FlowBright: Your weekly water report', message.format_message(), MAILGUN_TEST_MAIL);

if __name__ == '__main__':
  # Include mailgun settings in a settings.py file that will be included here.
  execfile('settings.py')
  main()