#Johnathan Hinebrook
#Python 3.X
import os,sys,time,math,urllib.request,urllib.parse,re

import pluginScript

URL = "http://bakabt.me/rss.php?uid="     #BBTs address
APASS = "&pass="

USR = "#"                           #User ID goes here
PASS = "#" #RSS Pass goes here

FNLURL = URL + USR + APASS + PASS         #makes the url

def site():
    print("Going out to the web")
    try:
        x = urllib.request.urlopen(FNLURL)
        req = urllib.request.Request(FNLURL, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        print("Pulling Raw HTML")
        file = open("output.html", "w+")
        file.write(str(respData))
        file.close()
        print("Exiting Site")
    except Exception as t:
        print("ERROR")
        print(str(t))
    print("Parsing")


    
    title = re.findall(r'<title>(.*?)</title>',str(respData))
    size = re.findall(r'<size>(.*?)</size>',str(respData))
    link = re.findall(r'<link>(.*?)</link>',str(respData))
    numfiles = re.findall(r'<numfiles>(.*?)</numfiles>',str(respData))

    title = str(title)

    #Title
    newt1 = "," + "<td>" + str(title) + "," + "</td>"
    newt2 = "<tr>" + newt1
    newt4 = newt2.replace(",","</td><td>")
    newt5 = newt4 + ("</tr><tr>")

    #Size
    newt6 = "," + "<td>" + str(size) + "," + "</td>"    
    newt7 = "<tr>" + "<td></td>" +newt6
    newt8 = newt7.replace(",","</td><td>")
    newt9 = newt8 + "</tr> <tr>"

    #numfiles
    newt10 = "," + "<td>" + str(numfiles) + "," + "</td>"    
    newt11 = "<tr>" + "<td></td>" +newt10
    newt12 = newt11.replace(",","</td><td>")
    newt13 = newt12 + "</tr> <tr>"

    #link
    newt14 = "," + '<td><a href="' + str(link) + "," + '">HERE</a></td>'    
    newt15 = "<tr>" + newt14
    newt16 = newt15.replace(",",'">HERE</a></td><td><a href="')
    newt17 = newt16.replace("'",'')
    newt18 = newt17 + "</tr> <tr>"


    finalnewt = '<table border="1" bgcolor="#CCCCCC">' + newt5 + newt9 + newt13 + newt18 + '</table>'




    pluginScript.TypeWriter("BakaRSS.html",str(finalnewt))
##    pluginScript.TypeWriter("links.out",str(link))
##    pluginScript.openFile("BakaRSS.html")


def main():
    site()
    pluginScript.timer(1)
    pluginScript.clearScreen()
    print("Done...")

main()



