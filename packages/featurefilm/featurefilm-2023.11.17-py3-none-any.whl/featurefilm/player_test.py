#!/usr/bin/env python

from time import sleep
from tqdm import tqdm
from ffpyplayer.player import MediaPlayer

movie_pname = 'Budapest_1.mp4'

print(f'Opening video stream from {movie_pname}')
player = MediaPlayer(movie_pname)

frame_count = 0

for fc in tqdm(range(180)):

    frame, val = player.get_frame()

    if val == 'eof':

        break

    elif frame is None:

        sleep(0.0167)

    else:

        img, t = frame

        tqdm.write(f'{val:0.3f} {frame_count:06d} {t:0.3f} {img.get_pixel_format()} {img.get_buffer_size()}')

#        sleep(val)

        frame_count += 1

player.close_player()
