import uuid


def group_uuid(name: str) -> str:
    """
    Returns a unique but human-readable string, to assist debugging orchestrated groups.

    Args:
        name (str): A human readable name

    Returns:
        readable_uid (str): name appended with a unique string
    """
    return f"{name}-{str(uuid.uuid4())[:6]}"


def inject(name: str):  # type: ignore
    """
    Function to mark a default argument of a plan method as a reference to a device
    that is stored in the Blueapi context.
    Bypasses mypy linting, returning x as Any and therefore valid as a default
    argument.

    Args:
        name (str): Name of a device to be fetched from the Blueapi context

    Returns:
        Any: name but without typing checking, valid as any default type

    """

    return name
