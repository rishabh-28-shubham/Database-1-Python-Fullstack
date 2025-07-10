# MySQL Cheat Sheet

This cheat sheet provides a concise reference for MySQL commands, covering database management, table operations, querying, advanced features, and common interview questions. It is designed for quick lookup of syntax and examples, suitable for beginners and experienced users.

## 1. Database Management

### Connect to MySQL

Log in to the MySQL server:

- Syntax: `mysql -u <username> -p`
- Example: `mysql -u root -p`

### Create Database

Create a new database:

- Syntax: `CREATE DATABASE <database_name>;`
- Example: `CREATE DATABASE blog_system;`

### Use Database

Switch to a specific database:

- Syntax: `USE <database_name>;`
- Example: `USE blog_system;`

### Show Databases

List all databases:

- Syntax: `SHOW DATABASES;`

### Drop Database

Delete a database:

- Syntax: `DROP DATABASE <database_name>;`
- Example: `DROP DATABASE blog_system;`

## 2. Table Operations

### Create Table

Define a new table:

- Syntax:

  ```sql
  CREATE TABLE <table_name> (
      <column_name> <data_type> [constraints],
      ...
  );
  ```
- Example:

  ```sql
  CREATE TABLE users (
      user_id VARCHAR(36) PRIMARY KEY,
      username VARCHAR(50) UNIQUE NOT NULL,
      created_at DATE
  );
  ```

### Show Tables

List all tables in the current database:

- Syntax: `SHOW TABLES;`

### Describe Table

View table structure:

- Syntax: `DESCRIBE <table_name>;`
- Example: `DESCRIBE users;`

### Drop Table

Delete a table:

- Syntax: `DROP TABLE <table_name>;`
- Example: `DROP TABLE users;`

### Alter Table

Modify table structure:

- Add column: `ALTER TABLE <table_name> ADD <column_name> <data_type>;`
- Example: `ALTER TABLE users ADD email VARCHAR(100);`
- Modify column: `ALTER TABLE <table_name> MODIFY <column_name> <new_data_type>;`
- Example: `ALTER TABLE users MODIFY username VARCHAR(100);`
- Drop column: `ALTER TABLE <table_name> DROP COLUMN <column_name>;`
- Example: `ALTER TABLE users DROP COLUMN email;`

## 3. Data Manipulation

### Insert Data

Add a new record:

- Syntax: `INSERT INTO <table_name> (<column1>, <column2>, ...) VALUES (<value1>, <value2>, ...);`
- Example:

  ```sql
  INSERT INTO users (user_id, username, created_at)
  VALUES ('aec92dd8-79dd-4b22-9deb-a2af00d568c8', 'alycia662571', '2023-10-15');
  ```

### Update Data

Modify existing records:

- Syntax: `UPDATE <table_name> SET <column>=<value> WHERE <condition>;`
- Example: `UPDATE users SET username='alycia_new' WHERE user_id='aec92dd8-79dd-4b22-9deb-a2af00d568c8';`

### Delete Data

Remove records:

- Syntax: `DELETE FROM <table_name> WHERE <condition>;`
- Example: `DELETE FROM users WHERE user_id='aec92dd8-79dd-4b22-9deb-a2af00d568c8';`

### Select Data

Retrieve data:

- Syntax: `SELECT <columns> FROM <table_name> [WHERE <condition>];`
- Example: `SELECT username, created_at FROM users WHERE user_id='aec92dd8-79dd-4b22-9deb-a2af00d568c8';`

## 4. Querying Data

### Basic Queries

- Select all columns: `SELECT * FROM <table_name>;`
- Example: `SELECT * FROM users;`
- Filter with WHERE: `SELECT <columns> FROM <table_name> WHERE <column>=<value>;`
- Example: `SELECT title FROM posts WHERE category='Entertainment';`

### Joins

Combine data from multiple tables:

- Inner Join: `SELECT <columns> FROM <table1> INNER JOIN <table2> ON <condition>;`
- Example: `SELECT p.title, u.username FROM posts p INNER JOIN users u ON p.user_id=u.user_id;`
- Left Join: `SELECT <columns> FROM <table1> LEFT JOIN <table2> ON <condition>;`
- Example: `SELECT u.username, COUNT(p.id) FROM users u LEFT JOIN posts p ON u.user_id=p.user_id GROUP BY u.user_id;`

