import re

def check_password(password):

    score = 0
    suggestions = []

    # Length
    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Password should contain at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 20
    else:
        suggestions.append("Add at least one number.")

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        suggestions.append("Add at least one special character.")

    return score, suggestions