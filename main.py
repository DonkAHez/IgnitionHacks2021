#from flask import Flask
from PeopleClass import student
from bs4 import BeautifulSoup
import requests 

users = []

#catches exceptions
try:
  file = open("userInfo.txt", "r")
except:
  print("Error :(")

#loops to read entries in the user info file 
on = True
while (on):
  #gets a line from the file
  line = file.readline()
  line = line.rstrip()

  #ends if there are no more lines to be read from
  if (line == ""):
    on = False

  #creates a student object with the use information
  else:
    atts = line.split(", ")
    user = student(atts[0], atts[1], atts[2], atts[3])
    users.append(user)


for i in users:
  print(i.get_attributes())


def get_acceptance_prediction(student):
  link = get_link(student)
  get_data(link, student)

def get_link(student):
  program = student.get_program()
  ID = get_program_ID(program)

  return "https://cudo.ouac.on.ca/page.php?id=7&table=9#univ=1,2,3,8,9,11,12,14,16,17,21,22,23,24,25,27,28,29,30,31,32,33,34,42&topic=B&table_hidden=5&y=2016&r=" + ID

def get_program_ID(program):
  file = open("cudoProgramIDs.txt", "r")
  for line in file:
    key = line.rstrip().split(", ")
    if key[0].lower() == program.lower():
      return key[1]

def get_data(link, student):
  html_text = requests.get(link)
  http = requests.get(link)
  print(http)
  print(html_text)
  # soup = BeautifulSoup(html_text, "lxml")
  soup = BeautifulSoup(http.text, 'lxml')
#   get_uni_row(soup, student)

# def get_uni_row(soup, student):
  uni = student.get_uni()
  # unis = soup.find_all("span", class_ = "title")
  unis = soup.find_all("div", class_ = "cell-wrap")
  print(unis)

get_acceptance_prediction(users[2])
