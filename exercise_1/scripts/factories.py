import decimal
import random
import constants as c
import entities as ent
from faker import Faker
from faker.providers import person, phone_number, internet, address, date_time, lorem, misc


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

    def year(self):
        return self._fake.year()

    def timestamp(self):
        return self._fake.date_time()

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

    def text(self):
        return self._fake.text()

    def __str__(self):
        return "LoremMixin"


class MiscMixin(BaseMixin):
    """MiscMixin"""
    def __init__(self, fake: Faker):
        super(MiscMixin, self).__init__(fake)
        self._fake.add_provider(misc)
        self._fake.add_provider(internet)

    @staticmethod
    def score():
        return random.randint(1, 5)

    @staticmethod
    def money():
        return decimal.Decimal(random.randrange(10000))/100

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
    def generate_addresses(n=1):
        """
        Generator of Address objects
        :param n: number of objects to be generated
        """
        for i in enumerate(range(n), start=1):
            data = {"address_id": i, "address_name": _fg.address_name(), "address_number": _fg.address_number(),
                    "city": _fg.city(), "country": _fg.country(), "postal_code": _fg.postal_code()}
            yield ent.Address.build_from_data(data)

    def __str__(self):
        return "AddressFactory"


class FacultyFactory(object):
    """Class used for generating fake Address entities"""

    @staticmethod
    def generate_faculties(n=10):
        """
        Generator of Faculty objects
        :param n: number of objects to be generated
        """
        for fac_id, name in enumerate(random.choices(c.FACULTIES["names"], c.FACULTIES["weights"], k=n), start=1):
            data = {"faculty_id": fac_id, "name": name, "university_name": c.EKPA}
            yield ent.Faculty.build_from_data(data)

    @staticmethod
    def generate_unique_faculties():
        """
        Generator of unique Faculty objects
        """
        for fac_id, name in enumerate(c.FACULTIES["names"]):
            data = {"faculty_id": fac_id, "name": name, "university_name": c.EKPA}
            yield ent.Faculty.build_from_data(data)

    def __str__(self):
        return "FacultyFactory"


class ScientistFactory(object):
    """Class used for generating fake Address entities"""

    @staticmethod
    def generate_scientists(n=10):
        """
        Generator of ScientistFactory objects
        :param n: number of objects to be generated
        """
        for sct_id, title in enumerate(random.choices(c.SCIENTIST_TITLES["names"],
                                                      c.SCIENTIST_TITLES["weights"], k=n), start=1):
            name, surname = _fg.first_name_and_last_name()
            data = {"scientist_id": sct_id, "title": title, "name": name, "surname": surname}
            yield ent.Scientist.build_from_data(data)

    @staticmethod
    def generate_scientists_per_title(n=10):
        """
        :param n: number of objects to be generated
        :return: A dictionary mapping scientists to their title
        """
        mapper = {
            c.PROFESSOR: [],
            c.ASSOCIATE_PROFESSOR: [],
            c.ASSISTANT_PROFESSOR: [],
            c.LECTURER: [],
            c.LABORATORY_TEACHING_STAFF: [],
            c.PHD_CANDIDATE: []}
        for sct in ScientistFactory.generate_scientists(n):
            mapper[sct.title].append(sct)
        return mapper

    def __str__(self):
        return "ScientistFactory"
