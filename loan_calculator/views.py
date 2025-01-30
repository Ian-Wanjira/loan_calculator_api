from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import calculate_loan
import re


@api_view(["POST"])
def loan_calculator(request):
    """
    API endpoint to calculate loan payments.
    """
    data = request.data
    required_fields = [
        "loan_amount",
        "interest_rate",
        "loan_term",
        "compound",
        "pay_back",
    ]

    if not all(field in data for field in required_fields):
        return Response(
            {"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        loan_amount = float(data["loan_amount"])
        interest_rate = float(data["interest_rate"])
        compound = data["compound"]
        pay_back = data["pay_back"]

        # Parse loan term which can be in years, months, or both
        loan_term_str = data["loan_term"]
        years, months = 0, 0

        if isinstance(loan_term_str, str):
            match = re.match(
                r"^(?:(\d+) years?)?\s*(?:(\d+) months?)?$",
                loan_term_str,
                re.IGNORECASE,
            )
            if match:
                if match.group(1):
                    years = int(match.group(1))
                if match.group(2):
                    months = int(match.group(2))
            else:
                return Response(
                    {"error": "Invalid loan term format"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif isinstance(loan_term_str, dict):
            years = loan_term_str.get("years", 0)
            months = loan_term_str.get("months", 0)

        if not years and not months:
            return Response(
                {"error": "Loan term must be specified in years, months, or both"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        loan_term = years + months / 12  # Convert everything to years

    except ValueError:
        return Response(
            {"error": "Invalid data types"}, status=status.HTTP_400_BAD_REQUEST
        )

    result = calculate_loan(loan_amount, interest_rate, loan_term, compound, pay_back)
    return Response(result, status=status.HTTP_200_OK)
