def downloader(URL, fileName):
#File downloader. places file in ./Downloaded_File/
    import urllib.request
    LOC = "Downloaded_Files/" + fileName
    urllib.request.urlretrieve(URL,LOC)


def TypeWriter(File,inputt):
    #writes file
    file = open(File, "w+")   
    file.write(str(inputt))        #Writes formated data to brout.html
    file.close()

def clearScreen():
    #clears termal screen
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
          \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def timer(How_Long_In_Secounds):
    import time
    time.sleep(How_Long_In_Secounds)
    
def openFile(File):
    import os,sys
    os.startfile(File)
