def install_package(package, version="upgrade"):
    from sys import executable
    from subprocess import check_call, CalledProcessError
    from pkg_resources import parse_version, get_distribution

    try:
        if version.lower() == "upgrade":
            check_call([executable, "-m", "pip", "install", package, "--upgrade", "--user","-i", "https://pypi.tuna.tsinghua.edu.cn/simple","some-package"])
        else:
            current_version = None
            try:
                current_version = get_distribution(package).version
            except Exception:
                pass

            if current_version is None or parse_version(current_version) < parse_version(version):
                installation_sign = "==" if ">=" not in version else ""
                check_call([executable, "-m", "pip", "install", package + installation_sign + version, "--user","-i", "https://pypi.tuna.tsinghua.edu.cn/simple","some-package"])
        return True
    except CalledProcessError:
        return False
