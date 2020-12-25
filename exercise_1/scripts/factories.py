import decimal
import random
import datetime

from faker import Faker
from faker.providers import person, phone_number, internet, address, date_time, lorem, misc

import constants as c
import entities as ent


class BaseMixin(object):
    """BaseMixin"""

    def __init__(self, fake: Faker):
        self._fake = fake

    def __str__(self):
        return "BaseMixin"


class AddressMixin(BaseMixin):
    """Address Mixin"""
    def __init__(self, fake: Faker):
        super(AddressMixin, self).__init__(fake)
        self._fake.add_provider(address)

    def address_name(self):
        return self._fake.street_name()

    def address_number(self):
        return self._fake.building_number()

    def country(self):
        return self._fake.country()

    def city(self):
        return self._fake.city()

    def postal_code(self):
        return self._fake.postcode()

    def __str__(self):
        return "AddressMixin"


class PersonMixin(BaseMixin):
    """BookMixin"""
    def __init__(self, fake: Faker):
        super(PersonMixin, self).__init__(fake)
        self._fake.add_provider(person)
        self._fake.add_provider(phone_number)

    def first_name_and_last_name(self):
        gender = 'Male' if self._fake.random.randint(0, 1) == 0 else 'Female'
        if gender == 'Male':
            return self._fake.first_name_male(), self._fake.last_name_male()
        return self._fake.first_name_female(), self._fake.last_name_female()

    def __str__(self):
        return "PersonMixin"


class DateTimeMixin(BaseMixin):
    """DateTimeMixin"""
    def __init__(self, fake: Faker):
        super(DateTimeMixin, self).__init__(fake)
        self._fake.add_provider(date_time)

    def date(self, start_date='-30y', end_date='-10y'):
        """
        :param start_date: start_date
        :param end_date: end_date
        """
        date = self._fake.date_between(start_date=start_date, end_date=end_date)
        return date.strftime("%d/%m/%Y")

    def funding_start_end_date(self, funding):
        """
        :param funding: the funding amount
        :return: a tuple of start and end dates
        """
        date = self._fake.date_between(start_date='-3y', end_date='-1y')
        if funding in range(500000):
            delta = datetime.timedelta(weeks=24)
        elif funding in range(500001, 1000000):
            delta = datetime.timedelta(weeks=48)
        elif funding in range(1000001, 2000000):
            delta = datetime.timedelta(weeks=72)
        elif funding in range(2000001, 3000000):
            delta = datetime.timedelta(weeks=96)
        elif funding in range(3000001, 4000001):
            delta = datetime.timedelta(weeks=110)
        else:
            delta = datetime.timedelta(weeks=140)
        return date.strftime("%d/%m/%Y"), (date + delta).strftime("%d/%m/%Y")

    def __str__(self):
        return "DateTimeMixin"


class LoremMixin(BaseMixin):
    """LoremMixin"""
    def __init__(self, fake: Faker):
        super(LoremMixin, self).__init__(fake)
        self._fake.add_provider(lorem)

    def sentence(self, nb_words=10):
        """
        :param nb_words: Number of words to be included
        """
        return self._fake.sentence(nb_words=nb_words)

    def text(self, max_nb_chars=200):
        """
        :param max_nb_chars: Number of characters to be included
        """
        return self._fake.text(max_nb_chars)

    def __str__(self):
        return "LoremMixin"


class MiscMixin(BaseMixin):
    """MiscMixin"""
    def __init__(self, fake: Faker):
        super(MiscMixin, self).__init__(fake)
        self._fake.add_provider(misc)
        self._fake.add_provider(internet)

    @staticmethod
    def budget(start=50000, limit=4000000):
        """
        :param start: starting budget
        :param limit: budget limit
        :return: a float number
        """
        num = format(random.randint(start, limit), '.2f')
        return decimal.Decimal(num)

    def __str__(self):
        return "MiscMixin"


class FakeGenerator(AddressMixin, PersonMixin, DateTimeMixin, LoremMixin, MiscMixin):
    """Class used for generating fake data"""

    def __init__(self):
        self._fake = Faker()
        super(FakeGenerator, self).__init__(self._fake)

    def clear_unique(self):
        """Clears the unique data generated"""
        self._fake.unique.clear()

    def __str__(self):
        return f"_FakeGenerator(fake_id={id(self._fake)})"


_fg = FakeGenerator()


class AddressFactory(object):
    """Class used for generating fake Address entities"""

    @staticmethod
    def generate_addresses(n=1, start=1):
        """
        Generator of Address objects
        :param n: number of objects to be generated
        :param start: the starting id
        """
        for address_id in range(start, n + start):
            data = {"address_id": address_id, "address_name": _fg.address_name(),
                    "address_number": _fg.address_number(), "city": _fg.city(), "country": _fg.country(),
                    "postal_code": _fg.postal_code()}
            yield ent.Address.build_from_data(data)

    def __str__(self):
        return "AddressFactory"


