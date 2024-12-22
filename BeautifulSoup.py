from bs4 import BeautifulSoup
import requests

# URL of the webpage to scrape
url = "http://quotes.toscrape.com/"

# Send a GET request
response = requests.get(url)
if response.status_code == 200:
    print("Page fetched successfully!")
    #print(response.text)  # Print the HTML content
    html_content = response.text
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Extract specific elements
title = soup.title.text
heading = soup.h1.text
paragraph = soup.p.text
links = [a['href'] for a in soup.find_all('a')]

#print("Title:", title)
#print("Heading:", heading)
#print("Paragraph:", paragraph)
#print("Links:", links)
# Write the extracted data to a text file
with open("c:/Temp/scraped_data.txt", "w", encoding="utf-8") as file:
    file.write(f"Title: {title}\n")
    file.write(f"Heading: {heading}\n")
    file.write(f"Paragraph: {paragraph}\n")
    file.write("Links:\n")
    for link in links:
        file.write(f"{link}\n")

print("Data has been written to c:/Temp/scraped_data.txt")
# Extract text in the list after the hyperlink tab
list_items = [li.text for li in soup.find_all('li')]

# Write the list items to the text file
with open("c:/Temp/scraped_data.txt", "a", encoding="utf-8") as file:
    file.write("List Items:\n")
    for item in list_items:
        file.write(f"{item}\n")

# Combine hyperlinks and list items in one line with pipe delimiter
with open("c:/Temp/scraped_data.txt", "a", encoding="utf-8") as file:
    file.write("Links and List Items:\n")
    for link, item in zip(links, list_items):
        file.write(f"{link} | {item}\n")

print("Links and list items have been written to c:/Temp/scraped_data.txt")

# Extract class text
class_texts = [element.text for element in soup.find_all(class_=True)]

# Write the class texts to the text file
with open("c:/Temp/scraped_data.txt", "a", encoding="utf-8") as file:
    file.write("Class Texts:\n")
    for text in class_texts:
        file.write(f"{text}\n")

print("Class texts have been written to c:/Temp/scraped_data.txt")
