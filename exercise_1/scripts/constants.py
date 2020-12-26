"""Constants"""
# Countries
GREECE = "Ελλάδα"
# University names
EKPA = "National and Kapodistrian University of Athens"

# Faculty names
ECONOMICS_AND_POLITICAL_SCIENCES = "ECONOMICS AND POLITICAL SCIENCES"
EDUCATION = "EDUCATION"
HEALTH_SCIENCES = "HEALTH SCIENCES"
LAW = "LAW"
PHILOSOPHY = "PHILOSOPHY"
PHYSICAL_EDUCATION_AND_SPORT_SCIENCE = "PHYSICAL EDUCATION AND SPORT SCIENCE"
SCIENCE = "SCIENCE"
THEOLOGY = "THEOLOGY"
AGRICULTURAL_DEVELOPMENT = "AGRICULTURAL DEVELOPMENT"
NUTRITION_AND_SUSTAINABILITY = "NUTRITION AND SUSTAINABILITY"

# Faculty staff titles
PROFESSOR = "Professor"
ASSOCIATE_PROFESSOR = "Associate Professor"
ASSISTANT_PROFESSOR = "Assistant Professor"
LECTURER = "Lecturer"
LABORATORY_TEACHING_STAFF = "Laboratory Teaching Staff"
RESEARCHER = "Researcher"

# Funder titles
EUROPEAN_UNION = "European Union"
UNDP = "UNDP"
NATIONAL_FUND = "National Fund"
MINISTRY_OF_AGRICULTURE = "Ministry of Agriculture"
MINISTRY_OF_HEALTH = "Ministry of Health"
MINISTRY_OF_TOURISM = "Ministry of Tourism"
NATIONAL_BANK_OF_GREECE = "National Bank of Greece"
EURO_BANK = "Eurobank"
PEIREAUS_BANK = "Peireaus bank"
ALPHA_BANK = "Alphabank"

UNIS = [EKPA]

FACULTIES = {
    "names": [
        ECONOMICS_AND_POLITICAL_SCIENCES,
        EDUCATION,
        HEALTH_SCIENCES,
        LAW,
        PHILOSOPHY,
        PHYSICAL_EDUCATION_AND_SPORT_SCIENCE,
        SCIENCE,
        THEOLOGY,
        AGRICULTURAL_DEVELOPMENT,
        NUTRITION_AND_SUSTAINABILITY,
    ],
    "weights": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
}

SCIENTIST_TITLES = {
    "names": [
        PROFESSOR,
        ASSOCIATE_PROFESSOR,
        ASSISTANT_PROFESSOR,
        LECTURER,
        LABORATORY_TEACHING_STAFF,
        RESEARCHER,
    ],
    "weights": [0.075, 0.1, 0.125, 0.2, 0.25, 0.25]
}

