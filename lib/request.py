import requests

class RequestClass: # class that handles requests
	def __init__(self, baseUrl: str, trustName: str): # Constructor 
		self.baseUrl = baseUrl
		self.trustName = trustName

		self.uploadUrl = "http://kapper.gideon.nu/api/review"

		self.url: str = self.baseUrl + self.trustName + "?languages=all"
	
	def getHtml(self):
		return requests.get(self.url).text

	def uploadOne(self, data: dict):
		return requests.post(self.uploadUrl, data=data)

	def getHtmlFromPage(self, pageNumber: int) -> str:
		return requests.get(self.url + "?page=" + str(pageNumber)).text
