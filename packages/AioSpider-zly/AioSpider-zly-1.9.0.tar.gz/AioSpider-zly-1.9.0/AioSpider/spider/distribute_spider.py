from .spider import Spider


class DistributeSpider(Spider):

    def start(self):
        from AioSpider.core import DistributeEngine
        DistributeEngine(self).start()
