
from flask import Blueprint
from seekr.data import DataService
from seekr.render import RenderService

class API(Blueprint):
    def __init__(self):
        super().__init__("seekr", __name__)
        self.__data = DataService()
        self.__render = RenderService()
        self.__define()

    def __define(self):

        @self.route("/seekr", methods=['GET'])
        def getData():
            data = self.__data.deliver()
            return self.__render.render(data)
