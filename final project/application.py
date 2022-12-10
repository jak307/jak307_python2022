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
from object_model import Review
from object_model import Review_Reply
from object_model import List
from object_model import List_Reply

config = {
    'host': '67.205.163.33',
    'user': 'jak307',
    'password': 'InfSci1500_4131521',
    'database': 'jak307'
}

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
                return i[0]
        if check1 == 0:
            print("Sorry, we can't find that username/password combo")
            quit()

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def display_films():
    films = []
    try:
        count = 0
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select * from films order by film_name;"
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            count = count + 1
            count1 = str(count)
            print(count1 + ": " + i[1])
            films.append((count, i[0], i[1]))
    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close
    return films



def display_film(f_id):
    f_id = f_id
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select * from films where film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        for tuple1 in result:
            print("\n")
            print("Name: " + tuple1[1])
            print("Year: " + tuple1[2])
            print("Language: " + tuple1[3])
            print("Plot: " + tuple1[4])

        cursor = connection.cursor()
        query = "select fk_genre_id from film_genre where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter1 = 0
        for tuple1 in result:
            g_id = tuple1[0]
            query = "select * from genres where genre_id = '" + g_id + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for tuple2 in result:
                if counter1 == 0:
                    print("Genre: " + tuple2[1])
                    counter1 = counter1 + 1
                else:
                    print("       " + tuple2[1])

        cursor = connection.cursor()
        query = "select fk_director_id from film_director where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter1 = 0
        for tuple1 in result:
            d_id = tuple1[0]
            query = "select * from directors where director_id = '" + d_id + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for tuple2 in result:
                if counter1 == 0:
                    print("Directed by: " + tuple2[1] + " " + tuple2[2])
                    counter1 = counter1 + 1
                else:
                    print("             " + tuple2[1] + " " + tuple2[2])
        
        cursor = connection.cursor()
        query = "select fk_actor_id from film_actor where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter1 = 0
        for tuple1 in result:
            a_id = tuple1[0]
            query = "select * from actors where actor_id = '" + a_id + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for tuple2 in result:
                if counter1 == 0:
                    print("Starring: " + tuple2[1] + " " + tuple2[2])
                    counter1 = counter1 + 1
                else:
                    print("          " + tuple2[1] + " " + tuple2[2])

        cursor = connection.cursor()
        query = "select fk_writer_id from film_writer where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter1 = 0
        for tuple1 in result:
            w_id = tuple1[0]
            query = "select * from writers where writer_id = '" + w_id + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for tuple2 in result:
                if counter1 == 0:
                    print("Written by: " + tuple2[1] + " " + tuple2[2])
                    counter1 = counter1 + 1
                else:
                    print("            " + tuple2[1] + " " + tuple2[2])

        cursor = connection.cursor()
        query = "select fk_producer_id from film_producer where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter1 = 0
        for tuple1 in result:
            p_id = tuple1[0]
            query = "select * from producers where producer_id = '" + p_id + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for tuple2 in result:
                if counter1 == 0:
                    print("Produced by: " + tuple2[1] + " " + tuple2[2])
                    counter1 = counter1 + 1
                else:
                    print("             " + tuple2[1] + " " + tuple2[2])

        cursor = connection.cursor()
        query = "select fk_cinematographer_id from film_cinematographer where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter1 = 0
        for tuple1 in result:
            ci_id = tuple1[0]
            query = "select * from cinematographers where cinematographer_id = '" + ci_id + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for tuple2 in result:
                if counter1 == 0:
                    print("Cinematography by: " + tuple2[1] + " " + tuple2[2])
                    counter1 = counter1 + 1
                else:
                    print("                   " + tuple2[1] + " " + tuple2[2])

        cursor = connection.cursor()
        query = "select fk_composer_id from film_composer where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter1 = 0
        for tuple1 in result:
            co_id = tuple1[0]
            query = "select * from composers where composer_id = '" + co_id + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for tuple2 in result:
                if counter1 == 0:
                    print("Score by: " + tuple2[1] + " " + tuple2[2])
                    counter1 = counter1 + 1
                else:
                    print("          " + tuple2[1] + " " + tuple2[2])

        cursor = connection.cursor()
        query = "select fk_editor_id from film_editor where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter1 = 0
        for tuple1 in result:
            e_id = tuple1[0]
            query = "select * from editors where editor_id = '" + e_id + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for tuple2 in result:
                if counter1 == 0:
                    print("Edited by: " + tuple2[1] + " " + tuple2[2])
                    counter1 = counter1 + 1
                else:
                    print("           " + tuple2[1] + " " + tuple2[2])

        cursor = connection.cursor()
        query = "select fk_studio_id from film_studio where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter1 = 0
        for tuple1 in result:
            s_id = tuple1[0]
            query = "select * from studios where studio_id = '" + s_id + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for tuple2 in result:
                if counter1 == 0:
                    print("Studio: " + tuple2[1] + " ")
                    counter1 = counter1 + 1
                else:
                    print("        " + tuple2[1] + " ")

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close




