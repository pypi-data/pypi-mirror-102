## airflow-mailgun-email

Airflow Email Backend to send email via Mailgun API 

## How to configure
In `airflow.cfg`
```
[email]
email_backend = airflow_mailgun_email.email_mailgun.send_email_mailgun

[mailgun]
domain_name = <your mailgun email domain name>
api_password = <api key>
```


#### How to build in Dev?
- `pip install --editable .`