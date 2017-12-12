

from scrapy.crawler import CrawlerProcess

from main import Spider



hi=Spider()

Spider.user=input("What is your K number ?")
Spider.passw=input("and your password?")



print(hi.getAc())


#get crweler to work
process = CrawlerProcess()
process.crawl(hi)
process.start()



print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in Spider.getList(Spider):
    print("\b"+"\b"+ i )
    print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")

print()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")