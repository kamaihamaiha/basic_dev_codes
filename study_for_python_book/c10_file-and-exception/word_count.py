def word_count(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(filename + " has " + str(len(contents.split())) + " words.")  
        

word_count('txt_files/Alice.txt')                     