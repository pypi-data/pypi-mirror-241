import csv
import json
from typing import List, Iterable, Dict
from pathlib import Path
import pickle

class NameRow:

    @classmethod
    def from_row(cls, row: List[str]) -> "NameRow":
        _, id_, lang, name = row[0:4]
        return NameRow(int(id_), lang, name)

    def __init__(self, id_, lang_code, name) -> None:
        self.id_ = id_
        self.lang_code = lang_code
        self.name = name

    def __str__(self):
        return f'{self.id_}, {self.lang_code}, {self.name}'

class CountryRow:
    
    def __init__(self, id_, name, alpha2, alpha3, fips, continent) -> None:
        self.id_ = id_
        self.name = name
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.fips = fips
        self.continent = continent

    @classmethod
    def from_row(cls, row: List[str]) -> "CountryRow":
        alpha2, alpha3, fips, _, name, capital, area_sqm2, population, continent, tld, currency, currency_name, phone_code, postal_code_format, postal_code_regex, languages, id_ = row[0:17]
        return CountryRow(int(id_), name, alpha2, alpha3, int(fips), continent)

    def update(self, names: List[NameRow]):
        if len(names):
            self.name = names[0].name

class CityRow:

    def __init__(self, id_, name, asciiname, alternate_names, latitude, longitude, country_code, admin1code, admin2code, admin3code, population, timezone, altitude, parent_code) -> None:
        self.id_ = id_
        self.name = name
        self.asciiname = asciiname
        self.alternate_names = alternate_names
        self.latitude = latitude
        self.longitude = longitude
        self.country_code = country_code
        self.admin1code = admin1code
        self.admin2code = admin2code
        self.admin3code = admin3code
        self.population = population
        self.timezone = timezone
        self.altitude = altitude
        self.parent_code = parent_code

    @classmethod
    def from_row(cls, row: List[str]) -> "CityRow":
        id_, name, asciiname, alternate_names, latitude, longitude, country_code, admin1code, admin2code, admin3code, population, altitude, timezone\
            = row[0], row[1], row[2], row[3].split(','), row[4], row[5], row[8], row[10], row[11], row[12], row[14], row[15], row[17]
        population = int(population)
        altitude = int(altitude) if altitude else -1
        parent = parent_code(country_code, admin1code, admin2code)
        return CityRow(int(id_), name, asciiname, alternate_names, latitude, longitude, country_code, admin1code, admin2code, admin3code, population, timezone, altitude, parent)

    def __str__(self, format=None):
        return f'<{self.id_}>: {self.name}'

    def update(self, names: List[NameRow]):
        if len(names):
            self.name = names[0].name
        if len(names) > 1:
            self.alternate_names = [n.name for n in names[1:]]
        
class AdminCodeRow:

    @classmethod
    def from_row(cls, row: List[str]) -> "AdminCodeRow":
        code, name, ascii_name, id_ = row[0:4]
        country_code = code[0:2]
        return AdminCodeRow(code, name, ascii_name, country_code, int(id_))

    def __init__(self, code, name, ascii_name, country_code, id_) -> None:
        self.code = code
        self.name = name
        self.ascii_name = ascii_name
        self.country_code = country_code
        self.id_ = id_
    
    def update(self, names: List[NameRow]):
        if len(names):
            self.name = names[0].name

def skip_comments(gen):
    for row in gen:
        if not row[0].startswith('#'):
            yield row

def dump(obj):
    return json.dumps(obj, ensure_ascii=False)

def parent_code(*args):
    return '.'.join([a for a in args if a is not None and len(a)])

def country_template(country_rows: List[CountryRow], continent_indexes):
    return f"""ids = {dump([x.id_ for x in country_rows])}
names = {dump([x.name for x in country_rows])}
alpha2_codes = {dump([x.alpha2 for x in country_rows])}
alpha3_codes = {dump([x.alpha3 for x in country_rows])}
fips_codes = {dump([x.fips for x in country_rows])}
continent_indexes = {dump(continent_indexes)}
"""

def city_template(all_cities: List[CityRow], states: Dict[str, AdminCodeRow], districts: Dict[str, AdminCodeRow], timezone_names: List[str]):
    return f"""ids = {dump([n.id_ for n in all_cities])}
names = {dump([n.name for n in all_cities])}
ascii_names = {dump([n.asciiname for n in all_cities])}    
positions = {dump([(n.latitude, n.longitude) for n in all_cities])}
alternate_names = {dump([n.alternate_names for n in all_cities])}
timezones = {dump([timezone_names.index(n.timezone) for n in all_cities])}
populations = {dump([n.population for n in all_cities])}
altitudes = {dump([n.altitude for n in all_cities])}
parents = {dump([n.parent_code for n in all_cities])}
states = {dump({k: [v.name, v.ascii_name, v.id_] for k, v in states.items()})}
districts = {dump({k: [v.name, v.ascii_name, v.id_] for k, v in districts.items()})}
"""

def write_constants(output, default_lang, available_languages, timezones):
    with open(output, 'w') as fp:
        fp.write(f"""default_language = "{default_lang}"
available_languages = {dump(available_languages)}
timezone_names = {dump(timezones)}
""")

def report(msg: str, end='\n'):
    print(msg, end=end)

