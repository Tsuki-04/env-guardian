def group_results(results):
    errors = []
    warnings = []
    info = []

    for result in results:
        if result.startswith("[ERROR]"):
            errors.append(result)
        elif result.startswith("[WARNING]"):
            warnings.append(result)
        elif result.startswith("[INFO]"):
            info.append(result)

    return errors, warnings, info