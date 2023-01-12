soup.py
=======

This file contains a class called `SoupClass` that processes HTML data using the Beautiful Soup library.

Class Definitions
-----------------

### `SoupClass`

The `SoupClass` class has the following class attributes:

*   `REVIEW_CARD` (dict): a dictionary containing the attribute and value to search for review elements in the HTML
*   `REVIEW_CONTENT` (dict): a dictionary containing the attribute and value to search for review content elements in the HTML
*   `REVIEW_STARS` (dict): a dictionary containing the attribute and value to search for review star rating elements in the HTML
*   `PAGE_NAV` (dict): a dictionary containing the attribute and value to search for pagination elements in the HTML

The `SoupClass` class has the following methods:

#### `get_soup(self, html: str) -> object`

This method takes in an HTML string and returns a Beautiful Soup object.

#### `get_element(self, soup: object, tag: str, attrs: dict) -> object`

This method takes in a Beautiful Soup object, a tag name, and a dictionary of attributes and values, and returns the first matching element as a Beautiful Soup object.

#### `get_elements(self, soup: object, tag: str, attrs: dict) -> list`

This method takes in a Beautiful Soup object, a tag name, and a dictionary of attributes and values, and returns a list of all matching elements as Beautiful Soup objects.

#### `get_review_element(self, soup: object) -> object`

This method takes in a Beautiful Soup object and returns the first review element as a Beautiful Soup object using the `REVIEW_CARD` class attribute to search for the element.

#### `get_review_elements(self, soup: object) -> list`

This method takes in a Beautiful Soup object and returns a list of all review elements as Beautiful Soup objects using the `REVIEW_CARD` class attribute to search for the elements.

#### `get_pagenav_element(self, soup: object) -> object`

This method takes in a Beautiful Soup object and returns the pagination element as a Beautiful Soup object using the `PAGE_NAV` class attribute to search for the element.

#### `get_review(self, element: object) -> dict`

This method takes in a review element as a Beautiful Soup object and returns a dictionary containing information about the review. The dictionary has the following keys:

*   `name` (str): the name of the reviewer
*   `title` (str): the title of the review
*   `description` (str): the description of the review
*   `rating` (str): the star rating of the review

#### `get_amount_of_pages(self, element: object) -> int`

This method takes in the pagination element as a Beautiful Soup object and returns the total number of pages as an integer. If the pagination element is not found, it returns 1.
