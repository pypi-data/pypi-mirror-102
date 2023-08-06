# Titulky

Tiny Python SubRip editor. Display infos, shift and re-fit timestamps. 

## Usage

Display informations for some `.srt` file.

```bash
python3 titulky.py test.srt
```

Shift subtitles by some amount.

```bash
python3 titulky.py test.srt shift 12.34
```

Refit subtitles to some interval.

```bash
python3 titulky.py test.srt shift 1:23.456 2:34:56
```
