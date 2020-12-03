import logger
import uuid


class Review:
    def __init__(self, text, customer, score):
        self.text = text
        self.customer = customer
        self.score = int(score)
        self.status = 'Moderation'
        self.log = logger
        self.log.info(f'New review of {self.customer} was created)

    def __str__(self):
        return f"Review {self.customer}: score {self.score}, {self.text}"

    def __repr__(self):
        return f"{self.customer}: score {self.score}, {self.text}"
