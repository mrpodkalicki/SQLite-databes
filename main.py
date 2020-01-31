import sqlite3
from sqlite3 import Error
import requests
import random

db_file_name = 'database_Courses.db'


def dowland_person_data():
    response = requests.get("https://api.namefake.com/")
    return response.json()


class Person:
    def __init__(self,id, name, surname, email, phone, id_kind_person ):
        self.name = name,
        self.surname = surname,
        self.email = email,
        self.phone = phone, 
        self.id_kind_person = id_kind_person,
        self.id =id

    def insertToTable__OSOBY(self,c):
        c.execute("INSERT INTO OSOBY VALUES ({0},'{1}','{2}','{3}','{4}', {5})".format( self.id, self.name[0], self.surname[0], self.email[0], self.phone[0], self.id_kind_person[0]))
        print('insert: {0} {0}'.format(self.name,self.surname))


class KindOfPerson:
    def __init__(self,id, kind):
        self.kind = kind,
        self.id = id

    def insertToTable__RODZAJ_OSOBY(self,c):
        c.execute(" INSERT INTO RODZAJ_OSOBY VALUES ({0}, '{1}')".format(self.id,self.kind[0]))
        print('insert:{0} {1}'.format(self.id,self.kind))


class KategoryOfCourses:
    def __init__(self, id, category):
        self.category = category,
        self.id = id

    def insertToTAble__KATEGORA_SZKOLEN(self,c):
        c.execute(" INSERT INTO KATEGORIE_SZKOLEN VALUES ({0}, '{1}')".format(self.id, self.category[0]))
        print('insert:{0} {1}'.format(self.id, self.category))



class Courses:
    def __init__(self, id, subject, category_id, person_id):
        self.id = id,
        self.subject = subject,
        self.category_id = category_id,
        self.person_id = person_id

    def insertToTable__SZKOLENIA(self, c):
        c.execute(" INSERT INTO SZKOLENIA VALUES ({0}, '{1}', {2},{3})".format(self.id[0], self.subject[0], self.category_id[0], self.person_id ))
        print('insert {0} ...'.format(self.subject))

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn
            
def create_table_persons ():
    return '''CREATE TABLE IF NOT EXISTS OSOBY (
        id integer PRIMARY KEY AUTOINCREMENT,
        imie text NOT NULL,
        nazwisko text NOT NULL,
        email text, 
        nr_telefonu text NOT NULL UNIQUE,
        rodzaj_osoby_id intiger NOT NULL,
        CONSTRAINT rodzaj_osoby
            FOREIGN KEY (rodzaj_osoby_id)
            REFERENCES  SZKOLENIA(id)
    )'''        

def create_table_kind_of_person():
    return '''CREATE TABLE IF NOT EXISTS RODZAJ_OSOBY(
        id integer PRIMARY KEY AUTOINCREMENT,
        rodzaj text NOT NULL
        
    )'''

def create_table_courses():
    return '''CREATE TABLE IF NOT EXISTS SZKOLENIA(
        id integer PRIMARY KEY AUTOINCREMENT,
        temat text NOT NULL,
        kategoria_id intiger NOT NULL,
        osoba_id intiger NOT NULL,
        CONSTRAINT kategoria
            FOREIGN KEY (kategoria_id)
            REFERENCES KATEGORIE_SZKOLEN(id)
            ,
        CONSTRAINT prowadzacy
            FOREIGN KEY (osoba_id)
            REFERENCES OSOBY(id)
    )'''

def create_table_courses_category():
    return ''' CREATE TABLE IF NOT EXISTS KATEGORIE_SZKOLEN(
        id integer PRIMARY KEY AUTOINCREMENT,
        kategoria text NOT NULL
    )'''


