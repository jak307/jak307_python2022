import mysql.connector
from object_model import User
from object_model import Film
from object_model import Studio
from object_model import Genre
from object_model import Director
from object_model import Actor
from object_model import Writer
from object_model import Producer
from object_model import Cinematographer
from object_model import Composer
from object_model import Editor

config = {
    'host': '67.205.163.33',
    'user': 'jak307',
    'password': 'InfSci1500_4131521',
    'database': 'jak307'
}

print("Welcome!")
print("You have two options")
print("Would you like to:")
print(" 1: sign in")
print(" 2: register")
surq = input("Which will it be? (please enter 1 or 2) ")

def check_reg(uname, pword, eml):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            if (i[1] == uname or i[2] == pword):
                print("sorry, that username or password is already used")
                quit()
            if (i[1] == eml):
                print("sorry, that username or password is already used")
                quit()
    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close

def validate_user(uname, pword):
    try:
        check1 = 0
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            if (i[1] == uname and i[2] == pword):
                check1 = 1
                break
        if check1 == 0:
            print("Sorry, we can't find that username/password combo")
            quit()

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close

if surq == "2":
    username = input("username: ")
    password = input("password: ")
    email = input("email: ")
    check_reg(username, password, email)
    user1 = User("", username, password, email)
    print("You have successfully registered!")

if surq == "1":
    username = input("username: ")
    password = input("password: ")
    validate_user(username, password)
    wlcm = "Hello, " + username + "!"
    print(wlcm)
    
