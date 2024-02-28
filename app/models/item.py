from datetime import datetime


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.created_at = datetime.utcnow()