def add_courses(c):
    one = Courses(1, 'React vs Angular',1,4)
    one.insertToTable__SZKOLENIA(c)
    two = Courses(2, 'Co nowego w JS 2020',1,4)
    two.insertToTable__SZKOLENIA(c)
    three = Courses(3, 'Czy Vue.js dogoni REACT',1,6)
    three.insertToTable__SZKOLENIA(c)
    foure = Courses(4, 'Amazon Cloudwatch',2,7)
    foure.insertToTable__SZKOLENIA(c)
    fife = Courses(5, 'Microsoft Cloud Monitoring',2,7)
    fife.insertToTable__SZKOLENIA(c)
    six = Courses(6, 'AppDynamics',2,4)
    six.insertToTable__SZKOLENIA(c)
    seven = Courses(7, 'Pro .NET Najlepsze praktyki',3,8)
    seven.insertToTable__SZKOLENIA(c)
    eight = Courses(8, 'ScanTool.net',3,8)
    eight.insertToTable__SZKOLENIA(c)
    nine = Courses(9, 'Cyber Security od podstaw',4,8)
    nine.insertToTable__SZKOLENIA(c)
    ten = Courses(10, 'Cybersecurity level up - 5 kroków ku bezpieczeństwu',4,9)
    ten.insertToTable__SZKOLENIA(c)
    eleven = Courses(11, 'ShareX',5,9)
    eleven.insertToTable__SZKOLENIA(c)


def  add_category_of_courses(c):
        webApplications = KategoryOfCourses(1, 'Web Aplications')
        cloud = KategoryOfCourses(2, 'CLOUDS')
        netApplications = KategoryOfCourses(3, 'APlikacje .NET')
        cybersecurity = KategoryOfCourses(4, 'Cybersecurity')
        applicationTesting =  KategoryOfCourses(5, 'Testowanie Aplikacji')
        webApplications.insertToTAble__KATEGORA_SZKOLEN(c)
        cloud.insertToTAble__KATEGORA_SZKOLEN(c)
        netApplications.insertToTAble__KATEGORA_SZKOLEN(c)
        cybersecurity.insertToTAble__KATEGORA_SZKOLEN(c)
        applicationTesting.insertToTAble__KATEGORA_SZKOLEN(c)


def add_person(c,count):
    c.execute('SELECT * FROM RODZAJ_OSOBY')
    var = None
    score = c.fetchone()
    for i in range(1,count+1):
        person = dowland_person_data()
        person_name = person['name'].split()
        if i == 4 or i == 6 or i == 7 or i == 8 or i == 9 :
            id_kind = 2
        else:
            id_kind = 1
        if person_name[0]  == 'Dr.' or person_name[0]  == 'Mr.' or person_name[0]  == 'Ms.' or person_name[0]  == 'Prof.' or person_name[0]  == 'Miss':
            name = person_name[1]
            surname = person_name[2]
        else:
            name = person_name[0]
            surname = person_name[1]
        try:
            person  = Person(i, name, surname, person['email_d'], person['phone_h'], id_kind  ) 
            person.insertToTable__OSOBY(c)
        except Error as e:
            print(e)

def add_kind_of_person(c):
    c.execute('SELECT * FROM RODZAJ_OSOBY')
    var = None
    score = c.fetchone()
    try:
        kind_participent =  KindOfPerson(1,'Uczestnik')
        kind_lecturer =  KindOfPerson(2,'Prowadzacy')
        kind_participent.insertToTable__RODZAJ_OSOBY(c)
        kind_lecturer.insertToTable__RODZAJ_OSOBY(c)
    except Error as e:
        print(e,'sacf')

      


def main():
    var = None
    conn = create_connection(db_file_name)
    c= conn.cursor()


    c.execute(create_table_courses_category())
    c.execute(create_table_kind_of_person())
    c.execute(create_table_persons())
    c.execute(create_table_courses())

    c.execute('SELECT * FROM KATEGORIE_SZKOLEN')
    score = c.fetchone()
    if (var == score):
        add_category_of_courses(c)
        conn.commit()



    c.execute('SELECT * FROM RODZAJ_OSOBY')
    score = c.fetchone()
    if (var == score):
        add_kind_of_person(c)
        conn.commit()


    c.execute('SELECT * FROM OSOBY')
    score = c.fetchone()
    if(var == score):
        add_person(c,20)
        conn.commit()

    c.execute('SELECT * FROM SZKOLENIA')
    score = c.fetchone()
    if(var == score):
        add_courses(c)
        conn.commit()
    
   
    conn.close()
    


main()