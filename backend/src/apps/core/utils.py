import uuid


def is_valid_uuid(uuid_value):
    try:
        uuid.UUID(uuid_value)

        return True
    except ValueError:
        return False
