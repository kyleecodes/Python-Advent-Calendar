# Filter non-emails from a series of emails.

import pandas as pd
# regular expression operations library
import re


def filter_emails(series):
    # identify pattern for emails
    pattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
    print([x[0] for x in [re.findall(pattern, email) for email in emails] if len(x) > 0])
    return [x[0] for x in [re.findall(pattern, email) for email in emails] if len(x) > 0]


if __name__ == '__main__':
    emails = pd.Series(['not an email', 'abc@def.com', 'kylee@kyleecodes.com', 'meow@meow.com'])
    filter_emails(emails)
