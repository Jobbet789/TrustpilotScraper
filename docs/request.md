request.py
==========

This file contains a class called `RequestClass` that handles HTTP requests.

Class Definitions
-----------------

### `RequestClass`

The `RequestClass` class has the following attributes:

*   `baseUrl` (str): the base URL for the requests
*   `trustName` (str): the trust name for the requests
*   `uploadUrl` (str): the URL for uploading data (fixed value: "[http://kapper.gideon.nu:3004/api/review](http://kapper.gideon.nu:3004/api/review)")
*   `url` (str): the full URL for the requests, constructed by concatenating `baseUrl` and `trustName`

The `RequestClass` class has the following methods:

#### `__init__(self, baseUrl: str, trustName: str)`

The constructor for the `RequestClass` class. It takes in the following arguments:

*   `baseUrl` (str): the base URL for the requests
*   `trustName` (str): the trust name for the requests

It initializes the `baseUrl`, `trustName`, `uploadUrl`, and `url` attributes with the given values.

#### `getHtml(self) -> str`

This method sends a GET request to the URL stored in the `url` attribute and returns the HTML response as a string.

#### `uploadOne(self, data: dict) -> requests.Response`

This method sends a POST request to the `uploadUrl` attribute with the given `data` (a dictionary) and returns the response object.

#### `getHtmlFromPage(self, pageNumber: int) -> str`

This method sends a GET request to the URL stored in the `url` attribute with a query parameter `page` set to the given `pageNumber`. It returns the HTML response as a string.
