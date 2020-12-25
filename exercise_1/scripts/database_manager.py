import functools
import random

import psycopg2
import factories as f
import constants as c
from psycopg2.extras import execute_values


def safe_connection(error_msg=None):
    """
    A decorator that wraps the passed in function closes the db connection on error safely.
    """
    def _safe_connection(method):
        @functools.wraps(method)
        def wrapper(db_manager, *args, **kwargs):
            try:
                return method(db_manager, *args, **kwargs)
            except(Exception, psycopg2.Error) as error:
                print(error_msg)
                db_manager.close()
                raise error
        return wrapper
    return _safe_connection


class _SQL(object):
    """Helper class that holds all sql statements used by the DB"""
    ADJUST_DATE_SQL = """
    SET datestyle = dmy
    """
    ADDRESS_SQL = """
        insert into address(address_name, address_number, city, country, postal_code)
        values %s
   """
    FACULTY_SQL = """
        insert into faculty(name, university_name)
        values %s
    """
    CONFERENCE_SQL = """
        insert into conference(faculty_id, address_id, start_date, end_date, title)
        values %s
    """
    SCIENTIST_SQL = """
        insert into scientist(title, name, surname)
        values %s
    """
    PHD_SQL = """
        insert into phd(date_received, description, supervisor_id, title, scientist_id)
        values %s
    """
    SCIENTIST_WORKS_AT_FACULTY_SQL = """
        insert into scientist_works_at_faculty(faculty_id, scientist_id)
        values %s
    """


class ScientificCommunityDBManager(object):
    """DB Wrapper for the scientific_community database"""

    def __init__(self):
        self._conn = None
        self._cursor = None

    def __str__(self):
        return f"ScientificCommunityDBManager(db_id={id(self._conn)})"

    def close(self):
        self._cursor.close()
        self._conn.close()

    @safe_connection("Error in executing generate_and_insert_fake_data method")
    def generate_and_insert_fake_data(self):
        """
        Generates and inserts all fake data
        """
        # some constants
        fac_num = 10
        conf_num = 50
        sc_per_fac = 40

        # generate and insert faculties
        faculties = list(f.FacultyFactory.generate_unique_faculties())
        values = [[fac.name, fac.university_name] for fac in faculties]
        execute_values(self._cursor, sql=_SQL.FACULTY_SQL, argslist=values)

        # generate and insert addresses
        addresses = list(f.AddressFactory.generate_addresses(n=conf_num))
        values = [[ad.address_name, ad.address_number, ad.city, ad.postal_code, ad.country] for ad in addresses]
        execute_values(self._cursor, sql=_SQL.ADDRESS_SQL, argslist=values)

        # adjust date
        self._cursor.execute(_SQL.ADJUST_DATE_SQL)
        # generate and insert conferences
        conferences = list(f.ConferenceFactory.generate_unique_conferences())
        self._map_conferences(conferences, conf_num, fac_num)
        values = [[conf.faculty_id, conf.address_id, conf.start_date, conf.end_date, conf.title]
                  for conf in conferences]
        execute_values(self._cursor, sql=_SQL.CONFERENCE_SQL, argslist=values)

        # generate and insert scientists along with their phds
        self._generate_and_insert_scientists_and_phds(fac_num, sc_per_fac)
        self._conn.commit()

    @staticmethod
    def _map_conferences(conferences, conf_num, fac_num):
        """
        Maps conferences to faculties
        :param conferences: a list with Conference objects
        :param conf_num: number of conferences
        :param fac_num: number of faculties
        """
        fac_id = 1
        conf_per_fac = conf_num // fac_num
        for idx, conf in enumerate(conferences, start=1):
            conf.faculty_id = fac_id
            conf.address_id = idx
            if idx % conf_per_fac == 0:
                fac_id += 1

    def _generate_and_insert_scientists_and_phds(self, fac_num, sc_per_fac):
        """
        Generates and inserts scientists to their faculties and phds
        ScientistFactory.generate_scientists_per_title
        :param fac_num: number of faculties
        :param sc_per_fac: number of scientists per faculty
        """
        fac_id = 1
        phd_starting_id = 1
        scientist_starting_id = 1
        for i in range(1, fac_num + 1):
            scientists = f.ScientistFactory.generate_scientists_per_title(sc_per_fac, start=scientist_starting_id)
            plain_scientists = [sc for sc_list in scientists.values() for sc in sc_list]
            # insert scientists
            values = [[sc.title, sc.name, sc.surname] for sc in plain_scientists]
            execute_values(self._cursor, sql=_SQL.SCIENTIST_SQL, argslist=values)
            # insert scientist_works_at_faculty relation
            values = [[fac_id, sc.scientist_id] for sc in plain_scientists]
            execute_values(self._cursor, sql=_SQL.SCIENTIST_WORKS_AT_FACULTY_SQL, argslist=values)
            # insert phds
            prof_list = scientists[c.PROFESSOR] + scientists[c.ASSISTANT_PROFESSOR] + scientists[c.ASSOCIATE_PROFESSOR]
            student_list = scientists[c.LECTURER] + scientists[c.RESEARCHER] + scientists[c.LABORATORY_TEACHING_STAFF]
            phd_ids = len(student_list)
            phds = list(f.PHDFactory.generate_phds(phd_ids, start=phd_starting_id))
            for j in range(phd_ids):
                phds[j].scientist_id = student_list[j].scientist_id
                for prof in random.choices(prof_list):
                    phds[j].supervisor_id = prof.scientist_id
            values = [[phd.date_received, phd.description, phd.supervisor_id, phd.title, phd.scientist_id]
                      for phd in phds]
            execute_values(self._cursor, sql=_SQL.PHD_SQL, argslist=values)
            phd_starting_id += phd_ids
            scientist_starting_id += sc_per_fac

    @safe_connection("Error in executing commit method")
    def commit(self):
        """Commit the changes to the database"""
        self._conn.commit()

    def truncate_tables(self):
        sql = """select table_name from information_schema.tables where table_schema = 'public'"""
        self._cursor.execute(sql)
        for table_name in self._cursor.fetchall():
            self._truncate_table(table_name)
        self._conn.commit()

    def _truncate_table(self, table_name):
        sql = """truncate "%s" restart identity cascade""" % table_name
        self._cursor.execute(sql)

    @classmethod
    def create(cls, database, password, user="postgres", host="localhost", port="5432"):
        """
        :param database: database name
        :param password: password for the specified database user
        :param user: database user - defaults to postgres
        :param host: host ip - defaults to localhost
        :param port: connection port - defaults to 5432
        :rtype: ScientificCommunityDBManager
        """
        db_manager = cls()
        try:
            conn = psycopg2.connect(database=database, password=password, user=user, host=host, port=port)
            cursor = conn.cursor()
            db_manager._conn = conn
            db_manager._cursor = cursor
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print(f"You are connected into the - {record}\n")
            print(f"DSN details: {conn.get_dsn_parameters()}\n")
            return db_manager
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database", error)
