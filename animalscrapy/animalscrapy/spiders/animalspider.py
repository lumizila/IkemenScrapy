import sys
import scrapy 
import random
from random import randint
from random import seed
from animalscrapy.items import Animal


def makeName():
	name = random.choice(("ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","ナ","ニ","ネ","ノ","サ","シ","ツ","テ","ト","マ","ミ","ム","メ","モ","タ","チ","ツ","テ","ト","ワ","ヲ","ラ","リ","ル","レ","ロ"))
	name = name + random.choice(("ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","ナ","ニ","ネ","ノ","サ","シ","ツ","テ","ト","マ","ミ","ム","メ","モ","タ","チ","ツ","テ","ト","ワ","ヲ","ン","ラ","リ","ル","レ","ロ"))
	name = name + random.choice(("ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","ナ","ニ","ネ","ノ","サ","シ","ツ","テ","ト","マ","ミ","ム","メ","モ","タ","チ","ツ","テ","ト","ワ","ヲ","ン","ラ","リ","ル","レ","ロ","","","","",""))
	return name

class AnimalspiderSpider(scrapy.Spider):
	name = 'animalspider'
	allowed_domains = ['www.kobe-ojizoo.jp/animal/pictorial']
	start_urls = ['http://www.kobe-ojizoo.jp/animal/pictorial/']

	seed(1)


	def getAnimalDetails(self, response):
		for animal in response.css('.detail'):
			
			#getting name and species
			animaldetails=animal.css('.blkA h2 img::attr(alt)').extract_first().strip()
			
			#splitting the details because they were all in the same img
			animaldetails = animaldetails.replace('/', '')
			#removing ideographic space
			animaldetails = animaldetails.replace('\u3000', ' ')
			#removing weirs bars
			animaldetails = animaldetails.replace('\\', '')

			splitdetails = animaldetails.split("\n")

			#getting description
			animaldesc = animal.css('.blkA p::text').get(default='not-found')

			#getting picture url
			animalpic = animal.css('div.thumbs img[src*=data]::attr(src)').get(default='not-found')
			#animalpic = animal.xpath('//div[@class="thumbs"]/a[@data-slide-index="#1"]/img/@src]').get()
			if(animalpic == "not-found" or animaldesc == "not-found"):
				yield 
			else:			
				yield Animal(
					animalName = makeName(), 
					animalJpName = animal.css('.blkA h1 img::attr(alt)').extract_first().strip(),
					animalSpecies = splitdetails[2].replace('学名：', ''), 
					animalSex = random.choice(("female", "male")),
					animalBirthday = str(randint(1,30))+"/"+str(randint(1,12))+"/"+str(randint(1990,2020)),
					animalPicture = "http://www.kobe-ojizoo.jp/"+animalpic,
					animalDescription = animaldesc,
					animalZooID = randint(1,30)
				) 

	def parse(self, response):

		for animal in response.css('.blkC table td'):

			animalurl = animal.css('a::attr(href)').extract_first().strip()

			if(animalurl != None and animalurl != ""):
				mergedurl = 'http://www.kobe-ojizoo.jp/animal/pictorial/'+animalurl

				request = scrapy.Request(mergedurl, callback=self.getAnimalDetails, dont_filter=True)
				if(request != "" and request != None):
					yield request


		
	
