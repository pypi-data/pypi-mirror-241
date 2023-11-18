import requests
import json
import os
from enum import Enum
from dotenv import load_dotenv
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from http import HTTPStatus
from sms_message_local import SMSMessage


load_dotenv()
print("Environment variables loaded successfully.")
SMS_INFORU_LOCAL_PYTHON_PACKAGE_COMPONENT_ID = 208
SMS_INFORU_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME = "SMS_INFORU_LOCAL_PYTHON_PACKAGE"
DEVELOPER_EMAIL = "emad.a@circ.zone" 
SENDER_ID = "circlez"
LOG_ZI_TOKEN = os.getenv("LOGZIO_TOKEN")
print(f"LOGZIO_TOKEN: {LOG_ZI_TOKEN}")

logger = Logger.create_logger(object={
    'component_id': SMS_INFORU_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    'component_name': SMS_INFORU_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
})

class SMSMessageInforu(SMSMessage):
    def __init__(self, phone, message, inforu_auth_token):
        super().__init__(phone, message)
        self.inforu_auth_token = inforu_auth_token

    def send(self):
        try:
            payload = {
                "Data": {
                    "Message": self.message,
                    "Recipients": [
                        {
                            "Phone": self.phone
                        }
                    ],
                    "Settings": {
                        "Sender": SENDER_ID
                    }
                }
            }
            url = 'https://capi.inforu.co.il/api/v2/SMS/SendSms'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'{self.inforu_auth_token}',
                
            }
            print(f'{self.inforu_auth_token}')
            response = requests.post(url, headers=headers, json=payload)
            print(f"Response Code: {response.status_code}")
            print(f"Response Content: {response.text}")
            
            if response.status_code == HTTPStatus.OK:
                logger.info(f"SMS sent successfully to {self.phone}.")
                logger.info("Response: " + response.text)
            else:
                logger.error(f"SMS sending failed to {self.phone} with status code: {response.status_code}")

            return {"status": "success", "message": "Message sent successfully"}
        except requests.RequestException as re:
            logger.error(f"RequestException: {re}")
        except Exception as e:
            logger.exception("An error occurred during the InforU API operation.")
            logger.error(f"Exception Type: {type(e).__name__}, Message: {str(e)}")
            logger.end()
            raise
        finally:
            logger.end("SMS message send")

inforu_auth_token = "Basic ZW1hZC5hOjNiOGI3NjkyLWJmNjItNDg2MC1hOTU0LWVhYWNhOWM4ZmFjZg=="
sms_message = SMSMessageInforu(phone="+972545232179", message="Hello, this is a test message.", inforu_auth_token=inforu_auth_token)
sms_message.send()