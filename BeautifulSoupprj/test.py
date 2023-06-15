import requests
from bs4 import BeautifulSoup

# Define the URL of the Amazon product page
url = "https://www.amazon.in/Sony-PS4-Slim-500-Console/dp/B01MUHVQWT/ref=sr_1_1?keywords=playstation+4&qid=1685556244&sr=8-1"
# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the product title
title_element = soup.find('span', {'id': 'productTitle'})
title = title_element.text.strip()

# Find the product price
price_element = soup.find('span', {'class': 'a-price-whole'})
price = price_element.text.strip()

# Find the product image URL
image_element = soup.find('img', {'id': 'landingImage'})
image_url = image_element['data-old-hires']

# Find the product rating
rating_element = soup.find('span', {'class': 'a-icon-alt'})
rating = rating_element.text.strip()

# Print the product details
print(f"Product Title: {title}")
print(f"Product Price: ${price}")
print(f"Product Image URL: {image_url}")
print(f"Product Rating: {rating}")