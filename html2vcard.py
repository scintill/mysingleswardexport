#!/usr/bin/python

import urllib2
import base64
import re
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen(path_to_saved_html);
soup = BeautifulSoup(page)

for wlist in soup.findAll('table', 'WardList'):
    for person in wlist.findAll('tr', attrs={"id": True}):
        cells = person.findAll('td')

        img = cells[0].find('img', 'smallPic')
        img = img['src']
        if img[-13:] == 'profile-1.jpg':
            img = None

        name = cells[1].a
        if name != None:
            name = name.contents[0].__str__()

        addr = cells[2].contents[0].strip()
        phone = cells[3].a
        if phone != None:
            phone = phone['href'].__str__()[4:]
        
        email = cells[4].a
        if email != None:
            email = email.contents[0].strip()

        print "BEGIN:VCARD"
        print "FN:"+name
        if addr != None:
            print "ADR;TYPE=home:;;"+addr.replace('\n', ';')
        if email != None:
            print "EMAIL:"+email
        if phone != None:
            print "TEL;TYPE=home,voice:"+phone
        if img != None:
            b64 = base64.b64encode(open(img).read());
            # http://stackoverflow.com/questions/6558072/how-to-split-string-at-a-specific-charset-of-chars-actually-but-with-specifie
            # could not get textwrap to work; maybe it's the old installation I'm using
            p = re.compile("(.{,72})")
            b64 = p.sub("\n \\1", b64)
            print "PHOTO;ENCODING=b;TYPE=JPEG:"+b64
            
        print "VERSION: 3.0"
        print "END:VCARD\n"
