

from scrapy.crawler import CrawlerProcess

from main import keats



hi=keats()

#hi.setInfo("k1763499","Fu07956496084")
print(hi.getAc())

process = CrawlerProcess()

process.crawl(hi)

process.start()



print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in keats.getList(keats):
    print("\b"+"\b"+ i )
    print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")

print()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")