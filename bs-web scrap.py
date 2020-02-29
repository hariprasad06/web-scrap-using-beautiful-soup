
import requests
from bs4 import BeautifulSoup

url=requests.get("https://codingbat.com/python")

soup = BeautifulSoup(url.text, "html.parser")
print(soup.findAll("tr")) # Get all table row values from the page