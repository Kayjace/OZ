from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import BookSchema


blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 메모리 내 데이터 저장소
books = []

@blp.route('/')
class BooksList(MethodView):
    @blp.response(200, BookSchema(many=True))
    def get(self):
        """책 목록을 반환합니다."""
        return books

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_book):
        """새 책을 추가합니다."""
        new_book['id'] = len(books) + 1
        books.append(new_book)
        return new_book


@blp.route('/<int:book_id>')
class Book(MethodView):
    @blp.response(200, BookSchema)
    def get(self, book_id):
        """특정 책의 정보를 반환합니다."""
        if book_id >= len(books) or book_id < 0:
            abort(404, message="Book not found.")
        return books[book_id]

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, updated_book, book_id):
        """특정 책의 정보를 업데이트합니다."""
        if book_id >= len(books) or book_id < 0:
            abort(404, message="책을 찾을 수 없습니다.")
        books[book_id] = updated_book
        return updated_book

    @blp.response(204)
    def delete(self, book_id):
        """특정 책을 삭제합니다."""
        if book_id >= len(books) or book_id < 0:
            abort(404, message="책을 찾을 수 없습니다.")
        books.pop(book_id)
        return '', 204