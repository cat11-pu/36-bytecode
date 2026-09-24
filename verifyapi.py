"""verifyapi.py：对外门面（老接口 verify 不能改）。"""
from __future__ import annotations

from bytecode import Verifier


class Checker:
    def __init__(self):
        self.verifier = Verifier()

    def verify(self, program) -> dict:
        return self.verifier.verify(program)

    def snapshot(self) -> bytes:
        return self.verifier.persist()

    def rebuild(self, blob: bytes = None) -> dict:
        return self.verifier.restore(blob)
