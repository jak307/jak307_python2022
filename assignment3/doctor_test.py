import unittest
import mysql.connector
from emr import Doctor

config = {
    'host': '67.205.163.33',
    'user': 'jak307',
    'password': 'InfSci1500_4131521',
    'database': 'jak307'
}

class TestDoctor(unittest.TestCase):

    def test_create(self):
        doctor = Doctor("", "test", "test")
        did = doctor.get_doctor_id()
        try:
            connection = mysql.connector.connect(**config)

            query = "select * from doctor where doctor_id = '" + did + "';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            testResults = [(did, "test", "test")]
            self.assertEqual(result, testResults, "failed to create entry")

        except mysql.connector.Error as error:
            print("Failed to read from MySQL {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        doctor.delete()

    def test_delete(self):
        doctor = Doctor("", "test", "test")
        did = doctor.get_doctor_id()
        doctor.delete()
        try:
            connection = mysql.connector.connect(**config)

            query = "select * from doctor where doctor_id = '" + did + "';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            testResults = []
            self.assertEqual(result, testResults, "failed to delete entry")

        except mysql.connector.Error as error:
            print("Failed to read from MySQL {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def test_update_fname(self):
        doctor = Doctor("", "test", "test")
        did = doctor.get_doctor_id()
        try:
            connection = mysql.connector.connect(**config)

            doctor.set_fname('test2')
            query = "select * from doctor where doctor_id = '" + did + "';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            testResults = [(did, "test2", "test")]
            self.assertEqual(result, testResults, "failed to update first name")

        except mysql.connector.Error as error:
            print("Failed to read from MySQL {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        doctor.delete()

    def test_update_lname(self):
        doctor = Doctor("", "test", "test")
        did = doctor.get_doctor_id()
        try:
            connection = mysql.connector.connect(**config)

            doctor.set_lname('test2')
            query = "select * from doctor where doctor_id = '" + did + "';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            testResults = [(did, "test", "test2")]
            self.assertEqual(result, testResults, "failed to update last name")

        except mysql.connector.Error as error:
            print("Failed to read from MySQL {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        doctor.delete()

# run the test
unittest.main()
