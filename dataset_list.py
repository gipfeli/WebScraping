#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:44:43 2017

@author: Gipfeli
Ex1: Number of datasets currently listed on opendata.swiss
"""

from lxml import html
import requests

response = requests.get('https://opendata.swiss/de/dataset')
doc = html.fromstring(response.text)
link = doc.cssselect("div.statsnumber")[0]             # To get data from div with class
print(link.text + "Datensaetze")

response = requests.get('https://opendata.swiss/de/dataset?q=&sort=metadata_modified+desc')
odc = html.fromstring(response.text)
title = doc.cssselect('h3.dataset-heading')[0].text_content()
print(title.strip())

r = requests.get("")