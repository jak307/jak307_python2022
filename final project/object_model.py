import uuid
import json
import mysql.connector
from flask import Flask
app = Flask(__name__)

config = {
    'host': '67.205.163.33',
    'user': 'jak307',
    'password': 'InfSci1500_4131521',
    'database': 'jak307'
}

class User:
    def __init__(self, user_id="", username = "", password = "", email = ""):
        self.__username = username
        self.__password = password
        self.__email = email
        if user_id == "":
            self.__user_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO users (user_id, username, user_password, user_email)
                           VALUES (%s, %s, %s, %s) """

                values = [(self.__user_id, self.__username, self.__password, self.__email)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__user_id = user_id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_user_id(self):
        return self.__user_id

    def get_email(self):
        return self.__email

    def set_username(self, username):
        self.__username = username
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE users SET username = %s WHERE user_id = %s;'

            data_tuple = (self.__username, self.__user_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_password(self, password):
        self.__password = password
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE users SET user_password = %s WHERE user_id = %s;'

            data_tuple = (self.__password, self.__user_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_email(self, email):
        self.__email = email
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE users SET user_email = %s WHERE user_id = %s;'

            data_tuple = (self.__email, self.__user_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from users where user_id = %s"""
            cursor.execute(query, (self.__users_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "user id" : self.__user_id,
            "username" : self.__username,
            "password" : self.__password,
            "email" : self.__email
        }

        return json.dumps(fields_data)




class Director:
    def __init__(self, director_id="", director_fname = "", director_lname = ""):
        self.__fname = director_fname
        self.__lname = director_lname
        if director_id == "":
            self.__director_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO directors (director_id, director_fname, director_lname)
                           VALUES (%s, %s, %s) """

                values = [(self.__director_id, self.__fname, self.__lname)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__director_id = director_id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_director_id(self):
        return self.__director_id

    def set_fname(self, director_fname):
        self.__fname = director_fname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE directors SET director_fname = %s WHERE director_id = %s;'

            data_tuple = (self.__fname, self.__director_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_lname(self, director_lname):
        self.__lname = director_lname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE directors SET director_lname = %s WHERE director_id = %s;'

            data_tuple = (self.__lname, self.__director_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from directors where director_id = %s"""
            cursor.execute(query, (self.__director_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__director_id,
            "director first name" : self.__fname,
            "director last name" : self.__lname,
        }

        return json.dumps(fields_data)




class Actor:
    def __init__(self, actor_id="", actor_fname = "", actor_lname = ""):
        self.__fname = actor_fname
        self.__lname = actor_lname
        if actor_id == "":
            self.__actor_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO actors (actor_id, actor_fname, actor_lname)
                           VALUES (%s, %s, %s) """

                values = [(self.__actor_id, self.__fname, self.__lname)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__actor_id = actor_id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_actor_id(self):
        return self.__actor_id

    def set_fname(self, actor_fname):
        self.__fname = actor_fname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE actors SET actor_fname = %s WHERE actor_id = %s;'

            data_tuple = (self.__fname, self.__actor_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_lname(self, actor_lname):
        self.__lname = actor_lname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE actors SET actor_lname = %s WHERE actor_id = %s;'

            data_tuple = (self.__lname, self.__actor_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from actors where actor_id = %s"""
            cursor.execute(query, (self.__actor_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__actor_id,
            "actor first name" : self.__fname,
            "actor last name" : self.__lname,
        }

        return json.dumps(fields_data)




class Writer:
    def __init__(self, writer_id="", writer_fname = "", writer_lname = ""):
        self.__fname = writer_fname
        self.__lname = writer_lname
        if writer_id == "":
            self.__writer_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO writers (writer_id, writer_fname, writer_lname)
                           VALUES (%s, %s, %s) """

                values = [(self.__writer_id, self.__fname, self.__lname)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__writer_id = writer_id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_writer_id(self):
        return self.__writer_id

    def set_fname(self, writer_fname):
        self.__fname = writer_fname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE writers SET writer_fname = %s WHERE writer_id = %s;'

            data_tuple = (self.__fname, self.__writer_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_lname(self, writer_lname):
        self.__lname = writer_lname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE writers SET writer_lname = %s WHERE writer_id = %s;'

            data_tuple = (self.__lname, self.__writer_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from writers where writer_id = %s"""
            cursor.execute(query, (self.__writer_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__writer_id,
            "writer first name" : self.__fname,
            "writer last name" : self.__lname,
        }

        return json.dumps(fields_data)
    




class Producer:
    def __init__(self, producer_id="", producer_fname = "", producer_lname = ""):
        self.__fname = producer_fname
        self.__lname = producer_lname
        if producer_id == "":
            self.__producer_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO producers (producer_id, producer_fname, producer_lname)
                           VALUES (%s, %s, %s) """

                values = [(self.__producer_id, self.__fname, self.__lname)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__producer_id = producer_id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_producer_id(self):
        return self.__producer_id

    def set_fname(self, producer_fname):
        self.__fname = producer_fname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE producers SET producer_fname = %s WHERE producer_id = %s;'

            data_tuple = (self.__fname, self.__producer_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_lname(self, producer_lname):
        self.__lname = producer_lname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE producers SET producer_lname = %s WHERE producer_id = %s;'

            data_tuple = (self.__lname, self.__producer_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from producers where producer_id = %s"""
            cursor.execute(query, (self.__producer_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__producer_id,
            "producer first name" : self.__fname,
            "producer last name" : self.__lname,
        }

        return json.dumps(fields_data)





class Cinematographer:
    def __init__(self, cinematographer_id="", cinematographer_fname = "", cinematographer_lname = ""):
        self.__fname = cinematographer_fname
        self.__lname = cinematographer_lname
        if cinematographer_id == "":
            self.__cinematographer_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO cinematographers (cinematographer_id, cinematographer_fname, cinematographer_lname)
                           VALUES (%s, %s, %s) """

                values = [(self.__cinematographer_id, self.__fname, self.__lname)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__cinematographer_id = cinematographer_id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_cinematographer_id(self):
        return self.__cinematographer_id

    def set_fname(self, cinematographer_fname):
        self.__fname = cinematographer_fname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE cinematographers SET cinematographer_fname = %s WHERE cinematographer_id = %s;'

            data_tuple = (self.__fname, self.__cinematographer_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_lname(self, cinematographer_lname):
        self.__lname = cinematographer_lname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE cinematographers SET cinematographer_lname = %s WHERE cinematographer_id = %s;'

            data_tuple = (self.__lname, self.__cinematographer_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from cinematographers where cinematographer_id = %s"""
            cursor.execute(query, (self.__cinematographer_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__cinematographer_id,
            "cinematographer first name" : self.__fname,
            "cinematographer last name" : self.__lname,
        }

        return json.dumps(fields_data)




class Composer:
    def __init__(self, composer_id="", composer_fname = "", composer_lname = ""):
        self.__fname = composer_fname
        self.__lname = composer_lname
        if composer_id == "":
            self.__composer_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO composers (composer_id, composer_fname, composer_lname)
                           VALUES (%s, %s, %s) """

                values = [(self.__composer_id, self.__fname, self.__lname)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__composer_id = composer_id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_composer_id(self):
        return self.__composer_id

    def set_fname(self, composer_fname):
        self.__fname = composer_fname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE composers SET composer_fname = %s WHERE composer_id = %s;'

            data_tuple = (self.__fname, self.__composer_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_lname(self, composer_lname):
        self.__lname = composer_lname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE composers SET composer_lname = %s WHERE composer_id = %s;'

            data_tuple = (self.__lname, self.__composer_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from composers where composer_id = %s"""
            cursor.execute(query, (self.__composer_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__composer_id,
            "composer first name" : self.__fname,
            "composer last name" : self.__lname,
        }

        return json.dumps(fields_data)




class Editor:
    def __init__(self, editor_id="", editor_fname = "", editor_lname = ""):
        self.__fname = editor_fname
        self.__lname = editor_lname
        if editor_id == "":
            self.__editor_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO editors (editor_id, editor_fname, editor_lname)
                           VALUES (%s, %s, %s) """

                values = [(self.__editor_id, self.__fname, self.__lname)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__editor_id = editor_id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_editor_id(self):
        return self.__editor_id

    def set_fname(self, editor_fname):
        self.__fname = editor_fname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE editors SET editor_fname = %s WHERE editor_id = %s;'

            data_tuple = (self.__fname, self.__editor_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_lname(self, editor_lname):
        self.__lname = editor_lname
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE editors SET editor_lname = %s WHERE editor_id = %s;'

            data_tuple = (self.__lname, self.__editor_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from editors where editor_id = %s"""
            cursor.execute(query, (self.__editor_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__editor_id,
            "editor first name" : self.__fname,
            "editor last name" : self.__lname,
        }

        return json.dumps(fields_data)




class Film:
    def __init__(self, film_id="", film_name = "", film_year = "", film_language = "", film_description = ""):
        self.__name = film_name
        self.__year = film_year
        self.__description = film_description
        self.__language = film_language
        if film_id == "":
            self.__film_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO films (film_id, film_name, film_year, film_language, film_description)
                           VALUES (%s, %s, %s, %s, %s) """

                values = [(self.__film_id, self.__name, self.__year, self.__language, self.__description)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__film_id = film_id

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_language(self):
        return self.__language

    def get_descripton(self):
        return self.__description

    def get_film_id(self):
        return self.__film_id

    def set_name(self, film_name):
        self.__name = film_name
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE films SET film_name = %s WHERE film_id = %s;'

            data_tuple = (self.__name, self.__film_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_year(self, film_year):
        self.__year = film_year
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE films SET film_year = %s WHERE film_id = %s;'

            data_tuple = (self.__year, self.__film_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_language(self, film_language):
        self.__language = film_language
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE films SET film_language = %s WHERE film_id = %s;'

            data_tuple = (self.__language, self.__film_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_description(self, film_description):
        self.__description = film_description
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE films SET film_description = %s WHERE film_id = %s;'

            data_tuple = (self.__description, self.__film_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from users where user_id = %s"""
            cursor.execute(query, (self.__users_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "film id" : self.__film_id,
            "film name" : self.__name,
            "film year" : self.__year,
            "film language" : self.__language,
            "film description" : self.__description,
        }

        return json.dumps(fields_data)




class Studio:
    def __init__(self, studio_id="", studio_name = ""):
        self.__name = studio_name
        if studio_id == "":
            self.__studio_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO studios (studio_id, studio_name)
                           VALUES (%s, %s) """

                values = [(self.__studio_id, self.__name)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__studio_id = studio_id

    def get_name(self):
        return self.__name

    def get_studio_id(self):
        return self.__studio_id

    def set_name(self, studio_name):
        self.__name = studio_name
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE studios SET studio_name = %s WHERE studio_id = %s;'

            data_tuple = (self.__name, self.__studio_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from studios where studio_id = %s"""
            cursor.execute(query, (self.__studio_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__studio_id,
            "studio name" : self.__name
        }

        return json.dumps(fields_data)




class Genre:
    def __init__(self, genre_id="", genre_name = ""):
        self.__name = genre_name
        if genre_id == "":
            self.__genre_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO genres (genre_id, genre_name)
                           VALUES (%s, %s) """

                values = [(self.__genre_id, self.__name)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__genre_id = genre_id

    def get_name(self):
        return self.__name

    def get_genre_id(self):
        return self.__genre_id

    def set_name(self, genre_name):
        self.__name = genre_name
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE genres SET genre_name = %s WHERE genre_id = %s;'

            data_tuple = (self.__name, self.__genre_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from genres where genre_id = %s"""
            cursor.execute(query, (self.__genre_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__genre_id,
            "genre name" : self.__name
        }

        return json.dumps(fields_data)




class Review:
    def __init__(self, review_id="", rating = "", review_body = "", user_id = "", film_id = ""):
        self.__rating = rating
        self.__body = review_body
        self.__user_id = user_id
        self.__film_id = film_id
        if review_id == "":
            self.__review_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO reviews (review_id, rating, review, fk_user_id, fk_film_id)
                           VALUES (%s, %s, %s, %s, %s) """

                values = [(self.__review_id, self.__rating, self.__body, self.__user_id, self.__film_id)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__review_id = review_id

    def get_rating(self):
        return self.__rating

    def get_body(self):
        return self.__body

    def get_user_id(self):
        return self.__user_id

    def get_film_id(self):
        return self.__film_id

    def get_review_id(self):
        return self.__review_id

    def set_rating(self, rating):
        self.__rating = rating
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE reviews SET rating = %s WHERE review_id = %s;'

            data_tuple = (self.__rating, self.__review_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_body(self, review_body):
        self.__body = review_body
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE reviews SET review_body = %s WHERE review_id = %s;'

            data_tuple = (self.__body, self.__review_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_user_id(self, user_id):
        self.__user_id = user_id
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE reviews SET fk_user_id = %s WHERE review_id = %s;'

            data_tuple = (self.__user_id, self.__review_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_film_id(self, film_id):
        self.__film_id = film_id
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE reviews SET fk_film_id = %s WHERE review_id = %s;'

            data_tuple = (self.__film_id, self.__film_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from reviews where review_id = %s"""
            cursor.execute(query, (self.__users_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "review id" : self.__review_id,
            "rating" : self.__rating,
            "review body" : self.__body,
            "user id" : self.__user_id,
            "film id" : self.__film_id,
        }

        return json.dumps(fields_data)





class Review_Reply:
    def __init__(self, reply_id="", reply = "", user_id = "", review_id = ""):
        self.__reply = reply
        self.__user_id = user_id
        self.__review_id = review_id
        if reply_id == "":
            self.__reply_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO review_replies (reply_id, reply_text, fk_user_id, fk_review_id
                           VALUES (%s, %s, %s, %s) """

                values = [(self.__reply_id, self.__reply, self.__user_id, self.__review_id)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__reply_id = reply_id

    def get_reply(self):
        return self.__reply

    def get_user_id(self):
        return self.__user_id

    def get_review_id(self):
        return self.__review_id
    
    def get_reply_id(self):
        return self.__review_id

    def set_reply(self, reply):
        self.__reply = reply
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE review_replies SET reply = %s WHERE reply_id = %s;'

            data_tuple = (self.__reply, self.__reply_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_user_id(self, user_id):
        self.__user_id = user_id
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE review_replies SET fk_user_id = %s WHERE reply_id = %s;'

            data_tuple = (self.__user_id, self.__reply_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_review_id(self, review_id):
        self.__review_id = review_id
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE review_replies SET fk_review_id = %s WHERE reply_id = %s;'

            data_tuple = (self.__review_id, self.__reply_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from review_replies where reply_id = %s"""
            cursor.execute(query, (self.__users_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "reply id" : self.__reply_id,
            "reply" : self.__reply,
            "user id" : self.__user_id,
            "review id" : self.__review_id,
        }

        return json.dumps(fields_data)




class List:
    def __init__(self, list_id="", list_title = "", fk_user_id = ""):
        self.__title = list_title
        self.__user_id = fk_user_id
        if list_id == "":
            self.__list_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO lists (list_id, list_title, fk_user_id)
                           VALUES (%s, %s, %s) """

                values = [(self.__list_id, self.__title, self.__user_id)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__list_id = list_id

    def get_title(self):
        return self.__title

    def get_user_id(self):
        return self.__user_id

    def get_list_id(self):
        return self.__list_id

    def set_title(self, list_title):
        self.__title = list_title
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE lists SET list_title = %s WHERE list_id = %s;'

            data_tuple = (self.__title, self.__list_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_user_id(self, fk_user_id):
        self.__user_id = fk_user_id
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE lists SET fk_user_id = %s WHERE list_id = %s;'

            data_tuple = (self.__user_id, self.__list_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from lists where list_id = %s"""
            cursor.execute(query, (self.__list_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__list_id,
            "list title" : self.__title,
            "user_id" : self.__user_id,
        }

        return json.dumps(fields_data)




class List_Reply:
    def __init__(self, reply_id="", reply = "", user_id = "", list_id = ""):
        self.__reply = reply
        self.__user_id = user_id
        self.__list_id = list_id
        if reply_id == "":
            self.__reply_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(**config)
                query = """INSERT INTO list_replies (reply_id, reply_text, fk_user_id, fk_list_id
                           VALUES (%s, %s, %s, %s) """

                values = [(self.__reply_id, self.__reply, self.__user_id, self.__list_id)]

                cursor = connection.cursor()
                cursor.executemany(query, values)
                connection.commit()

            except mysql.connector.Error as error:
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            self.__reply_id = reply_id

    def get_reply(self):
        return self.__reply

    def get_user_id(self):
        return self.__user_id

    def get_list_id(self):
        return self.__list_id
    
    def get_reply_id(self):
        return self.__list_id

    def set_reply(self, reply):
        self.__reply = reply
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE list_replies SET reply = %s WHERE reply_id = %s;'

            data_tuple = (self.__reply, self.__reply_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_user_id(self, user_id):
        self.__user_id = user_id
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE list_replies SET fk_user_id = %s WHERE reply_id = %s;'

            data_tuple = (self.__user_id, self.__reply_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_list_id(self, list_id):
        self.__list_id = list_id
        try:
            connection = mysql.connector.connect(**config)

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE list_replies SET fk_list_id = %s WHERE reply_id = %s;'

            data_tuple = (self.__list_id, self.__reply_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = """Delete from list_replies where reply_id = %s"""
            cursor.execute(query, (self.__users_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "reply id" : self.__reply_id,
            "reply" : self.__reply,
            "user id" : self.__user_id,
            "list id" : self.__list_id,
        }

        return json.dumps(fields_data)