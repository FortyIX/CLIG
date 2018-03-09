# Keats Crawler [![Build Status](https://travis-ci.org/FortyIX/Keats-Crawler.svg?branch=master)](https://travis-ci.org/FortyIX/Keats-Crawler) [![GitHub license](https://img.shields.io/github/license/FortyIX/Keats-Crawler.svg)](https://github.com/FortyIX/Keats-Crawler/blob/master/LICENSE) [![GitHub issues](https://img.shields.io/github/issues/FortyIX/Keats-Crawler.svg)](https://github.com/FortyIX/Keats-Crawler/issues)


A program which crawling Keats which is a student portal of KCL to fetch some usful informaition
such as Course and Grades information with no need to open the browser. Student ID and password are required

&nbsp;
&nbsp;
&nbsp;
&nbsp;


### Development Progress

- [x] Log into Keats with code (with pre defined password) 
- [x] Fetch Course Information and print out 
- [x] Log into Keats with code (with users input) 
- [ ] Fetch Grades Information and print out 
- [ ] Buiding Graphic User Interface 



### Installation

When you run the program, you will be asked to input your account detail 
```
What is your K number ?kxxxxxxx
and your password?xxxxxxxxx

```


after that you will get the output, following is an example of the output (excluding for Scrapy Output)

```
The Course you are doing 
+-----+------------------------------------------------------------------------------+
| No. |                                   Courses                                    |
+-----+------------------------------------------------------------------------------+
|  0  |                 4CCS1CS1 Computer Systems(17~18 SEM1 000001)                 |
|  1  |                 4CCS1CS1 Computer Systems(17~18 SEM1 000001)                 |
|  2  |                  Informatics SSLC Discussion Forums 2017-18                  |
|  3  |                          Informatics: Babbage House                          |
|  4  |                  4CCS1CIT Circuit Theory(17~18 SEM2 000001)                  |
|  5  |                   4CCS1LOD Logic Design(17~18 SEM2 000001)                   |
|  6  | 4CCS1PL1 Electronics Application Project and Engineering Lab I(17~18 000001) |
|  7  |         6CCS3AIP Artificial intelligence planning(17~18 SEM1 000001)         |
|  8  |            4CCS1FC1 Foundations of Computing 1(17~18 SEM1 000001)            |
|  9  |         4CCS1PPA Programming Practice and Applications(17~18 000001)         |
|  10 |                        Informatics Class Tests 17/18                         |
|  11 |        4CCP1351 Mathematical Methods in Physics 1(17~18 SEM1 000001)         |
|  12 |               KLaSS - King's Learning and Skills Services Home               |
|  13 |             Natural & Mathematical Sciences Practice Assignment              |
|  14 |                  5CCS2CIT Circuit Theory(17~18 SEM2 000001)                  |
|  15 |              7CCSMBDT Big Data Technologies(17~18 SEM2 000001)               |
|  16 |  7CCSMCMB Algorithms for Computational Molecular Biology(17~18 SEM2 000001)  |
|  17 |                 7CCSMML1 Machine Learning(17~18 SEM2 000001)                 |
|  18 |               4CCP1352 Classical Mechanics(17~18 SEM2 000001)                |
+-----+------------------------------------------------------------------------------+


and Your Grade
+------------------------------------------------------------------------------+-------+
|                                    Course                                    | Grade |
+------------------------------------------------------------------------------+-------+
|                  Informatics SSLC Discussion Forums 2017-18                  |   -   |
|                          Informatics: Babbage House                          |   -   |
|                  4CCS1CIT Circuit Theory(17~18 SEM2 000001)                  | 25.50 |
|                 4CCS1CS1 Computer Systems(17~18 SEM1 000001)                 | 25.50 |
|            4CCS1FC1 Foundations of Computing 1(17~18 SEM1 000001)            |   -   |
|                   4CCS1LOD Logic Design(17~18 SEM2 000001)                   |   -   |
| 4CCS1PL1 Electronics Application Project and Engineering Lab I(17~18 000001) | 25.00 |
|         4CCS1PPA Programming Practice and Applications(17~18 000001)         |   -   |
|                  5CCS2CIT Circuit Theory(17~18 SEM2 000001)                  |   -   |
|         6CCS3AIP Artificial intelligence planning(17~18 SEM1 000001)         |   -   |
|              7CCSMBDT Big Data Technologies(17~18 SEM2 000001)               |   -   |
|  7CCSMCMB Algorithms for Computational Molecular Biology(17~18 SEM2 000001)  |   -   |
|                 7CCSMML1 Machine Learning(17~18 SEM2 000001)                 |   -   |
|                        Informatics Class Tests 17/18                         |   -   |
|        4CCP1351 Mathematical Methods in Physics 1(17~18 SEM1 000001)         |   -   |
|               4CCP1352 Classical Mechanics(17~18 SEM2 000001)                |   -   |
|             Natural & Mathematical Sciences Practice Assignment              |   -   |
|                                     None                                     |  None |
|                                     None                                     |  None |
+------------------------------------------------------------------------------+-------+

```







### Do you want to make it better ? 

* **Pull Request**
* Email me at **fuzhang.work@gmail.com**

