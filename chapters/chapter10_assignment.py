def get_country_codes(prices):
    pl=list(prices)
    country_codes = ""
    for i in pl:
        if i.isalpha() or i in [',',' ']:
            country_codes += i
    return country_codes

def get_country_codes_alt(prices):
    glue = ', '
    prices_list = prices.split(glue)
    temp_list = []
    for i in prices_list:
        temp_list += i.split('$')
    country_list = []
    for i in temp_list:
        if i.isalpha():
            country_list.append(i)
    return glue.join(country_list)