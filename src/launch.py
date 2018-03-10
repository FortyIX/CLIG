from Crawling import  Crawl
import os


# Start point of the application

def main():
    spider = Crawl()
    # TODO: find a better way to open the use, perhaps an argument like -ui will work
    if("UI" in os.environ):
        from gui import KeatsApp
        app = KeatsApp()
        app.set_crawl(spider)
        app.run()
    else:
        spider.crawling()


    

if __name__ == "__main__":
    main()