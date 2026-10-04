from getpass import getpass
import hashlib
import secrets
from difflib import SequenceMatcher


def hash_password(password):
    salt = secrets.token_bytes(16)
    password_bytes = password.encode()

    password_hash = hashlib.scrypt(
        password_bytes,
        salt=salt,
        n=2**14,
        r=8,
        p=1
    )

    return salt, password_hash


def verify_password(password, salt, stored_hash):
    password_bytes = password.encode()

    password_hash = hashlib.scrypt(
        password_bytes,
        salt=salt,
        n=2**14,
        r=8,
        p=1
    )

    return secrets.compare_digest(password_hash, stored_hash)


def check_length(password):
    return len(password) >= 8


def check_uppercase(password):
    return any(char.isupper() for char in password)


def check_lowercase(password):
    return any(char.islower() for char in password)


def check_number(password):
    return any(char.isdigit() for char in password)


def check_special(password):
    return any(not char.isalnum() for char in password)


def normalize_password(password):
    normalized_password = password.lower()

    return "".join(
        char for char in normalized_password
        if char.isalnum()
    )


def normalize_common_variation(password):
    normalized_password = password.lower()

    substitutions = {
        "@": "a",
        "0": "o",
        "1": "i",
        "2": "z",
        "3": "e",
        "4": "a",
        "5": "s",
        "7": "t"
    }

    for old, new in substitutions.items():
        normalized_password = normalized_password.replace(old, new)

    return "".join(
        char for char in normalized_password
        if char.isalnum()
    )


def is_common_variation(password, common_password):
    normalized_password = normalize_common_variation(password)
    normalized_common = normalize_common_variation(common_password)

    if normalized_password == normalized_common:
        return True

    similarity = SequenceMatcher(
        None,
        normalized_password,
        normalized_common
    ).ratio()

    return similarity >= 0.8


def load_common_passwords():
    with open("data/common_passwords.txt", "r") as file:
        return [line.strip() for line in file if line.strip()]


def check_common_password(password, common_passwords):
    normalized_password = normalize_password(password)

    for common_password in common_passwords:
        normalized_common = normalize_password(common_password)

        if normalized_password == normalized_common:
            return True

        if is_common_variation(password, common_password):
            return True

    return False


def get_strength(password, is_common):
    if is_common:
        return "Weak"

    if check_repetition(password):
        return "Weak"

    if len(password) < 8:
        return "Weak"

    checks_passed = sum([
        check_uppercase(password),
        check_lowercase(password),
        check_number(password),
        check_special(password)
    ])

    if len(password) >= 14 and checks_passed == 4:
        return "Strong"

    if checks_passed >= 2:
        return "Moderate"

    return "Weak"

    if len(password) >= 14 and checks_passed == 4:
        return "Strong"

    if checks_passed >= 2:
        return "Moderate"

    return "Weak"

def analyze_password(password, common_passwords):
    feedback = []
    risk_indicators = []

    is_common = check_common_password(
        password,
        common_passwords
    )

    if is_common:
        feedback.append(
            "✗ Password is a common password. Consider changing it."
        )
        risk_indicators.append("⚠ Common password")
    else:
        feedback.append("✓ Password is not a common password")

    if check_repetition(password):
        feedback.append(
            "✗ Password contains repeated characters or patterns"
        )
        risk_indicators.append(
            "⚠ Repeated characters or patterns"
        )
    else:
        feedback.append(
            "✓ Password does not contain obvious repeated patterns"
        )

    checks = [
        (
            check_length(password),
            "✓ Password is at least 8 characters long",
            "✗ Password should be at least 8 characters long"
        ),
        (
            check_uppercase(password),
            "✓ Contains uppercase letters",
            "✗ Add at least one uppercase letter"
        ),
        (
            check_lowercase(password),
            "✓ Contains lowercase letters",
            "✗ Add at least one lowercase letter"
        ),
        (
            check_number(password),
            "✓ Contains numbers",
            "✗ Add at least one number"
        ),
        (
            check_special(password),
            "✓ Contains special characters",
            "✗ Add at least one special character"
        )
    ]

    for passed, success_message, failure_message in checks:
        if passed:
            feedback.append(success_message)
        else:
            feedback.append(failure_message)
            risk_indicators.append(
                failure_message.replace("✗", "⚠")
            )

    strength = get_strength(password, is_common)

    if is_common:
        recommendation = (
            "Change this password. It is based on a commonly used password."
        )
    elif strength == "Weak":
        recommendation = (
            "Use a longer password and include a mix of uppercase, lowercase, "
            "numbers, and special characters."
        )
    elif strength == "Moderate":
        recommendation = (
            "Your password is reasonable, but adding more characters and "
            "complexity would make it stronger."
        )
    else:
        recommendation = (
            "Your password has strong length and complexity and was not found "
            "in the common-password dataset."
        )

    

    return {
        "strength": strength,
        "recommendation": recommendation,
        "risk_indicators": risk_indicators,
        "feedback": feedback,
        "is_common": is_common
    }

def check_repetition(password):
    if len(password) < 4:
        return False

    half = len(password) // 2

    if password[:half] == password[half:half * 2]:
        return True

    return len(set(password)) == 1


def main():
    print("================================")
    print("     PASSWORD SECURITY ANALYZER")
    print("================================")
    print("\nEnter your password below.")
    password = getpass("Password: ")

    common_passwords = load_common_passwords()

    results = analyze_password(
        password,
        common_passwords
    )

    print("\nPASSWORD ANALYSIS")
    print("------------------")

    print(f"Strength: {results['strength']}")

    print("\nRecommendation:")
    print(results["recommendation"])

    print("\nRisk Indicators:")

    if results["risk_indicators"]:
        for risk in results["risk_indicators"]:
            print(risk)
    else:
        print("✓ No significant risk indicators found")

    print("\nFeedback:")
    for item in results["feedback"]:
        print(item)

    print("\nThank you for using Password Security Analyzer.")


if __name__ == "__main__":
    main()