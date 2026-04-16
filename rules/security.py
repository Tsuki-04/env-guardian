from src import messages


def check_app_debug(env_vars, strict_mode=False):
    results = []

    app_debug = env_vars.get("APP_DEBUG", "").strip().lower()

    if app_debug == "true":
        results.append(messages.app_debug_enabled(strict_mode=strict_mode))

    return results


def check_app_key(env_vars):
    results = []

    if "APP_KEY" not in env_vars:
        results.append(messages.app_key_missing())
        return results

    app_key = env_vars.get("APP_KEY", "").strip()

    if app_key == "":
        results.append(messages.app_key_empty())

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


def check_db_password(env_vars, strict_mode=False):
    results = []

    if "DB_PASSWORD" not in env_vars:
        results.append(messages.db_password_missing())
        return results

    db_password = env_vars.get("DB_PASSWORD", "").strip()

    if db_password == "":
        results.append(messages.db_password_empty())
        return results

    password_analysis = evaluate_password_strength(db_password)
    level = password_analysis["level"]
    issues = password_analysis["issues"]

    if level == "weak":
        results.append(messages.db_password_weak(issues, strict_mode=strict_mode))
    elif level == "medium":
        results.append(messages.db_password_medium(strict_mode=strict_mode))
    elif level == "strong":
        results.append(messages.db_password_strong())

    return results


def check_sensitive_variables(env_vars):
    results = []

    sensitive_keywords = ["SECRET", "TOKEN", "API_KEY", "PASSWORD"]
    weak_values = ["1234", "123456", "password", "admin", "test", "changeme"]
    excluded_variables = ["DB_PASSWORD"]

    for key, value in env_vars.items():
        key_upper = key.upper()
        value_clean = value.strip()

        if key_upper in excluded_variables:
            continue

        is_sensitive = any(keyword in key_upper for keyword in sensitive_keywords)

        if not is_sensitive:
            continue

        if value_clean == "":
            results.append(messages.sensitive_variable_empty(key))
            continue

        if value_clean.lower() in weak_values:
            results.append(messages.sensitive_variable_weak(key))

    return results