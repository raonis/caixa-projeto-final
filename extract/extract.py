import requests
import pandas as pd
import random

# Configurações
API_KEY = "SUA_API_KEY_AQUI"  # Substitua pela sua chave da OMDb
BASE_URL = "http://www.omdbapi.com/"

# 1. Lista de filmes para buscar (Exemplo)
movie_titles = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Pulp Fiction"]

def fetch_movie_data(titles):
    movies_list = []
    for title in titles:
        params = {'t': title, 'apikey': API_KEY}
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if data.get('Response') == 'True':
            movies_list.append({
                'movie_id': data.get('imdbID'),
                'title': data.get('Title'),
                'year': data.get('Year'),
                'genre': data.get('Genre'),
                'director': data.get('Director')
            })
    return pd.DataFrame(movies_list)

def generate_mock_data(movie_df):
    # Gerando Usuários fictícios
    users = pd.DataFrame({
        'user_id': [101, 102, 103, 104],
        'name': ['Alice', 'Bruno', 'Carla', 'Diego'],
        'email': ['alice@email.com', 'bruno@email.com', 'carla@email.com', 'diego@email.com']
    })
    
    # Gerando Ratings fictícios baseados nos IDs dos filmes extraídos
    ratings_list = []
    movie_ids = movie_df['movie_id'].tolist()
    
    for user_id in users['user_id']:
        # Cada usuário avalia 2 filmes aleatórios
        chosen_movies = random.sample(movie_ids, k=2)
        for m_id in chosen_movies:
            ratings_list.append({
                'user_id': user_id,
                'movie_id': m_id,
                'rating': random.randint(1, 5),
                'timestamp': '2023-10-27'
            })
    
    ratings = pd.DataFrame(ratings_list)
    return users, ratings

# Execução do Processo
print("Iniciando extração de filmes...")
df_movies = fetch_movie_data(movie_titles)

print("Gerando dados de usuários e avaliações...")
df_users, df_ratings = generate_mock_data(df_movies)

# Salvando os arquivos CSV
df_movies.to_csv('movies.csv', index=False)
df_users.to_csv('users.csv', index=False)
df_ratings.to_csv('ratings.csv', index=False)

print("\nArquivos gerados com sucesso:")
print("- movies.csv")
print("- users.csv")
print("- ratings.csv")