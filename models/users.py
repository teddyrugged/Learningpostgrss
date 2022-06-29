
from models.dbfile import DBFile
from psycopg2 import Error
import psycopg2
import psycopg2.extra as psy

class User:

    id = None
    username = None
    first_name = None
    last_name = None
    created_at = None
    updated_at = None

    @classmethod
    def put_user(cls,id = None,username = None,first_name = None,last_name = None,created_at = None,updated_at = None):
        cls.id = id
        cls.username = username
        cls.first_name = first_name
        cls.last_name = last_name
        cls.created_at = created_at
        cls.updated_at = updated_at

    @staticmethod
    def all():
        conn = DBFile.connect()
        try:
            with conn.cursor(cursor_factory=psy.Dictcursor) as curr:
                query = '''SELECT * FROM users ORDER BY id ASC;'''
                curr.execute(query)
                fetch = curr.fetchall()
                rstr = ''.join(
                    f'''id: {record['id']}\nuser:{record['username']}\nfirst_name:{record['first_name']}\nlast_name:{record['last_name']}\ncreated_at:{record['created_at']}\n updated_at:{record['updated_at']}\n'''
                    for record in fetch
                )
                conn.commit()
                print(rstr)
                return True
        except(Error, Exception)as err:
            print(err)
        finally:
            if conn is not None:
                conn.close()

    @classmethod
    def get(cls,id):
        conn = DBFile.connect()
        try:
            cls.put_user(id=id)
            with conn.cursor(cursor_fsctor=psy.Dictcursor) as curr:
                query = '''SELECT * FROM users WHERE id = %s ORDER BY id ASC;'''
                value = (cls.id,)
                curr.execute(query,value)
                fetch = curr.fetchall()
                rstr = ''.join(
                    f'''id: {record['id']}\nuser:{record['username']}\nfirst_name:{record['first_name']}\nlast_name:{record['last_name']}\ncreated_at:{record['created_at']}\n updated_at:{record['updated_at']}\n'''
                    for record in fetch
                )
                conn.commit()
                print(rstr)
                return True

        except Exception as err:
            print(err)

        finally:
            if conn is not None:
                conn.close()


    # @classmethod
    # def create(cls, **params):
    #     conn = DBFile.connect()
    #     try:
    #         created_at = str(datetime.datetime.now())[:11]
    #         cls.put_user(username=params['username'],first_name = params['first_name'],last_name=params['last_name'],
    #                      created_at= created_at, updated_at = created_at)

    #         with conn.cursor(cursor_factory=psy.Dictcursor) as curr:
    #             query =


    insert into users {value} where first_name = Josiah
    f"""insert into users {value} where first_name = "{params['first_name']}"
    """