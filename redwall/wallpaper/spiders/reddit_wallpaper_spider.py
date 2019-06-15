import scrapy
import re
from urllib.parse import urljoin
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.pipelines.images import ImagesPipeline
from wallpaper.items import WallpaperItem
from wallpaper.items import ImageItem

#wallpaper spider
class wallpaperSpider(scrapy.Spider):
    name = "wallpaper"
    start_urls = [
        #start with wallpaper subreddit frontpage
        'https://www.reddit.com/r/wallpaper/'
    ]

    def parse(self, response):
        #get div element containing link to page where fullsized image can be downloaded
        for imgLink in response.css("div._3JgI-GOrkmyIeDeyzXdyUD a::attr(href)"):
            #imgLink returns /r/wallpaper/* relative path selector, add relative path to reddit.com and join url
            imgCont = urljoin("https://www.reddit.com", imgLink.extract())
            #follow that link and use parseImagesPage as callback
            yield response.follow(imgCont, callback=self.parseImagesPage)

    def parseImagesPage(self, response):
        #gets fullsized image link from div with specific css selector
        for img in response.css("div._3Oa0THmZ3f5iZXAQ0hBJ0k a::attr(href)").re(r"https://i.redd.it.*"):
            #create item
            item = WallpaperItem()
            img_url = img
            #set img_url to ImageItem item and sent to Images pipeline
            yield ImageItem(image_urls=[img_url])
