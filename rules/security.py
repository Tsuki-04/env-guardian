def check_app_debug(env_vars):
    results = []

    app_debug = env_vars.get("APP_DEBUG", "").strip().lower()

    if app_debug == "true":
        results.append("[WARNING] APP_DEBUG is enabled. Disable it in production.")

    return results
