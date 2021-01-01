import json

class Spirit:

    def __init__(self, name, href, photoHref):
        self.name      = name
        self.href      = href
        self.photoHref = photoHref

    def toJson(self):
        d = {}
        d["name"]  = self.name
        d["href"]  = self.href
        d["photo"] = self.photoHref

        return json.dumps(d)


#{
#   "name": "Amidomaru",
#   "href": "wiki/Amidamaru",
#   "photo": ""
#}
