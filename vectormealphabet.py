import urllib2
from bs4 import BeautifulSoup
import time

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

"""
{'a': 591, 'b': 591,}
"""

for i in range(1, 591):
    url = "http://vector.me/tags/b/" + str(i)
    print "Starting %s" % url
    html = opener.open(url)
    soup = BeautifulSoup(html)
    newtags = soup.find('div', attrs={'class': 'tags_cloud'})
    newtags = newtags.findAll('a')
    newtags = [i.getText() for i in newtags]

    with open('/home/banteng/gitcode/victor/vectormetags.txt') as f:
        oldtags = f.readlines()
        oldtags = [tag.strip() for tag in oldtags]

    with open('/home/banteng/gitcode/victor/vectormetags.txt', 'a') as f2:
        for i in newtags:
            if i not in oldtags:
                f2.write(i + '\n')

    time.sleep(3)
    print 'wait for 3 second'