### Aggregation

Summarize data:

- Count: `SELECT COUNT(<column>) FROM <table_name>;`
- Example: `SELECT COUNT(*) FROM posts;`
- Group By: `SELECT <column>, COUNT(*) FROM <table_name> GROUP BY <column>;`
- Example: `SELECT category, COUNT(*) FROM posts GROUP BY category;`
- Sum, Avg, Min, Max: `SELECT SUM(<column>), AVG(<column>), MIN(<column>), MAX(<column>) FROM <table_name>;`

### Sorting

Order results:

- Syntax: `SELECT <columns> FROM <table_name> ORDER BY <column> [ASC|DESC];`
- Example: `SELECT title, created_at FROM posts ORDER BY created_at DESC;`

### Limiting Results

Restrict number of rows:

- Syntax: `SELECT <columns> FROM <table_name> LIMIT <number> [OFFSET <number>];`
- Example: `SELECT id, title FROM posts LIMIT 10 OFFSET 0;`

### Pattern Matching

Search with wildcards:

- Syntax: `SELECT <columns> FROM <table_name> WHERE <column> LIKE '<pattern>';`
- Example: `SELECT title FROM posts WHERE title LIKE '%Alien%';`

## 5. Advanced Features

### Indexes

Improve query performance:

- Create Index: `CREATE INDEX <index_name> ON <table_name>(<column>);`
- Example: `CREATE INDEX idx_user_id ON posts(user_id);`
- Drop Index: `DROP INDEX <index_name> ON <table_name>;`
- Example: `DROP INDEX idx_user_id ON posts;`

### Full-Text Search

Search text fields efficiently:

- Create Full-Text Index: `ALTER TABLE <table_name> ADD FULLTEXT(<column>);`
- Example: `ALTER TABLE posts ADD FULLTEXT(summary, main_content);`
- Search: `SELECT <columns> FROM <table_name> WHERE MATCH(<column>) AGAINST('<keyword>');`
- Example: `SELECT title FROM posts WHERE MATCH(summary, main_content) AGAINST('extraterrestrial');`

### Transactions

Ensure data integrity:

- Start: `START TRANSACTION;`
- Commit: `COMMIT;`
- Rollback: `ROLLBACK;`
- Example:

  ```sql
  START TRANSACTION;
  INSERT INTO users (user_id, username) VALUES ('new-id', 'newuser');
  INSERT INTO posts (id, user_id, title) VALUES ('post-id', 'new-id', 'Test');
  COMMIT;
  ```

### Triggers

Automate actions:

- Syntax:

  ```sql
  CREATE TRIGGER <trigger_name>
  BEFORE|AFTER INSERT|UPDATE|DELETE ON <table_name>
  FOR EACH ROW
  SET <column>=<value>;
  ```
- Example:

  ```sql
  CREATE TRIGGER update_timestamp
  BEFORE UPDATE ON posts
  FOR EACH ROW
  SET NEW.updated_at=CURDATE();
  ```

### Stored Procedures

Encapsulate logic:

- Syntax:

  ```sql
  DELIMITER //
  CREATE PROCEDURE <procedure_name>(<parameters>)
  BEGIN
      <statements>;
  END //
  DELIMITER ;
  ```
- Example:

  ```sql
  DELIMITER //
  CREATE PROCEDURE GetUserPosts(IN userId VARCHAR(36))
  BEGIN
      SELECT title FROM posts WHERE user_id=userId;
  END //
  DELIMITER ;
  CALL GetUserPosts('aec92dd8-79dd-4b22-9deb-a2af00d568c8');
  ```

## 6. Security

### User Management

- Create User: `CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>';`
- Example: `CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'secure_password';`
- Grant Privileges: `GRANT <privileges> ON <database>.* TO '<username>'@'localhost';`
- Example: `GRANT SELECT, INSERT, UPDATE ON blog_system.* TO 'app_user'@'localhost';`
- Revoke Privileges: `REVOKE <privileges> ON <database>.* FROM '<username>'@'localhost';`
- Drop User: `DROP USER '<username>'@'localhost';`

