
'''
Google IMage downloader - Takes one or more keywords as input and downloads the specified number of images from deviantArt
'''
import sys, os
import re
import requests
import Downloader
import Scraper

#Input keywords
keywords = input("Enter search terms : ").split()
d = Downloader.Downloader()
sc = Scraper.Scraper()

#Download the corresponding DeviantArt page
response = d.downloadPage(keywords)
#Scrape all page urls
linkTags = sc.getLinkTags(response)
#Open all page urls, download them and scrape the image urls along with names
imageURLs, imageNames = sc.getImageTags(linkTags)

#Create a new directory in C:\Users\HP\Pictures\Scraped if it does no already exist. Then switch to that directory
try:
    os.chdir(r'C:\Users\HP\Pictures\Scraped' + '\\' + " ".join(keywords).title())
except FileNotFoundError:
    os.makedirs(r'C:\Users\HP\Pictures\Scraped' + '\\' + " ".join(keywords).title())
    os.chdir(r'C:\Users\HP\Pictures\Scraped' + '\\' + " ".join(keywords).title())

#For each url in the list, download and save in the above directory
for i in range(len(imageURLs)):
    url = imageURLs[i]
    name = imageNames[i]
    #Get rid of all unaccpeted special characters from the file name
    name = re.sub(r'[^0-9a-zA-Z. ]', ' ', name)

    #Open file in write binary mode to save image
    file = open(name+'.jpg', 'wb')
    img = requests.get(url)
    try:
        assert img.status_code==200
    except AssertionError:
        print(name + " image could not be opened")
        continue

    #Write the content of the requests response object to the file
    file.write(img.content)
    file.close()
