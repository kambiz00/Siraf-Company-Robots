# This function calculates the percentage of company shares owned by a stay-at-home mom (sahm) based on the number of transactions
# she has made on the company's stock (tedad_tarakonesh)
def sahm_ECD_darsad(tedad_tarakonesh):
    if tedad_tarakonesh <= 100:
        return 0.9  # if the number of transactions is less than or equal to 100, the sahm owns 90% of the company's shares
    else:
        if tedad_tarakonesh <= 250:
            return 0.5  # if the number of transactions is between 101 and 250 (inclusive), the sahm owns 50% of the company's shares
        else:
            return 0.2  # if the number of transactions is greater than 250, the sahm owns 20% of the company's shares


# This function calculates the percentage of company shares owned by a company (sherkat) based on the number of shares purchased (tedad_kharid)
def sahm_sherkat_darsad(tedad_kharid):
    if tedad_kharid <= 100:
        return 0  # if the number of shares purchased is less than or equal to 100, the company does not own any shares
    else:
        if tedad_kharid <= 250:
            return 0.4  # if the number of shares purchased is between 101 and 250 (inclusive), the company owns 40% of the company's shares
        else:
            if tedad_kharid <= 500:
                return 0.6  # if the number of shares purchased is between 251 and 500 (inclusive), the company owns 60% of the company's shares
            else:
                return 0.75  # if the number of shares purchased is greater than 500, the company owns 75% of the company's shares


# This function returns a value (vres) based on the number of transactions made on the company's stock (tedad_tarakonesh)
def vres(tedad_tarakonesh):
    if tedad_tarakonesh == 0:
        return 1
    elif tedad_tarakonesh in range(1, 11):
        return 2
    elif tedad_tarakonesh in range(11, 21):
        return 3
    elif tedad_tarakonesh in range(21, 31):
        return 4
    elif tedad_tarakonesh in range(31, 61):
        return 5
    elif tedad_tarakonesh in range(61, 81):
        return 6
    elif tedad_tarakonesh in range(81, 101):
        return 7
    elif tedad_tarakonesh in range(101, 151):
        return 8
    elif tedad_tarakonesh in range(151, 226):
        return 9
    elif tedad_tarakonesh in range(226, 331):
        return 10
    elif tedad_tarakonesh in range(331, 501):
        return 11
    elif tedad_tarakonesh in range(501, 751):
        return 12
    elif tedad_tarakonesh in range(751, 1101):
        return 13
    elif tedad_tarakonesh in range(1101, 100001):
        return 14