class AlternateNamesReader:

    def __init__(self, path) -> None:
        self.cache_file = path.parent / 'names.cache'
        self.fp = open(path, 'r')
        self.file_size = path.stat().st_size
        self.id_map: Dict[str, List[NameRow]] = {}

    def save_cache_file(self):
        with open(self.cache_file, 'wb') as fp:
            pickle.dump(self.id_map, fp)

    def load_cache_file(self):
        if self.cache_file.exists():
            with open(self.cache_file, 'rb') as fp:
                self.id_map = pickle.load(fp)
                return True
        else:
            return False

    def ensure_names(self):
        report('building names...')
        if len(self.id_map) > 0:
            return
        if self.load_cache_file():
            report(f'loaded from cache!')
            return
        self.fp.seek(0)
        last_pos = -1
        while True:
            line = self.fp.readline()
            if not line:
                break
            _, id_, lang, name, _, _, _, _, _, _ = line.split('\t')
            if not lang or lang == 'link':
                continue
            id_ = int(id_)
            if id_ not in self.id_map:
                self.id_map[id_] = []
            self.id_map[id_].append(NameRow(id_, lang, name))
            pos = round(self.fp.tell() / self.file_size, ndigits=2) * 100
            if last_pos != pos:
                last_pos = pos
                report(f'Building cache: {round(last_pos)}%', end='\r')
        self.fp.close()
        self.save_cache_file()

    def read_names_for(self, place_id, selected_lang):
        return [n for n in self.id_map[place_id] if n.lang_code == selected_lang] if place_id in self.id_map else []

class Generator:

    alternate_names_file = 'alternateNamesV2.txt'
    countries_file = 'countryInfo.txt'
    states_file = 'admin1CodesASCII.txt'
    districts_file = 'admin2Codes.txt'

    def __init__(self, input_path, output_path) -> None:
        self.input_path = self.path_for(input_path)
        self.output_path = self.path_for(output_path)
        self.name_reader = AlternateNamesReader(self.input_path / self.alternate_names_file)
        self.timezone_names = None

    @classmethod
    def path_for(cls, path):
        return Path(path) if not isinstance(path, Path) else path

    def read_admin_codes(self, input, lang) -> Dict[str, Dict[str, AdminCodeRow]]:
        countries = {}
        with open(self.input_path / input, 'r') as fp:
            reader = csv.reader(fp, delimiter='\t')
            for row in skip_comments(reader):
                admin_row = AdminCodeRow.from_row(row)
                names = self.name_reader.read_names_for(admin_row.id_, lang)
                admin_row.update(names)
                countries[admin_row.country_code] = {} if admin_row.country_code not in countries else countries[admin_row.country_code]
                countries[admin_row.country_code][admin_row.code] = admin_row
        return countries

    def read_country_codes(self, input):
        with open(self.input_path / input, 'r') as fp:
            reader = csv.reader(fp, delimiter='\t')
            codes = []
            for row in skip_comments(reader):
                country = CountryRow.from_row(row)
                codes.append(country.alpha2)
            return sorted(codes) 

    def generate_package(self):
        with open(self.output_path / '__init__.py', 'w'):
            pass

    def generate_countries(self, lang):
        def _generate_continent_indexes(countries: List[CountryRow]):
            last_continent = None
            continent_indexes = []
            for i, country in enumerate(countries):
                if country.continent != last_continent:
                    if last_continent:
                        if len(continent_indexes) > 0:
                            start_ = continent_indexes[-1][2]
                        else:
                            start_ = 0
                        continent_indexes.append((last_continent, start_, i))
                    last_continent = country.continent
            continent_indexes.append((last_continent, continent_indexes[-1][1], len(countries)))
            return continent_indexes

        with open(self.input_path / self.countries_file, 'r') as fp:
            reader = csv.reader(fp, delimiter='\t')
            countries = []
            for row in skip_comments(reader):
                country = CountryRow.from_row(row)
                names = self.name_reader.read_names_for(country.id_, lang)
                country.update(names)
                countries.append(country)
        countries = sorted(countries, key=lambda a: (a.continent, a.name))
        continent_indexes = _generate_continent_indexes(countries)
        folder = self.output_path / lang
        if not folder.exists():
            folder.mkdir()
        with open(folder / f'countries_{lang}.py', 'w') as fp:
            fp.write(country_template(countries, continent_indexes))

    def generate_cities(self, file, lang):
        cities = {}
        timezones = []
        states = self.read_admin_codes(self.states_file, lang)
        districts = self.read_admin_codes(self.districts_file, lang)
        with open(self.input_path / file, 'r') as fp:
            reader = csv.reader(fp, delimiter='\t')
            for row in skip_comments(reader):
                city = CityRow.from_row(row)
                names = self.name_reader.read_names_for(city.id_, lang)
                city.update(names)
                if city.country_code not in cities:
                    cities[city.country_code] = []
                cities[city.country_code].append(city)
                if city.timezone not in timezones:
                    timezones.append(city.timezone)
        self.timezone_names = sorted(timezones)
        
        codes = self.read_country_codes(self.countries_file)
        for code in codes:
            city_list = cities[code] if code in cities else []
            with open(self.output_path / lang / f'{code}_{lang}.py', 'w') as fp:
                fp.write(city_template(city_list,
                                    states[code] if code in states else {},
                                    districts[code] if code in districts else {},
                                    self.timezone_names))


    def generate_values(self, city_file: str, languages: Iterable[str], default_language):
        self.generate_package()
        self.name_reader.ensure_names()
        for lang in languages:
            self.generate_countries(lang)
            self.generate_cities(city_file, lang)
        write_constants(self.output_path / 'constants.py', default_language, languages, self.timezone_names)
