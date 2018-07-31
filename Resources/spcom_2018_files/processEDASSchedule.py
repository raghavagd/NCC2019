#!/usr/bin/python

from bs4 import BeautifulSoup
import os,sys

EDASScheduleFileName = 'SPCOM2018-Program.html'
OutFileName = 'output.html'

html = open(EDASScheduleFileName, 'r')
soup = BeautifulSoup(html, 'html.parser')
html.close()

Sessions = soup.find_all('a', attrs={'class':'inh'})

for Session in Sessions:
    oldHref = Session['href']
    newHref = '#' + str(oldHref.split('#')[-1])
    Session['href'] = newHref
    # print('changed ' + oldHref + ' =====> ' + newHref)

People = soup.find_all('a', attrs={'title':'Show person'})

for Person in People:
    Person.unwrap()

Papers = soup.find_all('span', attrs={'class':'papertitle'})

for Paper in Papers:
    Paper.string.wrap(soup.new_tag('i'))

for Day in soup.find_all('h2', attrs={'class':'sessionday'}):
    Day.name = 'h3'
    Day.string.wrap(soup.new_tag('b'))

for Session in soup.find_all('h3', attrs={'class':'sessiontime'}):
    Session.name = 'h4'

with open(OutFileName, 'w') as file:
    file.write(soup.prettify())
