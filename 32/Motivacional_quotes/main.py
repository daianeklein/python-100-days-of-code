import datetime as dt
import smtplib
import random
import os
import json
import smtplib
from dotenv import load_dotenv

#quotes
path = '/Users/daianeklein/Documents/DS/python-100-days-of-code/32/Motivacional_quotes/quotes.txt'

quotes = []

with open(path, 'r') as f:
    for line in f:
        quote_text, author = line.strip().split('-')
        quote = {
            'author': author.strip(),
            'quote': quote_text.strip()
        }
        quotes.append(quote)

#picking a random quote
quotes_list_count = len(quotes)
index_quote_of_day = random.randint(1, quotes_list_count)
quote_of_day = quotes[index_quote_of_day]
quote_of_day_author = quote_of_day['author']
quote_of_day_msg = quote_of_day['quote']

#date
today = dt.datetime.now()
today_day = today.weekday()

#sending e-mail
if today_day == 0:

    #email and password
    load_dotenv()
    my_email = 'dklein.dev@gmail.com'
    password = os.getenv('MY_PASSWORD_BIRTHDAY_WISHER')

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(user=my_email,
                         password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='daiane.klein22@gmail.com',
                            msg=f'Subject:Quote of the day\n\n{quote_of_day_author} : {quote_of_day_msg}')