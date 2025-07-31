import re

def count_vowels(text):
    text="".join(chr.lower() for chr in text if chr.isalnum())
    count=0
    vow="aeuioAEUIO"
    for chr in text:
        if chr in vow:
            count+=1
    return count


# def count_vowels(text):
#     text="".join(chr.lower() for chr in text if chr.isalnum())
#     count=0
#     for chr in text:
#         if chr=="a":
#             count+=1
#         elif chr=="e":
#             count+=1
#         elif chr=="o":
#             count+=1
#         elif chr=="i":
#             count+=1
#         elif chr=="u":
#             count+=1
#     return count


input_text=input("please insert the text")
print("count of vowels : " , count_vowels(input_text))