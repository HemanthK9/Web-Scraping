'''
Scraper.py: Given the response object, it searches for image urls in deviant art using BeautifulSoup and downloads these webpages and
extracts the image url and stores them in a list. Returns this list.

'''
from bs4 import BeautifulSoup
from Downloader import Downloader
class Scraper:
    def __init__(self):
        self.imgPage = Downloader()

    #This method scrapes all link tags from the DeviantArt page to open them and download a higher quality image
    #These links can be found by the torpedo-thumb-link attribute in the a tags
    def getLinkTags(self, responseObject):
        soup = BeautifulSoup(responseObject.text, "html.parser")
        tags = soup.find_all('a', class_ = 'torpedo-thumb-link')
        return list(tags)

    #From the page that contains the image, return a list of image url as well as a  list of names for each image (which will be used as file name)
    def getImageTags(self, links):
        imgURLs = []
        imgNames = []
        for link in links:
            url = link['href']
            response = self.imgPage.downloadImagePage(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            tags = soup.find_all('img')
            tag = tags[0]
            img_url = tag['src']
            imgURLs.append(img_url)
            imgNames.append(tag['alt'])
        return imgURLs, imgNames
