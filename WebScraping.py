from PeopleClass import student
from bs4 import BeautifulSoup
import requests 

from selenium import webdriver

import os
import stat
from selenium.webdriver.chrome.options import Options


st = os.stat('chromedriver')
os.chmod('chromedriver', st.st_mode | stat.S_IEXEC)
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome('./chromedriver', options=chrome_options)

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
  driver.get(link)
  uni = get_uni(driver, student)
  print(uni)
  get_percentages()


def get_uni(driver, student):
  uni = student.get_uni()
  
  p_element = driver.find_elements_by_class_name("title")
  for i in range (len(p_element)):
    if p_element[i].text == uni:
      return i+1

def get_precentages(driver, uni)

get_acceptance_prediction(users[2])

