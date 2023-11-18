from enum import Enum

# TODO Add all those values http://www.lingoes.net/en/translator/langcode.htm
# TODO We should split between LangCodes which is all lang codes and LangCode which is the Type/Class of one lang code
# TODO We need those values in array or other data structure so we can present all lang code in menu, so we can link them to country_id, so we can sort by langauge, sort by country ...
class LangCode(Enum):

    HEBREW = 'he'
    HEBREW_ISRAEL = 'he-IL'
    ENGLISH = 'en'
    ENGLISH_United_Kingdom = 'en-GB'
    ENGLISH_United_States = 'en-US'

