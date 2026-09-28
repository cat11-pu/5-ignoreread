# -*- coding: utf-8 -*-
"""验收：从源码与运行行为现算标准答案，再和 answers.json 逐项比对。
全部一致退出码 0；有不过的打印「不过」并退出码 1。"""
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

PROBE = r"""
const make = require("./index.js");
function safe(fn) { try { return fn(); } catch (error) { return "抛错"; } }
const out = {};
out.tab_pattern_ignores_a = safe(() => make().add("a\t").ignores("a"));
out.tab_pattern_ignores_tab = safe(() => make().add("a\t").ignores("a\t"));
out.negated_keep_ignored = safe(() => make().add(["*.md", "!keep.md"]).ignores("keep.md"));
out.negated_other_ignored = safe(() => make().add(["*.md", "!keep.md"]).ignores("notes.md"));
out.inner_slash_rooted = safe(() => make().add("a/b").ignores("x/a/b"));
out.dir_only_itself = safe(() => make().add("d/").ignores("d"));
out.case_default_insensitive = safe(() => make().add("A").ignores("a"));
out.array_input_works = safe(() => make().add(["a", "b"]).ignores("b"));
out.strict_relative = safe(() => { make().ignores("../x"); return "不报错"; });
out.export_keys = Object.keys(require("./index.js")).sort();
console.log(JSON.stringify(out));
"""


def truth():
    res = subprocess.run(["node", "-e", PROBE], cwd=HERE, capture_output=True, text=True)
    if res.returncode != 0:
        raise SystemExit("行为探针没跑起来：" + (res.stderr or "")[:200])
    out = json.loads(res.stdout.strip())
    source = io.open(os.path.join(HERE, "index.js"), encoding="utf-8").read()
    out["regex_constants"] = re.findall(r"const (REGEX_[A-Z_]+) =", source)
    out["class_names"] = re.findall(r"^class (\w+)", source, re.M)
    return out


def main():
    want = truth()
    path = os.path.join(HERE, "answers.json")
    if not os.path.exists(path):
        print("缺少 answers.json")
        return 1
    got = json.loads(io.open(path, encoding="utf-8").read())
    bad = 0
    for key in sorted(want):
        mine = got.get(key, "（缺这一项）")
        if mine == want[key]:
            print("通过", key, "=", json.dumps(mine, ensure_ascii=False))
        else:
            bad += 1
            print("不过", key, "期望", json.dumps(want[key], ensure_ascii=False),
                  "实际", json.dumps(mine, ensure_ascii=False, default=str))
    print("事实题 %d/%d 通过" % (len(want) - bad, len(want)))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