CONFERENCES = [
    ["International Conference on Artificial Intelligence, Robots and Mechanical Engineering", "23/12/2019",
     "23/12/2019"],
    ["International Conference on Control system, power and electrical engineering", "24/12/2019", "24/12/2019"],
    ["International Conference on Environment, Agriculture and Biotechnology", "26/12/2019", "26/12/2019"],
    ["International Conference on Medical and Health Sciences", "27/12/2019", "27/12/2019"],
    ["International Conference on Recent Advances in Science, Technology &amp; Engineering", "28/12/2019",
     "28/12/2019"],
    ["International Conference on Recent Developments in Social Science and Business Management", "29/12/2019",
     "29/12/2019"],
    ["International Conference on Software Engineering and Computer Science", "30/12/2019", "30/12/2019"],
    ["International Research Conference on Arts, Commerce, and Business Management", "31/12/2019", "31/12/2019"],
    ["International conference on Applied Science Mathematics and Statistics", "2/1/2019", "2/1/2019"],
    ["International Conference on Business, Economics, Social Science and Humanities", "3/1/2019", "3/1/2019"],
    ["International Conference on Industrial Electronics and Electrical Engineering", "4/1/2019", "4/1/2019"],
    ["International Conference on Mechanical, Aerospace and Production Engineering", "5/1/2019", "5/1/2019"],
    ["International conference on Medical and Health Sciences", "6/1/2019", "6/1/2019"],
    ["International conference on Oncology &amp; Cancer Research", "7/1/2019", "8/1/2019"],
    ["International Congress on Oil and Gas", "8/1/2019", "9/1/2019"],
    ["International Conference on Robotics, Automation and Communication Engineering", "9/1/2019", "10/1/2019"],
    ["International Conference on Recent Innovations in Computer Science and Information Technology", "10/1/2019",
     "11/1/2019"],
    ["International Conference on Recent Innovations in Science, Engineering and Technology", "11/1/2019", "12/1/2019"],
    ["World Conference on Disaster Management", "12/1/2019", "13/1/2019"],
    ["World Congress on Medical Imaging and Clinical Research", "13/1/2019", "14/1/2019"],
    ["International Conference on Business Management and Social Innovation", "14/1/2019", "15/1/2019"],
    ["International Conference On Electrical and Electronics Engineering", "15/1/2019", "16/1/2019"],
    ["International Conference on Forestry Food and Sustainable Agriculture", "16/1/2019", "17/1/2019"],
    ["International Conference on Mechanical &amp; Production Engineering", "17/1/2019", "18/1/2019"],
    ["International Conference on Recent Advances in Computer Science and Information Technology", "18/1/2019",
     "19/1/2019"],
    ["International Conference on Recent Advances in Medical, Medicine and Health Sciences", "19/1/2019", "20/1/2019"],
    ["International Conference on Research in Science, Engineering and Technology", "20/1/2019", "21/1/2019"],
    ["National Conference on Recent Advances in Science, Engineering, Technology and Management", "21/1/2019",
     "22/1/2019"],
    ["International Conference on Oncolytic Virus Therapeutics (ICOVT)", "22/1/2019", "23/1/2019"],
    ["International Conference on Civil and Environmental Engineering (I2C2E)", "23/1/2019", "24/1/2019"],
    ["International Conference on Arts, Education and Social Science (ICAES)", "24/1/2019", "25/1/2019"],
    ["International Conference on Applied Physics and Mathematics (ICAPM)", "25/1/2019", "26/1/2019"],
    ["International Conference on Chemical and Biochemical Engineering (ICCBE)", "26/1/2019", "27/1/2019"],
    ["International Conference on Communication and Signal Processing (ICCSP)", "27/1/2019", "28/1/2019"],
    ["International Conference on Economics and Finance Research (ICEFR)", "28/1/2019", "29/1/2019"],
    ["International Conference on Internet Technologies and Society (ICITS)", "29/1/2019", "30/1/2019"],
    ["International Conference on Medical and Biosciences (ICMBS)", "30/1/2019", "31/1/2019"],
    ["International Conference on Power Control and Embedded System (ICPCES)", "31/1/2019", "1/2/2019"],
    ["International Conference on Science, Technology, Engineering and Management (ICSTEM)", "1/2/2019", "2/2/2019"],
    ["International conference on Applied Science Mathematics and Statistics (ICASMS)", "2/2/2019", "3/2/2019"],
    ["International Conference on Communication, Electronics and Electrical Engineering (ICCEEE)", "3/2/2019",
     "4/2/2019"],
    ["International Conference on Computer science and Information Technology (ICCSIT)", "4/2/2019", "5/2/2019"],
    ["International Conference on Mechanical, Manufacturing, Industrial and Civil Engineering (ICMMICE)", "5/2/2019",
     "6/2/2019"],
    ["International conference on Medical Health Science, Pharmacology &amp; Bio Technology (ICMPB)", "6/2/2019",
     "7/2/2019"],
    ["International Conference on Recent Developments in Social Science and Business Management (ICRDSSBM)", "7/2/2019",
     "8/2/2019"],
    ["International conference on Science Engineering &amp; Technology (ICSET)", "8/2/2019", "9/2/2019"],
    ["International conference on agriculture and animal science (IC2AS)", "9/2/2019", "10/2/2019"],
    ["International Conference on Social Science, Literature, Economics and Education (IC2SL2E)", "10/2/2019",
     "11/2/2019"],
    ["International conference on arts and humanities (ICAH)", "11/2/2019", "12/2/2019"],
    ["International conference on biological and medical sciences (ICBMS) ", "12/2/2019", "13/2/2019"]
]


FUNDING = {
    "names": [
        EUROPEAN_UNION,
        UNDP,
        NATIONAL_FUND,
        MINISTRY_OF_AGRICULTURE,
        MINISTRY_OF_HEALTH,
        MINISTRY_OF_TOURISM,
        NATIONAL_BANK_OF_GREECE,
        EURO_BANK,
        PEIREAUS_BANK,
        ALPHA_BANK],
    "weights": [0.25, 0.15, 0.1, 0.05, 0.05, 0.05, 0.1, 0.1, 0.05, 0.1]
}
