from pymongo import MongoClient
from datetime import datetime

def insert_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.Newdb  # 'local' 데이터베이스 사용

    # 책 데이터 삽입
    books = [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "genre": "Magical Realism", "year": 2002},
        {"title": "Mistborn: The Final Empire", "author": "Brandon Sanderson", "genre": "Fantasy", "year": 2006},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "genre": "Romance", "year": 2009},
        {"title": "1Q84", "author": "Haruki Murakami", "genre": "Science Fiction", "year": 2009},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Historical Fiction", "year": 2009},
        {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "year": 1949},
        {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "genre": "Fantasy", "year": 2007},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "year": 1951},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "year": 1813},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Coming-of-Age", "year": 1951},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy", "year": 1954},
        {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy", "year": 1954}
    ]
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = [
    {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
    {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
    {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0},
    {"title": "Dunkirk", "director": "Christopher Nolan", "year": 2017, "rating": 7.9},
    {"title": "Pulp Fiction", "director": "Quentin Tarantino", "year": 1994, "rating": 8.9},
    {"title": "Kill Bill: Vol. 1", "director": "Quentin Tarantino", "year": 2003, "rating": 8.1},
    {"title": "Once Upon a Time in Hollywood", "director": "Quentin Tarantino", "year": 2019, "rating": 7.6},
    {"title": "Reservoir Dogs", "director": "Quentin Tarantino", "year": 1992, "rating": 8.3},
    {"title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994, "rating": 9.3},
    {"title": "The Green Mile", "director": "Frank Darabont", "year": 1999, "rating": 8.6},
    {"title": "The Mist", "director": "Frank Darabont", "year": 2007, "rating": 7.1},
    {"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972, "rating": 9.2},
    {"title": "The Godfather Part II", "director": "Francis Ford Coppola", "year": 1974, "rating": 9.0},
    {"title": "Apocalypse Now", "director": "Francis Ford Coppola", "year": 1979, "rating": 8.4}
]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {"user_id": 1, "action": "click", "timestamp": datetime(2023, 4, 2, 9, 0, 0)},
        {"user_id": 1, "action": "view", "timestamp": datetime(2023, 4, 2, 9, 0, 0)},
        {"user_id": 2, "action": "purchase", "timestamp": datetime(2023, 4, 11, 8, 0, 0)},
        {"user_id": 1, "action": "purchase", "timestamp": datetime(2023, 4, 11, 10, 0, 0)},
        {"user_id": 1, "action": "view", "timestamp": datetime(2023, 4, 14, 9, 0, 0)},
        {"user_id": 1, "action": "add_cart", "timestamp": datetime(2023, 4, 14, 10, 0, 0)}
    ]
    db.user_actions.insert_many(user_actions)

    print("Data inserted successfully")
    client.close()

if __name__ == "__main__":
    insert_data()
