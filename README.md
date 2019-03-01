<h1 style="text-align: center;">KCLIG</h1> 

[![Build Status](https://travis-ci.org/FortyIX/CLIG.svg?branch=master)](https://travis-ci.org/FortyIX/CLIG) [![GitHub license](https://img.shields.io/github/license/FortyIX/CLIG.svg)](https://github.com/FortyIX/CLIG/blob/master/LICENSE) [![GitHub issues](https://img.shields.io/github/issues/FortyIX/CLIG.svg)](https://github.com/FortyIX/CLIG/issues) ![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)  ![GitHub last commit](https://img.shields.io/badge/Dev-Fu%20Zhang-blue.svg)



KCLIG is command line program which intends to help the student from King's College London to quickly look up their selected modules and their grade using their Kings' ID number. this project has been achived and stop updating. the code is purely for learning purpose
&nbsp;
&nbsp;
&nbsp;
&nbsp;

**BY USING THIS SOFTWARE, YOU ARE AGREED WITH MY [END-USER AGGREMENT](https://github.com/FortyIX/Keats-Crawler/blob/master/END-USER%20%26%20FURTHER%20DEVELOPMENT%20AGGREMENT.md)**

## Notifications

- A basic GUI using kivy has been developed but it is not yet stable, it's recommanded to still use command line 



&nbsp;
&nbsp;
&nbsp;
&nbsp;


## Features
- No browser needed, what you need is only a termial that comes with the operating system 
- Lower internet usage, Becuase the style sheet of the page is not needed ,therefore, it consume less intetnet
- Work perfectly within poor internet. as no style sheet needed
- quick, get all information you need in instant with only one line of command 
- safe, with safe mode on, password will be hiden

</br>

## Development Progress

- [x] Log into Keats with code (with pre defined password) 
- [x] Fetch Course Information and print out 
- [x] Log into Keats with code (with users input) 
- [x] Fetch Grades Information and print out 
- [ ] Buiding Graphic User Interface 

</br>

## Installation

0. Install pip, a python package manager

```shell
$ sudo easy_install pip

```
  > For window, pleas refer to [pip website](https://pip.pypa.io/en/stable/installing/) to install and upgrade

</br>

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
$ python launch.py [-g] [-s]
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
$ python launch.py -g -s 
```
</br>
 you will be asking to verify your identity first by typing in your K number and password 

```shell
What is your K number ?"kxxxxxxxxx"
Password: 

```
> Your password will not be shown while your typing in Safe Mode


</br></br>

Following output is then generated(Sample data) 


```text
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


## Known Issue
- Program won't tell users whether their password and username are typed correctly or not, it will output nothing when any of the information is incorrect
- Does not have a Graphic user interface


</br>

## Safety Notice 


- If you are interested in use this tool, pleas download ONLY from here, as the version you download from elsewhere may have been modified with virus or other unsafe addons

- I am NOT responible for the lost of any Student account.

- It is a crime to modifiy the program for storing other user's account 



## License

FortyIX/CLIG is licensed under the
GNU General Public License v3.0

</br>




## Contact me

<a href="mailto:contact@fzhang.co.uk?subject=Contact From github">contact@fzhang.co.uk</a>
Or [open a issue ](https://github.com/FortyIX/CLIG/issues)





