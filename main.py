import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
animes = pd.read_csv('anime.csv')
animes =  animes[['anime_id','names','genre','type','rating','episodes']]
animes.dropna(inplace=True)
new_df = animes[['anime_id','names','genre']]
# new_df['genre'] = new_df['genre'].apply(lambda x: " ".join(x))

cv = CountVectorizer(max_features=13000,stop_words='english')
vectors = cv.fit_transform(new_df['genre']).toarray()
ps = PorterStemmer()
def stem(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_df['genre'] = new_df['genre'].apply(stem)
similarity = cosine_similarity(vectors)

def recommend(anime):
    anime_index = new_df[new_df['names'] == anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    for i in anime_list:
        print(new_df.iloc[i[0]].names)
        print(new_df.iloc[i[0]].anime_id)

#print(new_df)
recommend('Fullmetal Alchemist: Brotherhood')
# pickle.dump(new_df.to_dict(),open('animes_dict.pkl','wb'))
# pickle.dump(similarity,open('similarity1.pkl','wb'))