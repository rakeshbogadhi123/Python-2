import requests
from bs4 import BeautifulSoup
source = requests.get('https://www.imdb.com/search/title-text/?plot=top+movies').text
html_soup = BeautifulSoup(source,'lxml')
movie_list = html_soup.find_all('div',class_='lister-item mode-detail').text
print(type(movie_list))
print(len(movie_list))
#print(movie_list.h3)
