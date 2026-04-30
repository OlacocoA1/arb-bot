def calculate_stakes(total_stake, odds_a, odds_b):
    """
    Splits stake so profit is equal no matter outcome.
    """

    inverse_sum = (1 / odds_a) + (1 / odds_b)

    if inverse_sum >= 1:
        return None  # no arb possible

    stake_a = total_stake * (1 / odds_a) / inverse_sum
    stake_b = total_stake * (1 / odds_b) / inverse_sum

    return round(stake_a, 2), round(stake_b, 2)
