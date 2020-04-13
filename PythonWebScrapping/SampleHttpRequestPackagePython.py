# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:00:05 2020

@author: srira
"""


from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://en.wikipedia.org/wiki/Association_football")
r.status_code

#print(r.html)

urls=r.html.links
#print(urls)

absoluteurls=r.html.absolute_links
#print(absoluteurls)

type(absoluteurls)

links=r.html.find('a')
#print( links)

onlywikipedialinks = r.html.find('a', containing="wikipedia")
#print(onlywikipedialinks)

textinwikipedialink=[wikipedialink.text for wikipedialink in onlywikipedialinks]
#print(textinwikipedialink)

#print(r.html.find("p", first=True))

knownsoccer=r.html.search_all("known{}soccer")
print(knownsoccer)

session.close()
