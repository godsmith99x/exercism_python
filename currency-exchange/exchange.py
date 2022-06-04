def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    exchange_amt = budget / exchange_rate

    return exchange_amt


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    remaining = budget - exchanging_value

    return remaining


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    val = denomination * number_of_bills

    return val


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    num_of_bills = budget // denomination

    return num_of_bills


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    spread_percent = spread / 100

    effective_ex_rate = exchange_rate + (exchange_rate * spread_percent)

    ex_val_full = budget / effective_ex_rate

    num_of_bills = ex_val_full // denomination

    ex_val_final = num_of_bills * denomination

    return ex_val_final



def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """

    spread_percent = spread / 100

    effective_ex_rate = exchange_rate + (exchange_rate * spread_percent)

    ex_val_full_round_down = budget // effective_ex_rate

    ex_val = exchangeable_value(budget, exchange_rate, spread, denomination)

    non_ex_val = ex_val_full_round_down - ex_val

    return non_ex_val

