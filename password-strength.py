# Inspired in https://www.instagram.com/p/CCss-g6APhH/

import re

def password_strength(password: str):
  if (len(password) >= 8):
    if bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*!@#$%^&*).{8,30})', password)) == True:
      return "The password is strong"

  return "The password is weak"

password = input("Enter the password: ")

print(password_strength(password))
