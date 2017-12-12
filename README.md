# Keats Crawler [![Build Status](https://travis-ci.org/FortyIX/Keats-crawler.png?branch=master)](https://travis-ci.org/FortyIX/Keats-crawler)

A Command line program which crawling Keats which is a student portal of KCL to fetch some usful informaition
such as Course and Grades information with no need to open the browser. Student ID and password are required



### Development Progress

* Log into Keats with code (with pre defined password) [**FINISHED**]
* Fetch Course Information and print out [**FINISHED**]
* Log into Keats with code (with users input) [**FINISHED**]
* Fetch Grades Information and print out [**DEVELOPING**]
* Buiding Graphic User Interface [**DEVELOPING**]

Following code in the **[run.py](https://github.com/FortyIX/Keats-crawler/blob/master/run.py)** defines the layout of the course information shown on the console

```python
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in Spider.getList(Spider):
    print("\b"+"\b"+ i )
    print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")

print()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
```

### How to Use it 

When you run the program, you will be asked to input your account detail 
```
What is your K number ?kxxxxxxx
and your password?xxxxxxxxx

```


after that you will get the output, following is an example of the output (excluding for Scrapy Output)

```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Informatics SSLC Discussion Forums 2017-18
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

Informatics SSLC Discussion Forums 2017-18
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

Informatics: Babbage House
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

4CCS1CIT Circuit Theory(17~18 SEM2 000001)
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

4CCS1CS1 Computer Systems(17~18 SEM1 000001)
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

4CCS1FC1 Foundations of Computing 1(17~18 SEM1 000001)
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

4CCS1LOD Logic Design(17~18 SEM2 000001)
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

4CCS1PL1 Electronics Application Project and Engineering Lab I(17~18 000001)
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

4CCS1PPA Programming Practice and Applications(17~18 000001)
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

6CCS3AIP Artificial intelligence planning(17~18 SEM1 000001)
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

Informatics Class Tests 17/18
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

4CCP1351 Mathematical Methods in Physics 1(17~18 SEM1 000001)
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

NMS: Consent Matters: Boundaries, Respect and Positive Intervention
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

KLaSS - King's Learning and Skills Services Home
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

NS-0ZDOAKG1-3 17~18 AKC
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

Natural & Mathematical Sciences Practice Assignment
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```







### Do you want to make it better ? 

* **Pull Request**
* Email me at **fuzhang.work@gmail.com**

