DROP TABLE IF EXIST songs;
DROP TABLE IF EXIST users;

CREATE TABLE user(
id serial PRIMARY KEY,
username varchar (30) UNIQUE NOT NULL,
first_username varchar (30) NOT NULL,
last_name varchar (30)  NOT NULL,
created_at date NOT NULL,
updated_at date
);

CREATE TABLE songs(
id  serial PRIMARY KEY,
user_id int NOT NULL,
name varchar (30) NOT NULL,
genre varchar (30)  NOT NULL,
created_at date NOT NULL,
updated_at date,
CONSTRAINT user_id FOREIGN Key (user-id) REFERENCES user(id) on DELETE CASCADE
);
