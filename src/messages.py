def app_debug_enabled(strict_mode=False):
    if strict_mode:
        return "[ERROR] APP_DEBUG is enabled. Disable it for production."
    return "[WARNING] APP_DEBUG is enabled. Disable it in production."


def app_key_missing():
    return "[ERROR] APP_KEY is missing."


def app_key_empty():
    return "[ERROR] APP_KEY is empty."


def db_password_missing():
    return "[ERROR] DB_PASSWORD is missing."


def db_password_empty():
    return "[ERROR] DB_PASSWORD is empty."


def db_password_weak(issues, strict_mode=False):
    joined_issues = ", ".join(issues)
    if strict_mode:
        return f"[ERROR] DB_PASSWORD is weak because {joined_issues}."
    return f"[WARNING] DB_PASSWORD is weak because {joined_issues}."


def db_password_medium(strict_mode=False):
    if strict_mode:
        return "[WARNING] DB_PASSWORD is medium. Use a stronger password for production."
    return "[INFO] DB_PASSWORD is medium. Consider improving it."


def db_password_strong():
    return "[INFO] DB_PASSWORD looks strong."


def sensitive_variable_empty(key):
    return f"[ERROR] Sensitive variable {key} is empty."


def sensitive_variable_weak(key):
    return f"[WARNING] Sensitive variable {key} uses a suspiciously weak value."


def missing_env_variable(key, strict_mode=False):
    if strict_mode:
        return f"[ERROR] Missing variable in .env: {key}"
    return f"[WARNING] Missing variable in .env: {key}"


def undocumented_env_variable(key):
    return f"[INFO] Undocumented variable in .env: {key}"


def required_env_file_not_found(file_path):
    return f"[ERROR] Required .env file not found: {file_path}"


def optional_reference_not_found(file_path):
    return f"[INFO] Optional reference file not found: {file_path}. Structure comparison skipped."


def results_exported(file_path):
    return f"[INFO] Results exported to {file_path}"