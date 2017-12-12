

from scrapy.crawler import CrawlerProcess

import main

hi=main.Spider()

main.Spider.user=input("What is your K number ?")
#get K number
main.Spider.passw=input("and your password?")
#get password





#get crweler to work
process = CrawlerProcess()
process.crawl(hi)
process.start()



print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in main.Spider.getList(main.Spider):
    print("\b"+"\b"+ i )
    print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")

print()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
