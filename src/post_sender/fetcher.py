import email
import imaplib
import datetime
import os

from tqdm import tqdm


class FetchEmail():
    connection = None
    error = None

    def __init__(self, username, password, mail_folder, mail_server='outlook.office365.com'):
        self.connection = imaplib.IMAP4_SSL(mail_server)
        self.connection.login(username, password)
        self.connection.select(mail_folder)

    def close_connection(self):
        """
        Close the connection to the IMAP server
        """
        self.connection.close()

    def save_attachment(self, msg, download_folder):
        """
        Given a message, save its attachments to the specified
        download folder

        return: file path to attachment
        """
        att_path = "No attachment found."
        fcount = 0

        for part in msg.walk():
            if part.get_filename() is not None:
                filename = part.get_filename()
                att_path = os.path.join(download_folder + filename)

                if not os.path.isfile(att_path):
                    fp = open(att_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fcount += 1
                    print "{0} attachment(s) fetched\n------\n".format(fcount)
                    fp.close()
        return att_path

    def fetch_messages(self, subject, error_date):
        """
        Find all email by search query parameter on specified date

        return: list of emails
        """
        emails = []

        objDate = datetime.datetime.strptime(error_date, '%d-%b-%Y')
        since_date = (objDate - datetime.timedelta(hours=2)).strftime("%d-%b-%Y") #Include objects UK time differences
        before_date = (objDate + datetime.timedelta(hours=24)).strftime("%d-%b-%Y")

        searchQuery = '(SUBJECT "{0}" SINCE {1} BEFORE {2})'.format(subject, since_date, before_date)
        result, messages = self.connection.search(None, searchQuery)
        pbar = tqdm(messages[0].split())

        if result == "OK" or '' not in messages:
            for message in pbar:
                pbar.set_description("Fetching messages")

                try:
                    result, data = self.connection.fetch(message, '(RFC822)')
                except:
                    print "No new emails to read."
                    self.close_connection()
                    exit()

                msg = email.message_from_string(data[0][1])
                if isinstance(msg, str) == False:
                    emails.append(msg)

            return emails
        print "\n"

        self.error = "Failed to retreive emails."
        return emails