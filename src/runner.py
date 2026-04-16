from rules.security import (
    check_app_debug,
    check_app_key,
    check_db_password,
    check_sensitive_variables,
)
from rules.structure import compare_env_files


def run_analysis(env_vars, example_vars=None, strict_mode=False):
    results = []

    results.extend(check_app_debug(env_vars, strict_mode=strict_mode))
    results.extend(check_app_key(env_vars))
    results.extend(check_db_password(env_vars, strict_mode=strict_mode))
    results.extend(check_sensitive_variables(env_vars))

    if example_vars is not None:
        results.extend(compare_env_files(env_vars, example_vars, strict_mode=strict_mode))

    return results