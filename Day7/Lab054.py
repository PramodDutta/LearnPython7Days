#File I/O
# File I/O refers to reading from and writing to files.
with open("example.txt", 'r') as file:
    content = file.read()
    print(content)
    
with open("example.txt", 'a') as file:
    file.write("Hello")