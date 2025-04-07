from bs4 import BeautifulSoup
import requests
import html2text
import json

url = "https://ie.trustpilot.com/review/codeinstitute.net"
text = ""

page = 1
url = 'https://ie.trustpilot.com/review/codeinstitute.net?page={page}'
while True:
    paginated_url = url.format(page=page)
    res = requests.get(paginated_url)
    if res.status_code != 200:
        break
    
    text += res.text
    # This will only get the first page unless you remove the break statement
    break

soup = BeautifulSoup(text, 'html.parser')
articles = soup.find_all('article')

# Create a list to store all reviews
reviews = []
for article in articles:
    review_text = html2text.html2text(str(article))
    reviews.append({"review": review_text})

# Write to JSON file
with open('code_institute_reviews.json', 'w', encoding='utf-8') as f:
    json.dump(reviews, f, ensure_ascii=False, indent=4)

print(f"Saved {len(reviews)} reviews to code_institute_reviews.json")