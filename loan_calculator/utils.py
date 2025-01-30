import math


def calculate_loan(principal, rate, term, compound_frequency, payback_frequency):
    """
    Calculate the loan amortization schedule based on different compounding and payback options.
    """
    frequency_map = {
        "Annually (APY)": lambda r, t: principal * (1 + r) ** t,
        "Annually (APR)": lambda r, t: principal * (1 + r / 1) ** (1 * t),
        "Semi-Annually": lambda r, t: principal * (1 + r / 2) ** (2 * t),
        "Quarterly": lambda r, t: principal * (1 + r / 4) ** (4 * t),
        "Monthly (APR)": lambda r, t: principal * (1 + r / 12) ** (12 * t),
        "Monthly (APY)": lambda r, t: principal * (1 + r / 12) ** (12 * t),
        "Semi-Monthly": lambda r, t: principal * (1 + r / 24) ** (24 * t),
        "Biweekly": lambda r, t: principal * (1 + r / 26) ** (26 * t),
        "Weekly": lambda r, t: principal * (1 + r / 52) ** (52 * t),
        "Daily": lambda r, t: principal * (1 + r / 365) ** (365 * t),
        "Continuously": lambda r, t: principal * math.exp(r * t),
    }

    payback_map = {
        "Every Day": 365,
        "Every Week": 52,
        "Every 2 Weeks": 26,
        "Every Half Month": 24,
        "Every Month": 12,
        "Every Quarter": 4,
        "Every Six Months": 2,
        "Every Year": 1,
    }

    # Convert rate to decimal
    rate = rate / 100

    n = frequency_map.get(compound_frequency)
    p = payback_map.get(payback_frequency)

    if n is None:
        amount = frequency_map["Continuously"](rate, term)
    else:
        amount = n(rate, term)

    # Calculate periodic payment using annuity formula
    if p:
        if n is None:
            payment = amount / (term * p)  # Continuous case
        else:
            if rate > 0:
                payment = (principal * (rate / p)) / (1 - (1 + rate / p) ** (-p * term))
            else:
                payment = principal / (term * p)  # No interest case
    else:
        payment = (
            amount / term
        )  # Default to annual if payback frequency is not in the map

    # Generate amortization schedule
    amortization_schedule = {}
    beginning_balance = principal

    for period in range(1, term * p + 1):
        interest_payment = beginning_balance * (rate / p)
        principal_payment = payment - interest_payment
        ending_balance = beginning_balance - principal_payment

        year = (period - 1) // p + 1
        year_label = f"Year {year}"

        if year_label not in amortization_schedule:
            amortization_schedule[year_label] = []

        amortization_schedule[year_label].append(
            {
                "Period": period,
                "Beginning Balance": round(beginning_balance, 2),
                "Interest": round(interest_payment, 2),
                "Principal": round(principal_payment, 2),
                "Ending Balance": max(0, round(ending_balance, 2)),
            }
        )

        beginning_balance = ending_balance

    return {
        "Payment Every Month": round(payment, 2),
        "Total Payments": round(payment * term * p, 2),
        "Total Interest": round((payment * term * p) - principal, 2),
        "Principal Percentage": round(principal / (payment * term * p) * 100),
        "Interest Percentage": round(
            ((payment * term * p) - principal) / (payment * term * p) * 100
        ),
        "Amortization Schedule": amortization_schedule,
    }
