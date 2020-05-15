
from flask import Blueprint
from seekr.data import DataService
from seekr.render import RenderService
from seekr.constant import ASSET

class API(Blueprint):
    def __init__(self, info=None):
        super().__init__("seekr_unique_route", __name__, template_folder=ASSET)
        self.__data = DataService(info)
        self.__render = RenderService(info)
        self.__define()

    def __define(self):

        @self.route("/seekr", methods=['GET'])
        def getData():
            data = self.__data.deliver()
            return self.__render.render(data)
