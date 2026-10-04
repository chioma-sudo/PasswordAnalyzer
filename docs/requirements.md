# Password Security Analyzer — Requirements Specification

## 1. Functional Requirements

Functional requirements describe the specific functions and behaviours that the Password Security Analyzer must provide.

### FR-01: Password Input

The system shall allow a user to enter a password for analysis.

The password shall be entered through a hidden input field so that the password is not visibly displayed while being entered.

### FR-02: Password Length Analysis

The system shall determine whether the password contains at least 8 characters.

### FR-03: Uppercase Character Detection

The system shall determine whether the password contains at least one uppercase letter.

### FR-04: Lowercase Character Detection

The system shall determine whether the password contains at least one lowercase letter.

### FR-05: Number Detection

The system shall determine whether the password contains at least one numerical digit.

### FR-06: Special Character Detection

The system shall determine whether the password contains at least one special character.

### FR-07: Common Password Detection

The system shall compare the password against a collection of commonly used passwords.

The system shall also normalize the password before comparison in order to detect simple variations of common passwords.

For example, a password such as `Password123!` should be recognized as a variation of `password123`.

### FR-08: Password Strength Classification

The system shall calculate a password score based on the password requirements that are satisfied.

The system shall classify the password as:

* **Weak**
* **Moderate**
* **Strong**

A password identified as a common password shall be classified as **Weak**, regardless of its complexity score.

### FR-09: Security Feedback

The system shall provide feedback indicating which password security requirements have been satisfied and which requirements have not been satisfied.

### FR-10: Risk Indicators

The system shall identify failed security requirements and display them as risk indicators.

Common passwords shall also be identified as a security risk.

### FR-11: Security Recommendation

The system shall provide a recommendation based on the identified password weaknesses.

Recommendations shall encourage users to improve weak or potentially vulnerable passwords.

### FR-12: Password Hashing

The system shall support secure password hashing using the `scrypt` key-derivation function.

The system shall generate a unique cryptographically secure random salt for each password.

### FR-13: Password Verification

The system shall be able to verify a password by deriving a hash using the stored salt and comparing the resulting hash with the stored password hash.

The original plaintext password shall not be required for verification.

### FR-14: Automated Testing

The system shall include automated tests for its core password-analysis and password-security functions.

The test suite shall verify both successful and unsuccessful cases where appropriate.

## 2. Non-Functional Requirements

Non-functional requirements define the quality attributes and operational expectations of the Password Security Analyzer.

### NFR-01: Security

The system shall avoid displaying plaintext passwords during input.

The system shall use a cryptographically secure random salt when generating password hashes.

Password hashing shall use a password-focused key-derivation function rather than a fast general-purpose hashing algorithm.

### NFR-02: Privacy

The system shall not display or expose the user's plaintext password as part of the analysis results.

The system shall not require users to provide passwords belonging to real accounts.

### NFR-03: Usability

The system shall provide clear and understandable feedback to users.

Security weaknesses shall be presented in a format that allows users to understand how their passwords can be improved.

### NFR-04: Performance

The password analysis functions shall execute efficiently for normal user input.

Password hashing may intentionally require additional computational resources because password-focused key-derivation functions are designed to make brute-force attacks more difficult.

### NFR-05: Reliability

The system shall produce consistent analysis results for the same password and configuration.

Password verification shall correctly distinguish between valid and invalid passwords.

### NFR-06: Maintainability

The system shall use modular functions to separate password analysis, normalization, common-password detection, hashing, verification, and strength classification.

The code shall be structured so that individual components can be modified or tested without unnecessarily affecting other components.

### NFR-07: Testability

Core functionality shall be independently testable.

The project shall maintain an automated test suite to identify regressions when changes are made to the system.

### NFR-08: Extensibility

The system shall be designed so that additional password-analysis rules, larger password datasets, and new user-interface components can be added in future versions.

The architecture shall support future development of a web-based interface.

### NFR-09: Documentation

The project shall maintain documentation describing its purpose, requirements, risks, system design, implementation, and testing.

### NFR-10: Portability

The command-line version shall run on systems with a compatible Python 3 installation and the required standard-library modules.

## 3. User Requirements

The user should be able to:

* Enter a password without having it visibly displayed.
* Receive a password strength assessment.
* Understand which password requirements have been satisfied.
* Identify weaknesses in the password.
* Know whether the password resembles a commonly used password.
* Receive recommendations for improving password security.
* Understand the security risks associated with the password.
* Use the system without needing advanced cybersecurity knowledge.

## 4. System Requirements

### 4.1 Software Requirements

The system requires:

* Python 3.x
* Python standard library modules:

  * `getpass`
  * `hashlib`
  * `secrets`
  * `unittest`

No external Python packages are required for the current command-line version.

### 4.2 Hardware Requirements

The current version has minimal hardware requirements and can run on a standard computer capable of running Python 3.

Recommended minimum requirements include:

* Modern desktop or laptop computer
* At least 2 GB of available RAM
* Sufficient storage for the application and project files
* Keyboard for password input

### 4.3 Operating System

The application is intended to support operating systems capable of running Python 3, including:

* Windows
* macOS
* Linux

### 4.4 Development Environment

The project can be developed using:

* Visual Studio Code or another Python-compatible IDE
* Command-line terminal
* Git for version control
* GitHub for source-code hosting and project documentation

## 5. Requirements Traceability

The project will maintain a relationship between requirements, implementation, and testing.

For example:

| Requirement                        | Implementation            | Testing                                    |
| ---------------------------------- | ------------------------- | ------------------------------------------ |
| FR-02: Password Length Analysis    | `check_length()`          | `test_check_length()`                      |
| FR-03: Uppercase Detection         | `check_uppercase()`       | `test_check_uppercase()`                   |
| FR-04: Lowercase Detection         | `check_lowercase()`       | `test_check_lowercase()`                   |
| FR-05: Number Detection            | `check_number()`          | `test_check_number()`                      |
| FR-06: Special Character Detection | `check_special()`         | `test_check_special()`                     |
| FR-07: Common Password Detection   | `check_common_password()` | `test_check_common_password()`             |
| FR-08: Strength Classification     | `get_strength()`          | `test_get_strength()`                      |
| FR-12: Password Hashing            | `hash_password()`         | `test_password_hashing_and_verification()` |
| FR-13: Password Verification       | `verify_password()`       | `test_password_verification_edge_cases()`  |

This traceability helps ensure that important requirements are implemented and verified through testing.
