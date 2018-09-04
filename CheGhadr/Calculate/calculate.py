"""Only calculate how much you must work to earn the product!"""

def calculate(wage, price):
    """calculate how much you must work"""
    result = dict()
    daily_wage = wage / 20
    hourly_wage = daily_wage / 8
    # add to dictionary
    result['day'], result['hour'] = (price / daily_wage), (price / hourly_wage)

    return result