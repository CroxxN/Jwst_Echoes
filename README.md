# A sonification system to hear images--especially astronomical images--of the universe played with different instruments.

## How to use?

- The entry point is `main.py`, you can supply your image to sonify through the assets folder.
- To add new instruments, simply download that instrument's `soundfont(.sf2)` file, and pass it through the init function
- The `generated_audio.mp3` is the sonified output.

## Dependencies

- FFMpeg
- fluidsynth
- python dependencies specified in `requirements.txt`

## A note on video mode

- You can also generate a video from the image and sonified audio.
- The video contains the original image, with a green vertical progress bar, indicating the position in image of the playing notes.