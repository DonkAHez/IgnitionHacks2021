#from flask import Flask
from PeopleClass import student

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
