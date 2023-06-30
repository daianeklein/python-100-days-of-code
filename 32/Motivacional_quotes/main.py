import datetime as dt
import smtplib
import random
import json

#date
today = dt.datetime.now()
today_day = today.weekday()

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
#author_list = []
# quotes_list = []
# quotes_dict = {}

# with open(path, 'r') as f:
#     for line in f:
#         quotes, author = line.strip().split('-')
#         author_list.append(author)
#         quotes_list.append(quotes)

# author_list = [element.strip() for element in author_list]
# quotes_list = [element.strip() for element in quotes_list]

# for author, quote in zip(author_list, quotes_list):
#     quotes_dict[author] = quote

# items = list(quotes_dict.items())
# print(items)

#pick random text
