import time                                                          
import requests                                                 #downloading the site
from bs4 import BeautifulSoup                                   #parsing the downloaded site
import smtplib                                                  #notifying via email

websites = {}                                                   #to store web addresses and contents
timeout = 5                                                     #the script checks every website on the list every [timeout] seconds
                                                                #NOTE: The "real" timeout will be longer depending on the amount of websites in websites.txt. Every website takes a short time to check

if __name__ == "__main__":
    with open("websites.txt", "r") as file:                     #first loop to store data
        for url in file.readlines():
            if(url[-1:] == "\n"):                               #remove endline characters
                url = url[:-1]
            if(url[:4] != "http"):                              #add https:// if there's none
                url = "https://"+url
            response = requests.get(url)                        #download website
            soup = BeautifulSoup(response.text, "lxml")         #parse the contents
            websites[url] = str(soup)                           #include contents in the dictionary
    
    while(True):                                                #endless loop of checking the condition; CTRL+C to interrupt the program
        for url in websites.keys():
            response = requests.get(url) 
            soup = BeautifulSoup(response.text, "lxml") 
            if (websites[url] != str(soup)):                     #if the website has changed
                websites[url] = str(soup)                        #update the data in the dict
                print("CHANGED: ",url) #to be changed soon
            print(time.time())
        time.sleep(timeout)
