import random
import uuid


def is_valid_uuid(uuid_value):
    try:
        uuid.UUID(uuid_value)

        return True
    except ValueError:
        return False


def toss(items: list) -> dict:
    if len(items) < 2:
        return dict()

    to_receivers = []
    tossed = dict()

    for item in items:
        receiver = random.choice(items)
        while True:
            if receiver == item:
                receiver = random.choice(items)
                continue
            tossed[item] = receiver
            to_receivers.append(receiver)
            items.remove(receiver)
            break

    while items:
        try:
            key = set(to_receivers).difference(set(tossed.keys())).pop()
            value = items.pop()
            tossed[key] = value
        except KeyError:
            tossed[value] = set(tossed.keys()).difference(set(to_receivers)).pop()  # noqa
            break
    return tossed
