from urllib import request
import json


def fetch_book(url):
    response = request.urlopen(url).read()
    return json.loads(response)


# URL_BOOK = "http://localhost:1234/book"
# fetch_book(URL_BOOK) == dict(
#   title="Remarkable Saga of the Clacks",
#   author="Alexandra Scott",
#   lent_by=null,
#   lent_since=null,
#   lent_times=8,
#   year="The 7th year after Turtle Moves",
#   catalogued="year -395 in the 2nd month",
#   location="Great Hall: bottom shelve. 5m from the end",
#   excerpt=(
#       "Near the bubbling cauldron had never seen such a"
#       " sight: some dwarf miner raised the dead. The "
#       "annual magical cooking competition begins."
#   ),
# )
