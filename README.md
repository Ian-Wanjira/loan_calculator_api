# Loan Calculator API

## Description
The Loan Calculator API is a backend service for calculating loan payments, interest rates, and other related financial computations. It is primarily built using the DjangoRestFramework and can be easily deployed using Docker.

## Features
- Calculate loan payments based on principal, interest rate, and term.
- Compute amortization schedules.
- Support for multiple loan types (fixed-rate, variable-rate).
- RESTful API endpoints for integration with other applications.

## Technologies Used
- **Python**: Main programming language.
- **Docker**: Containerization for easy deployment.
- **Procfile**: Used for specifying commands that are run by the application.

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/Ian-Wanjira/loan_calculator_api.git
   cd loan_calculator_api

2. **Set up a Virtual Environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt

4. **Make migrations, migrate then run the Application**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.