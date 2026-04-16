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


def render_section(title, items):
    if not items:
        return

    print(f"\n--- {title} ({len(items)}) ---")
    for item in items:
        print(item)


def render_summary(errors, warnings, info):
    status = "FAILED" if errors else "PASSED"
    exit_code = 1 if errors else 0

    print("\n--- Summary ---")
    print(f"Errors:   {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Info:     {len(info)}")
    print(f"Status:   {status}")
    print(f"Exit code:{exit_code}")


def render_console_output(errors, warnings, info, env_path, example_path, strict_mode):
    status = "FAILED" if errors else "PASSED"
    scan_type = "Production Check" if strict_mode else "Standard Check"
    mode = "strict" if strict_mode else "normal"

    print("\n--- Security analysis ---")
    print(f"Tool:      ENV GUARDIAN")
    print(f"Scan:      {scan_type}")
    print(f"Target:    {env_path}")
    print(f"Reference: {example_path if example_path else 'None'}")
    print(f"Mode:      {mode}")
    print(f"Status:    {status}")

    render_section("Critical issues", errors)
    render_section("Warnings", warnings)
    render_section("Informational notes", info)
    render_summary(errors, warnings, info)