def write_items_to_file(filename,items):
    with open(filename,"w") as file:
        for item in items:
            file.write(item+ "\n")
            
def read_item_from_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.readlines())
    except FileNotFoundError:
        print(f"file {filename} not found")
    except IOError:
        print(f"file {filename} not found")

items=["cherry","banana","carrot", "apple"]
write_items_to_file("fruit.txt",items)
read_item_from_file("fruit.txt")