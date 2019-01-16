"""
Elisabeth Vehling
A5
vehling@usc.edu

Description: I attempted to write a program that would ask the user for how many units they wanted to search for
and return the information for the courses that matched. I managed to do this and add the information to a list,
but I couldn't figure out how to parse each row's information in order.

"""

from bs4 import BeautifulSoup
import urllib.request
import ssl
url= "https://classes.usc.edu/term-20183/classes/inf/"
context = ssl._create_unverified_context()
page = urllib.request.urlopen(url, context= context)

soup = BeautifulSoup(page.read(), "html.parser")
#I set the variable courseTag to find where the tag "div" and the class="course-info expandable"
#both appeared. the class was specific to each individual course in the catalogue.
courseTag = soup.find_all("div", class_="course-info expandable")


userInput = input("How many units are you looking for? (1.0-4.0)")
nums = ["1.0","2.0", "3.0", "4.0"]
#this checks if the number of units is in the header text
while userInput not in nums:
    userInput = (input("How many units are you looking for? (Enter as float 1.0-4.0)"))

for course in courseTag:
    courseTitle = course.find("a", class_="courselink")
    if userInput in courseTitle.text:
        print(courseTitle.text)
#Created a new list to append my information to
        courseList= []
        tableRow = course.find_all("tr")
        tableHeader=course.find_all("th")
#this passes over the info in table headers that have the same class_ names as the info in  tb
        if tableHeader in tableRow:
            pass
        else:
            allSections = course.find_all("td", class_= "section")
            for section in allSections:
                courseList.append(section.text)
            #print(section.text)
            allDays = course.find_all("td", class_="days")
            for day in allDays:
                courseList.append(day.text)
            #print(day.text)
            allTimes = course.find_all("td", class_= 'time')
            for time in allTimes:
                courseList.append(time.text)
            #print(time.text)
            allInstructors = course.find_all("td", class_='instructor')
            for instructor in allInstructors:
                courseList.append(instructor.text)
            #print(instructor.text)
            allStudents = course.find_all("td", class_="registered")
            for students in allStudents:
                courseList.append(students.text)
            #print(students.text)
            print(courseList)




