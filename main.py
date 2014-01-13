import pycurl
from cStringIO import StringIO
import json
import urllib
from pprint import pprint


apikey = "RutmEhKIK8vsUH8YfcVSmUSgfHzyd6Nu"
keyword = "glass"

url = "http://"+apikey+"@api.fotolia.com/Rest/1/search/getSearchResults?"

data = {
    "search_parameters[words]": keyword,
    "search_parameters[language_id]": 2,
    "search_parameters[limit]": 2,
    }

buf = StringIO()

c = pycurl.Curl()
c.setopt(c.URL, url + urllib.urlencode(data))
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()

html = buf.getvalue()

pprint(json.loads(html))
buf.close()
