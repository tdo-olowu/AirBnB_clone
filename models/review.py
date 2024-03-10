#!/usr/bin/python3
"""Review class public"""


class Review(BaseModel):
    """user reviews, presumably
    Attributes:
        place_id (string)
        user_id (string)
        text (string)
    """
    place_id = ""
    user_id = ""
    text = ""
