def check_arb(o1, o2):
    inv = (1/o1) + (1/o2)

    if inv < 1:
        return True, round((1 - inv) * 100, 2)

    return False, 0


def calc_stake(total, o1, o2):
    inv = (1/o1) + (1/o2)

    s1 = total * (1/o1) / inv
    s2 = total * (1/o2) / inv

    return round(s1), round(s2)
