Test

curl -X GET http://127.0.0.1:8000/api/books
curl -X POST -H "Content-Type: application/json" -d '{
    "title": "Book #1",
    "author": "Author",
    "status": "reading",
}' http://127.0.0.1:8000/api/books
curl -X GET http://127.0.0.1:8000/api/books/1
curl -X PUT -H "Content-Type: application/json" -d '{
    "status": "finished",
    "rating": 5
}' http://127.0.0.1:8000/api/books/1
curl -X GET http://127.0.0.1:8000/api/books/stats
curl -X DELETE http://127.0.0.1:8000/api/books/1