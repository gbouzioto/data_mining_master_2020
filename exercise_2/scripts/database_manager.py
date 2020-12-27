import functools
import random

import psycopg2
from psycopg2.extras import execute_values

import exercise_2.scripts.constants as c
import exercise_2.scripts.factories as f


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
        insert into conference(faculty_id, address_id, start_date, end_date, title, fee)
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
    FUNDING_SQL = """
        insert into funding(scientist_id, funder, budget, start_date, end_date)
        values %s
    """
    FUNDING_FUNDS_PHD_SQL = """
       insert into funding_funds_phd(funding_id, phd_id, working_hours_spent)
       values %s
   """
    PUBLICATION_SQL = """
       insert into publication(main_author_id, title, summary, conference_id, funding_id, won_first_prize)
       values %s
   """
    PUBLICATION_SECONDARY_AUTHOR_SQL = """
       insert into publication_secondary_author(author_id, publication_id)
       values %s
   """
    SCIENTIST_PARTICIPATES_AT_CONFERENCE_SQL = """
       insert into scientist_participates_at_conference(conference_id, scientist_id, is_volunteer)
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
        values = [[ad.address_name, ad.address_number, ad.city, ad.country, ad.postal_code] for ad in addresses]
        execute_values(self._cursor, sql=_SQL.ADDRESS_SQL, argslist=values)

        # adjust date
        self._cursor.execute(_SQL.ADJUST_DATE_SQL)
        # generate and insert conferences
        conferences = list(f.ConferenceFactory.generate_unique_conferences())
        self._map_conferences(conferences, conf_num, fac_num)
        values = [[conf.faculty_id, conf.address_id, conf.start_date, conf.end_date, conf.title, conf.fee]
                  for conf in conferences]
        execute_values(self._cursor, sql=_SQL.CONFERENCE_SQL, argslist=values)

        # generate and insert scientists along with their phds, publications and funding
        self._generate_and_insert_scientist_relations(fac_num, sc_per_fac, len(conferences))
        self._conn.commit()

    @staticmethod
    def _map_conferences(conferences, conf_num, fac_num):
        """
        Maps conferences to their faculties and addresses
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

    def _generate_and_insert_scientist_relations(self, fac_num, sc_per_fac, conf_num):
        """
        Generates and inserts scientists to their faculties and phds
        ScientistFactory.generate_scientists_per_title
        :param fac_num: number of faculties
        :param sc_per_fac: number of scientists per faculty
        :param conf_num: number of conferences
        """
        fac_id = 1
        phd_starting_id = 1
        scientist_starting_id = 1
        funding_starting_id = 1
        publication_starting_id = 1
        # tracks which publications have already won a first prize
        won_first_prize_ids = set()
        scientists_participate_at_conf_mapping = {k: set() for k in range(1, conf_num + 1)}
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
            prof_num = len(prof_list)
            non_prof_list = scientists[c.LECTURER] + scientists[c.RESEARCHER] + scientists[c.LABORATORY_TEACHING_STAFF]
            phd_num = len(non_prof_list)
            phds = list(f.PHDFactory.generate_phds(phd_num, start=phd_starting_id))
            for j in range(phd_num):
                phds[j].scientist_id = non_prof_list[j].scientist_id
                for prof in random.choices(prof_list):
                    phds[j].supervisor_id = prof.scientist_id
            values = [[phd.date_received, phd.description, phd.supervisor_id, phd.title, phd.scientist_id]
                      for phd in phds]
            execute_values(self._cursor, sql=_SQL.PHD_SQL, argslist=values)
            # insert funding
            funding = list(f.FundingFactory.generate_funding(prof_num, funding_starting_id))
            funding_num = len(funding)
            values = []
            for j in range(prof_num):
                funding[j].scientist_id = prof_list[j].scientist_id
                values.append([funding[j].scientist_id, funding[j].funder, funding[j].budget, funding[j].start_date,
                               funding[j].end_date])
            execute_values(self._cursor, sql=_SQL.FUNDING_SQL, argslist=values)
            # give each phd a funding randomly
            values = []
            for phd in phds:
                for fund in random.choices(funding):
                    values.append([fund.funding_id, phd.phd_id, f.MiscMixin.phd_working_hours(fund.budget)])
            execute_values(self._cursor, sql=_SQL.FUNDING_FUNDS_PHD_SQL, argslist=values)
            # insert publications
            publications = list(f.PublicationFactory.generate_publications(prof_num, publication_starting_id))
            publications_num = len(publications)
            values = []
            for j in range(prof_num):
                publications[j].main_author_id = prof_list[j].scientist_id
                publications[j].funding_id = random.randint(funding_starting_id, len(funding) + funding_starting_id - 1)
                publications[j].conference_id = random.randint(1, conf_num)
                # if there is no other first prize publication in the conference, attempt to win the first prize
                if not publications[j].conference_id in won_first_prize_ids:
                    if f.MiscMixin.publication_wins_first_prize():
                        publications[j].won_first_prize = True
                        won_first_prize_ids.add(publications[j].conference_id)
                values.append([publications[j].main_author_id, publications[j].title, publications[j].summary,
                               publications[j].conference_id, publications[j].funding_id,
                               publications[j].won_first_prize])
            execute_values(self._cursor, sql=_SQL.PUBLICATION_SQL, argslist=values)
            # insert publication secondary authors
            values = []
            for pub in publications:
                # select up to five non professor individuals for each publication
                temp_list = non_prof_list[:]
                for non_prof in f.MiscMixin.choices_no_replacement(temp_list, k=random.randint(1, 5)):
                    values.append([non_prof.scientist_id, pub.publication_id])
            execute_values(self._cursor, sql=_SQL.PUBLICATION_SECONDARY_AUTHOR_SQL, argslist=values)

            # insert scientist participates at conference randomly
            values = []
            for sc in plain_scientists:
                # get a random_conference id
                conference_id = random.randint(1, conf_num)
                if sc.scientist_id in scientists_participate_at_conf_mapping[conference_id]:
                    # scientist already participated in that conference
                    continue
                scientists_participate_at_conf_mapping[conference_id].add(sc.scientist_id)
                is_volunteer = f.MiscMixin.is_volunteer()
                values.append([conference_id, sc.scientist_id, is_volunteer])
            execute_values(self._cursor, sql=_SQL.SCIENTIST_PARTICIPATES_AT_CONFERENCE_SQL, argslist=values)

            # update ids
            phd_starting_id += phd_num
            scientist_starting_id += sc_per_fac
            funding_starting_id += funding_num
            publication_starting_id += publications_num
            fac_id += 1

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