def display_reviews(f_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select reviews.review_id, reviews.rating, reviews.review, users.username from reviews inner join users on reviews.fk_user_id=users.user_id where fk_film_id = '" + f_id + "';"
        cursor.execute(query)
        result1 = cursor.fetchall()
        counter = 1
        reviews = []
        for tuple1 in result1:
            counter1 = str(counter)
            print(counter1 + ":  " + tuple1[3] + "- "+ tuple1[1] + "/10")
            print("     " + tuple1[2])
            reviews.append((counter1, tuple1[0]))
            counter = counter + 1
        return reviews

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def get_user_reviews(u_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select reviews.review_id, reviews.rating, reviews.review, films.film_name, films.film_id from reviews inner join films on reviews.fk_film_id=films.film_id where fk_user_id = '" + u_id + "';"
        cursor.execute(query)
        result1 = cursor.fetchall()
        result2 = []
        counter = 1
        for tuple1 in result1:
            counter1 = str(counter)
            print(counter1 + ": " + tuple1[3])
            result2.append((counter1, tuple1[0], tuple1[1], tuple1[2], tuple1[3], tuple1[4]))
            counter = counter + 1
        return result2

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def display_review(r_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select reviews.review_id, reviews.rating, reviews.review, films.film_name from reviews inner join films on reviews.fk_film_id=films.film_id where review_id = '" + r_id + "';"
        cursor.execute(query)
        result1 = cursor.fetchall()
        result2 = []
        counter = 1
        for tuple1 in result1:
            counter1 = str(counter)
            print(tuple1[3] + ": "+ tuple1[1] + "/10")
            print("     " + tuple1[2])
            counter = counter + 1
        return result2

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def reply_to_review(u_id, r_id):
    reply1 = input("What is your reply? ")
    reply2 = Review_Reply("", reply1, u_id, r_id)
    print("reply submitted")



def read_review_replies(r_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select users.username, review_replies.reply_text from users inner join review_replies on review_replies.fk_user_id=users.user_id where fk_review_id = '" + r_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print(x[0] + " said: ")
            print("     " + x[1])
    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def user_review_replies(u_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select review_replies.reply_id, reviews.review, review_replies.reply_text, reviews.fk_film_id, reviews.fk_user_id from reviews inner join review_replies on review_replies.fk_review_id=reviews.review_id where review_replies.fk_user_id = '" + u_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        replies = []
        counter = 1
        for x in result:
            counter1 = str(counter)
            replies.append((counter1, x[0], x[1], x[2], x[3], x[4]))
            counter = counter + 1
        for x in replies:
            query = "select * from users where user_id = '" + x[5] + "';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                uname = i[1]
            query = "select * from films where film_id = '" + x[4] + "';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                fname = i[1]
            print(x[0] + ":  " + uname + "'s review of " + fname + ": ")
            print("     " +  x[2])
            print("         Your reply:")
            print("             " + x[3])
        return replies

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def display_lists(u_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select * from lists where fk_user_id = '" + u_id + "' order by list_title;"
        cursor.execute(query)
        result1 = cursor.fetchall()
        counter = 1
        result2 = []
        for tuple1 in result1:
            counter1 = str(counter)
            print(counter1 + ": " + tuple1[1])
            result2.append((counter1, tuple1[0], tuple1[1]))
            counter = counter + 1
        return result2

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close




def display_list(l_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select * from list_films where fk_list_id = '" + l_id + "' order by list_rank;"
        cursor.execute(query)
        results = cursor.fetchall()
        counter = 1
        for x in results:
            counter1 = str(counter)
            cursor = connection.cursor()
            query = "select * from films where film_id = '" + x[1] + "';"
            cursor.execute(query)
            result = cursor.fetchall()
            for film in result:
                print(counter1 + ": " + film[1])
            counter = counter + 1

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close




def append_list(l_id, f_id):
    try:
        rank = input("Which place do you want to add the film? ")
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select * from list_films where fk_list_id = '" + l_id + "' order by list_rank;"
        cursor.execute(query)
        results = cursor.fetchall()
        new_rank = 0
        for x in results:
            if x[2] == rank:
                new_rank = x[2] + 1
                cursor = connection.cursor(prepared=True)
                query = 'UPDATE list_films SET list_rank = %s WHERE fk_list_id = %s;'
                data_tuple = (new_rank, l_id)
                cursor = connection.cursor()
                cursor.execute(query, data_tuple)
                connection.commit()
                new_rank = new_rank + 1
            if new_rank > 0:
                cursor = connection.cursor(prepared=True)
                query = 'UPDATE list_films SET list_rank = %s WHERE fk_list_id = %s;'
                data_tuple = (new_rank, l_id)
                cursor = connection.cursor()
                cursor.execute(query, data_tuple)
                connection.commit()
                new_rank = new_rank + 1
        cursor = connection.cursor()
        query = """INSERT INTO list_films (fk_list_id, fk_film_id, list_rank) VALUES (%s, %s, %s) """
        values = [(l_id, f_id, rank)]
        cursor.executemany(query, values)
        connection.commit()
        print("\nnew list:")
        display_list(l_id)
    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def reply_to_list(u_id, l_id):
    reply1 = input("What is your reply? ")
    reply2 = List_Reply("", reply1, u_id, l_id)
    print("reply submitted")



def read_list_replies(l_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select users.username, list_replies.reply_text from users inner join list_replies on list_replies.fk_user_id=users.user_id where fk_list_id = '" + l_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print(x[0] + " said: ")
            print("     " + x[1])
    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def user_list_replies(u_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select list_replies.reply_id, lists.list_id, lists.list_title, list_replies.reply_text, lists.fk_user_id from lists inner join list_replies on list_replies.fk_list_id=lists.list_id where list_replies.fk_user_id = '" + u_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        counter = 1
        replies = []
        for x in result:
            counter1 = str(counter)
            replies.append((counter1, x[0], x[1], x[2], x[3], x[4]))
            counter = counter + 1
        for x in replies:
            query = "select * from users where user_id = '" + x[5] + "';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                print(x[0] + ":  " + x[3] + " by " + i[1])
                query = "select list_films.list_rank, films.film_name from list_films inner join films on list_films.fk_film_id=films.film_id where list_films.fk_list_id = '" + x[2] + "' order by list_films.list_rank;"
                cursor = connection.cursor()
                cursor.execute(query)
                result2 = cursor.fetchall()
                for j in result2:
                    rank = str(j[0])
                    print("     " + rank + ": " + j[1])
            print("  You said:  " + x[4])
        return replies        

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def display_users(u_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select * from users order by username;"
        cursor.execute(query)
        result1 = cursor.fetchall()
        counter = 1
        result2 = []
        for tuple1 in result1:
            counter1 = str(counter)
            if tuple1[0] == u_id or tuple1[0] == "93e46d0e-cc76-4d6e-9d16-e171994324bd":
                pass
            else:
                print(counter1 + ": " + tuple1[1])
                result2.append((counter1, tuple1[0]))
                counter = counter + 1
        return result2

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def get_username(u_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select * from users where user_id = '" + u_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        for tuple1 in result:
            u_name = tuple1[1]
        return (u_id, u_name)

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def follow_user(u_id, f_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = """INSERT INTO user_followers (fk_user_id, fk_follower_id)
                           VALUES (%s, %s) """
        values = [(u_id, f_id)]
        cursor = connection.cursor()
        cursor.executemany(query, values)
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def unfollow_user(u_id, f_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "delete from user_followers where fk_user_id = '" + u_id + "' and fk_follower_id = '" + f_id + "';"
        cursor.execute(query)
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def see_followers(u_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select users.username from users inner join user_followers on users.user_id=user_followers.fk_follower_id where user_followers.fk_user_id = '" + u_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print(x[0])

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



def see_following(f_id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "select users.username, user_followers.fk_follower_id from users inner join user_followers on users.user_id=user_followers.fk_user_id where user_followers.fk_follower_id = '" + f_id + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        following = []
        counter = 1
        for x in result:
            counter1 = str(counter)
            print(counter1 + ": " + x[0])
            following.append((counter1, x[1]))
            counter = counter + 1
        return following

    except mysql.connector.Error as error:
        print("Failed to read from MySQL {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close



print("Welcome!")
print("You have two options")
print("Would you like to:")
print(" 1: sign in")
print(" 2: register")
surq = input("Which will it be? (please enter 1 or 2) ")

if surq == "2":
    username = input("username: ")
    password = input("password: ")
    email = input("email: ")
    check_reg(username, password, email)
    user1 = User("", username, password, email)
    user_id = user1.get_user_id()
    print("You have successfully registered!")

if surq == "1":
    username = input("username: ")
    password = input("password: ")
    user_id = validate_user(username, password)
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
        print("   3: create a list")
        print("   4: view your profile")
        choice2 = input("What will it be? ")
        if choice2 == "1":
            films = display_films()
            choice3 = input("Which film page would you like to visit? (please enter the number) ")
            choice3 = int(choice3)
            for i in films:
                if i[0] == choice3:
                    film_id = i[1]
                    display_film(film_id)
                    break
            print("You have four options")
            print("   1: rate and review")
            print("   2: read reviews")
            print("   3: add to a list")
            print("   4: go back")
            choice4 = input("What would you like to do? ")
            if choice4 == "1":
                rating = input("On a scale from 1-10, how would you rate this film? ")
                rating = int(rating)
                body = input("What did you think? ")
                review1 = Review("", rating, body, user_id, film_id)
                print("review submitted")
            if choice4 == "2":
                reviews = display_reviews(film_id)
                choice5 = input("Would you like to see the replies to any reviews? (y/n) ")
                if choice5 == "y":
                    choice6 = input("Which review would you like to read replies for? ")
                    for x in reviews:
                        if x[0] == choice6:
                            read_review_replies(x[1])
                            break
                    choice6 = input("Would you like to reply to this review? (y/n) ")
                    if choice6 == "y":
                        reply_to_review(user_id, x[1])
            if choice4 == "3":
                tuple_list = display_lists(user_id)
                choice5 = input("Which list would you like to add this film to? ")
                for i in tuple_list:
                    if choice5 == i[0]:
                        display_list(i[1])
                        append_list(i[1], film_id)
        if choice2 == "2":
            results = display_users(user_id)
            choice5 = input("Which user would you like to select? ")
            for j in results:
                if choice5 == j[0]:
                    chosen_user_id = j[1]
            chosen_user = get_username(chosen_user_id)
            print(chosen_user[1] + "'s lists: ")
            user_lists = display_lists(chosen_user[0])
            print("films that " + chosen_user[1] + " has reviewed: ")
            user_reviews = get_user_reviews(chosen_user[0])
            print("You have three options")
            print("   1: See a list")
            print("   2: Read a review")
            print("   3: Follow user")
            choice5 = input("Which will it be? ")
            if choice5 == "1":
                choice6 = input("which list would you like to see? ")
                for x in user_lists:
                    if x[0] == choice6:
                        print(x[2] + ": ")
                        display_list(x[1])
                        print("     Replies to " + x[2] + ": ")
                        read_list_replies(x[1])
                        break
                choice6 = input("Would you like to reply to this list? (y/n) ")
                if choice6 == "y":
                    reply_to_list(user_id, x[1])
            if choice5 == "2":
                choice6 = input("which review would you like to read? ")
                for x in user_reviews:
                    if x[0] == choice6:
                        display_review(x[1])
                        print("     Replies: ")
                        read_review_replies(x[1])
                        break
                choice6 = input("Would you like to reply to this review? (y/n) ")
                if choice6 == "y":
                    reply_to_review(user_id, x[1])
            if choice5 == "3":
                follow_user(chosen_user[0], user_id)
                print("followed")
        if choice2 == "3":
            title = input("What is the name of your list? ")
            list1 = List("", title, user_id)
            print("list added")
        if choice2 == "4":
            print("\nFilms that you've reviewed: ")
            user_reviews = get_user_reviews(user_id)
            print("\nLists that you've made: ")
            user_lists = display_lists(user_id)
            print("\nYour replies to reviews: ")
            r_replies = user_review_replies(user_id)
            print("\nYour replies to lists: ")
            l_replies = user_list_replies(user_id)
            print("\nUsers that you follow: ")
            following = see_following(user_id)
            print("\nYour followers: ")
            see_followers(user_id)
            print("\nYou have four options: ")
            print("   1: Edit/delete a review")
            print("   2: Edit/delete a list")
            print("   3: Edit/delete a review reply")
            print("   4: Edit/delete a list reply")
            print("   5: Check up on a followed user")
            print("   6: Unfollow a user")
            choice5 = input("What will it be? ")
            if choice5 == "1":
                choice6 = input("Which review would you like to edit/delete? ")
                for review in user_reviews:
                    if review[0] == choice6:
                        review1 = Review(review[1], review[2], review[3], user_id, review[5])
                        print("You rated " + review[4] + " " + review[2] + "/10 and said: " + review[3])
                        print("You have 4 options: ")
                        print("   1: Change the rating")
                        print("   2: Change the review")
                        print("   3: Delete the review")
                        print("   4: Go back")
                        choice7 = input("What will it be? ")
                        if choice7 == "1":
                            new_rating = input("On a scale of 1-10, what do you want to change the rating to? ")
                            review1.set_rating(new_rating)
                        if choice7 == "2":
                            new_review = input("What do you want to say this time? ")
                            review1.set_body(new_review)
                        if choice7 == "3":
                            review1.delete()
                            print("The review has been deleted")
                        if choice7 == "4":
                            pass
            if choice5 == "2":
                pass
            if choice5 == "3":
                choice6 = input("Which review reply would you like to edit/delete? ")
                for reply in r_replies:
                    if reply[0] == choice6:
                        reply1 = Review_Reply(reply[1], reply[3], user_id, reply[4])
                        print("You said: " + reply[3])
                        print("You have 3 options: ")
                        print("   1: Change the reply")
                        print("   2: Delete the reply")
                        print("   3: Go back")
                        choice7 = input("What will it be? ")
                        if choice7 == "1":
                            new_reply = input("What do you want to say this time? ")
                            reply1.set_reply(new_reply)
                        if choice7 == "2":
                            reply1.delete()
                            print("The reply has been deleted")
                        if choice7 == "3":
                            pass
            if choice5 == "4":
                choice6 = input("Which list reply would you like to edit/delete? ")
                for reply in l_replies:
                    if reply[0] == choice6:
                        reply1 = List_Reply(reply[1], reply[4], user_id, reply[2])
                        print("You said: " + reply[4])
                        print("You have 3 options: ")
                        print("   1: Change the reply")
                        print("   2: Delete the reply")
                        print("   3: Go back")
                        choice7 = input("What will it be? ")
                        if choice7 == "1":
                            new_reply = input("What do you want to say this time? ")
                            reply1.set_reply(new_reply)
                        if choice7 == "2":
                            reply1.delete()
                            print("The reply has been deleted")
                        if choice7 == "3":
                            pass
            if choice5 == "5":
                pass
            if choice5 == "6":
                pass
        check5 = input("Would you like to go back home? (y/n) ")