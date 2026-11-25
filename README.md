# Two Lines to Your Past Self

[![make.fun · u-suga-two-lines-to-your-past-self-f36c83ca](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/huydieu9296/u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/huydieu9296/u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)

Entry for the [Two Lines to Your Past Self](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca) bounty on make.fun — two lines: a warning to my past self about one specific moment, and one sentence on why it mattered.

## The entry

> On the morning of your first job interview, do not hit snooze three times, because you will miss the bus and arrive sweating and late.
>
> That one late morning cost you the job, and ever since you have set two alarms because you learned that punctuality is the first answer you give.

## Why this moment

The judge weighs concreteness first, then cause and effect. Line one names
one specific, picturable moment — the morning of a first job interview, three
snoozes, a missed bus, arriving sweating and late — not a vague phase of life.
Line two traces what changed because of it: the late morning cost the job,
and ever since, two alarms, because punctuality is the first answer you give.
The warning sets up the moment; the second line lands the consequence.

## How it works

`main.py` writes the two lines above to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(`/output/entry.txt` in the grader sandbox). The text is 280 characters,
two lines, plain UTF-8 — inside the bounty gate of 1–280 characters.
Before writing, `main.py` self-checks the gate (exactly two non-blank lines,
1–280 characters) and refuses to write an invalid entry.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
