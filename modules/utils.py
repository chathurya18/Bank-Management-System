def authenticate(customers, name, pin):
    """Verify if the customer exists and the PIN matches."""
    for c in customers:
        if c["name"].lower() == name.lower() and c["pin"] == pin:
            return c
    return None
