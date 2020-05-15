
from seekr.api import API
from seekr.endpoint import Endpoint

class Seekr:
    def __init__(self, flask):
        self.__endpoints = []
        self.__set(flask)
        flask.register_blueprint(API())

    def __set(self, flask):
        attr = [{"url": n.rule, "method": n.methods} for n in flask.url_map.iter_rules()]
        for a in attr:
            self.__endpoints.append(Endpoint(a))
        return

    def getEndpoints(self):
        return self.__endpoints
