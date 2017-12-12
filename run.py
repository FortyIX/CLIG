

from scrapy.crawler import CrawlerProcess

from main import Spider



hi=Spider()


print(hi.getAc())

process = CrawlerProcess()

process.crawl(hi)

process.start()



print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in Spider.getList(Spider):
    print("\b"+"\b"+ i )
    print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")

print()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")