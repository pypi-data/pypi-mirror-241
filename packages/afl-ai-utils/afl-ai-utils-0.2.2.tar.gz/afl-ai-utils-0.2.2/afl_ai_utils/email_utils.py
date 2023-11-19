from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import pandas as pd


class Email():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def sendmail(self, subject: str, msg_body: str, data_frame: pd.DataFrame, from_email: str, to: str, cc: str, bcc: str, attachment_file: str):

        # emaillist = recipients+cc_recipients
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to
        msg['Cc'] = cc
        rcpt = cc.split(",") + bcc.split(",") + [to]

        html = """\
        <html>
            {0}
          <head></head>
          <body>
            {1}
          </body>
        </html>
        """.format(msg_body, data_frame.to_html())

        part1 = MIMEText(html, 'html')
        msg.attach(part1)

        attachment = attachment_file
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(attachment, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=attachment)
        msg.attach(part)


        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(msg['From'], rcpt, msg.as_string())

    def send_message(self, subject: str, msg_body: str, from_email: str, to: list, cc: list, attachment_file: str):
        attachment = attachment_file
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['Body'] = msg_body
        msg['From'] = from_email
        msg['To'] = to
        msg['Cc'] = cc

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(attachment, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=attachment)
        msg.attach(part)

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(attachment, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=attachment)
        msg.attach(part)


        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login(self.email, self.password)
            server.send_message(msg)

# e = Email()
# e.sendmail(subject=subject, data_frame=df, from_email=from_email, to=to, cc=cc, bcc=bcc, attachment_file=attachment_file, msg_body=body)
