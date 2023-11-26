#Function to read the context of text file and print it in console 
def read():
    #Open the text file to be read 
    f=open("PAT23Task7.txt",'r')
    #Read the context of the file and print it 
    print(f.read())
read()