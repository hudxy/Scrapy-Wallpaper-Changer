import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.pipelines.images import ImagesPipeline
from wallpaper.items import WallpaperItem
from wallpaper.items import ImageItem

class wallpaperSpider(scrapy.Spider):
    name = "wallpaper"
    start_urls = [
    #start at socwall homepage
        'https://www.socwall.com/'
    ]

    def parse(self, response):
        #get div element containing link to fullsized image
        for imgLink in response.css("div a::attr(href)").re(r"desktop.*"):
            #using relative path returned from imgLink, urljoin to get full path
            imgCont = response.urljoin(imgLink)
            #follow that link and use parseImagesPage as callback
            yield response.follow(imgCont, callback=self.parseImagesPage)

    def parseImagesPage(self, response):
        #gets fullsized image link from div with specific css selector
        for img in response.css("div.wallpaper a img::attr(src)"):
            #create item
            item = WallpaperItem()
            #extract relative path url from response (img) and urljoin to retrieve fullpath
            img_url = response.urljoin(img.extract())
            #set img_url to ImageItem item and sent to Images pipeline
            yield ImageItem(image_urls=[img_url])
