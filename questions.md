# 读源码答事实卷

这份 `index.js` 是一个 gitignore 语义实现（Node，零依赖）。请读源码、必要时真跑它，
把 12 项事实写进 `answers.json`（键名照抄，值填对）。

行为题（真跑库；前八项填 true / false，第九项填「抛错」或「不报错」）：
1. `tab_pattern_ignores_a`：规则 `a` 后接一个制表符，路径 `a` 会不会被忽略。
2. `tab_pattern_ignores_tab`：同一条规则下，路径 `a` 后接制表符会不会被忽略。
3. `negated_keep_ignored`：规则 `["*.md", "!keep.md"]` 下，`keep.md` 会不会被忽略。
4. `negated_other_ignored`：同一条规则下，`notes.md` 会不会被忽略。
5. `inner_slash_rooted`：规则 `a/b`（中间带斜杠）下，`x/a/b` 会不会被忽略。
6. `dir_only_itself`：规则 `d/`（斜杠结尾）下，`d` 本身会不会被忽略。
7. `case_default_insensitive`：默认配置下，规则 `A` 能不能忽略路径 `a`。
8. `array_input_works`：规则传数组 `["a", "b"]`，`b` 会不会被忽略。
9. `strict_relative`：默认配置下，`../x` 这种路径是哪种情况（填题目给的两个词之一）。

结构题（读源码，填列表）：
10. `regex_constants`：源码里以 `REGEX_` 开头的常量名，按出现先后排列。
11. `class_names`：源码里的类名，按出现先后排列。
12. `export_keys`：把这份模块 require 进来后，可枚举键按字典序排列。