if username == "admin" and password == "password1":
    check2 = "y"
    while (check2 == "y"):
        print("Here are your options:")
        print("   1: add a new film entry")
        print("   2: update a film entry")
        print("   3: delete a film entry")
        print("   4: add a new director entry")
        print("   5: update a director entry")
        print("   6: delete a director entry")
        print("   7: add a new actor entry")
        print("   8: update an actor entry")
        print("   9: delete an actor entry")
        print("   10: add a new writer entry")
        print("   11: update a writer entry")
        print("   12: delete a writer entry")
        print("   13: add a new producer entry")
        print("   14: update a producer entry")
        print("   15: delete a producer entry")
        print("   16: add a new cinematographer entry")
        print("   17: update a cinematographer entry")
        print("   18: delete a cinematographer entry")
        print("   19: add a new composer entry")
        print("   20: update a composer entry")
        print("   21: delete a composer entry")
        print("   22: add a new editor entry")
        print("   23: update an editor entry")
        print("   24: delete an editor entry")
        print("   25: add a new studio entry")
        print("   26: update a studio entry")
        print("   27: delete a studio entry")
        print("   28: add a new genre entry")
        print("   29: update a genre entry")
        print("   30: delete a genre entry")
        
        choice = input("Which do you choose? ")

        if (choice == "1"):
            film_name = input("What is the name of this film? ")
            film_year = input("What year was this film released? ")
            film_language = input("What language is this film in? ")
            film_description = input("Write a brief plot summary of the film: ")
            film1 = Film("", film_name, film_year, film_language, film_description)
            film_id = film1.get_film_id()
            check4 = "y"
            while (check4 == "y"):
                d_id = input("What is the id of the person who directed this film? ")
                try:
                    connection = mysql.connector.connect(**config)
                    cursor = connection.cursor()
                    query = """INSERT INTO film_director (fk_film_id, fk_director_id)
                               VALUES (%s, %s) """
                    values = [(film_id, d_id)]
                    cursor = connection.cursor()
                    cursor.executemany(query, values)
                    connection.commit()
                except mysql.connector.Error as error:
                    print("Failed to read from MySQL {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close
                check4 = input("Is there anyone else who directed this film? (y/n )")
            check4 = "y"
            while (check4 == "y"):
                a_id = input("What is the id of an actor who starred in this film? ")
                try:
                    connection = mysql.connector.connect(**config)
                    cursor = connection.cursor()
                    query = """INSERT INTO film_actor (fk_film_id, fk_actor_id)
                               VALUES (%s, %s) """
                    values = [(film_id, a_id)]
                    cursor = connection.cursor()
                    cursor.executemany(query, values)
                    connection.commit()
                except mysql.connector.Error as error:
                    print("Failed to read from MySQL {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close
                check4 = input("Are there more actors you'd like to add? (y/n )")
            check4 = "y"
            while (check4 == "y"):
                w_id = input("What is the id of the person who wrote this film? ")
                try:
                    connection = mysql.connector.connect(**config)
                    cursor = connection.cursor()
                    query = """INSERT INTO film_writer (fk_film_id, fk_writer_id)
                               VALUES (%s, %s) """
                    values = [(film_id, w_id)]
                    cursor = connection.cursor()
                    cursor.executemany(query, values)
                    connection.commit()
                except mysql.connector.Error as error:
                    print("Failed to read from MySQL {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close
                check4 = input("Is there anyone else who wrote this film? (y/n )")
            check4 = "y"
            while (check4 == "y"):
                w_id = input("What is the id of the person who produced this film? ")
                try:
                    connection = mysql.connector.connect(**config)
                    cursor = connection.cursor()
                    query = """INSERT INTO film_producer (fk_film_id, fk_producer_id)
                               VALUES (%s, %s) """
                    values = [(film_id, w_id)]
                    cursor = connection.cursor()
                    cursor.executemany(query, values)
                    connection.commit()
                except mysql.connector.Error as error:
                    print("Failed to read from MySQL {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close
                check4 = input("Is there anyone else who produced this film? (y/n )")
            check4 = "y"
            while (check4 == "y"):
                ci_id = input("What is the id of the person who did cinematography for this film? ")
                try:
                    connection = mysql.connector.connect(**config)
                    cursor = connection.cursor()
                    query = """INSERT INTO film_cinematographer (fk_film_id, fk_cinematographer_id)
                               VALUES (%s, %s) """
                    values = [(film_id, ci_id)]
                    cursor = connection.cursor()
                    cursor.executemany(query, values)
                    connection.commit()
                except mysql.connector.Error as error:
                    print("Failed to read from MySQL {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close
                check4 = input("Is there anyone else who did cinematography for this film? (y/n )")
            check4 = "y"
            while (check4 == "y"):
                co_id = input("What is the id of the person who wrote music for this film? ")
                try:
                    connection = mysql.connector.connect(**config)
                    cursor = connection.cursor()
                    query = """INSERT INTO film_composer (fk_film_id, fk_composer_id)
                               VALUES (%s, %s) """
                    values = [(film_id, co_id)]
                    cursor = connection.cursor()
                    cursor.executemany(query, values)
                    connection.commit()
                except mysql.connector.Error as error:
                    print("Failed to read from MySQL {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close
                check4 = input("Is there anyone else who wrote music for this film? (y/n )")
            check4 = "y"
            while (check4 == "y"):
                e_id = input("What is the id of the person who edited this film? ")
                try:
                    connection = mysql.connector.connect(**config)
                    cursor = connection.cursor()
                    query = """INSERT INTO film_editor (fk_film_id, fk_editor_id)
                               VALUES (%s, %s) """
                    values = [(film_id, e_id)]
                    cursor = connection.cursor()
                    cursor.executemany(query, values)
                    connection.commit()
                except mysql.connector.Error as error:
                    print("Failed to read from MySQL {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close
                check4 = input("Is there anyone else who edited this film? (y/n )")
            check4 = "y"
            while (check4 == "y"):
                s_id = input("What is the id of the studio that produced this film? ")
                try:
                    connection = mysql.connector.connect(**config)
                    cursor = connection.cursor()
                    query = """INSERT INTO film_studio (fk_film_id, fk_studio_id)
                               VALUES (%s, %s) """
                    values = [(film_id, s_id)]
                    cursor = connection.cursor()
                    cursor.executemany(query, values)
                    connection.commit()
                except mysql.connector.Error as error:
                    print("Failed to read from MySQL {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close
                check4 = input("Are there any other companies that financed this film? (y/n )")
            check4 = "y"
            while (check4 == "y"):
                g_id = input("What is the genre of this film? ")
                try:
                    connection = mysql.connector.connect(**config)
                    cursor = connection.cursor()
                    query = """INSERT INTO film_genre (fk_film_id, fk_genre_id)
                               VALUES (%s, %s) """
                    values = [(film_id, g_id)]
                    cursor = connection.cursor()
                    cursor.executemany(query, values)
                    connection.commit()
                except mysql.connector.Error as error:
                    print("Failed to read from MySQL {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close
                check4 = input("Are there any other genres this film? (y/n )")
                

        if (choice == "4"):
            director_fname = input("What is the first name of the director? ")
            director_lname = input("What is the last name of the director? ")
            director1 = Director("", director_fname, director_lname)
        if (choice == "5"):
            director_id = input("What is the director's id? ")
            director_fname = input("What is the first name of the director? ")
            director_lname = input("What is the last name of the director? ")
            director1 = Director(director_id, director_fname, director_lname)
            check3 = input("would you like to update the first name? (y/n) ")
            if check3 == "y":
                director_fname = input ("what would you like the new name to be? ")
                director1.set_fname(director_fname)
            check3 = input("would you like to update the last name? (y/n) ")
            if check3 == "y":
                director_lname = input ("what would you like the new name to be? ")
                director1.set_lname(director_lname)
        if (choice == "6"):
            director_id = input("What is the director's id? ")
            director1 = Director(director_id, director_fname, director_lname)
            director1.delete()

        if (choice == "7"):
            actor_fname = input("What is the first name of the actor? ")
            actor_lname = input("What is the last name of the actor? ")
            actor1 = Actor("", actor_fname, actor_lname)
        if (choice == "8"):
            actor_id = input("What is the actor's id? ")
            actor_fname = input("What is the first name of the actor? ")
            actor_lname = input("What is the last name of the actor? ")
            actor1 = Actor(actor_id, actor_fname, actor_lname)
            check3 = input("would you like to update the first name? (y/n) ")
            if check3 == "y":
                actor_fname = input ("what would you like the new name to be? ")
                actor1.set_fname(actor_fname)
            check3 = input("would you like to update the last name? (y/n) ")
            if check3 == "y":
                actor_lname = input ("what would you like the new name to be? ")
                actor1.set_lname(actor_lname)
        if (choice == "9"):
            actor_id = input("What is the actor's id? ")
            actor1 = Actor(actor_id, actor_fname, actor_lname)
            actor1.delete()

        if (choice == "10"):
            writer_fname = input("What is the first name of the writer? ")
            writer_lname = input("What is the last name of the writer? ")
            writer1 = Writer("", writer_fname, writer_lname)
        if (choice == "11"):
            writer_id = input("What is the writer's id? ")
            writer_fname = input("What is the first name of the writer? ")
            writer_lname = input("What is the last name of the writer? ")
            writer1 = Writer(writer_id, writer_fname, writer_lname)
            check3 = input("would you like to update the first name? (y/n) ")
            if check3 == "y":
                writer_fname = input ("what would you like the new name to be? ")
                writer1.set_fname(writer_fname)
            check3 = input("would you like to update the last name? (y/n) ")
            if check3 == "y":
                writer_lname = input ("what would you like the new name to be? ")
                writer1.set_lname(writer_lname)
        if (choice == "12"):
            writer_id = input("What is the writer's id? ")
            writer1 = Writer(writer_id, writer_fname, writer_lname)
            writer1.delete()

        if (choice == "13"):
            producer_fname = input("What is the first name of the producer? ")
            producer_lname = input("What is the last name of the producer? ")
            producer1 = Producer("", producer_fname, producer_lname)
        if (choice == "14"):
            producer_id = input("What is the producer's id? ")
            producer_fname = input("What is the first name of the producer? ")
            producer_lname = input("What is the last name of the producer? ")
            producer1 = Producer(producer_id, producer_fname, producer_lname)
            check3 = input("would you like to update the first name? (y/n) ")
            if check3 == "y":
                producer_fname = input ("what would you like the new name to be? ")
                producer1.set_fname(producer_fname)
            check3 = input("would you like to update the last name? (y/n) ")
            if check3 == "y":
                producer_lname = input ("what would you like the new name to be? ")
                producer1.set_lname(producer_lname)
        if (choice == "15"):
            producer_id = input("What is the producer's id? ")
            producer1 = Producer(producer_id, producer_fname, producer_lname)
            producer1.delete()

        if (choice == "16"):
            cinematographer_fname = input("What is the first name of the cinematographer? ")
            cinematographer_lname = input("What is the last name of the cinematographer? ")
            cinematographer1 = Cinematographer("", cinematographer_fname, cinematographer_lname)
        if (choice == "17"):
            cinematographer_id = input("What is the cinematographer's id? ")
            cinematographer_fname = input("What is the first name of the cinematographer? ")
            cinematographer_lname = input("What is the last name of the cinematographer? ")
            cinematographer1 = Cinematographer(cinematographer_id, cinematographer_fname, cinematographer_lname)
            check3 = input("would you like to update the first name? (y/n) ")
            if check3 == "y":
                cinematographer_fname = input ("what would you like the new name to be? ")
                cinematographer1.set_fname(cinematographer_fname)
            check3 = input("would you like to update the last name? (y/n) ")
            if check3 == "y":
                cinematographer_lname = input ("what would you like the new name to be? ")
                cinematographer1.set_lname(cinematographer_lname)
        if (choice == "18"):
            cinematographer_id = input("What is the cinematographer's id? ")
            cinematographer1 = Cinematographer(cinematographer_id, cinematographer_fname, cinematographer_lname)
            cinematographer1.delete()

        if (choice == "19"):
            composer_fname = input("What is the first name of the composer? ")
            composer_lname = input("What is the last name of the composer? ")
            composer1 = Composer("", composer_fname, composer_lname)
        if (choice == "20"):
            composer_id = input("What is the composer's id? ")
            composer_fname = input("What is the first name of the composer? ")
            composer_lname = input("What is the last name of the composer? ")
            composer1 = Composer(composer_id, composer_fname, composer_lname)
            check3 = input("would you like to update the first name? (y/n) ")
            if check3 == "y":
                composer_fname = input ("what would you like the new name to be? ")
                composer1.set_fname(composer_fname)
            check3 = input("would you like to update the last name? (y/n) ")
            if check3 == "y":
                composer_lname = input ("what would you like the new name to be? ")
                composer1.set_lname(composer_lname)
        if (choice == "21"):
            composer_id = input("What is the composer's id? ")
            composer1 = Composer(composer_id, composer_fname, composer_lname)
            composer1.delete()

        if (choice == "22"):
            editor_fname = input("What is the first name of the editor? ")
            editor_lname = input("What is the last name of the editor? ")
            editor1 = Editor("", editor_fname, editor_lname)
        if (choice == "23"):
            editor_id = input("What is the editor's id? ")
            editor_fname = input("What is the first name of the editor? ")
            editor_lname = input("What is the last name of the editor? ")
            editor1 = Editor(editor_id, editor_fname, editor_lname)
            check3 = input("would you like to update the first name? (y/n) ")
            if check3 == "y":
                editor_fname = input ("what would you like the new name to be? ")
                editor1.set_fname(editor_fname)
            check3 = input("would you like to update the last name? (y/n) ")
            if check3 == "y":
                editor_lname = input ("what would you like the new name to be? ")
                editor1.set_lname(editor_lname)
        if (choice == "24"):
            editor_id = input("What is the editor's id? ")
            editor1 = Editor(editor_id, editor_fname, editor_lname)
            editor1.delete()

        if (choice == "25"):
            studio_name = input("What is the name of the studio? ")
            studio1 = Studio("", studio_name)
        if (choice == "26"):
            studio_id = input("What is the studio's id? ")
            studio_name = input("What is the name of the studio? ")
            studio1 = Studio(studio_id, studio_name)
            studio_name = input ("what would you like the new name to be? ")
            studio1.set_name(studio_name)
        if (choice == "27"):
            studio_id = input("What is the studio's id? ")
            studio1 = Studio(studio_id, studio_name)
            studio1.delete()

        if (choice == "28"):
            genre_name = input("What is the name of the genre? ")
            genre1 = Genre("", genre_name)
        if (choice == "29"):
            genre_id = input("What is the genre's id? ")
            genre_name = input("What is the name of the genre? ")
            genre1 = Genre(genre_id, genre_name)
            genre_name = input ("what would you like the new name to be? ")
            genre1.set_name(genre_name)
        if (choice == "30"):
            genre_id = input("What is the genre's id? ")
            genre1 = Genre(genre_id, genre_name)
            genre1.delete()

        check2 = input("Would you like to keep going? (y/n) ")
else:
    check5 = "y"
    while (check5 == "y"):
        print("Here are your options: ")
        print("   1: search for films")
        print("   2: search for users")
        choice2 = input("What will it be?")
        if choice2 == "1":
            print("films will be listed here when i get that done. i need to populate the database first.")

        check5 = input("Would you like to keep going? (y/n) ")
 
