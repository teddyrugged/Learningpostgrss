TRUNCATE TABLE songs;
TRUNCATE TABLE user CASCADE;
""" to remove the users table and songs table"""

INSERT INTO user (user_name, first_name, last_name, created_at, updated_at)
VALUES ('bloodtrist123', 'ben', 'Ubong', '2022-03-19','2022-03-21')
        ('bdrgonprobB', 'chineye', 'samuel', '2022-03-19','2022-03-21')
        ('flexGod', 'folake', 'forthenight', '2022-03-19','2022-03-21');


INSERT INTO songs (user_id, name, genre, created_at, updated_at)
                   (1,'stay with me', 'rnb',)'2022-03-19','2022-03-21'
                   (2, 'folake for the night', 'hiphop''2022-03-19','2022-03-21')
                   (3, 'forever young', 'pop','2022-03-19','2022-03-21');