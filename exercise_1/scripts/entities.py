"""Database entities"""


class BaseEntity(object):
    """BaseEntity Object"""
    @classmethod
    def build_from_data(cls, data: dict):
        """Builds the object from the given data"""
        obj = cls()
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return obj

    def __str__(self):
        return "BaseEntity"


class Address(BaseEntity):
    """Represents an Address entity"""
    def __init__(self):
        self.address_id = None
        self.address_name = None
        self.address_number = None
        self.city = None
        self.country = None
        self.postal_code = None

    def __str__(self):
        return f"Address(address_id={self.address_id})"

    def to_dict(self):
        return {"address_id": self.address_id, "address_name": self.address_name, "address_number": self.address_number,
                "city": self.city, "country": self.country, "postal_code": self.postal_code}


class Conference(BaseEntity):
    """Represents a Conference entity"""
    def __init__(self):
        self.conference_id = None
        self.faculty_id = None
        self.address_id = None
        self.start_date = None
        self.end_date = None
        self.title = None
        self.fee = None

    def __str__(self):
        return f"Conference(conference_id={self.conference_id}, faculty_id={self.faculty_id})"


class Faculty(BaseEntity):
    """Represents a Faculty entity"""

    def __init__(self):
        self.faculty_id = None
        self.name = None
        self.university_name = None

    def __str__(self):
        return f"Faculty(faculty_id={self.faculty_id})"


class Funding(BaseEntity):
    """Represents a Funding entity"""

    def __init__(self):
        self.funding_id = None
        self.scientist_id = None
        self.funder = None
        self.budget = None
        self.start_date = None
        self.end_date = None

    def __str__(self):
        return f"Funding(funding_id={self.funding_id}, scientist_id={self.scientist_id})"


class FundingFundsPHD(BaseEntity):
    """Represents a FundingFundsPHD entity"""

    def __init__(self):
        self.funding_id = None
        self.phd_id = None
        self.working_hours_spent = None

    def __str__(self):
        return f"FundingFundsPHD(funding_id={self.funding_id}, phd_id={self.phd_id})"


class PHD(BaseEntity):
    """Represents a PHD entity"""

    def __init__(self):
        self.phd_id = None
        self.date_received = None
        self.description = None
        self.supervisor_id = None
        self.title = None
        self.scientist_id = None

    def __str__(self):
        return f"PHD(phd_id={self.phd_id}, scientist_id={self.scientist_id})"


class Publication(BaseEntity):
    """Represents a Publication entity"""

    def __init__(self):
        self.publication_id = None
        self.main_author_id = None
        self.title = None
        self.summary = None
        self.conference_id = None
        self.funding_id = None
        self.won_first_prize = None

    def __str__(self):
        return f"Publication(publication_id={self.publication_id}, main_author_id=({self.main_author_id})"


class PublicationSecondaryAuthor(BaseEntity):
    """Represents a PublicationSecondaryAuthor entity"""

    def __init__(self):
        self.publication_id = None
        self.scientist_id = None

    def __str__(self):
        return f"PublicationSecondaryAuthor(publication_id={self.publication_id}, scientist_id=({self.scientist_id})"


class Scientist(BaseEntity):
    """Represents a Scientist entity"""

    def __init__(self):
        self.scientist_id = None
        self.title = None
        self.name = None
        self.surname = None

    def __str__(self):
        return f"Scientist(scientist_id={self.scientist_id})"


class ScientistParticipatesAtConference(BaseEntity):
    """Represents a ScientistParticipatesAtConference entity"""

    def __init__(self):
        self.conference_id = None
        self.scientist_id = None
        self.is_volunteer = None
        self.fee = None

    def __str__(self):
        return f"ScientistParticipatesAtConference(scientist_id={self.scientist_id}, " \
               f"conference_id={self.conference_id})"


class ScientistWorksAtFaculty(BaseEntity):
    """Represents a ScientistWorksAtFaculty entity"""

    def __init__(self):
        self.faculty_id = None
        self.scientist_id = None

    def __str__(self):
        return f"ScientistWorksAtFaculty(faculty_id={self.faculty_id}, scientist_id=({self.scientist_id})"
