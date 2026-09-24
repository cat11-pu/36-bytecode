"""check_sample.py：按 sample/programs.json 走一圈，打印验收面。"""
import json
import os
import sys

from bytecode import Verifier


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join("sample", "programs.json")
    with open(path, encoding="utf-8") as handle:
        spec = json.load(handle)
    results = {}
    for name, program in spec["programs"].items():
        results[name] = Verifier().verify(program)
    verifier = Verifier()
    valid = verifier.verify(spec["programs"]["valid"])
    blob = verifier.persist()
    reborn = Verifier()
    restored = reborn.restore(blob)
    print("合法程序是否通过 =", results["valid"]["ok"])
    print("越界跳转 =", (results["bad_jump"]["pc"], results["bad_jump"]["reason"]))
    print("栈下溢 =", (results["bad_stack"]["pc"], results["bad_stack"]["reason"]))
    print("未定义变量 =", (results["bad_var"]["pc"], results["bad_var"]["reason"]))
    print("不可达指令数 =", results["unreachable"]["unreachable"])
    print("不可达程序是否通过 =", results["unreachable"]["ok"])
    print("每条指令只检查一遍（访问计数） =", valid.get("checked"))
    print("恢复后的校验计数 =", restored.get("checked"))
    print("指令数上限（规模判据） =", spec["instruction_budget"])
    print("不变量（栈深在合流处一致） =", spec["stack_invariant"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
