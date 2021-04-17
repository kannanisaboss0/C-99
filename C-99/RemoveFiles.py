import os
import time
import shutil
import datetime
from datetime import date
path=input("Enter file path:")

old_time = datetime.datetime.now()
print("The current time is:"+str(old_time))
new_time = old_time - datetime.timedelta(days=30)
print("The time thirty days ago was:"+str(new_time))
print("Removing files older than"+" "+str(new_time))
time=time.time()
count=0


if(os.path.exists(path)):
    print("Path Identified")
    for roots,dirs,files in os.walk(path):
       list=os.listdir(roots)
       for file in list: 
        new_path=roots+'/'+file
        file_time=os.stat(new_path).st_ctime
        time_converted=date.fromtimestamp(file_time)
        print(file+":"+str(time_converted))
        if(str(new_time)>str(time_converted)):
            print("This file is older than 30 days")
            count=count+1
            if(os.path.exists("C:/BackupFiles")):
                print("file 'BackupFiles' already exists, moving files there")  
                print(shutil.move(new_path,"C:/BackupFiles/"+file))
            else:
                print("file 'BackupFiles' does not exist, creating new one and moving files there") 
                os.mkdir("C:/BackupFiles")   
        else:
            print("File is within time tim limit") 
    if (count==1):
        print(str(count)+" file was found to be older than 30 days")
        print("Thank You for using RemoveFiles.py")
    elif(count>1):
        print(str(count)+" files were found to be older than 30 days")
        print("Thank You for using RemoveFiles.py")
    elif(count==0):
        print("No files were found to be older than 30 days")  
        print("Thank You for using RemoveFiles.py")      
            


    
       
        

    
       
       
           

else:
    print("Path Does Not Exist")        


    
'''
  for directory in dirs:
            directory_global=directory
        list_root=os.listdir(root)
        for item in list_root:
            new_path=path+'/'+directory_global+'/'+item
            main_root,ext=os.path.splitext(new_path)
            if(ext!=""):
                print(new_path)
'''


           
        
     
            
       
            
       
               
 
       

