import uuid
import mysql.connector
import json

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

            query = 'UPDATE doctor SET doctor_fname = %s WHERE user_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__fname, self.__doctor_id))
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

            query = 'UPDATE doctor SET doctor_lname = %s WHERE user_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__lname, self.__doctor_id))
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

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

            query = 'UPDATE patient SET patient_fname = %s WHERE patient_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__fname, self.__patient_id))
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

            query = 'UPDATE patient SET patient_lname = %s WHERE patient_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__lname, self.__patient_id))
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

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

    def set_procedure_name(self, procedure_name):
        self.__procedure = procedure_name
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            query = 'UPDATE procedures SET procedure_name = %s WHERE procedure_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__procedure, self.__procedure_id))
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

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

    def set_diagnosis_name(self, diagnosis_name):
        self.__diagnosis = diagnosis_name
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            query = 'UPDATE diagnosis SET diagnosis_name = %s WHERE diagnosis_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__diagnosis, self.__diagnosis_id))
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def to_json(self):
        fields_data = {
            "id" : self.__diagnosis_id,
            "diagnosis" : self.__procedure
        }

        return json.dumps(fields_data)



class Visit:
    def __init__(self, visit_id="", doctor_id = "", patient_id = ""):
        self.__doctor_id = doctor_id
        self.__patient_id = patient_id
        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            try:
                connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')
                query = """INSERT INTO viit (visit_id, doctor_id, patient_id) 
                           VALUES (%s, %s, %s) """

                values = [(self.__visit_id, self.__doctor_id, self.__patient_id)]

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

    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id
        try:
            connection = mysql.connector.connect(host='67.205.163.33',
                                         database='jak307',
                                         user='jak307',
                                         password='InfSci1500_4131521')

            query = 'UPDATE visit SET fk_doctor_id = %s WHERE visit_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__doctor_id, self.__visit_id))
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

            query = 'UPDATE visit SET fk_patient_id = %s WHERE visit_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__patient_id, self.__visit_id))
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    def to_json(self):
        fields_data = {
            "visit id" : self.__visit_id,
            "doctor id" : self.__fname,
            "patient id" : self.__lname,
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

            query = 'UPDATE visit_procedure SET fk_visit_id = %s WHERE fk_procedure_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__visit_id, self.__procedure_id))
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

            query = 'UPDATE visit_procedure SET fk_procedure_id = %s WHERE fk_visit_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__procedure_id, self.__visit_id))
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

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

            query = 'UPDATE visit_diagnosis SET fk_visit_id = %s WHERE fk_diagnosis_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__visit_id, self.__procedure_id))
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

            query = 'UPDATE visit_diagnosis SET fk_diagnosis_id = %s WHERE fk_visit_id = %s;'
            
            cursor = connection.cursor()
            cursor.executemany(query, (self.__diagnosis_id, self.__visit_id))
            connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

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
