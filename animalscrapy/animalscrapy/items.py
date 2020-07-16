# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimalscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Animal(scrapy.Item):
    animalName = scrapy.Field()
    animalJpName = scrapy.Field()
    animalSpecies = scrapy.Field()
    animalSex = scrapy.Field()
    animalBirthday = scrapy.Field()
    animalPicture = scrapy.Field()
    animalDescription = scrapy.Field()
    animalZooID = scrapy.Field()

class Zoo(scrapy.Item):
    zooName = scrapy.Field()
    zooInformation = scrapy.Field()
    zooPicture = scrapy.Field()
    zooAddress = scrapy.Field()
    zooLatitude = scrapy.Field()
    zooLongitude = scrapy.Field()

