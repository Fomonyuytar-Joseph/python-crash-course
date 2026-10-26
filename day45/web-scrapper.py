from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")


section_heading = soup.find(name="h3" , class_="heading")

name = soup.select_one(selector="#name")


heading = soup.select(".heading")
print(heading)
print(name)
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
