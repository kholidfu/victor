import pycurl
from cStringIO import StringIO
import json

apikey = "RutmEhKIK8vsUH8YfcVSmUSgfHzyd6Nu"
keyword = "glass"

url = "http://"+apikey+"@api.fotolia.com/Rest/1/search/getSearchResults?search_parameters%5Bwords%5D="+keyword+"&search_parameters%5Blanguage_id%5D=2&search_parameters%5Blimit%5D=2"

buf = StringIO()

c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()

html = buf.getvalue()
from pprint import pprint
pprint(json.loads(html))
buf.close()
