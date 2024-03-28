import time                                                          
import requests                                                 #downloading the site
from bs4 import BeautifulSoup                                   #parsing the downloaded site
import smtplib                                                  #notifying via email

with open("secret.txt", "r") as secret:                         #get login and password for the email;
    credentials = secret.readline().split(" ")

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
    

    server = smtplib.SMTP('smtp.gmail.com', 587)                #connect to the email service
    server.starttls()
    server.login(credentials[0], credentials[1])
                
    while(True):                                                #endless loop of checking the condition; CTRL+C to interrupt the program
        for url in websites.keys():
            response = requests.get(url) 
            soup = BeautifulSoup(response.text, "lxml") 
            if (websites[url] != str(soup)):                     #if the website has changed
                websites[url] = str(soup)                        #update the data in the dict
                msg = 'WEBSITE UPDATED\nGo check it out at '+url #subject \n message
                sender = credentials[0]                          #FROM address
                recipient = 'veleth@icloud.com'                  #TO address
                server.sendmail(sender, recipient, msg)          #send email
                print("UPDATE: ", url ,"\nNotification sent to ", recipient)
        time.sleep(timeout)

#1.NOTE: libraries might need to be installed separately. The easiest way is to get pip and >pip install [name]
#2.NOTE: If you're using Gmail, you may need to enable "Less secure applications" to be able to log into your account, 
#otherwise you may get an error "Username and password not accepted"
