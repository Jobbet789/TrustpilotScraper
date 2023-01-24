from bs4 import BeautifulSoup

'''
	elementList = SoupClass.get_elements(SoupClass.get_soup(RequestClass.getHtml()), "article", {"class": "styles_reviewCard__hcAvl"}) 
	element = elementList[0].section
	print(SoupClass.get_element(element, "div", {"class": "styles_reviewContent__0Q2Tg"}).a.h2.text)

'''


class SoupClass:
	REVIEW_CARD = {"class": "styles_reviewCard__hcAvl"}
	REVIEW_CONTENT = {"class": "styles_reviewContent__0Q2Tg"}
	REVIEW_STARS = {"class": "styles_reviewHeader__iU9Px"}
	PAGE_NAV = {"class": "styles_pagination__6VmQv"}

	def get_soup(self, html: str) -> object: # return soup
		return BeautifulSoup(html, 'html.parser')
	
	def get_element(self, soup: object, tag: str, attrs: dict) -> object: # return element
		return soup.find(tag, attrs=attrs)

	def get_elements(self, soup, tag: str, attrs: dict) -> list: # return list of elements
		return soup.find_all(tag, attrs=attrs)

	def get_review_element(self, soup: object) -> object: # return review element
		return self.get_element(soup, "article", self.REVIEW_CARD)

	def get_review_elements(self, soup: object) -> list: # return list of review elements
		return self.get_elements(soup, "article", self.REVIEW_CARD)

	def get_pagenav_element(self, soup: object) -> object: # return pagenav element
		return self.get_element(soup, "div", self.PAGE_NAV)

	def get_review(self, element: object) -> str:
		mainReview = self.get_element(element, "div", self.REVIEW_CONTENT)
		reviewName = element.aside.div.a.span.text
		return {
				"name": reviewName,
				"title": mainReview.a.h2.text,
				"description": mainReview.p.text,
				"rating": self.get_element(element, "div", self.REVIEW_STARS).get("data-service-review-rating")
		}
	
	def get_amount_of_pages(self, element: object) -> int: # element is the pagenav element
		lastButton = element.find('a', {'name': 'pagination-button-last'}) # get the last button
		try:
			return lastButton.span.text # return the text of the last button
		except AttributeError:
			return 1



