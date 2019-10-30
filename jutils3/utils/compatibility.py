def get_version():
    """Returns a tuple providing the major, minor, patch, and pre-release identifier like so: (Major, Minor, Patch, Identifier)"""
    return (0, 1, 0, "")

def get_version_string():
    """Returns the version in the following format: Major.Minor.Patch(-Pre-release Indetifier)\nThe identifier may be absent if the release is a full release."""
    version_data = get_version()
    return ("%s.%s.%s" % version_data[:-1]) + ("" if len(version_data[3]) == 0 else "-%s" % version_data[3])

def get_simple_version():
    """Returns a tuple providing the major, minor, and patch information for easier handing of compatibility."""
    return get_version()[:-1]

def get_major_version():
    """Returns the major version number."""
    return get_version()[0]