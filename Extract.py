import requests
from BeautifulSoup import BeautifulSoup

url = 'https://www.youtube.com/results?search_query='
#query = 'mockingbird'
query = raw_input('Enter the song name to search: ')
search_url = url + query
#url = raw_input("Entet the youtube url: ")
response = requests.get(search_url)
html = response.content
soup = BeautifulSoup(html)
#extract the first result
all_result = soup.find('ol' , attrs = {'class' : 'item-section'})
first_result = all_result.find('a')
url = first_result['href']
url = 'https://www.youtube.com'+url

#scrape the rating from this link
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
likes = soup.find('button' , attrs = {'title' : 'I like this'})
dislikes = soup.find('button' , attrs = {'title' : 'I dislike this'})
related_videos = soup.find('ul' , attrs = {'id' : 'watch-related'})
views = soup.find('div', attrs={'class': 'watch-view-count'})
ups = int(likes.getText().replace(',' , ''))
downs = int(dislikes.getText().replace(',' , ''))
print("likes: " , ups)
print("dislikes: " , downs)
print("views: " , views.getText())
for row in related_videos.findAll('a' , href=True):
	video_url = "https://www.youtube.com" + row['href']
	print video_url



