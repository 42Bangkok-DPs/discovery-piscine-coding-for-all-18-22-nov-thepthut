#!/usr/bin/env python
user_input = input("What you gotta say? : ")
while True:
    if user_input != "STOP":
      user_input = input("I got that! Anything else? : ")
    elif user_input == "STOP":
       break