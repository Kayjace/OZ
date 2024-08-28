from pymongo import MongoClient
from datetime import datetime

# 연결 설정 및 데이터베이스 선택
client = MongoClient('mongodb://localhost:27017/')
db = client['Newdb']

def get_books_by_genre(db, genre):
    """주어진 장르의 책들을 조회하여 출력합니다."""
    books_collection = db['books']
    query = {"genre": genre}
    projection = {"_id": 0, "title": 1, "author": 1}

    books = books_collection.find(query, projection)
    for book in books:
        print(book)

def get_director_average_ratings(db):
    """영화 감독별 평균 평점을 계산하여 출력합니다."""
    movies_collection = db['movies']
    pipeline = [
        {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},
        {"$sort": {"average_rating": -1}}
    ]

    results = movies_collection.aggregate(pipeline)
    for result in results:
        print({
            "Director": result["_id"],
            "Average_rating": result["average_rating"]
        })

def get_recent_user_actions(db, user_id, limit):
    """특정 사용자의 최근 행동을 조회하여 limit 만큼 출력합니다."""
    user_actions_collection = db['user_actions']
    query = {"user_id": user_id}
    sort_criteria = [("timestamp", -1)]
    projection = {"_id": 0}
    actions = user_actions_collection.find(query, projection).sort(sort_criteria).limit(limit)
    for action in actions:
        print(action)

def get_book_counts_by_year(db):
    """연도별 책의 개수를 집계하여 출력합니다."""
    books_collection = db['books']
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]

    results = books_collection.aggregate(pipeline)
    for result in results:
        print(result)

def update_user_actions_before_date(db, user_id, date, old_action, new_action):
    """특정 날짜 이전의 사용자의 행동을 업데이트합니다. (old_action to new_action)"""
    user_actions_collection = db['user_actions']
    query = {"user_id": user_id, "action": old_action, "timestamp": {"$lt": date}}
    update = {"$set": {"action": new_action}}

    result = user_actions_collection.update_many(query, update)
    print(f"Updated {result.modified_count} documents.")

def main():
    try:
        print("Books in the 'Fantasy' genre:")
        get_books_by_genre(db, "Fantasy")
        
        print("\nAverage ratings by director:")
        get_director_average_ratings(db)
        
        print("\nRecent actions by user with ID 1, limit to 5:")
        get_recent_user_actions(db, 1, 5)
        
        print("\nBook counts by year:")
        get_book_counts_by_year(db)
        
        print("\nUpdating user actions before April 10, 2023:")
        update_user_actions_before_date(db, 1, datetime(2023, 4, 10), "view", "seen")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()