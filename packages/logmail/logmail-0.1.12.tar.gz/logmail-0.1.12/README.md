logmail
========

A simple package for sending emails (as simple, as writing logs with [loguru](https://github.com/Delgan/loguru))

Install
-------
```
pip install logmail
```

or with [poetry](https://python-poetry.org/):
```
poetry add logmail
```

Usage
-----
Setting global config:

```
from logmail import mailer

mailer.configure(
    smtp_host="mail.example.com",
    smtp_port=25,
    smtp_timeout=2,
    service_name="AWESOME SERVICE",
    recipient_list=["foo@example.com", "bar@example.com"],
    mail_from="Cool Mailer <noreply-some-service@example.com>",
)
```

From any *.py file in your awesome project:
```
from logmail import mailer

mailer.debug("This is debug message!")
mailer.info("This is info message!")
mailer.success("This is success message!")
mailer.warning("This is warning message!")
mailer.error("This is error message!")
mailer.critial("This is critial message!")
```

If you need to send email with custom params:
```
from logmail import mailer
...
mailer.send_mail(
    subject="Some subject", 
    message="Some message",  # may be html string
    mail_from="Mr Foo <foo@example.com>",
    recipient_list=["fizzbuzz@example.com"]
)
```



Advanced usage
--------------

You may see debugging info while sending emails by:
```
from logmail import mailer

...

with mailer.debugging():
    mailer.info("Mail sent with debugging this process")

```

You may easily set production and testing config by:
```
from logmail import mailer

mailer.configure(
    smtp_host="mail.example.com",
    smtp_port=25,
    smtp_timeout=2,
    service_name="AWESOME SERVICE",
    recipient_list=["foo@example.com", "bar@example.com"],
    mail_from="Cool Mailer <noreply-some-service@example.com>",
    testing=True,
    test_service_name="SOME TEST SERVICE",
    test_recipient_list=["testfoo@example.com", "testbar@example.com"],
    test_mail_from="Testing Cool Mailer <test-noreply-some-service@example.com>",
)
```

Setting global debugging while sending mails:
```
from logmail import mailer

# at configuration time
mailer.configure(
    ...
    debug=True
)

# in other place
mailer.set_debug(debug=True)
```


You may also set limit of exceptions in traceback (if it was raised):
```
from logmail import mailer

# at configuration time
mailer.configure(
    ...
    traceback_limit=666
)

# in other place
mailer.set_traceback_limit(666)
```

If you need to convert summary and message to html by default, try this:
```
from logmail import mailer

# at configuration time
mailer.configure(
    ...
    convert_all_data_to_html=True
)

# in other place
mailer.set_convert_all_data_to_html(True)
```
*Note: logmail will apply **convert_str_to_html** method to summary and message with its default params every time when logmail sends not custom message*