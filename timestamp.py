#Python function to open a file and print the current time stamp 
#Import the date time function 
import datetime
def time():
    #Open a file name in write mode 
    f=open("PAT23Task7.txt",'w')
    #Write the context in the file 
    f.write ("Current time stamp :"+'\t')
    f.write(datetime.datetime.now().ctime())
    #Print the current time in console for verification 
    print (datetime.datetime.now())
time()