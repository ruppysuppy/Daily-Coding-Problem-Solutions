'''
Problem:

Implement a URL shortener with the following methods:
* shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
* restore(short), which expands the shortened string into the original url. 
If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
'''

# importing sha224 hash function
from hashlib import sha224

# URL_Shortner class
class URL_Shortner():
    # initialization function
    def __init__(self):
        # url_short: dictionary mapping the hash to the corresponding address
        # url_prefix: domain of the site
        self.url_short = {}
        self.url_prefix = "http://short_url.in/"
    
    # shorten function
    def shorten(self, url):
        # taking the 6 hex characters (48 out of the 224 characters) for short_url
        short_url = sha224(url.encode()).hexdigest()[:6]

        # if the hash doesn't contains a value, its stored in the dictionary
        if (short_url not in self.url_short):
            self.url_short[short_url] = url
        
        # returning the full shortened url (with domain)
        return (self.url_prefix + short_url)
    
    # restore function
    def restore(self, short):
        # if the shortened url is valid, the corresponding address is returned
        if (short[-6:] in self.url_short):
            return self.url_short[short[-6:]]
        # else None is returned
        return None

# DRIVER CODE
us = URL_Shortner()

url = "https://www.google.com/"
short = us.shorten(url)
print(short)

print(us.restore(short))
print(us.restore('http://short_url.in/64f827'))