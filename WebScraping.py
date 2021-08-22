from PeopleClass import student

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
  df = []
  for i in range(12):
    driver.switch_to.window(driver.window_handles[i])
    link, program = get_link(student, i)
    lst = get_data(link, student)
    lst.append(i+2005)
    lst.append(program)
    df.append(lst)
    driver.execute_script("window.open('');")
  driver.quit()
  return df

def get_link(student, index):
  year = str(index + 2005)
  program = student.get_program()
  ID = get_program_ID(program)

  return "https://cudo.ouac.on.ca/page.php?id=7&table=9#univ=1,2,3,8,9,11,12,14,16,17,21,22,23,24,25,27,28,29,30,31,32,33,34,42&topic=B&table_hidden=5&y=" + year + "&r=" + ID, program

def get_program_ID(program):
  file = open("cudoProgramIDs.txt", "r")
  for line in file:
    key = line.rstrip().split(", ")
    if key[0].lower() == program.lower():
      return key[1]

def get_data(link, student):
  driver.get(link)
  uni = get_uni(driver, student)
  # print(uni)
  return(get_precentages(driver, uni))


def get_uni(driver, student):
  uni = student.get_uni()
  
  p_element = driver.find_elements_by_class_name("title")
  for i in range (len(p_element)):
    if p_element[i].text == uni:
      return i

def get_precentages(driver, uni):
  p_element = driver.find_elements_by_tag_name("td")
  p_element = p_element[uni*9:(uni+1)*9]
  for i in range (len(p_element)):
    if i != 0:
      p_element[i] = cast_to_float(p_element[i])
    else:
      p_element[i] = p_element[i].text
  return p_element


def cast_to_float(element):
  element = element.text
  if element != "*": 
    if element == "n/a":
        return float(0)
    else:
      string = ""
      for i in range (len(element)-1):
        string += element[i]
      return float(string)
  return float(0)


print(get_acceptance_prediction(users[2]))