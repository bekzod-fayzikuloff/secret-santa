from typing import Union

from ...core.utils import toss
from ..models import Box, TossResult


class TossService:
    def __init__(self):
        self.model = TossResult

    @staticmethod
    def toss(box: Box) -> Union[str, dict]:
        if box.box_state == "CL":
            return "Game already close"

        if box.members.count() < 3:
            return "Need Add more members"

        members = [member for member in box.members.all()]
        tossed = toss(members)

        TossResult.objects.bulk_create(
            [TossResult(box=box, get_from=get_from, present_to=to_receive) for get_from, to_receive in tossed.items()]
        )

        box.box_state = "CL"
        box.save()

        return box.members
