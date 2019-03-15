'''
Downloader.py : Downloads the webpage using the requests module and returns a response object if download is successful
'''
import requests
class Downloader:
    def __init__(self):
        self.query = ""
        self.url = "https://www.deviantart.com/popular-all-time/?q="

    #Downloads the main query page. 
    def downloadPage(self, keywords):
        self.query = "+".join(keywords)
        self.url = self.url + self.query
        response = requests.get(self.url)
        try:
            assert response.status_code == 200
        except AssertionError:
            print("Page download failed. Status Code :", response.status_code)
            sys.exit()

        return response

    #Downloads the DeviantArt page which contains the image in it to extract the image url
    def downloadImagePage(self, url):
        self.url = url
        response = requests.get(self.url)
        try:
            assert response.status_code == 200
        except AssertionError:
            print("Page download failed. Status Code :", response.status_code)
            sys.exit()

        return response
