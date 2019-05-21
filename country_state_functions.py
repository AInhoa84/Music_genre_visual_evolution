#!/usr/bin/env python3

import re
import pandas as pd
import pycountry as co

extra_country_names= {
    "UK": "United Kingdom",
    "England": "United Kingdom",
    "Scotland": "United Kingdom",
    "Wales": "United Kingdom",
    "Great Britain": "United Kingdom",
    "U.S": "United States", # Also matches "U.S."
    "US": "United States", # Also matches "USA"
}
def get_country(text):
    """ Return a list of possible countries found in the string provided."""
    result = []
    for country in co.countries:
        if country.name in text:
            result.append(country.name)
        elif "official_name" in country.__dict__["_fields"] and country.official_name in text:
            result.append(country.name)
        elif "common_name" in country.__dict__["_fields"] and country.common_name in text:
            result.append(country.name)

    # US and UK are known not to be always written as they should
    # Try to find them if no result so far
    if len(result) == 0:
        for extra in extra_country_names:
            if extra in text:
                result.append(extra_country_names[extra])

    return result


def get_us_state(text):
    """ Get US state based on a predefined list. """
    states_df = pd.read_csv("USA_states.csv", sep='\t', header=0)

    for i in states_df["subdivision"]:
        if i in text:
            return i

    return ""


def get_city(text):
    """ Get a name which is at least 3 letters long """
    matches = re.search(r"[a-zA-Z- .]{3,}", text)

    if matches:
        ret = matches.group()
    else:
        ret = None

    return ret



def remove_refs(text):
    """ Remove any tag in the form "<ref***>***</refs>". """
    return re.sub("<ref[^>]*>[^<]*<\/ref>", "", text)


def get_country_state_city(text):
    """ Return a list of the form [city, state, [list of countries]]. """
    s = remove_refs(text).split(",")
    city = " "
    state = " "
    country = get_country(s[-1])

    if country == ["United States"]:
        state = get_us_state(i)

    if len(country) == 0:
        state = get_us_state(s[-1])
        if state != "":
            country = ["United States"]


    # If we've got the country, try to find the city
    # Check if we've a country and
    if (len(country) == 1) and (len(i) >1):
        city = get_city(s[0])

    return [city, state, country]



if __name__ == "__main__":
    df = pd.read_csv("Chunks_completed/chunk1.csv", sep='\t', header=0, encoding='utf-8')
    #count_countries(df)
    for i in df["birth_place"]:
        if type(i) == type(str()):
           print(get_country_state_city(i))
