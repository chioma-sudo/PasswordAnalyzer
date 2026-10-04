# Password Security Analyzer — System Design

## 1. Introduction

This document describes the design and structure of the Password Security Analyzer.

The system is designed as a modular cybersecurity application in which individual components are responsible for password analysis, common-password detection, security assessment, password hashing, and password verification.

The initial implementation operates through a command-line interface. The architecture is designed to support future development of a web-based application using Flask, HTML, CSS, and JavaScript.

## 2. System Overview

The Password Security Analyzer accepts a password from the user and performs a series of security checks.

The system:

1. Accepts a password through hidden input.
2. Normalizes the password for common-password detection.
3. Checks the password against common-password patterns.
4. Evaluates password length and character requirements.
5. Calculates a complexity score.
6. Determines the password strength.
7. Identifies security risks.
8. Generates security recommendations.
9. Provides feedback to the user.

The system also contains password-security functions that demonstrate salted password hashing and password verification using `scrypt`.

## 3. System Components

The current system consists of the following major components.

### 3.1 User Input Component

Responsible for accepting the password from the user.

The command-line version uses Python's `getpass` module so that the password is not displayed while being entered.

### 3.2 Password Normalization Component

Responsible for converting the password into a normalized form before common-password comparison.

Normalization currently includes:

* Converting characters to lowercase.
* Removing selected special characters.

This allows the system to identify simple variations of common passwords.

For example:

`Password123!`

can be normalized to:

`password123`

### 3.3 Password Analysis Component

The analysis component evaluates the password against several requirements:

* Minimum length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Each requirement returns a Boolean result indicating whether the requirement has been satisfied.

### 3.4 Common Password Detection Component

This component compares the normalized password against a local collection of commonly used passwords.

If a match is detected, the password is considered a security risk and is classified as **Weak**, regardless of its complexity score.

### 3.5 Strength Classification Component

The strength classification component uses the password's complexity score and common-password status to determine whether the password is:

* Weak
* Moderate
* Strong

### 3.6 Risk Assessment Component

This component identifies weaknesses in the password.

Failed security requirements are converted into risk indicators so that users can clearly see potential weaknesses.

A common password is also reported as a security risk.

### 3.7 Recommendation Component

The recommendation component generates guidance based on the password's security assessment.

Recommendations encourage users to address identified weaknesses and avoid commonly used passwords.

### 3.8 Password Hashing Component

The hashing component demonstrates secure password handling using:

* A cryptographically secure random salt generated with `secrets`.
* The `scrypt` key-derivation function provided by Python's `hashlib`.

The original plaintext password is not returned as part of the hashing process.

### 3.9 Password Verification Component

The verification component accepts a password, salt, and previously generated password hash.

It derives a new hash using the same salt and compares it with the stored hash.

The password is considered valid only when the derived hash matches the stored hash.

## 4. System Architecture

The current command-line system follows a modular architecture.

```text
                    ┌──────────────────────┐
                    │        User          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Password Input    │
                    │      (getpass)       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Password Analysis   │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
        ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
        │ Complexity  │ │   Common    │ │ Normalization│
        │   Checks    │ │  Password   │ │   Component  │
        └──────┬──────┘ │  Detection  │ └──────────────┘
               │        └──────┬──────┘
               └────────┬──────┘
                        ▼
              ┌─────────────────────┐
              │ Strength & Risk     │
              │    Assessment       │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Feedback &          │
              │ Recommendation      │
              └─────────────────────┘


        Separate Security Functions
        ────────────────────────────

        Password
            │
            ▼
      ┌───────────────┐
      │   scrypt +    │
      │  Random Salt  │
      └───────┬───────┘
              │
              ▼
       Salt + Password Hash
              │
              ▼
      Password Verification
```

The hashing and verification functions are implemented as reusable security functions and are separate from the password-strength analysis workflow.

## 5. Data Flow

The primary analysis flow is:

```text
User enters password
        │
        ▼
Hidden password input
        │
        ▼
Normalize password
        │
        ▼
Check common-password list
        │
        ▼
Perform complexity checks
        │
        ▼
Calculate score
        │
        ▼
Determine strength
        │
        ▼
Identify risks
        │
        ▼
Generate recommendation
        │
        ▼
Display security report
```

The password itself is not displayed as part of the final analysis report.

## 6. Core Functions

The current implementation contains the following major functions:

| Function                  | Responsibility                            |
| ------------------------- | ----------------------------------------- |
| `check_length()`          | Checks minimum password length            |
| `check_uppercase()`       | Detects uppercase characters              |
| `check_lowercase()`       | Detects lowercase characters              |
| `check_number()`          | Detects numerical digits                  |
| `check_special()`         | Detects special characters                |
| `normalize_password()`    | Normalizes passwords before comparison    |
| `check_common_password()` | Detects common-password patterns          |
| `get_strength()`          | Determines password strength              |
| `hash_password()`         | Generates a salted `scrypt` password hash |
| `verify_password()`       | Verifies a password against a stored hash |

## 7. Security Design

Security is considered throughout the system design.

The system uses hidden password input to reduce accidental exposure of plaintext passwords.

Common-password detection is performed before the final strength classification so that a password that is highly complex but based on a common pattern can still be identified as weak.

Password hashing uses a unique random salt and `scrypt`, a password-focused key-derivation function.

The current implementation is educational and is not intended to serve as a complete production authentication system.

## 8. Future Web Architecture

The planned web version will extend the current architecture.

The future architecture is expected to contain:

                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ HTML/CSS/JS   │
                    │   Frontend    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Flask Backend │
                    └───────┬───────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
      ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
      │  Password   │ │    Risk     │ │  Security   │
      │   Analysis  │ │ Assessment  │ │   Functions │
      └─────────────┘ └─────────────┘ └─────────────┘
```

The web version will allow the existing analysis logic to be presented through a user-friendly graphical interface.

Additional security controls will be considered during web development, including input validation, secure handling of sensitive data, secure error handling, and protection against common web application vulnerabilities.

## 9. Design Principles

The project follows several software-engineering principles:

### Modularity

Different responsibilities are separated into independent functions.

### Separation of Responsibilities

Password analysis, normalization, risk assessment, and password hashing are handled by separate components.

### Reusability

Core functions can be imported and tested independently.

### Testability

Core functionality is covered by automated unit tests.

### Extensibility

The current design allows additional analysis rules, larger password datasets, and a web interface to be added later.

### Security by Design

Password privacy and secure password handling are considered during system development rather than being treated as an afterthought.

## 10. Design Constraints

The current design has several constraints:

* The common-password dataset is limited.
* The command-line interface provides limited visual feedback.
* The application does not currently use a database.
