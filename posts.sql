

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO users (name, email) VALUES
('Ravi', 'ravi@gmail.com'),
('Anu', 'anu@gmail.com'),
('Kumar', 'kumar@gmail.com'),
('Divya', 'divya@gmail.com');




CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    title VARCHAR(200) NOT NULL,
    content TEXT
);

INSERT INTO posts (user_id, title, content) VALUES
(1, 'Ravi First Post', 'Hello from Ravi'),
(1, 'Ravi Second Post', 'Learning SQL'),
(2, 'Anu Post 1', 'Database basics'),
(3, 'Kumar Post 1', 'PostgreSQL learning'),
(3, 'Kumar Post 2', 'Joins practice');


UPDATE posts
SET title = 'Updated Ravi First Post'
WHERE id = 1;




DELETE FROM posts
WHERE id = 5;



SELECT 
    p.id AS post_id,
    p.title,
    u.name AS author_name
FROM posts p
INNER JOIN users u
ON p.user_id = u.id;




SELECT 
    u.id,
    u.name,
    p.title
FROM users u
LEFT JOIN posts p
ON u.id = p.user_id;



SELECT 
    u.id,
    u.name,
    COUNT(p.id) AS total_posts
FROM users u
LEFT JOIN posts p
ON u.id = p.user_id
GROUP BY u.id, u.name
ORDER BY u.id;