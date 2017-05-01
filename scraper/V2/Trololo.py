#Johnathan Hinebrook
#Python 3.X

TestURL = "https://www.python.org/" #test address
filename = 'test.html'
browserpath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

   
def site(URL,FileName,FileType):
    import urllib.request
    filename=FileName+FileType
    urllib.request.urlretrieve(URL, filename)

def openScrape(URL):
    import webbrowser
    webbrowser.open_new(URL)

USRinput = input("Please enter address you would like to go to\n(Keep blank to test)\n\n:")
if(USRinput == ""):
    URL = TestURL
try:
    site(URL,filename,'.html')
except:
    print("Error")
print("Done...")
openScrape(filename)
