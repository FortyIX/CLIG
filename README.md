# Keats Crawler

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



### Do you want to make it better ? 

* **Pull Request**
* Email me at **fuzhang.work@gmail.com**

