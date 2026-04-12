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