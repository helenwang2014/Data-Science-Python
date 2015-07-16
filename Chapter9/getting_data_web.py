'''

from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')

first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

first_paragraph_id = soup.p['id']
first_paragraph_id2 = soup.p.get('id')

all_paragraphs = soup.find_all('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

important_paragraghs = soup('p', {'class': 'important'})
important_paragraghs2 = soup('p', 'important')
important_paragraghs3 = [p for p in soup('p') 
						 if 'important' in p.get('class', [])]


spans_inside_divs = [span 
						for div in soup('div')
						for span in div('span')]




url = "http://shop.oreilly.com/category/browse-subject/data.do?sortby=publicationDate&page=1"
soup = BeautifulSoup(requests.get(url).text,'html5lib')

tds = soup('td', "thumbtext")
print len(tds)



# test for videos with:
def is_video(td):
	#it's a video if it has exactly one pricelabel, and if the stripped text inside that pricelabel starts with 'Video'

	pricelabels = td('span', 'pricellabel')
	return (len(pricelabels) == 1 and pricelabels[0].text.strip().startswith("Video"))

print len([td for td in tds if not is_video(td)])

def book_info(td):
	title = td.find("div", "thumbheader").a.text

	author_name = td.find('div', 'AuthorName').text
	authors = [x.strip() for x in re.sub("^By ", "", author_name).split(",")]

	isbn_link = td.find("div", "thumbheader").a.get("href")

	isbn = re.match("/product/(.*)\.do", isbn_link).group(1)

	date = td.find("span", "directorydate").text.strip()


	return {
			"title" : title,
			"authors" : authors,
			"isbn" : isbn,
			"date" : date
			}



'''


# ready to scrape
from bs4 import BeautifulSoup
import requests
from time import sleep
base_url = "http://shop.oreilly.com/category/browse-subject/data.do?sortby=publicationDate&page="

books = []
NUM_PAGES = 3

for page_num in range(1, NUM_PAGES + 1):
	print "souping page", page_num, ",", len(books), "found so Far"
	url = base_url + str(page_num)
	soup = BeautifulSoup(requests.get(url).text, 'html5lib')

	for td in soup('td', 'thumbtext'):
		if not is_video(td):
			books.append(book_info(td))

	sleep(30)


from collections import Counter
# plot the number of books published each year
def get_year(book):
	#book["date"] looks like 'November 2014' so we need to split on the space and then take the second piece
	return int(book["date"].split()[1])

	# 2014 is the last complet year of data(when I ran this)

year_counts = Counter(get_year(book) for book in books
							if get_year(book) <= 2014)

import matplotlib.pyplot as plt 
years = sorted(year_counts)
book_counts = [year_counts[year] for year in years]
plt.plot(years, book_counts)
plt.ylabel("# of data books")
plt.title("Data is Big!")
plt.show()





