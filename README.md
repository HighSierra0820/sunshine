# sunshine
 A simple [_Moonlight Window puzzle_](https://github.com/Sapium59/moonlight_window) solver using exhaustive search.

## Requirements
- Python 3.?
- OpenCV

## How this work & Notes
- images of glyphs are generated and stored in `tgscc/`
  - character set: [_Table of General Standard Chinese Characters_](https://en.wikipedia.org/wiki/Table_of_General_Standard_Chinese_Characters)
  - only non-blank glyphs are stored; characters with 0 _windows_ are represented by `Ｘ` (fullwidth capital x)
- differences of input image (sliced) and glyphs in the character set are calculated, among which the character with lowest difference is taken
- initial execution of `solve.py` may experience prolonged runtime (possibly due to Explorer indexing 5000+ files)

## Usage
- `solve.py <targetImageFile>`

## Samples
```
(base) PS D:\code\projects\sunshine> python .\solve.py samples\target_1219.png
2023-12-21 15:02:13
detectCharLength: 4
改  diff: 0
旗  diff: 0
易  diff: 0
帜  diff: 0
改旗易帜
2023-12-21 15:02:26
(base) PS D:\code\projects\sunshine> python .\solve.py samples\target_1221.png
2023-12-21 15:02:32
detectCharLength: 4
踽  diff: 0
踽  diff: 0
独  diff: 0
Ｘ  diff: 0
踽踽独Ｘ
2023-12-21 15:02:45
(base) PS D:\code\projects\sunshine>_
```

## References
- the original [_Moonlight Window puzzle_](https://github.com/Sapium59/moonlight_window)
- [OpenCV](https://opencv.org/) - Open Computer Vision Library