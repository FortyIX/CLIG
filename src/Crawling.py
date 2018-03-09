

from scrapy.crawler import CrawlerProcess
from prettytable import PrettyTable
import getpass
import sys

import Crawler


class Crawl:
    # Init the Crawler object
    scanner = Crawler.Spider()

    # init setting for the application
    gradeDisable = False
    safeMode = True



    def __init__(self):
        # init the spider instance
        self.scanner = Crawler.Spider()

        # following fine isnt needed
        # but i kept it there to make it like how other languages work
        self.gradeDisable = True
        self.safeMode = False

    pass





    # print the course table
    def printCourseTable(self):
        course_table = PrettyTable(["No.", "Courses"])
        for i in range(0, len(self.scanner.getCourse())):
            course_table.add_row([i, self.scanner.getCourse()[i]])

        print(course_table)
    pass


    # print the grade table
    def printGradeTable(self):
        course_table = PrettyTable(["Course", "Grade"])
        for i in range(0, len(self.scanner.getCourse())):
            course_table.add_row([self.scanner.getGradeTitle()[i], self.scanner.getGradeMarks()[i]])

        print(course_table)
    pass


    # Print the final result which are two table combined / is the course table
    def printResult(self):

        # uncommont the following code to use the orginal output
        # Please only use the original output when prettyTable package is unavailable
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print("Course List")
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # for i in self.scanner.getCourse():
        #     print("\b"+"\b"+ i )
        #     print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
        #
        # print()
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        #
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print("Grades ")
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # for i in range(0,len(scanner.getGradeTitle())):
        #     print("\b"+"\b"+ self.scanner.getGradeTitle()[i]+"\b"+"\b"+self.scanner.getGradeMarks()[i])
        #     print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
        #
        # print()
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


        # by default only print the course
        print("The Course you are doing ")
        self.printCourseTable()

        print("\n")

        if (self.gradeDisable == False):
            print("and Your Grade")
            self.printGradeTable()

    pass




    def parseArguments(self):
        # Deal with the arguments
        if (len(sys.argv) > 1):
            if sys.argv[1] == "-g":
                self.gradeDisable = False
                if len(sys.argv) > 2:
                    if sys.argv[2] == "-s":
                        self.safeMode = False
                    else:
                        self.safeMode = True
                else:
                    self.safeMode = True

            elif sys.argv[1] == "-s":
                self.safeMode = False
                if len(sys.argv) > 2:
                    if sys.argv[2] == "-g":
                        self.gradeDisable = False
                    else:
                        self.fgradeDisable = True
        else:
            self.gradeDisable = True
            self.safeMode = True

    pass




    def getUserInfo(self):

        # get K number
        Crawler.Spider.user = input("What is your K number ?")


        self.parseArguments()

        # get password
        if self.safeMode == True:
            Crawler.Spider.passw = getpass.getpass()

        else:
            Crawler.Spider.passw = input("What is your password ?")

    pass




    def startCrawling(self):
        # run the crawler
        process = CrawlerProcess()
        process.crawl(self.scanner)
        process.start()

    pass



    def crawling(self):
        self.getUserInfo()
        self.startCrawling()
        self.printResult()

    pass


pass


a=Crawl
a.safeMode=False
a.crawling()











