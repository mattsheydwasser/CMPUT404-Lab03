#!/usr/bin/env python3


from templates import login_page, secret_page, after_login_incorrect
import os, json
import secret
from http.cookies import SimpleCookie
import cgitb, cgi


# initialize the cgitb and field storage for cookies
# check if the input values are the same as the secret values
cgitb.enable()
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

form_ok = username ==  secret.username and password == secret.password


# initialize the cooker with the HTTP_COOKIE header
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None


# if the fields are not empty, set them as username and password fields
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value


# check if the cookie values are the same as the secret values
# if so, set them as the username and password
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

if cookie_ok:
    username = cookie_username
    password = cookie_password


# if the inputted values are the same as the secret values, set 
# the cookies and hold them to allow for auto login
print("Content-Type: text/html")
if form_ok:
    print(f"Set-Cookie: username = {username}")
    print(f"Set-Cookie: password = {password}")
print()


# handle correct and incorrect logins
if not username and not password:
    print(login_page())
elif username==secret.username and password==secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
    # print("Username and password: ", username, password)
