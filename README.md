# P4 English Question Bank

A free, offline-capable question bank built from **153 scanned Primary 4 English
past-year exam papers (2021-2025)** — 3,808 questions.

**Live site:** https://emilyimemily.github.io/p4-english-question-bank/

## What is here

| File | Purpose |
| --- | --- |
| `index.html` | Main app (English UI). Loads `data/question_bank.json`. |
| `offline.html` | Same app with the whole bank embedded — double-click to use with no server. |
| `data/question_bank.json` | The full question bank. |
| `visuals/` | Cropped scans of the original printed questions and passages. |
| `sw.js` / `manifest.webmanifest` | PWA offline support. |

## Features

- **Practice online** — one question per screen, submit to see score and the reference answer.
- **Paper Builder** — assemble a paper from any mix of year / school / exam / topic.
- **Wrong Book** — every missed question is kept for revision, with progress export.
- **Image-first** — the printed scan, not OCR text, is the authoritative question.
  Cloze passages include the printed reference word box inside the scan; where
  the printed blanks can be measured, answers are typed directly into boxes on
  the scan.
- Questions whose source paper had no printed answer key are marked
  *Needs teacher checking* rather than being wrongly marked incorrect.

## Data notes

Questions were located by OCR line geometry at 150 dpi; the scans themselves
were cut from the source PDFs. `needs_review=true` means no official key was
found in the paper. All material is provided for personal study.

Generated 2026-11-12.