class FacultyFactory(object):
    """Class used for generating fake Address entities"""

    @staticmethod
    def generate_faculties(n=10, start=1):
        """
        Generator of Faculty objects
        :param n: number of objects to be generated
        :param start: the starting id
        """
        for fac_id, name in enumerate(random.choices(c.FACULTIES["names"], c.FACULTIES["weights"], k=n), start=start):
            data = {"faculty_id": fac_id, "name": name, "university_name": c.EKPA}
            yield ent.Faculty.build_from_data(data)

    @staticmethod
    def generate_unique_faculties():
        """
        Generator of unique Faculty objects
        """
        for fac_id, name in enumerate(c.FACULTIES["names"], start=1):
            data = {"faculty_id": fac_id, "name": name, "university_name": c.EKPA}
            yield ent.Faculty.build_from_data(data)

    def __str__(self):
        return "FacultyFactory"


class ScientistFactory(object):
    """Class used for generating fake Address entities"""

    @staticmethod
    def generate_scientists(n=10, start=1):
        """
        Generator of Scientist objects
        :param n: number of objects to be generated
        :param start: the starting id
        """
        for sct_id, title in enumerate(random.choices(c.SCIENTIST_TITLES["names"],
                                                      c.SCIENTIST_TITLES["weights"], k=n), start=start):
            name, surname = _fg.first_name_and_last_name()
            data = {"scientist_id": sct_id, "title": title, "name": name, "surname": surname}
            yield ent.Scientist.build_from_data(data)

    @staticmethod
    def generate_scientists_per_title(n=10, start=1):
        """
        :param n: number of objects to be generated
        :return: A dictionary mapping scientists to their title
        :param start: the starting id
        """
        mapper = {key: [] for key in c.SCIENTIST_TITLES["names"]}
        for sct in ScientistFactory.generate_scientists(n, start):
            mapper[sct.title].append(sct)
        return mapper

    def __str__(self):
        return "ScientistFactory"


class PHDFactory(object):
    """Class used for generating fake PHD entities"""

    @staticmethod
    def generate_phds(n=10, start=1):
        """
        Generator of PHD objects
        :param n: number of objects to be generated
        :param start: the starting id
        """
        for phd_id in range(start, n + start):
            nb_words = random.randint(11, 22)
            max_nb_chars = random.randint(1000, 2000)
            data = {"phd_id": phd_id, "date_received": _fg.date(),
                    "description": _fg.text(max_nb_chars=max_nb_chars), "title": _fg.sentence(nb_words=nb_words)}
            yield ent.PHD.build_from_data(data)

    def __str__(self):
        return "PHDFactory"


class ConferenceFactory(object):
    """Class used for generating fake Conference entities"""

    @staticmethod
    def generate_unique_conferences():
        """
        Generator of unique Conference objects
        """
        for conf_id, data in enumerate(c.CONFERENCES, start=1):
            title, start_date, end_date = data
            data = {"conference_id": conf_id, "start_date": start_date, "end_date": end_date, "title": title}
            yield ent.Conference.build_from_data(data)

    def __str__(self):
        return "ConferenceFactory"


class PublicationFactory(object):
    """Class used for generating fake Publication entities"""

    @staticmethod
    def generate_publications(n=10, start=1):
        """
        Generator of Publication objects
        :param n: number of objects to be generated
        :param start: the starting id
        """
        for pub_id in range(start, n + start):
            nb_words = random.randint(10, 15)
            max_nb_chars = random.randint(2000, 3000)
            data = {"publication_id": pub_id, "title": _fg.sentence(nb_words), "summary": _fg.text(max_nb_chars)}
            yield ent.Publication.build_from_data(data)

    def __str__(self):
        return "PublicationFactory"


class FundingFactory(object):
    """Class used for generating fake Publication entities"""

    @staticmethod
    def generate_fundings(n=10, start=1):
        """
        Generator of Funding objects
        :param n: number of objects to be generated
        :param start: the starting id
        """
        for fund_id, funder in enumerate(random.choices(c.FUNDING["names"], c.FUNDING["weights"], k=n), start=start):
            budget = _fg.budget()
            start_date, end_date = _fg.funding_start_end_date(budget)
            data = {"funding_id": fund_id, "funder": funder, "budget": budget, "start_date": start_date,
                    "end_date": end_date}
            yield ent.Funding.build_from_data(data)

    def __str__(self):
        return "PublicationFactory"
