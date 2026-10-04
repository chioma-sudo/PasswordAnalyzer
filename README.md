# Password Security Analyzer

A Python-based cybersecurity tool that analyzes password strength, identifies common and easily guessable passwords, provides security recommendations, and demonstrates secure password hashing and verification.

## Features

* Password strength analysis based on length and character requirements
* Detection of common and easily guessable passwords
* Password normalization to identify common passwords with simple variations
* Security feedback and recommendations
* Risk indicator reporting
* Secure password hashing using `scrypt` with a unique salt
* Password verification
* Automated unit testing with Python's `unittest` framework

## Security Concepts Demonstrated

This project demonstrates several foundational cybersecurity concepts:

* **Password strength assessment** — evaluating passwords against basic complexity requirements.
* **Common password detection** — identifying passwords that are commonly used or easily guessed.
* **Password normalization** — detecting simple variations of common passwords, such as adding special characters or changing letter case.
* **Salted password hashing** — using a unique random salt when hashing passwords.
* **Key derivation** — using Python's `hashlib.scrypt()` for password hashing.
* **Password verification** — verifying a password against a previously generated salt and hash without storing the original password.
* **Risk assessment** — identifying weaknesses and presenting them as risk indicators.
* **Automated security testing** — using unit tests to verify that security-related functions behave as expected.

## Technologies Used

* **Python 3**
* `hashlib` — password hashing with `scrypt`
* `secrets` — cryptographically secure random salt generation
* `getpass` — hidden password input in the terminal
* `unittest` — automated testing

## Project Structure

```text
Password Security Analyzer/
│
├── main.py              # Main password analyzer
├── test_analyzer.py     # Automated unit tests
└── README.md            # Project documentation
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate into the project folder

```bash
cd password-security-analyzer
```

### 3. Run the password analyzer

```bash
python main.py
```

The program will prompt you to enter a password. Your input will be hidden while typing.

### 4. Run the automated tests

```bash
python -m unittest test_analyzer.py
```

All tests should pass before making changes to the project.

cd password-security-analyzer

## Example Output

```text
Password Security Analyzer
==========================

Enter a password to analyze:

PASSWORD ANALYSIS
------------------
Score: 4/5
Strength: Moderate
Recommendation: Your password has reasonable complexity, but it can still be improved.

Risk Indicators:
⚠ Add at least one special character

Feedback:
✓ Password is at least 8 characters long
✓ Contains uppercase letters
✓ Contains lowercase letters
✓ Contains numbers
✗ Add at least one special character
```

For a password identified as common, the analyzer overrides the complexity score and classifies it as **Weak**.

```text
Score: 5/5
Strength: Weak

Risk Indicators:
⚠ Common password
```

## Testing

The project includes automated unit tests using Python's built-in `unittest` framework.

The test suite covers:

* Password length validation
* Uppercase letter detection
* Lowercase letter detection
* Number detection
* Special character detection
* Password normalization
* Common password detection
* Password strength classification
* Password hashing and verification
* Salt uniqueness and incorrect-password rejection

Run the tests with:

```bash
python -m unittest test_analyzer.py
```

The current test suite contains **10 automated tests**, all of which pass successfully.

## Limitations

This project is designed as an educational cybersecurity project and currently has some limitations:

* The common-password list is limited and stored locally.
* Password strength is evaluated using basic complexity rules rather than advanced password-strength estimation.
* The current version runs through a command-line interface.
* The application does not connect to a production database.
* The password hashing implementation is intended for demonstration and learning rather than direct production deployment.

## Future Improvements

Planned improvements include:

* Expand the common-password database.
* Implement more advanced password-strength analysis.
* Develop a web interface using Flask.
* Build a responsive frontend using HTML, CSS, and JavaScript.
* Add visual security indicators and password-strength meters.
* Improve security reporting and risk classification.
* Add more comprehensive security and integration testing.
* Deploy the application as a web-based cybersecurity tool.
* Update the system documentation and architecture diagrams as the application evolves.

