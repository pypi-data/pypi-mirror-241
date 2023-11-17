import random
import json
import requests
from bs4 import BeautifulSoup
from .fake_person import FakePerson



url = "https://www.fakenamegenerator.com/advanced.php"
namesets = ('us', 'ar', 'au', 'br', 'celat', 'ch', 'zhtw', 'hr', 'cs', 'dk', 'nl', 'en', 'er', 'fi', 'fr', 'gr', 'gl', 'sp', 'hobbit', 'hu', 'is', 'ig', 'it', 'jpja', 'tlh', 'ninja', 'no', 'fa', 'pl', 'ru', 'rucyr', 'gd', 'sl', 'sw', 'th', 'vn')
countries = ('au', 'as', 'bg', 'br', 'ca', 'cyen', 'cygk', 'cz', 'dk', 'ee', 'fi', 'fr', 'gr', 'gl', 'hu', 'is', 'it', 'nl', 'nz', 'no', 'pl', 'pt', 'sl', 'za', 'sp', 'sw', 'sz', 'tn', 'uk', 'us', 'uy')



def getUrl(worldWide=False, nameset=[], country=[]):
    if not worldWide and not nameset and not country:
        return url

    current_url = url + "?t=country"

    if worldWide:
        current_namesets = list(namesets)
        random.shuffle(current_namesets)
        nameset.extend(current_namesets[:random.randint(0,len(current_namesets))])

        current_countries = list(countries)
        random.shuffle(current_countries)
        country.extend(current_countries[:random.randint(0,len(current_countries))])


    for nameset in set(nameset):
        current_url += ("&n%5B%5D=" + nameset)

    for country in set(country):
        current_url += ("&c%5B%5D=" + country)


    return current_url






def getIdentity(minage="19", maxage="85", worldWide=False, nameset=[], country=[], gender="50"):
    soup = BeautifulSoup(
        requests.get(getUrl(worldWide, nameset, country),
        params={'age-min' : minage, 'age-max': maxage, 'gen' : gender},
        headers={'User-Agent': 'Mozilla/5.0'}).text, "html.parser"
    )

    content = soup.find("div", {"class": "content"})

    details = content.find("div", {"class": "address"})
    name = details.find("h3").text
    address = details.find("div", {"class": "adr"}).text.strip()

    phone_local = content.find("dt", string="Phone").findNext("dd").text
    phone_code = content.find("dt", string="Country code").findNext("dd").text

    age = content.find("dt", string="Age").findNext("dd").text
    birthday = content.find("dt", string="Birthday").findNext("dd").text
    zodiac = content.find("dt", string="Tropical zodiac").findNext("dd").text

    blood = content.find("dt", string="Blood type").findNext("dd").text

    return FakePerson(name, address, phone_local, phone_code, age, birthday, zodiac, blood)




def main():
    print("Hello World!")

    iden = getIdentity(nameset=['hobbit'], country=['sl', 'is']);

    print(json.dumps(iden, default=vars))

    print("\n\n")

    print("Bye-bye " + iden.name + " of age " + iden.age
    + " from " + iden.address + " with phone " + iden.phone
    + " borned at " + iden.birthday + " which make hime " + iden.zodiac
    + " and by the way your blood type was " + iden.blood_type + " of resus " + iden.blood_resus)



if __name__ == "__main__":
    main()
