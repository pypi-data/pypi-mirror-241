import random
from collections import OrderedDict
from datetime import date, timedelta
from typing import List

from faker import Faker
from faker.providers import BaseProvider

from faker_healthcare_system.taxonomy_generator import TaxonomyGenerator


class IndividualProvider(BaseProvider):
    __taxonomy = TaxonomyGenerator()

    def npi(self) -> int:
        return self.generator.random_number(digits=9, fix_len=True)

    def tin(self) -> int:
        return self.generator.random_int(min=100000000, max=999999999)

    def gender(self) -> str:
        return random.choice(["M", "F"])

    def enumeration_date(self) -> date:
        return self.generator.date_between(start_date="-5y", end_date="today")

    def taxonomy(self):
        return self.__taxonomy.get_random_taxonomy().__dict__

    def individual_taxonomies(self, quantity: int) -> List[dict]:
        taxonomies_list = self.__taxonomy.get_taxonomies_individuals(quantity)
        return [tax.__dict__ for tax in taxonomies_list]

    def individual_unique_taxonomies(self, quantity: int):
        return self.__taxonomy.get_uniques_taxonomies_individuals(quantity)

    def person_name_by_gender(self, gender: str) -> dict:
        return {
            'first_name': self.generator.first_name_female() if gender == "F" else self.generator.first_name_male(),
            'last_name': self.generator.last_name_female() if gender == "F" else self.generator.last_name_male(),
            'name_prefix': self.generator.prefix_female() if gender == "F" else self.generator.prefix_male(),
            'name_suffix': self.generator.suffix_female() if gender == "F" else self.generator.suffix_male(),
            'type_name': 'Personal Name',
        }

    def person_married_name(self, person_object: dict) -> dict:
        new_last_name = self.generator.last_name_male()

        new_person_object = {
            'first_name': person_object['first_name'],
            'last_name': new_last_name,
            'name_prefix': person_object['name_prefix'],
            'name_suffix': person_object['name_suffix'],
            'type_name': 'Married',
        }
        return new_person_object

    def address_with_purpose(self, purpose: str = 'Mailing') -> dict:
        address_type = ["DOM", "FGN", "MIL"]
        us_states = [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "Florida",
            "Georgia",
            "Hawái",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Luisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Míchigan",
            "Minnesota",
            "Misisipi",
            "Misuri",
            "Montana",
            "Nebraska",
            "Nevada",
            "Nuevo Hampshire",
            "Nueva Jersey",
            "Nuevo México",
            "Nueva York",
            "Carolina del Norte",
            "Dakota del Norte",
            "Ohio",
            "Oklahoma",
            "Oregón",
            "Pensilvania",
            "Rhode Island",
            "Carolina del Sur",
            "Dakota del Sur",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "Virginia Occidental",
            "Wisconsin",
            "Wyoming",
        ]
        return {
            'country_code': self.generator.current_country_code(),
            'country_name': self.generator.current_country(),
            'purpose': purpose,
            'address_type': random.choice(address_type) if purpose != 'Main Office' else 'Physical',
            'address_1': self.generator.address(),
            'address_2': self.generator.address(),
            'city': self.generator.city(),
            'state': random.choice(us_states),
            'postal_code': self.generator.postcode(),
            'telephone_number': self.generator.phone_number(),
            'fax_number': self.generator.phone_number(),
        }

    def dea(self) -> dict:
        start_date: date = self.generator.date_this_decade()
        return {
            'number': f"{random.choice(['A', 'C', 'M'])}{self.generator.random_int(min=1000000, max=9999999)}",
            'allow_prescribe': self.generator.boolean(),
            'start_date': start_date,
            'expiration_date': start_date + timedelta(365 * self.generator.random_int(min=1, max=4)),
            'supervising_number': f"{random.choice(['X', 'Y'])}{self.generator.random_int(min=1000000, max=9999999)}",
            'supervising_license': self.generator.random_int(min=1000000, max=9999999),
        }

    def professional_degree_school(self) -> str:
        medical_universities_usa = [
            "Harvard University - Harvard Medical School",
            "Stanford University - Stanford School of Medicine",
            "Johns Hopkins University - Johns Hopkins School of Medicine",
            "Yale University - Yale School of Medicine",
            "University of California, San Francisco - UCSF School of Medicine",
            "Columbia University - Vagelos College of Physicians and Surgeons",
            "University of Pennsylvania - Perelman School of Medicine",
            "University of Chicago - Pritzker School of Medicine",
            "Washington University in St. Louis - Washington University School of Medicine",
            "Duke University - Duke University School of Medicine",
            "University of Michigan - Michigan Medicine",
            "Vanderbilt University - Vanderbilt University School of Medicine",
            "University of California, Los Angeles - David Geffen School of Medicine",
            "University of North Carolina at Chapel Hill - UNC School of Medicine",
            "University of Washington - UW School of Medicine",
            "Emory University - Emory University School of Medicine",
            "University of Virginia - UVA School of Medicine",
            "Baylor College of Medicine",
            "Mayo Clinic College of Medicine and Science",
            "University of Texas Southwestern Medical Center - UT Southwestern Medical School",
        ]
        return random.choice(medical_universities_usa)

    def practitioner_language(self) -> dict:
        iso_639_languages = [
            ("Abkhazian", "ab"),
            ("Afar", "aa"),
            ("Afrikaans", "af"),
            ("Akan", "ak"),
            ("Albanian", "sq"),
            ("Amharic", "am"),
            ("Arabic", "ar"),
            ("Aragonese", "an"),
            ("Armenian", "hy"),
            ("Assamese", "as"),
            ("Avaric", "av"),
            ("Avestan", "ae"),
            ("Aymara", "ay"),
            ("Azerbaijani", "az"),
            ("Bambara", "bm"),
            ("Bashkir", "ba"),
            ("Basque", "eu"),
            ("Belarusian", "be"),
            ("Bengali, Bangla", "bn"),
            ("Bihari", "bh"),
            ("Bislama", "bi"),
            ("Bosnian", "bs"),
            ("Breton", "br"),
            ("Bulgarian", "bg"),
            ("Burmese", "my"),
            ("Catalan", "ca"),
            ("Chamorro", "ch"),
            ("Chechen", "ce"),
            ("Chichewa, Chewa, Nyanja", "ny"),
            ("Chinese", "zh"),
            ("Chuvash", "cv"),
            ("Cornish", "kw"),
            ("Corsican", "co"),
            ("Cree", "cr"),
            ("Croatian", "hr"),
            ("Czech", "cs"),
            ("Danish", "da"),
            ("Divehi, Dhivehi, Maldivian", "dv"),
            ("Dutch", "nl"),
            ("Dzongkha", "dz"),
            ("English", "en"),
            ("Esperanto", "eo"),
            ("Estonian", "et"),
            ("Ewe", "ee"),
            ("Faroese", "fo"),
            ("Fijian", "fj"),
            ("Finnish", "fi"),
            ("French", "fr"),
            ("Frisian", "fy"),
            ("Fulah", "ff"),
            ("Galician", "gl"),
            ("Ganda", "lg"),
            ("Georgian", "ka"),
            ("German", "de"),
            ("Greek", "el"),
            ("Guaraní", "gn"),
            ("Gujarati", "gu"),
            ("Haitian, Haitian Creole", "ht"),
            ("Hausa", "ha"),
            ("Hebrew (modern)", "he"),
            ("Herero", "hz"),
            ("Hindi", "hi"),
            ("Hiri Motu", "ho"),
            ("Hungarian", "hu"),
            ("Interlingua", "ia"),
            ("Indonesian", "id"),
            ("Interlingue", "ie"),
            ("Irish", "ga"),
            ("Igbo", "ig"),
            ("Inupiaq", "ik"),
            ("Ido", "io"),
            ("Icelandic", "is"),
            ("Italian", "it"),
            ("Inuktitut", "iu"),
            ("Japanese", "ja"),
            ("Javanese", "jv"),
            ("Kalaallisut, Greenlandic", "kl"),
            ("Kannada", "kn"),
            ("Kanuri", "kr"),
            ("Kashmiri", "ks"),
            ("Kazakh", "kk"),
            ("Khmer", "km"),
            ("Kikuyu, Gikuyu", "ki"),
            ("Kinyarwanda", "rw"),
            ("Kirghiz, Kyrgyz", "ky"),
            ("Komi", "kv"),
            ("Kongo", "kg"),
            ("Korean", "ko"),
            ("Kurdish", "ku"),
            ("Kwanyama, Kuanyama", "kj"),
            ("Latin", "la"),
            ("Luxembourgish, Letzeburgesch", "lb"),
            ("Ganda", "lg"),
            ("Lingala", "ln"),
            ("Lao", "lo"),
            ("Lithuanian", "lt"),
            ("Luba-Katanga", "lu"),
            ("Latvian", "lv"),
            ("Manx", "gv"),
            ("Macedonian", "mk"),
            ("Malagasy", "mg"),
            ("Malay", "ms"),
            ("Malayalam", "ml"),
            ("Maltese", "mt"),
            ("Maori", "mi"),
            ("Marathi (Mara?hi)", "mr"),
            ("Marshallese", "mh"),
            ("Mongolian", "mn"),
            ("Nauru", "na"),
            ("Navajo, Navaho", "nv"),
            ("Norwegian Bokmål", "nb"),
            ("North Ndebele", "nd"),
            ("Nepali", "ne"),
            ("Ndonga", "ng"),
            ("Norwegian Nynorsk", "nn"),
            ("Norwegian", "no"),
            ("Nuosu", "ii"),
            ("South Ndebele", "nr"),
            ("Occitan", "oc"),
            ("Ojibwe, Ojibwa", "oj"),
            ("Old Church Slavonic, Church Slavic, Church Slavonic, Old Bulgarian, Old Slavonic", "cu"),
            ("Oromo", "om"),
            ("Oriya", "or"),
            ("Ossetian, Ossetic", "os"),
            ("Panjabi, Punjabi", "pa"),
            ("Pali", "pi"),
            ("Persian", "fa"),
            ("Polish", "pl"),
            ("Pashto, Pushto", "ps"),
            ("Portuguese", "pt"),
            ("Quechua", "qu"),
            ("Romansh", "rm"),
            ("Kirundi", "rn"),
            ("Russian", "ru"),
            ("Sanskrit", "sa"),
            ("Sardinian", "sc"),
            ("Sindhi", "sd"),
            ("Northern Sami", "se"),
            ("Samoan", "sm"),
            ("Sango", "sg"),
            ("Serbian", "sr"),
            ("Gaelic, Scottish Gaelic", "gd"),
            ("Shona", "sn"),
            ("Sinhalese, Sinhala", "si"),
            ("Slovak", "sk"),
            ("Slovene", "sl"),
            ("Somali", "so"),
            ("Southern Sotho", "st"),
            ("Spanish", "es"),
            ("Sundanese", "su"),
            ("Swahili", "sw"),
            ("Swati", "ss"),
            ("Swedish", "sv"),
            ("Tamil", "ta"),
            ("Telugu", "te"),
            ("Tajik", "tg"),
            ("Thai", "th"),
            ("Tigrinya", "ti"),
            ("Tibetan", "bo"),
            ("Turkmen", "tk"),
            ("Tagalog", "tl"),
            ("Tswana", "tn"),
            ("Tonga (Tonga Islands)", "to"),
            ("Turkish", "tr"),
            ("Tsonga", "ts"),
            ("Tatar", "tt"),
            ("Twi", "tw"),
            ("Tahitian", "ty"),
            ("Uighur, Uyghur", "ug"),
            ("Ukrainian", "uk"),
            ("Urdu", "ur"),
            ("Uzbek", "uz"),
            ("Venda", "ve"),
            ("Vietnamese", "vi"),
            ("Volapük", "vo"),
            ("Walloon", "wa"),
            ("Welsh", "cy"),
            ("Wolof", "wo"),
            ("Western Frisian", "fy"),
            ("Xhosa", "xh"),
            ("Yiddish", "yi"),
            ("Yoruba", "yo"),
            ("Zhuang, Chuang", "za"),
            ("Zulu", "zu")
        ]
        lang: tuple[str, str] = random.choice(iso_639_languages)
        return {
            'code': lang[1].upper(),
            'description': lang[0],
            'language_type': 'Practitioner'
        }

    def practitioner_languages_plus_english(self, quantity: int) -> List[dict]:
        list_languages: List[dict] = []
        english = {'code': 'en', 'description': 'English', 'language_type': 'Practitioner'}
        english_exist: bool = False
        for _ in range(quantity):
            language: dict = self.practitioner_language()
            list_languages.append(language)
            if language['code'] == 'en':
                english_exist = True
        return list_languages if english_exist else list_languages + [english]

    def practitioner_ethnicity_code(self) -> dict:
        ethnicity: dict = {
            "0": "UNKNOWN/NOT DISCLOSED",
            "1": "WHITE (CAUCASIAN)",
            "2": "HISPANIC/LATINO",
            "3": "BLACK (AFRICAN AMERICAN)",
            "4": "ASIAN/PACIFIC ISLANDER",
            "5": "AMERICAN INDIAN/ALASKAN",
            "7": "FILIPINO",
            "A": "AMERASIAN",
            "C": "CHINESE",
            "H": "CAMBODIAN",
            "J": "JAPANESE",
            "K": "KOREAN",
            "M": "SAMOAN",
            "N": "ASIAN INDIAN",
            "P": "HAWAIIAN",
            "R": "GUAMANIAN",
            "T": "LAOTIAN",
            "V": "VIETNAMESE",
            "Z": "OTHER",
        }
        random_key, random_value = random.choice(list(ethnicity.items()))
        return {
            'code': random_key,
            'description': random_value
        }

    def gender_restriction(self) -> str:
        return self.generator.random_element(
            elements=OrderedDict([
                ("F", 0.1),  # Generates "variable_1" 50% of the time
                ("M", 0.1),  # Generates "variable_2" 20% of the time
                ("NR", 0.8),  # Generates "variable_3" 20% of the time
            ]))

    def malpractice(self) -> dict:
        malpractice_insurance = [
            "Admiral Insurance Company",
            "The Doctor's Company",
            "The Doctors Company",
            "HRSA (Federal Torts Claim Act)",
            "NORCAL Mutual Insurance Company",
            "Norcal Mutual Insurance Co",
            "Cooperative of American Physicians",
            "Lancet Indemnity Insurance",
            "Beta Healthcare Group",
            "General Star Indemnity Company",
            "OMIC Ophthalmic Mutual Insurance Company",
            "Cooperative of American Physicians, Inc.",
            "Doctor's Company Insurance Group",
            "Fairway Physicians Ins. Co.",
            "Medical Protective Company",
            "Accord",
            "United States Liability Insurance Company",
            "Hallmark Specialty Insurance Company",
            "COOPERATIVE  OF AMERICAN PHYSICIANS",
            "CAP/MPT",
            "Lancet Indemnity, RRG",
            "CARE Risk Retention Group, INC",
            "Landmark American Insurance Co.",
            "Desert Mountain Insurance Services, Inc.",
            "AMS Risk Retention Group Inc.",
            "AMS Risk Retention Group",
            "AMS Risk Retention Group Inc.",
            "AMS Risk Retention Group Inc.",
            "Superior Malpractice Insurance Services, Inc.",
            "Ophthalmic Mutual Ins Co Rrg",
            "Medical Insurance Exchange of California",
            "Applied Medico-Legal Solutions RRG, Inc.",
            "Preferred Professional Insurance Company",
            "PPIC Insurance",
            "Liberty Insurance Underwriters Inc.",
            "BETA HealthCare Group",
            "American Casualty Company of Reading, PA",
            "NORCAL MUTUAL INSURANCE COMPANY",
            "Mutual Protection Trust",
            "Nurses Service Organization - CNA",
            "Mutual Protection Trust",
            "The Medical Protective Company",
            "MUTUAL PROTECTION TRUST",
            "Steadfast Ins Co",
            "PICA Mutual INS Company",
            "Podiatry Insurance Company of America",
            "PICA Treated Fairly",
            "The Podiatry Insurance Company of America",
            "Mercer Consumer",
        ]
        return {
            'insurance': random.choice(malpractice_insurance),
            'insurance_policy_number': self.generator.random_number(fix_len=True),
            'covered_amount': f" {self.generator.random_int(min=0, max=9)}-{self.generator.random_int(min=0, max=9)}",
        }

    def license(self) -> dict:
        us_states = [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "Florida",
            "Georgia",
            "Hawái",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Luisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Míchigan",
            "Minnesota",
            "Misisipi",
            "Misuri",
            "Montana",
            "Nebraska",
            "Nevada",
            "Nuevo Hampshire",
            "Nueva Jersey",
            "Nuevo México",
            "Nueva York",
            "Carolina del Norte",
            "Dakota del Norte",
            "Ohio",
            "Oklahoma",
            "Oregón",
            "Pensilvania",
            "Rhode Island",
            "Carolina del Sur",
            "Dakota del Sur",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "Virginia Occidental",
            "Wisconsin",
            "Wyoming",
        ]
        start_date: date = self.generator.date_this_decade()
        return {
            'license': f'{self.generator.random_uppercase_letter()}{self.generator.random_number(digits=9)}',
            'state': random.choice(us_states),
            'is_primary': self.generator.boolean(),
            'start_date': start_date,
            'end_date': start_date + timedelta(365 * self.generator.random_int(min=1, max=4)),
        }

    def individual_object(self) -> dict:
        gender = self.gender()
        person_name: dict = self.generator.person_name_by_gender(gender)
        last_updated_epoch: date = self.generator.date_this_decade()
        created_epoch = last_updated_epoch - timedelta(365 * self.generator.random_int(min=1, max=4))
        languages = self.practitioner_languages_plus_english(6)
        credential = random.choice(["DMD", "PhD", "MD", "Dr"])
        sole_proprietor = random.choice(["YES", "NO"])
        ethnicity_code = self.practitioner_ethnicity_code()['code']
        return {
            'npi': self.npi(),
            'tin': self.tin(),
            'last_updated_epoch': last_updated_epoch,
            'created_epoch': created_epoch,
            'enumeration_date': self.enumeration_date(),
            "status": "Active",
            "email": self.generator.email(),
            "enumeration_type": "NPI-1",
            "mailing_address": self.address_with_purpose(),
            "location_address": self.address_with_purpose(purpose='LOCATION'),
            "main_office_address": self.address_with_purpose(purpose='Main Office'),
            "taxonomies": self.individual_unique_taxonomies(4),
            "licenses": [self.license() for _ in range(4)],
            "identifiers": "",
            "taxonomy_qualification": "",
            "taxonomy_endpoints": "",
            "schedule": "",
            'credential': credential,
            'sole_proprietor': sole_proprietor,
            'gender': gender,
            'personal_name': person_name,
            'other_names': '' if gender == 'M' else self.person_married_name(person_name),
            'dea': self.dea(),
            'ethnicity_code': ethnicity_code,
            'date_of_birth': self.generator.date_of_birth(),
            'languages': languages,
            'gender_restriction': self.gender_restriction(),
            'malpractice': self.malpractice(),
            'professional_degree_school': self.professional_degree_school()
        }


fake = Faker()
fake.add_provider(IndividualProvider)
Faker.seed(123)


print(fake.license())

fake_person_names = [fake.individual_object() for _ in range(1)]
for i in fake_person_names:
    print(i)
    print(i['taxonomies'])

