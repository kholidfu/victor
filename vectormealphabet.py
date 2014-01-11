import urllib2
from bs4 import BeautifulSoup
import time

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

# number of pages on each alphabet tag
# pgnum = {'a': 591, 'b': 591, 'c': 1204, 'd': 489, 'e': 279, 'f': 586,
#     'g': 446, 'h': 458, 'i': 373, 'j': 113, 'k': 153, 'l': 230, 'm': 230,
#     'n': 226, 'o': 230, 'p': 645, 'q': 22, 'r': 413, 's': 645, 't': 520,
#     'u': 101, 'v': 887, 'w': 22, 'x': 18, 'y': 55, 'z': 34}

pgnum = {'j': 113, 'k': 153, 'l': 230, 'm': 230,
    'n': 226, 'o': 230, 'p': 645, 'q': 22, 'r': 413, 's': 645, 't': 520,
    'u': 101, 'v': 887, 'w': 22, 'x': 18, 'y': 55, 'z': 34}

def main():
    for page in sorted(pgnum):
        for i in range(1, int(pgnum[page])):
            url = "http://vector.me/tags/" + page + "/" + str(i)
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

if __name__ == "__main__":
    main()
