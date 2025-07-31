import re

def emailaaddress(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    text=re.sub(email_pattern,"XXX@gmail.com",text)
    return text


input_text=input("please insert the text")
print("new email addresses are : " , emailaaddress(input_text))