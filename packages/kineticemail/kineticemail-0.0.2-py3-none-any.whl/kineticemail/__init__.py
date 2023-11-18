#
# Kinetic Email - 2023
#    Copyright 2023 - Kinetic Seas Inc, Chicago Illinois
#    Edward Honour, Joseph Lehman
#

import json
import imaplib
import smtplib
from smtplib import SMTPException, SMTPAuthenticationError, SMTPServerDisconnected
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import socket
from email.header import decode_header
from pathlib import Path
import tempfile
import smtplib
from email.message import EmailMessage
import os
from bs4 import BeautifulSoup

__version__ = '0.4'

# Add a tiny bit of compatibility to pyPdf

__all__ = """PdfWriter PdfReader PdfObject PdfName PdfArray
             PdfTokens PdfParseError PdfDict IndirectPdfDict
             PdfString PageMerge""".split()
class KineticEmail:
    def __init__(self, connection_path):
        pass

    @staticmethod
    def connect_imap(server, email_address, email_password):
        try:
            imap = imaplib.IMAP4_SSL(server)
            imap.login(email_address, email_password)
            return imap
        except imaplib.IMAP4.abort as e:
            return {"error_code": "9000", "error_msg": "IMAP4 connection aborted: " + str(e), "data": {}}
        except imaplib.IMAP4.error as e:
            return {"error_code": "9000", "error_msg": "IMAP4 error occurred: " + str(e), "data": {}}
        except socket.gaierror as e:
            return {"error_code": "9000", "error_msg": "Address-related socket error occurred: " + str(e), "data": {}}
        except socket.timeout as e:
            return {"error_code": "9000", "error_msg": "Socket timeout occurred: " + str(e), "data": {}}
        except socket.error as e:
            return {"error_code": "9000", "error_msg": "Socket error occurred: " + str(e), "data": {}}
        except Exception as e:  # A generic catch-all for any other exceptions
            return {"error_code": "9000", "error_msg": "An unexpected error occurred: " + str(e), "data": {}}

    #
    # Function to download an attachment from an email and save to
    # the filesystem.
    #
    @staticmethod
    def download_attachment(cls, emailPart, file_path):
        output_file_name = file_path + '/' + emailPart.get_filename()
        open(output_file_name, 'wb').write(emailPart.get_payload(decode=True))
        return output_file_name

    #
    # Function to move a file from one folder (mailbox) to another.
    #
    @staticmethod
    def move_file_mailbox(self, imap, messageNum, targetMailbox):
        status, email_data = imap.fetch(messageNum, '(UID)')
        uid = email_data[0].split()[-1].decode("utf-8")  # Get the UID
        uid = uid[:-1]
        a, b = imap.uid('COPY', uid, targetMailbox)
        self.imap.uid('STORE', uid, '+FLAGS', '(\Deleted)')

    #
    # Get all messages from an imap mailbox and return the
    # status of the mailbox request and messages.
    #
    @staticmethod
    def get_imap_messages(imap, mailbox, search="ALL"):
        imap.select(mailbox)
        status, messages = imap.search(None, search)
        return status, messages

    #
    # Process all message from an imap server.
    # Legacy POC code.
    #

    @staticmethod
    def get_email_attachments(imap, msgnums):
        for msgnum in msgnums[0].split():
            _, data = imap.fetch(msgnum, '(BODY.PEEK[])')
            message = email.message_from_bytes(data[0][1])
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    pass
                if part.get_content_maintype() != "multipart" and part.get('Content-Disposition') is not None:
                    KineticEmail.download_attachment(part, "/tmp")

    #
    # Close the imap mailbox connection.
    #
    @staticmethod
    def close_imap_mail(imap):
        imap.expunge()
        imap.close()
        imap.logout()

    @staticmethod
    def get_mailbox_messages_vault(connection_vault_path, attachment_path='', mailbox="Inbox", process_function=None,
                                   attachment_function=None):
        try:
            with open(connection_vault_path, 'r') as connection_file:
                connection_dict = json.load(connection_file)
                return KineticEmail.get_mailbox_messages(connection_dict, attachment_path, mailbox,
                                                         process_function, attachment_function)
        except FileNotFoundError:
            return {"error_code": "9001", "error_msg": "File " + connection_vault_path + " not found.", "data": {}}
        except json.JSONDecodeError as e:
            return {"error_code": "9002", "error_msg": "Error decoding JSON: " + str(e), "data": {}}

    #
    # process function is a function to process the entire email without the attachments.  The email
    #                  dictionary object is the only parameter.
    # process_attachment function is a function to process each attachment.  The email object and filename of the
    #                  attachment are the parameters.
    #
    @staticmethod
    def get_mailbox_messages(connection, attachment_path='', mailbox="Inbox", process_function=None,
                             attachment_function=None):

        imap = KineticEmail.connect_imap(
            connection['imap_server'],
            connection['email_address'],
            connection['email_password']
        )

        # Get the mailbox status and all directories from the inbox.
        #
        status, messages = KineticEmail.get_imap_messages(imap, mailbox)

        # list to return data.
        email_data = []

        #
        # only process if retrieval is OK.
        #
        if status == 'OK':
            #
            # Convert the result list to individual message numbers
            #
            message_numbers = messages[0].split()

            #
            # Process each email.
            for num in message_numbers:
                # Fetch the email by its number (RFC822 protocol for full email)
                # status, data = imap.fetch(num, '(RFC822)')
                status, data = imap.fetch(num, '(BODY.PEEK[])')
                if status == 'OK':
                    # Parse the email content
                    msg = email.message_from_bytes(data[0][1])

                    #
                    # Get message id, recipient email, subject, and sender
                    #
                    message_id = msg.get('Message-ID')
                    message_id = message_id.strip('<>') if message_id else "unknown"
                    to_address = msg.get('To')

                    subject = decode_header(msg["subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()

                    sender = decode_header(msg.get("From"))[0][0]
                    if isinstance(sender, bytes):
                        sender = sender.decode()

                    # Count and download attachments.
                    #
                    # Only download attachments if a path was specified.
                    #
                    # Initialize attachment count
                    body = ""
                    attachment_count = 0
                    attachment_filenames = []
                    #
                    # Both single part and multipart emails may have attachments.
                    #      We only download multipart.
                    #
                    if msg.is_multipart():
                        for part in msg.walk():
                            #
                            # Check if part is an attachment
                            #
                            content_type = part.get_content_type()
                            if content_type == "text/plain":
                                body = part.get_payload(decode=True).decode()

                                # Extracting HTML content and converting it to text
                            elif content_type == "text/html":
                                html_content = part.get_payload(decode=True).decode()
                                soup = BeautifulSoup(html_content, "html.parser")
                                body = soup.get_text()

                            if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
                                continue
                            disposition = part.get('Content-Disposition')
                            if 'attachment' in disposition or 'filename' in disposition:
                                filename = part.get_filename()
                                if filename:
                                    filename = decode_header(filename)[0][0]
                                    if isinstance(filename, bytes):
                                        filename = filename.decode()
                                    if '/' in filename:
                                        f = filename.split('/')
                                        filename = f[-1]
                                    if attachment_path != '':
                                        output_file_name = attachment_path + '/' + message_id + '-' + filename
                                        file_path = Path(output_file_name)
                                        if not file_path.exists():
                                            open(output_file_name, 'wb').write(part.get_payload(decode=True))
                                    else:
                                        output_file_name = filename

                                    attachment_filenames.append(output_file_name)
                            attachment_count += 1
                    else:
                        #
                        # Email does not have multiple parts, so we can identify attachments but
                        # not download them.
                        #
                        payload = msg.get_payload(decode=True).decode()
                        if msg.get_content_type() == "text/plain":
                            body = payload
                        elif msg.get_content_type() == "text/html":
                            soup = BeautifulSoup(payload, "html.parser")
                            body = soup.get_text()

                        if msg.get_content_maintype() != 'text' and msg.get('Content-Disposition') is not None:
                            filename = msg.get_filename()
                            if filename:
                                filename = decode_header(filename)[0][0]
                                if isinstance(filename, bytes):
                                    filename = filename.decode()

                                attachment_filenames.append("single-part:" + filename)
                            attachment_count += 1

                    # Append email to the list.

                    em = {'message_number': num.decode(),
                          'from_address': sender,
                          'to_address': to_address,
                          'subject': subject,
                          'body': body,
                          'attachment_path': attachment_path,
                          'attachment_count': attachment_count,
                          'attachments': attachment_filenames}

                    if process_function is not None:
                        result = process_function(connection,em)
                        em['process_result'] = result
                    else:
                        em['process_result'] = {}

                    attachment_results = []
                    if attachment_function is not None:
                        for em2 in em['attachments']:
                            path = str(em2)
                            result = attachment_function(connection, em, path)
                            attachment_results.append(result)
                        em['attachment_results'] = attachment_results
                    else:
                        em['attachment_results'] = []

                    email_data.append(em)

        return {"error_code": "0", "error_msg": "", "data": email_data}

    @staticmethod
    def email_form(j, connection, attachment):

        message = MIMEMultipart()
        message['To'] = j['to']
        message['From'] = j['from']
        message['Subject'] = j['subject']
        body = j['body']
        message.attach(MIMEText(body,'plain'))

        fn = attachment.split("/")[-1]
        print(attachment)
        try:
            with open(attachment, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
        except FileNotFoundError:
            return {"error_code": "9011", "error_msg": "File " + attachment + " not found.", "data": {}}

        try:
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {fn}')
            message.attach(part)
        except:
            print('didnt work 2')

        try:
            print('connection')
            print(connection)
            try:
                with smtplib.SMTP(connection['smtp_server'], connection['smtp_port']) as server:
                    try:
                        server.starttls()
                    except Exception as e:
                        pass

                    try:
                        server.login(connection['email_address'], connection['email_password'])
                    except smtplib.SMTPAuthenticationError:
                        return {"error_code": "9010", "error_msg": "Authentication failed, check email and password.", "data": {}}
                    try:
                        server.send_message(message)
                    except smtplib.SMTPException:
                        return {"error_code": "9010", "error_msg": "Failed to send the messge.", "data": {}}
                    server.quit()
            # Rest of the code
            except smtplib.SMTPConnectError:
                return {"error_code": "9011", "error_msg": "Error: Could not connect to the SMTP server.", "data": {}}
        except Exception as e:
            return {"error_code": "9011", "error_msg": "An unexpected error occurred." + str(e), "data": {}}

