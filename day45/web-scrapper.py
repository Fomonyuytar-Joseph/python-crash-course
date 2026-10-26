from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")


yc_webpage = response.text
soup = BeautifulSoup(yc_webpage,"html.parser")


articles  = soup.select(".title .titleline a")

article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)

    article_link = article_tag.get("href") 
    article_links.append(article_link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)

largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])



# print(article_upvotes)
# print(article_texts)
# print(article_links)

# headings = soup.select(".title .titleline a")

# print(headings)


# for heading in headings:
#     print(heading.getText())



# print(soup.title)












# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")


# section_heading = soup.find(name="h3" , class_="heading")

# name = soup.select_one(selector="#name")


# heading = soup.select(".heading")
# print(heading)
# print(name)
# company_url = soup.select_one(selector="p a")

# print(section_heading)





# print(soup.find_all(name="p"))
# for tag in all_anchor_tags:
#      print(tag.getText())
#     print(tag.get("href"))

    

# heading = soup.find(name="h1", id="name")
# print(heading)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
