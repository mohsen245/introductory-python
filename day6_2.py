def count_words_lines(filename):
    try:    
        with open(filename , "r") as file:
            list_lines= file.readlines()
            count_line=len(list_lines)
            count_words=0
            count_words=sum(len(line.split()) for line in list_lines)
            # for line in list_lines:
            #     list_of_oneline=line.split()
            #     length_of_oneline=len(list_of_oneline)
            #     count_words+=length_of_oneline
            
            print(f"number of lines : {count_line}")
            print(f"number of words : {count_words}")
    except FileNotFoundError:
        print(f"file with name of {filename} not found")
        
count_words_lines("sample.txt")