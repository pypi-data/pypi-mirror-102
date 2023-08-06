# Copyright (C) 2019 Majormode.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


# [Domain Administrator]
# Google Mail
#   > Admin
#     > Security
#       > Basic Settings
#         > Go to settings for less secure apps
#           > Allow users to manage their access to less secure apps
#
# [Standard User]
# Google Mail
#   > My Account
#     > Connected apps & sites
#       > Allow less secure apps

# https://www.google.com/settings/security/lesssecureapps


COMMASPACE = ', '


def __build_author_name_expr(author_name, author_email_address):
    """
    Build the name of the author of a message as described in the Internet
    Message Format specification: https://tools.ietf.org/html/rfc5322#section-3.6.2


    :param author_name: complete name of the originator of the message.

    :param author_email_address: address of the mailbox to which the author
        of the message suggests that replies be sent.


    :return: a string representing the author of the message, that is, the
        mailbox of the person or system responsible for the writing of the
        message.  This string is intended to be used as the "From:" field
        of the message.
    """
    assert author_name is not None or author_email_address is not None, "Both arguments MUST NOT be bull"

    # Use the specified name of the author or the username of his email
    # address.
    author_name_expr = author_name or author_email_address[:author_email_address.find('@')]

    # Escape the name of the author if it contains a space character.
    if ' ' in author_name_expr:
        author_name_expr = f'"{author_name_expr}"'

    # Complete the name of the author with his email address when specified.
    if author_email_address:
        author_name_expr = f"{author_name_expr} <{author_email_address}>"

    return author_name_expr


def send_email(
        hostname,
        username,
        password,
        author_name,
        author_email_address,
        recipient_email_addresses,
        subject, content,
        bcc_recipient_email_addresses=None,
        cc_recipient_email_addresses=None,
        file_path_names=None,
        port_number=587,
        unsubscribe_mailto_link=None,
        unsubscribe_url=None):
    """
    Send a electronic mail to a list of recipients.


    @note: Outlook and Gmail leverage the list-unsubscribe option for
        senders with good sending reputations:

        "In order to receive unsubscribe feedback, senders must include an
        RFC2369-compliant List-Unsubscribe header containing a mailto: address.
        Please note that we only enable this feedback via email, so URIs for
        other protocols such as http will be ignored. The sender must also
        have a good reputation, and must act promptly in removing users from
        their lists. We do not provide unsubscribe feedback to senders when a
        user unsubscribes from an untrusted message."
        [https://sendersupport.olc.protection.outlook.com/pm/junkemail.aspx]

        "This only works for some senders right now. We're actively encouraging
        senders to support auto-unsubscribe — we think 100% should.  We won't
        provide the unsubscribe option on messages from spammers: we can't
        trust that they'll actually unsubscribe you, and they might even send
        you more spam.  So you'll only see the unsubscribe option for senders
        that we're pretty sure are not spammers and will actually honor your
        unsubscribe request.  We're being pretty conservative about which
        senders to trust in the beginning; over time, we hope to offer the
        ability to unsubscribe from more email."
        [https://gmail.googleblog.com/2009/07/unsubscribing-made-easy.html]


    :param hostname: Internet address or fully qualified domain name --
        human-readable nickname that corresponds to the address -- of the
        SMTP server is running on.

    :param username: username to authenticate with against the SMTP server.

    :param password: password associate to the username to authenticate
        with against the SMTP server.

    :param author_name: complete name of the originator of the message.

    :param author_email_address: address of the mailbox to which the author
        of the message suggests that replies be sent.

    :param recipient_email_addresses: email address(es) of the primary
        recipient(s) of the message.  A bare string will be treated as a
        list with one address.

    :param subject: a short string identifying the topic of the message.

    :param content: the body of the message.

    :param file_path_names: a list of complete fully qualified path name
        (FQPN) of the files to attach to this message.

    :param port_number: Internet port number on which the remote SMTP
        server is listening at.

        SMTP communication between mail servers uses TCP port 25.  Mail
        clients on the other hand, often submit the outgoing emails to a mail
        server on port 587.  Despite being deprecated, mail providers
        sometimes still permit the use of nonstandard port 465 for this
        purpose.

    :param unsubscribe_mailto_link: an email address to directly
        unsubscribe the recipient who requests to be removed from the
        mailing list (https://tools.ietf.org/html/rfc2369.html).

        In addition to the email address, other information can be provided.
        In fact, any standard mail header fields can be added to the mailto
        link.  The most commonly used of these are "subject", "cc", and "body"
        (which is not a true header field, but allows you to specify a short
        content message for the new email). Each field and its value is
        specified as a query term (https://tools.ietf.org/html/rfc6068).

    :param unsubscribe_url: a link that will take the subscriber to a
        landing page to process the unsubscribe request.  This can be a
        subscription center, or the subscriber is removed from the list
        right away and gets sent to a landing page that confirms the
        unsubscribe.
    """
    # Convert bare string representing only one email address as a list with
    # this single email address.
    if isinstance(recipient_email_addresses, str):
        recipient_email_addresses = [recipient_email_addresses]

    if cc_recipient_email_addresses and isinstance(cc_recipient_email_addresses, str):
        cc_recipient_email_addresses = [cc_recipient_email_addresses]

    if bcc_recipient_email_addresses and isinstance(bcc_recipient_email_addresses, str):
        bcc_recipient_email_addresses = [bcc_recipient_email_addresses]

    # Build the message to be sent.
    message = MIMEMultipart()
    message['From'] = __build_author_name_expr(author_name, author_email_address)
    message['To'] = COMMASPACE.join(recipient_email_addresses)
    if cc_recipient_email_addresses:
        message['Cc'] = COMMASPACE.join(cc_recipient_email_addresses)
    message['Date'] = formatdate(localtime=True)
    message['Subject'] = subject

    if author_email_address:
        message.add_header('Reply-To', author_email_address)

    # Add method(s) to unsubscribe a recipient from a mailing list at his
    # request.
    if unsubscribe_mailto_link or unsubscribe_url:
        unsubscribe_methods = [
            unsubscribe_url and f'<{unsubscribe_url}>',
            unsubscribe_mailto_link and f'<mailto:{unsubscribe_mailto_link}>',
        ]

        message.add_header('List-Unsubscribe', ', '.join([method for method in unsubscribe_methods if method]))

    # Detect whether the content of the message is a plain text or an HTML
    # content, based on whether the content starts with "<" or not.
    message.attach(MIMEText(
        content.encode('utf-8'),
        _charset='utf-8',
        _subtype='html' if content and content.strip()[0] == '<' else 'plain'))

    # Attache the specified files to the message.
    if file_path_names:
        if not isinstance(file_path_names, (list, set, tuple)):
            file_path_names = [file_path_names]

        for file_path_name in file_path_names or []:
            part = MIMEBase('application', 'octet-stream')

            with open(file_path_name, 'rb') as handle:
                part.set_payload(handle.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path_name))
            message.attach(part)

    # Connect the remote mail server and send the message.
    smtp_server = smtplib.SMTP_SSL(hostname) if port_number == 465 else smtplib.SMTP(hostname, port_number)
    smtp_server.ehlo()

    if port_number != 465:
        smtp_server.starttls()
        smtp_server.ehlo()

    smtp_server.login(username, password)

    email_addresses = recipient_email_addresses
    if cc_recipient_email_addresses:
        email_addresses += cc_recipient_email_addresses
    if bcc_recipient_email_addresses:
        email_addresses += bcc_recipient_email_addresses

    smtp_server.sendmail(author_email_address, email_addresses, message.as_string())

    smtp_server.close()
