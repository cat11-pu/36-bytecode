"""bytecode.py：字节码校验（基线：只认操作码名字）。"""
from __future__ import annotations

OPCODES = {"PUSH": 1, "LOAD": 1, "STORE": 1, "ADD": 0, "JMP": 1, "JZ": 1, "HALT": 0}


class Verifier:
    def __init__(self):
        self.checked = 0

    def verify(self, program) -> dict:
        """基线：只看操作码认不认识，别的都不查。"""
        for index, instruction in enumerate(program):
            op = instruction[0]
            self.checked += 1
            if op not in OPCODES:
                return {"ok": False, "pc": index, "reason": "unknown_opcode", "unreachable": 0}
            if len(instruction) - 1 != OPCODES[op]:
                return {"ok": False, "pc": index, "reason": "bad_arity", "unreachable": 0}
        return {"ok": True, "pc": None, "reason": None, "unreachable": 0}

    def persist(self) -> bytes:
        raise NotImplementedError("快照还没实现")

    def restore(self, blob: bytes = None) -> dict:
        raise NotImplementedError("重启恢复还没实现")

    def stats(self) -> dict:
        return {"checked": self.checked}
