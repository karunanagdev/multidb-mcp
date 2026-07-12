VALID_STATUS = [
    "Active",
    "Completed",
    "Delayed",
    "Scheduled"
]

def validate_status(status):

    if status not in VALID_STATUS:
        raise ValueError(
            f"Invalid voyage status: {status}"
        )

    return status

