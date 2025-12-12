# 1. Movie Ratings Analyzer 
# Ask the user to input a list of movies with ratings like [("Titanic", 8), ("Inception", 9), ...]. Compute 
# the average rating, find the highest-rated movie, and list all movies with rating above the 
# average. 

n=int(input("Enter the number of the movies you want to analyse:"))
movies=[]
s_rate=0

for i in range(n):
    name=input("Enter the movie name:")
    rating=float(input("Enter the movie rating (out of 10):"))
    s_rate+=rating
    movies.append((name, rating))   

average_rating=s_rate/n
print(f"The average rating is:{average_rating}")

h_rate=movies[0]
# print(movies[1])
# print(h_rate[1])
for movie in movies:
    if movie[1]> h_rate[1]:
        h_rate = movie
print(f"The highest rating is: {h_rate[1]} for '{h_rate[0]}'")

print("Movies with rating above average:")
for movie in movies:
    if movie[1]>average_rating:
        print(movie)
