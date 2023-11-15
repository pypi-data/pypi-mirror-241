from typing import Any


class DiscarderOperation:
    def __init__(self, keep_n: int = 1, discard_n: int = 0):
        self.keep_n = keep_n
        self.discard_n = discard_n
        self.idx = 0

    def get_next(self, _: Any) -> bool:
        res = self.idx % (self.keep_n + self.discard_n) < self.keep_n

        self.idx += 1

        return res
