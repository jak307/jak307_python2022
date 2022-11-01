# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline
# pylint: disable=consider-using-f-string
import uuid
import json
import mysql.connector
from flask import Flask
app = Flask(__name__)

class Doctor:
    def __init__(self, doctor_id="", doctor_fname = "", doctor_lname = ""):
        self.__fname = doctor_fname
        self.__lname = doctor_lname
        if doctor_id == "":
            self.__doctor_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
                query = """INSERT INTO doctor (doctor_id, doctor_fname, doctor_lname)
                           VALUES (%s, %s, %s) """

                values = [(self.__doctor_id, self.__fname, self.__lname)]

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
            self.__doctor_id = doctor_id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_doctor_id(self):
        return self.__doctor_id

    def set_fname(self, doctor_fname):
        self.__fname = doctor_fname
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE doctor SET doctor_fname = %s WHERE doctor_id = %s;'

            data_tuple = (self.__fname, self.__doctor_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_lname(self, doctor_lname):
        self.__lname = doctor_lname
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE doctor SET doctor_lname = %s WHERE doctor_id = %s;'

            data_tuple = (self.__lname, self.__doctor_id)
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
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
            cursor = connection.cursor(prepared=True)
            query = """Delete from doctor where doctor_id = %s"""
            cursor.execute(query, (self.__doctor_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__doctor_id,
            "doctor first name" : self.__fname,
            "doctor last name" : self.__lname,
        }

        return json.dumps(fields_data)




class Patient:
    def __init__(self, patient_id="", patient_fname = "", patient_lname = ""):
        self.__fname = patient_fname
        self.__lname = patient_lname
        if patient_id == "":
            self.__patient_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
                query = """INSERT INTO patient (patient_id, patient_fname, patient_lname)
                           VALUES (%s, %s, %s) """

                values = [(self.__patient_id, self.__fname, self.__lname)]

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
            self.__patient_id = patient_id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_patient_id(self):
        return self.__patient_id

    def set_fname(self, patient_fname):
        self.__fname = patient_fname
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE patient SET patient_fname = %s WHERE patient_id = %s;'

            data_tuple = (self.__fname, self.__patient_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_lname(self, patient_lname):
        self.__lname = patient_lname
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE patient SET patient_lname = %s WHERE patient_id = %s;'

            data_tuple = (self.__lname, self.__patient_id)
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
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
            cursor = connection.cursor(prepared=True)
            query = """Delete from patient where patient_id = %s"""
            cursor.execute(query, (self.__patient_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__patient_id,
            "patient first name" : self.__fname,
            "patient last name" : self.__lname,
        }

        return json.dumps(fields_data)



class Procedure:
    def __init__(self, procedure_id="", procedure_name = ""):
        self.__procedure = procedure_name
        if procedure_id == "":
            self.__procedure_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
                query = """INSERT INTO procedures (procedure_id, procedure_name)
                           VALUES (%s, %s) """

                values = [(self.__procedure_id, self.__procedure)]

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
            self.__procedure_id = procedure_id

    def get_procedure_name(self):
        return self.__procedure

    def get_procedure_id(self):
        return self.__procedure_id

    def set_name(self, procedure_name):
        self.__procedure = procedure_name
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE procedures SET procedure_name = %s WHERE procedure_id = %s;'

            data_tuple = (self.__procedure, self.__procedure_id)
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
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
            cursor = connection.cursor(prepared=True)
            query = """Delete from procedures where procedure_id = %s"""
            cursor.execute(query, (self.__procedure_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__procedure_id,
            "procedure" : self.__procedure
        }

        return json.dumps(fields_data)




class Diagnosis:
    def __init__(self, diagnosis_id="", diagnosis_name = ""):
        self.__diagnosis = diagnosis_name
        if diagnosis_id == "":
            self.__diagnosis_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
                query = """INSERT INTO diagnosis (diagnosis_id, diagnosis_name)
                           VALUES (%s, %s) """

                values = [(self.__diagnosis_id, self.__diagnosis)]

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
            self.__diagnosis_id = diagnosis_id

    def get_diagnosis_name(self):
        return self.__diagnosis

    def get_diagnosis_id(self):
        return self.__diagnosis_id

    def set_name(self, diagnosis_name):
        self.__diagnosis = diagnosis_name
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE diagnosis SET diagnosis_name = %s WHERE diagnosis_id = %s;'

            data_tuple = (self.__diagnosis, self.__diagnosis_id)
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
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
            cursor = connection.cursor(prepared=True)
            query = """Delete from diagnosis where diagnosis_id = %s"""
            cursor.execute(query, (self.__diagnosis_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "id" : self.__diagnosis_id,
            "diagnosis" : self.__diagnosis
        }

        return json.dumps(fields_data)



class Visit:
    def __init__(self, visit_id = "", date = "", doctor_id = "", patient_id = ""):
        self.__doctor_id = doctor_id
        self.__patient_id = patient_id
        self.__date = date
        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
                query = """INSERT INTO visit (visit_id, visit_date, fk_doctor_id, fk_patient_id)
                           VALUES (%s, %s, %s, %s) """

                values = [(self.__visit_id, self.__date, self.__doctor_id, self.__patient_id)]

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
            self.__visit_id = visit_id

    def get_visit_id(self):
        return self.__visit_id

    def get_doctor_id(self):
        return self.__doctor_id

    def get_patient_id(self):
        return self.__patient_id

    def get_visit_date(self):
        return self.__date

    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE visit SET fk_doctor_id = %s WHERE visit_id = %s;'

            data_tuple = (self.__doctor_id, self.__visit_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE visit SET fk_patient_id = %s WHERE visit_id = %s;'

            data_tuple = (self.__patient_id, self.__visit_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_date(self, date):
        self.__date = date
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE visit SET visit_date = %s WHERE visit_id = %s;'

            data_tuple = (self.__date, self.__visit_id)
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
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
            cursor = connection.cursor(prepared=True)
            query = """Delete from visit where visit_id = %s"""
            cursor.execute(query, (self.__visit_id,))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "visit id" : self.__visit_id,
            "doctor id" : self.__doctor_id,
            "patient id" : self.__patient_id,
        }

        return json.dumps(fields_data)




class Visit_Procedure:
    def __init__(self, visit_id="", procedure_id = ""):
        self.__visit_id = visit_id
        self.__procedure_id = procedure_id

    def get_visit_id(self):
        return self.__visit_id

    def get_procedure_id(self):
        return self.__procedure_id

    def set_visit_id(self, visit_id):
        self.__visit_id = visit_id
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE visit_procedure SET fk_visit_id = %s WHERE fk_procedure_id = %s;'

            data_tuple = (self.__visit_id, self.__procedure_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_procedure_id(self, procedure_id):
        self.__procedure_id = procedure_id
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE visit_procedure SET fk_procedure_id = %s WHERE fk_visit_id = %s;'

            data_tuple = (self.__procedure_id, self.__visit_id)
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
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
            cursor = connection.cursor(prepared=True)
            query = """Delete from visit_procedure where fk_visit_id = %s 
                        and fk_procedure_id = %s"""
            cursor.execute(query, (self.__visit_id, self.__procedure_id))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "visit id" : self.__visit_id,
            "procedure id" : self.__procedure_id
        }

        return json.dumps(fields_data)




class Visit_Diagnosis:
    def __init__(self, visit_id="", diagnosis_id = ""):
        self.__visit_id = visit_id
        self.__diagnosis_id = diagnosis_id

    def get_visit_id(self):
        return self.__visit_id

    def get_procedure_id(self):
        return self.__diagnosis_id

    def set_visit_id(self, visit_id):
        self.__visit_id = visit_id
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE visit_diagnosis SET fk_visit_id = %s WHERE fk_diagnosis_id = %s;'

            data_tuple = (self.__visit_id, self.__diagnosis_id)
            cursor = connection.cursor()
            cursor.execute(query, data_tuple)
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def set_diagnosis_id(self, diagnosis_id):
        self.__diagnosis_id = diagnosis_id
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            cursor = connection.cursor(prepared=True)
            query = 'UPDATE visit_diagnosis SET fk_diagnosis_id = %s WHERE fk_visit_id = %s;'

            data_tuple = (self.__diagnosis_id, self.__visit_id)
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
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
            cursor = connection.cursor(prepared=True)
            query = """Delete from visit_diagnosis where fk_visit_id = %s 
                        and fk_diagnosis_id = %s"""
            cursor.execute(query, (self.__visit_id, self.__diagnosis_id))
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def to_json(self):
        fields_data = {
            "visit id" : self.__visit_id,
            "diagnosis id" : self.__diagnosis_id
        }

        return json.dumps(fields_data)

@app.route('/')
def index():
    
    d = Doctor("", "Natalie", "Walker")
    p = Patient("", "John", "Mills")

    doctor_id = d.get_doctor_id()
    patient_id = p.get_patient_id()

    v1 = Visit("", "2022-10-17", doctor_id, patient_id)
    v2 = Visit("", "2022-10-31", doctor_id, patient_id)

    v1json = v1.to_json()
    v2json = v2.to_json()

    visits_json = v1json() + v2json()

    return visits_json