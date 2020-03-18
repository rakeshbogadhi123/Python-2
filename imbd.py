import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.imdb.com/chart/top').text

soup = BeautifulSoup(source,'lxml')

movies = [] ; years=[] ; ratings = []; movie_year_dict={}
for movie in soup.find_all('td',class_='titleColumn'):
    movies.append(movie.a.text)

for year in soup.find_all('span',class_='secondaryInfo'):
    years.append(year.text)

for rating in soup.find_all('strong'):
    ratings.append(rating.text)

movie_year_dict = {movies[i]:{years[i]:rating[i]} for i in range(len(movies))}

print(movie_year_dict)
