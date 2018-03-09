

from scrapy.crawler import CrawlerProcess
from prettytable import PrettyTable
import getpass
import sys

import Crawler

#init the spider instance
scanner=Crawler.Spider()


#init setting
gradeDisable=True
safemode=False





# Deal with the arguments
if(len(sys.argv)>1):
    if sys.argv[1] == "-g":
        gradeDisable=False
        if len(sys.argv) > 2:
            if sys.argv[2]=="-s":
                safemode=True
            else:
                safemode=False
        else:
            safemode=False

    elif sys.argv[1] == "-s":
        safemode=True
        if len(sys.argv) > 2:
            if sys.argv[2]=="-g":
                gradeDisable=False
            else:
                gradeDisable=True
else:
    gradeDisable=True
    safemode=False



# get K number

Crawler.Spider.user = input("What is your K number ?")


#get password
if safemode == True:
    Crawler.Spider.passw = getpass.getpass()

else:
    Crawler.Spider.passw = input("What is your password ?")






#run the crawler
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


# print the course table
def printCourseTable():
    course_table = PrettyTable(["No.", "Courses"])
    for i in range(0, len(scanner.getCourse())):
        course_table.add_row([i, scanner.getCourse()[i]])

    print(course_table)
    pass


# print the grade table
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


if(gradeDisable==False):
    print("and Your Grade")
    printGradeTable()














