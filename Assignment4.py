# Task 1 
# try:
#     name = 'sample.txt'
#     file1 = open(name, 'r')
#     lines = file1.readlines()
#     for i in range(len(lines)):
#         print("Line", i+1, ":", lines[i].strip())
#     file1.close()
    

# except FileNotFoundError:
#     print("The file",name,"was not found.")
    
    
# Task 2 

def write_to_file(filename,mode, text,message ):
    try:
        with open(filename, mode) as file:
            file.write(text + '\n')
        print(message)
    except Exception as e:
        print("An error occurred:", e)
        
        
first_input = input("Enter the text to write to the file: ")
write_to_file('output.txt','w', first_input, "Data successfully written to Output.txt")
second_input = input("Enter additional text to append: ")
write_to_file('output.txt','a', second_input, "Data successfully appended ")

file2 = open('output.txt', 'r')
print("Final Content of output.txt: \n",file2.read())
file2.close()


