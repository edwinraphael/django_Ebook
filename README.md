# django_Ebook
API Documentation URLS METHOD DESCRIPTION 1-localhost:8000/account/signup for registering the user 2-localhost:8000/token,generate token by giving username and password
localhost:8000/genres/ get to list all genres in Ebook 4-localhost:8000/genres/genres id / to get specific genre. 4-/localhost:8000/genres/genre-id/add_books for adding book for specific genre(only for admin)

5-localhost:8000/genre/{genre-id}/get_books/ for getting book of specific genre 6-localhost:8000/books/?genres=genre_name(fiction) for filtering the book according to the genre.
7-localhost:8000/books/book_id/add_review for adding comment for a specific book. 8-localhost:8000/books/for listing all books 





created a admin user with username=admin password=admin,only admin can   manage genre and adding books and other users can view the books and post comment
