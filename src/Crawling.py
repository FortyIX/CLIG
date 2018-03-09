

from scrapy.crawler import CrawlerProcess
from prettytable import PrettyTable
import getpass
import sys

import Crawler

#init the spider instance
scanner=Crawler.Spider()



Crawler.Spider.user=input("What is your K number ?")
#get K number
Crawler.Spider.passw=getpass.getpass()
#get password



#get crweler to work
process = CrawlerProcess()
process.crawl(scanner)
process.start()




# uncommont the following code to use the orginal output
# Please only use the original output when prettyTable package is unavailable
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print("Course List")
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# for i in scanner.getCourse():
#     print("\b"+"\b"+ i )
#     print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
#
# print()
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print("Course List")
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# for i in range(0,len(scanner.getGradeTitle())):
#     print("\b"+"\b"+ scanner.getGradeTitle()[i]+"\b"+"\b"+scanner.getGradeMarks()[i])
#     print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
#
# print()
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



def printCourseTable():
    course_table = PrettyTable(["No.", "Courses"])
    for i in range(0, len(scanner.getCourse())):
        course_table.add_row([i, scanner.getCourse()[i]])

    print(course_table)
    pass



def printGradeTable():
    course_table = PrettyTable(["Course", "Grade"])
    for i in range(0, len(scanner.getCourse())):
        course_table.add_row([scanner.getGradeTitle()[i], scanner.getGradeMarks()[i]])

    print(course_table)
    pass



# by default only print the course
print("The Course you are doing ")
printCourseTable()

print("\n")


if(len(sys.argv) > 1 ):
    if(sys.argv[1]=="-g"):
       print("and Your Grade")
       printGradeTable()














