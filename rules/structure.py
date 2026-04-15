def compare_env_files(env_vars, example_vars, strict_mode=False):
    results = []

    env_keys = set(env_vars.keys())
    example_keys = set(example_vars.keys())

    missing_keys = example_keys - env_keys
    extra_keys = env_keys - example_keys

    for key in sorted(missing_keys):
        if strict_mode:
            results.append(f"[ERROR] Missing variable in .env: {key}")
        else:
            results.append(f"[WARNING] Missing variable in .env: {key}")

    for key in sorted(extra_keys):
        results.append(f"[INFO] Undocumented variable in .env: {key}")

    return results