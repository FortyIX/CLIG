<h1 style="text-align: center;">Keats Crawler</h1> 

[![Build Status](https://travis-ci.org/FortyIX/Keats-Crawler.svg?branch=master)](https://travis-ci.org/FortyIX/Keats-Crawler) [![GitHub license](https://img.shields.io/github/license/FortyIX/Keats-Crawler.svg)](https://github.com/FortyIX/Keats-Crawler/blob/master/LICENSE) [![GitHub issues](https://img.shields.io/github/issues/FortyIX/Keats-Crawler.svg)](https://github.com/FortyIX/Keats-Crawler/issues) ![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)  ![GitHub last commit](https://img.shields.io/badge/Dev-Fu%20Zhang-blue.svg)



A program which crawling Keats which is a student portal of KCL to fetch some usful informaition
such as Course and Grades information with no need to open the browser. Student ID and password are required

&nbsp;
&nbsp;
&nbsp;
&nbsp;


## Development Progress

- [x] Log into Keats with code (with pre defined password) 
- [x] Fetch Course Information and print out 
- [x] Log into Keats with code (with users input) 
- [x] Fetch Grades Information and print out 
- [ ] Buiding Graphic User Interface 

</br>

## Installation

1. Please install the dependencies
```shell
$ pip install scrapy
$ pip install prettytable
```

2. Clone the repository 
```shell
$ git clone https://github.com/FortyIX/Keats-Crawler
```
</br>

## Usage 

> Please note that the grade of users will not be printed unless it is specified 

```shell
$ python Crawling.py [-g] [-s]
```

Options: 
```
-g: show the grades of the user, grade is hidden by default 
-s: Safe mode, you password will not be shown while you type them on the termial 

No Argument: grade will not be shown and Safe mode will be off

```
</br>

## Usage Sample 

By running 
```shell
$ python Crawling.py -g -s 
```
</br>
 you will be asking to verify your identity first by typing in your K number and password 

```shell
What is your K number ?"kxxxxxxxxx"
Password: 

```
> Your password will not be shown while your typing in Safe Mode


</br></br>

Following output is then generater(Sample data) 
The Course you are doing 

```text
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


## Known Issue
- Program won't tell users whether their password and username are typed correctly or not, it will output nothing when any of the information is incorrected
- Does not have a Graphic user interface


</br>

## Safety Notice 

- If you are interested in use this tool, pleas download ONLY from here, as the version you download from elsewhere may have been modified with virus or other unsafe addons

- I am NOT responible for the lost of any K number if they are not downloaded directly from here 

- It is a crime to modifiy the program for storing other user's account 



## License

FortyIX/Keats-Crawler is licensed under the
GNU General Public License v3.0

</br>


## Contrubtion Notice

- Whatever package you used, please add the dependencies in requirement.text
- Please email me for any change made in your use 


</br>

## Contact me

<a href="mailto:contact@fzhang.co.uk?subject=Contact From github">contact@fzhang.co.uk</a>
Or [open a issue ](https://github.com/FortyIX/Keats-Crawler/issues)





