# ignoreread

仓库里是一份真实的 gitignore 语义实现（`index.js`，来自 kaelzhang/node-ignore，MIT）。
任务是**读懂它**，然后把 `questions.md` 里的 12 项事实填进 `answers.json`。

## 跑验收

    python3 check_answers.py

它自己从源码与运行行为现算标准答案，再和你的 `answers.json` 逐项比对；全部通过才退出码 0。

## 约束

- 只改 `answers.json`；`index.js`、`check_answers.py`、`questions.md` 都不要动。
- 列表题要精确：元素名称、先后顺序都要对；行为题填 `true` / `false` 或题目里给的那两个词。
- 行为题可以用 `node -e` 真跑这份库；不要再引入依赖。
