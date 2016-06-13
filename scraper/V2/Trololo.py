#Johnathan Hinebrook
#Python 3.X
import os,sys,time,math,urllib.request,urllib.parse,re,subprocess

URL = "https://en.wikipedia.org/wiki/World_War_II" #test address
filename = 'test.html'
browserpath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

def site(inputofplayers,filename):
    print("Going out to the web")
    try:
        x = urllib.request.urlopen(inputofplayers)
        req = urllib.request.Request(inputofplayers, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        print("Pulling Raw HTML")
        file = open(filename, "w+")
        file.write(str(respData))
        file.close()
        print("Exiting Site")
    except Exception as t:
        print("ERROR")
        print(str(t))
   


def main():
    print("Site")
    #playerinput = input()
    playerinput = URL
    print("Dirname")
    site(playerinput,filename)
    print("Done...")
    #os.startfile(filename)
    subprocess.Popen("%s %s" % (browserpath, filename))

main()



