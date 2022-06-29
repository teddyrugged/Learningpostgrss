from models.dbfile import DBFile


class ChangeSchema():
    @staticmethod
    def run():
        try:
            conn = DBFile.connect()
            curr = conn.cursor()
            with open('schema.sql', 'r', ) as file:
                curr.execute(file.read())
                conn.commit()
                print('database has been created !!!')
                return True
        except Exception as err:
            print(err)
        finally:
            if curr is not None:
                curr.close()
            if conn is not None:
                conn.close()

class ChangeSeeder():
    @staticmethod
    def run():
        try:
            conn = DBFile.connect()
            curr = conn.cursor()
            with open('seeder.sql', 'r', ) as file:
                curr.execute(file.read())
                conn.commit()
                print('Table records added  !!!')
                return True
        except Exception as err:
            print(err)
        finally:
            if curr is not None:
                curr.close()
            if conn is not None:
                conn.close()