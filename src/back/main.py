from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import Optional
import requests


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = '15d2ea6d0dc1d476efbca3eba2b9bbfb'
recommendation_payload = {'api_key': api_key, 'language': 'en-US'}

r = requests.get('https://api.themoviedb.org/3/genre/movie/list',
                params=recommendation_payload, timeout=10).json()['genres']

movie_genres=dict()
for genre in r:
    movie_genres[str(genre['id'])]=genre['name']

@app.get("/recommendation/{title}")
async def recommendation(title: str = Path(None, description="Title of the basis movie (mandatory)"),
                         #limit: Optional[int] = Query(None, description="Max nr of movies to list."),
                         #genre: Optional[str] = Query(None, description="Search by genre"),
                         #director: Optional[str] = Query(None, description="Search by director"),
                         #actor: Optional[str] = Query(None, description="Search by actor"),
                         #keyword: Optional[str] = Query(None, description="Search by a keyword from description"),
                         #release_year: Optional[int] = Query(None, description="Search by release year")
                         ):

    movie_payload = {
        'api_key': api_key,
        'language': 'en-US',
        'include_adult': 'false',
        'query': title
    }

    r = requests.get('https://api.themoviedb.org/3/search/movie',
                     params=movie_payload, timeout=10)

    if(not r.ok):
        raise HTTPException(status_code=r.status_code, detail="Some error")

    if(r.json()['total_results'] == 0):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No movie found")

    movie_found=r.json()['results'][0]
    movie_id = movie_found['id']

    r = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations', params=recommendation_payload, timeout=10)

    if(not r.ok):
        raise HTTPException(status_code=r.status_code, detail="Some error")

    results = r.json()['results']
    results.insert(0,movie_found)
    for movie in results:
        movie['poster_path'] = 'https://image.tmdb.org/t/p/original' + movie['poster_path']
        id=movie['id']
        imdb_id = requests.get(
            f'https://api.themoviedb.org/3/movie/{id}',
            params=recommendation_payload,
            timeout=10).json()['imdb_id']
        movie['imdb_path'] = 'https://www.imdb.com/title/' + imdb_id
        
        providers = requests.get(
            f'https://api.themoviedb.org/3/movie/{id}/watch/providers?api_key={api_key}',
            timeout=10).json()['results']
        
        if 'FI' in providers:
            providers=providers['FI']
        else:
            providers=providers['US']

        if 'flatrate' in providers:
            movie['providers'] = providers['flatrate']
        else:
            movie['providers'] = providers['buy']

        for provider in movie['providers']:
            provider['logo_path'] = 'https://image.tmdb.org/t/p/original' + provider['logo_path']
        genres=[]
        for genre in movie['genre_ids']:
           genres.append(movie_genres[str(genre)])
        movie['genre_ids']=genres
        movie['release_date']=movie['release_date'][0:4]
    
   

    return results