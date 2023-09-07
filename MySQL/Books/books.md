INSERT INTO users (first_name, last_name) VALUES ("Jane", "Amsden"),("Emily", " Dixon"),("Theodore", " Dostoevsky"),("William", " Shapiro"),("Lau", " Xiu");

INSERT INTO books (title, num_of_pages) VALUES ("C Sharp",500),("Java",600),("Python",600),("PHP",1000),("Ruby",2000);

UPDATE books SET title = 'C#' WHERE title = 'C Sharp';

UPDATE users SET first_name = "Bill" WHERE id = 4;

INSERT INTO favorites (users_id,books_id)
VALUES (1,1),(1,2),;

INSERT INTO favorites (users_id,books_id) VALUES (1,1),(1,2);

INSERT INTO favorites (users_id,books_id) VALUES (2,1),(2,2),(2,3);

INSERT INTO favorites (users_id,books_id) VALUES (4,1),(4,2),(4,3),(4,4),(4,5);

SELECT * FROM books JOIN favorites on books.id = favorites.books_id JOIN users on users.id = favorites.users_id WHERE books.id = 3;

INSERT INTO favorites (users_id, books_id) VALUES (5,2);

SELECT users_id from favorites WHERE books_id = 3 ORDER BY users_id LIMIT 1;

SELECT * FROM books JOIN favorites ON books.id = favorites.books_id JOIN users ON users.id = favorites.users_id WHERE books.id = 5;