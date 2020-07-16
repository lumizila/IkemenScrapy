import scrapy
import random
import sys
from animalscrapy.items import Zoo
from random import randint

class ZoospiderSpider(scrapy.Spider):

    name = 'zoospider'
    allowed_domains = ['www.jalan.net/kankou/g2_27/']
    start_urls = ['https://www.jalan.net/kankou/g2_27/']

    def getZooInfo(self, response):
        for zoo in response.css('div.main'):
            get_information = zoo.css('div.main div.aboutArea p::text').get(default="not found")
            zooImage = zoo.css('div#galleryArea div div.galleryArea-image img::attr(src)').get(default="not found")
            zooImage = "https:" + zooImage
            zooAddress = zoo.css('#aboutArea table tr:nth-child(2) td::text').get(default="not found")
            zooAddress = zooAddress.replace("\t", "")
            zooAddress = zooAddress.replace("\n", " ")
            zooAddress = zooAddress.replace("\u3000", "")
            zooName = zoo.css('div.galleryArea h1::text').get(default="not found")
            if(zooImage != None and zooImage != "https://not found" and zooAddress != "not found" and zooName != "not found"):
                yield Zoo(
                    #TODO complete zoo data
                    zooName = zooName,
                    zooInformation = get_information.replace('\u3000', ''),
                    zooPicture = zooImage,
                    zooAddress = zooAddress,
                    #TODO limit the latitude/longitude to be INSIDE Japan
                    zooLatitude = str(randint(20,45))+"."+str(randint(0,9999999)),
                    zooLongitude = str(randint(123,153))+"."+str(randint(0,9999999))
                )
            else:
                yield

    def parse(self, response):
        for zoo in response.css('ul.cassetteList-list li'):
            zooUrl = zoo.css('div.item-listContents div.item-info p.item-name a::attr(href)').get(default="not found")
            if(zooUrl != "not found"):
                mergedurl = "https:"+zooUrl
                request = scrapy.Request(mergedurl, callback=self.getZooInfo, dont_filter=True)
                yield request
