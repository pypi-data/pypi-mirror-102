class Value:
    def __init__(self, data):
        self.json = data

        try: self.data: str = data["data"]
        except (KeyError, TypeError): self.data: str = "Undefined"
        try: self.code: str = data["code"]
        except (KeyError, TypeError): self.code: str = "Undefined"