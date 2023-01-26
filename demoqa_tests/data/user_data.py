from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    address: str
    gender: str
    birth_year: str
    birth_month: str
    birth_day: int
    subject: str
    hobby: str
    picture: str
    state: str
    city: str


nikita = User(first_name='nikita',
                     last_name='kuznetsov',
                     email='mamintargetolog@gmail.com',
                     mobile='9111111111',
                     address='Moscow',
                     gender='Other',
                     birth_year='1991',
                     birth_month='November',
                     birth_day=19,
                     subject='Economics',
                     hobby='Sports',
                     picture='screen.jpg',
                     state='NCR',
                     city='Delhi')


