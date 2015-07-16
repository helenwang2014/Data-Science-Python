from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

'''first_paragraph = soup.find('p')

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

'''


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
