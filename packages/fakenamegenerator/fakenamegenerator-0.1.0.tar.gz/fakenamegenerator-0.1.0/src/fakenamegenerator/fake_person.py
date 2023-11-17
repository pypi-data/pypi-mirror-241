from datetime import datetime

class FakePerson:
    def __init__(self, name, address, phone_local, phone_code, age, birthday, zodiac, blood):
        self.name = name
        self.address = address
        self.phone_local = phone_local
        self.phone_code = phone_code
        self.age = age
        self.birthday = birthday
        self.zodiac = zodiac
        self.blood = blood

    @property
    def first_name(self):
        return self.name.split()[0]

    @property
    def last_name(self):
        return self.name.split()[-1]

    @property
    def blood_resus(self):
        return self.blood[-1]

    @property
    def blood_type(self):
        return self.blood[0:-1].replace('O','')

    @property
    def phone(self):
        return "(" + self.phone_code + ") " + self.phone_local

    @property
    def birthday_date(self):
        return datetime.strptime(self.birthday, '%B %d, %Y').date()
