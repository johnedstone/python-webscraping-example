# sendinblue_example_sendmail.py
"""
Reference:
    https://developers.brevo.com/reference/sendtransacemail
    There is curl example there that could be uses as well, with the Blues notecard
"""
import os
import sys
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

from dotenv import load_dotenv

load_dotenv('.debug.env')

DEBUG = True

API_KEY = os.getenv('API_KEY_EMAIL')
TO_NAME = os.getenv('TO_NAME')
TO_EMAIL = os.getenv('TO_EMAIL')
SENDER_NAME = os.getenv('SENDER_NAME')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
REPLY_TO_NAME = os.getenv('REPLY_TO_NAME')
REPLY_TO_EMAIL = os.getenv('REPLY_TO_EMAIL')

for n, ea in enumerate([API_KEY, TO_NAME, TO_EMAIL, SENDER_NAME, SENDER_EMAIL, REPLY_TO_NAME, REPLY_TO_EMAIL]):
        if DEBUG:
            print(f'{n}: {ea}')
        if not ea:
            sys.exit()

def send_transactional_email(to_name=TO_NAME,
        to_email=TO_EMAIL,
        sender_name=SENDER_NAME,
        sender_email=SENDER_EMAIL,
        reply_to_name=REPLY_TO_NAME,
        reply_to_email=REPLY_TO_EMAIL,
        subject="Rosco's Hello World",
        msg='Roscoe says hello!'):
    try:
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = API_KEY 
    
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        subject = subject
        html_content = f"<html><body><div>{msg}</div></body></html>"
        sender = {"name": sender_name,"email": sender_email}
        to = [{"name":to_name, "email": to_email}]
        reply_to = {"email":reply_to_email,"name":reply_to_name}
        #cc = [{"email":"example@example.com","name":"John Doe"}]
        #bcc = [{"name":"John Doe","email":"example@example.com"}]
        #headers = {"Some-Custom-Name":"unique-id-1234"}
        #params = {"parameter":"My param value","subject":"New Subject"}
        #send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to,
                reply_to=reply_to,
                html_content=html_content, sender=sender, subject=subject)
    
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    
    except Exception as e:
        print(f'Exception: {e}')

if __name__ == '__main__':
    send_transactional_email()

# vim: ai ts=4 sw=4 sts=4 et nu
