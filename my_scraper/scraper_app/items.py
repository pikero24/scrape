from scrapy.item import Item, Field

class LivingSocialDeal(Item):
	"Livingsocial container (dictionary-like object) for scraped data"
	title = Field()
	location = Field()
	description = Field()
	link = Field()
	category = Field()
	price = Field()
	original_price = Field()

# Test Statements
# deal = LivingSocialDeal(title="$20 off yoga classes", category="health")
# print deal
# print deal['title']
# deal['location'] = "New York"
# print deal['location']