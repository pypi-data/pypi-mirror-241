import email
import imaplib
import re
from dataclasses import dataclass, field

import undetected_chromedriver as uc
from decouple import config


class init:
    def driver(self):
        try:
            options = uc.ChromeOptions()
            options.add_argument("--headless")
            # No windows
            driver = uc.Chrome(version_main=109, options=options)
            # Yes windows
            # driver = uc.Chrome(version_main=109)
            return driver
        except Exception as err:
            raise Exception(f"Failed to start google {err=}, {type(err)=}")

    def get_code_email(self):
        try:
            email_address = "EMAIL_VERCEL"
            password = "PASS_VERCEL"
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(email_address, password)
            mail.select("inbox")
            status, email_ids = mail.search(None, "(UNSEEN)")
            email_id_list = email_ids[0].split()

            getCode = ""
            # Lee los correos no leídos
            for email_id in email_id_list:
                status, msg_data = mail.fetch(email_id, "(RFC822)")
                msg = email.message_from_bytes(msg_data[0][1])
                my_string = msg["from"]

                if re.search(r"GitHub <noreply@github.com>", my_string):
                    target_code = str(msg)
                    code = re.search(r"Verification code:\s(\S+)", str(target_code))
                    getCode = code.group(1)
                    print(getCode)

            mail.logout()
            return getCode
        except Exception as err:
            raise Exception(f"Failed to get code {err=}, {type(err)=}")
