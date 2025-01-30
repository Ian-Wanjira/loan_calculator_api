from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import calculate_loan


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
        loan_term = int(data["loan_term"])
        compound = data["compound"]
        pay_back = data["pay_back"]
    except ValueError:
        return Response(
            {"error": "Invalid data types"}, status=status.HTTP_400_BAD_REQUEST
        )

    result = calculate_loan(loan_amount, interest_rate, loan_term, compound, pay_back)
    return Response(result, status=status.HTTP_200_OK)
