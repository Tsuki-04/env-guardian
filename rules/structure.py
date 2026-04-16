from src import messages

def compare_env_files(env_vars, example_vars, strict_mode=False):
    results = []

    env_keys = set(env_vars.keys())
    example_keys = set(example_vars.keys())

    missing_keys = example_keys - env_keys
    extra_keys = env_keys - example_keys

    for key in sorted(missing_keys):
        results.append(messages.missing_env_variable(key, strict_mode=strict_mode))

    for key in sorted(extra_keys):
        results.append(messages.undocumented_env_variable(key))

    return results