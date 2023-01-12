from lib import request
from lib import soup

numberOfReviews: int = 1

website: str = "www.amazon.com" # The domain of the website you want to scrape
# The website has to be uploaded onto trustpilot.


RequestClass: object = request.RequestClass("https://www.trustpilot.com/review/", website) # making the request class object
SoupClass: object = soup.SoupClass() # soupclass object


def getReviewsOfaPage(page: int) -> list: # get the reviews of a page.
	global numberOfReviews
	html: str = RequestClass.getHtmlFromPage(page) # Get html from website
	soup: object = SoupClass.get_soup(html) # Get soup from html


	elementList = SoupClass.get_review_elements(soup)

	reviewList = []
	for element in elementList:
		review: dict = SoupClass.get_review(element)
		reviewList.append(review)
		print(f'Number of Reviews: {numberOfReviews:^20}')
		print(f'Name: {review["name"]:^20}')
		print(f'Title: {review["title"]:^20}')
		print(f'Description: {review["description"]:^20}')
		print(f'Rating: {review["rating"]:^20}\n')
		numberOfReviews += 1
	return reviewList



def getNumberOfPages() -> int: # get the number of pages 
	html: str = RequestClass.getHtml() # Get html from website
	soup: object = SoupClass.get_soup(html) # Get soup from html
	
	# get the amount of pages 
	pageNav: object = SoupClass.get_pagenav_element(soup)
	amount: int = SoupClass.get_amount_of_pages(pageNav)

	return int(amount)

def main(): # get all the reviews (from all the pages)
	amountOfPages: int = getNumberOfPages() # get the amount
	
	# save everything in a list
	allReviews = []
	for page in range(1, amountOfPages+1):
		for review in getReviewsOfaPage(page):
			allReviews.append(review)
			# RequestClass.uploadOne(review) # in this example I'm using the request class to upload the reviews to a database using an api request.




if __name__ == "__main__":
	main() # call the main function
