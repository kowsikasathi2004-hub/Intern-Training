
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    user_id INT,
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

-- ==============================
-- INSERT USERS
-- ==============================
INSERT INTO users (name, email)
VALUES
('John', 'john@gmail.com'),
('Alice', 'alice@gmail.com'),
('Bob', 'bob@gmail.com'),
('David', 'david@gmail.com');

-- ==============================
-- INSERT POSTS
-- ==============================
INSERT INTO posts (title, content, user_id)
VALUES
('SQL Basics', 'Introduction to SQL', 1),
('Database Design', 'Learning Normalization', 1),
('Python Guide', 'Python Programming Basics', 2),
('FastAPI Tutorial', 'Building REST APIs', 2),
('PostgreSQL Joins', 'Understanding JOIN Operations', 3);

-- ==============================
-- VIEW DATA
-- ==============================
SELECT * FROM users;
SELECT * FROM posts;

-- ==============================
-- UPDATE OPERATION
-- ==============================
UPDATE posts
SET title = 'Advanced SQL'
WHERE post_id = 1;

SELECT * FROM posts;

-- ==============================
-- DELETE OPERATION
-- ==============================
DELETE FROM posts
WHERE post_id = 4;

SELECT * FROM posts;

-- ==============================
-- INNER JOIN
-- ==============================
SELECT
    p.post_id,
    p.title,
    p.content,
    u.name AS author_name
FROM posts p
INNER JOIN users u
ON p.user_id = u.user_id;

-- ==============================
-- LEFT JOIN (FIXED)
-- ==============================
SELECT
    u.user_id,
    u.name,
    p.title
FROM users u
LEFT JOIN posts p
ON u.user_id = p.user_id
ORDER BY u.user_id;

-- ==============================
-- GROUP BY (POST COUNT)
-- ==============================
SELECT
    u.user_id,
    u.name,
    COUNT(p.post_id) AS total_posts
FROM users u
LEFT JOIN posts p
ON u.user_id = p.user_id
GROUP BY u.user_id, u.name
ORDER BY u.user_id;

-- ==============================
-- TOTAL POSTS
-- ==============================
SELECT COUNT(*) AS total_posts FROM posts;

-- ==============================
-- USER WITH MAX POSTS
-- ==============================
SELECT
    u.name,
    COUNT(p.post_id) AS post_count
FROM users u
LEFT JOIN posts p
ON u.user_id = p.user_id
GROUP BY u.user_id, u.name
ORDER BY post_count DESC;

-- ==============================
-- POSTS BY JOHN
-- ==============================
SELECT
    p.title,
    p.content
FROM posts p
INNER JOIN users u
ON p.user_id = u.user_id
WHERE u.name = 'John';