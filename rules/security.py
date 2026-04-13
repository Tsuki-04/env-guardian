def check_app_debug(env_vars):
    results = []

    app_debug = env_vars.get("APP_DEBUG", "").strip().lower()

    if app_debug == "true":
        results.append("[WARNING] APP_DEBUG is enabled. Disable it in production.")

    return results


def check_app_key(env_vars):
    results = []

    if "APP_KEY" not in env_vars:
        results.append("[ERROR] APP_KEY is missing.")
        return results

    app_key = env_vars.get("APP_KEY", "").strip()

    if app_key == "":
        results.append("[ERROR] APP_KEY is empty.")

    return results


def evaluate_password_strength(password):
    score = 0
    issues = []

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    if len(password) >= 8:
        score += 1
    else:
        issues.append("it is shorter than 8 characters")

    if has_lower:
        score += 1
    else:
        issues.append("it has no lowercase letters")

    if has_upper:
        score += 1
    else:
        issues.append("it has no uppercase letters")

    if has_digit:
        score += 1
    else:
        issues.append("it has no numbers")

    if has_symbol:
        score += 1
    else:
        issues.append("it has no symbols")

    if score <= 2:
        level = "weak"
    elif score <= 4:
        level = "medium"
    else:
        level = "strong"

    return {
        "score": score,
        "level": level,
        "issues": issues
    }


def check_db_password(env_vars):
    results = []

    if "DB_PASSWORD" not in env_vars:
        results.append("[ERROR] DB_PASSWORD is missing.")
        return results

    db_password = env_vars.get("DB_PASSWORD", "").strip()

    if db_password == "":
        results.append("[ERROR] DB_PASSWORD is empty.")
        return results

    password_analysis = evaluate_password_strength(db_password)
    level = password_analysis["level"]
    issues = password_analysis["issues"]

    if level == "weak":
        results.append(
            "[WARNING] DB_PASSWORD is weak because " + ", ".join(issues) + "."
        )
    elif level == "medium":
        results.append(
            "[INFO] DB_PASSWORD is medium. Consider improving it."
        )
    elif level == "strong":
        results.append(
            "[INFO] DB_PASSWORD looks strong."
        )

    return results