### Password Hashing

Use `SHA2` for passwords:

- Example: `SELECT SHA2('password', 256);`
- Note: In production, use application-level hashing (e.g., bcrypt).

## 7. Common MySQL Interview Questions

Below are frequently asked MySQL interview questions to help prepare for technical interviews, covering basic to advanced concepts.

### Basic Questions

1. **What is MySQL, and how does it differ from other databases like PostgreSQL?**

   - MySQL is an open-source RDBMS using SQL for structured data. It differs from PostgreSQL in areas like default storage engines (InnoDB vs. PostgreSQL’s native engine), JSON support, and advanced features (PostgreSQL has more robust support for complex queries).

2. **What are primary and foreign keys?**

   - A primary key uniquely identifies each record in a table (e.g., `user_id`). A foreign key links records between tables, enforcing referential integrity (e.g., `posts.user_id` references `users.user_id`).

3. **Explain the difference between DELETE and TRUNCATE.**

   - `DELETE` removes specific rows based on a `WHERE` clause and is reversible with transactions. `TRUNCATE` removes all rows and resets the table structure, is faster, but cannot be rolled back in some engines.

### Intermediate Questions

4. **What is a JOIN, and what are the different types?**

   - A `JOIN` combines rows from multiple tables based on a condition. Types include:
     - `INNER JOIN`: Returns matching records from both tables.
     - `LEFT JOIN`: Returns all records from the left table, with matching records from the right (NULL if no match).
     - `RIGHT JOIN`: Opposite of `LEFT JOIN`.
     - `FULL JOIN`: Returns all records when there’s a match in either table (MySQL emulates with `UNION`).

5. **How does indexing improve performance?**

   - Indexes create data structures (e.g., B-trees) to speed up searches on columns. They reduce query execution time for `WHERE`, `JOIN`, and `ORDER BY` but increase write time and storage.

6. **What is the difference between CHAR and VARCHAR?**

   - `CHAR` has a fixed length (padded with spaces), faster for fixed-size data. `VARCHAR` has variable length, saving space for varying data but slightly slower.

### Advanced Questions

 7. **Explain ACID properties in MySQL.**

    - **Atomicity**: Ensures all operations in a transaction complete, or none do.
    - **Consistency**: Guarantees the database remains in a valid state.
    - **Isolation**: Transactions are independent, preventing interference.
    - **Durability**: Committed transactions are permanently saved, even in a crash.

 8. **How would you optimize a slow query?**

    - Use `EXPLAIN` to analyze the query plan.
    - Add indexes on frequently filtered or joined columns.
    - Avoid `SELECT *` and specify needed columns.
    - Optimize joins by ensuring proper indexing.
    - Consider partitioning or caching for large datasets.

 9. **What is a stored procedure, and when would you use one?**

    - A stored procedure is a precompiled set of SQL statements stored in the database. Use them for repetitive tasks, complex logic, or to reduce application-side code (e.g., generating reports).

10. **How do you prevent SQL injection in MySQL?**

    - Use prepared statements or parameterized queries to separate SQL code from user input.
    - Escape user inputs if necessary.
    - Limit database user privileges to minimize damage.

### Practical Questions

11. **Write a query to find duplicate records in a table.**

    - Example: Find duplicate usernames in the `users` table:

      ```sql
      SELECT username, COUNT(*) as count
      FROM users
      GROUP BY username
      HAVING count > 1;
      ```

12. **Design a query to retrieve the top 5 most recent posts by a user.**

    - Example:

      ```sql
      SELECT title, created_at
      FROM posts
      WHERE user_id = 'aec92dd8-79dd-4b22-9deb-a2af00d568c8'
      ORDER BY created_at DESC
      LIMIT 5;
      ```

13. **How would you implement a full-text search in MySQL?**

    - Create a full-text index and use `MATCH...AGAINST`:

      ```sql
      ALTER TABLE posts ADD FULLTEXT(title, summary);
      SELECT title
      FROM posts
      WHERE MATCH(title, summary) AGAINST('search term');
      ```