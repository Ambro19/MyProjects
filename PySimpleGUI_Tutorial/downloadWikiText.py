import requests
from bs4 import BeautifulSoup

# define the Wikipedia URL to download
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# retrieve the HTML content from the URL
response = requests.get(url)
html_content = response.content

# extract the text content from the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
article_div = soup.find("div", {"id": "content"})

if article_div is not None:
    article_text = article_div.get_text()

    # write the text content to a file
    filename = "python_wikipedia.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(article_text)
else:
    print("Error: could not find article text")