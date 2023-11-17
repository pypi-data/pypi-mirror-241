from datetime import datetime


class Fluxo:
    def __init__(
        self,
        name: str,
        interval: dict = None,
        active: bool = None
    ):
        self.name = name
        self.interval = interval
        self.active = active
