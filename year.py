def next_year(year=1987):
    print("fin de l'année {}".format(year))
    year += 1
    print("début de l'année {}".format(year))
    return year

year = 2018

next_year()
year = next_year(year)