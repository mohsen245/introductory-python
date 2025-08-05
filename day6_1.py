with open("sample.txt" , "w") as file:
    file.write("hello world!")
    file.writelines(["ali","gholi", "25"])
    # content= file.read()
    # print(content)