# The Long Score

An explorable constellation of Baroque, Classical and Romantic composers. Travel through time by dragging or scrolling: the music crossfades between composers, the palette shifts with the era, and every composer is paired with a painting. Includes a "Match the painting" game.

Open `index.html` through any static server (audio loads with `fetch`, so `file://` will not work):

```bash
python3 -m http.server 8000
```

## Layout
- `index.html`: the built page (data embedded)
- `audio/`: 18 clips of about 80 seconds, trimmed from Wikimedia Commons recordings
- `src/`: HTML template and composer text
- `data/`: Open Opus and Art Institute of Chicago data snapshot, plus recording metadata
- `tools/`: scripts used to fetch the data and audio (need `imageio-ffmpeg` for trimming)
- `build.py`: rebuilds `index.html`

## Credits
- Composer data and portraits: [Open Opus](https://openopus.org)
- Paintings: open-access collection of the [Art Institute of Chicago](https://www.artic.edu)
- Recordings: Wikimedia Commons. Three are CC BY-SA (Vivaldi, Mozart, Chopin); see `data/audio_meta.json` for each file's license and page. Excerpts are trimmed and faded.
