import re

# text= "contact me at 123-456-7890"
# digits= re.findall(r"\d+", text)
# print(digits)

# text= "contact me at 123-456-7890"
# hide_text=re.sub(r"\d","X", text)
# print(hide_text)

def clean_text(text):
    text=re.sub(r"[^\w\s]","",text)
    text=" ".join(text.split())
    return text.lower()

def Is_palindrome(text):
    text="".join(chr.lower() for chr in text if chr.isalnum())
    return text== text[::-1] 


input_text= input("Please enter the text")
if Is_palindrome(input_text):
    print(f"{input_text} is a palindrome.")
else:
    print(f"{input_text} is not a palindrome.")