from airflow import configuration
from past.builtins import basestring
from requests.auth import HTTPBasicAuth
import requests


def send_email_mailgun(
    to,
    subject,
    html_content,
    files=None,
    dryrun=False,
    cc=None,
    bcc=None,
    mime_subtype="mixed",
    mime_charset="us-ascii",
    **kwargs,
):
    """
    Send an email with html content

    >>> send_email_mailgun('test@example.com', 'foo', '<b>Foo</b> bar', ['/dev/null'], dryrun=True)
    """
    smtp_mail_from = configuration.conf.get("smtp", "SMTP_MAIL_FROM")

    to = get_email_address_list(to)

    payload = {
        "from": smtp_mail_from,
        "to": ", ".join(to),
        "html": html_content,
        "subject": subject,
    }

    if cc:
        cc = get_email_address_list(cc)
        payload["cc"] = ", ".join(cc)

    if bcc:
        # don't add bcc in header
        bcc = get_email_address_list(bcc)
        payload["bcc"] = bcc

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    mailgun_domain_name = configuration.conf.get("mailgun", "domain_name")
    url = f"https://api.mailgun.net/v3/{mailgun_domain_name}/messages"

    api_password = configuration.conf.get("mailgun", "api_password")

    response = requests.request(
        "POST",
        url,
        headers=headers,
        data=payload,
        auth=HTTPBasicAuth("api", api_password),
    )

    print(response.text.encode("utf8"))


def get_email_address_list(address_string):
    if isinstance(address_string, basestring):
        if "," in address_string:
            address_string = [address.strip() for address in address_string.split(",")]
        elif ";" in address_string:
            address_string = [address.strip() for address in address_string.split(";")]
        else:
            address_string = [address_string]

    return address_string
