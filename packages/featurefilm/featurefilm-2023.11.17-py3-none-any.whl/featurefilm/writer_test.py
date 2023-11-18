#!/usr/bin/env python

import os
import cv2
import time
import os.path as op
import numpy as np

from ffpyplayer.player import MediaPlayer
from psychopy.tools.movietools import MovieFileWriter

output_video = True

movie_pname = 'Budapest_1.mp4'
outvid_pname = movie_pname.replace('.mp4', '_faces.mp4')

print(f'Input  : {movie_pname}')
print(f'Output : {outvid_pname}')

player = MediaPlayer(
    movie_pname,
    an=True,  # No audio
    sn=True,  # No subtitles

)

# Wait for metadata to populate
while player.get_metadata()['src_vid_size'] == (0, 0):
    time.sleep(0.01)
meta = player.get_metadata()

# Pull video parameters from wrapped OpenCV stream
fps = meta['frame_rate'][0] / float(meta['frame_rate'][1])
frame_width, frame_height = meta['src_vid_size']
frame_area = frame_width * frame_height

# frame_time = 0.75 / fps
frame_time = 1.0 / fps

print(f'Video filename : {op.basename(movie_pname)}')
print(f'FPS            : {fps}')
print(f'Frame W x H    : {frame_width} x {frame_height}')
print(f'Frame area     : {frame_area} pixels')

if op.isfile(outvid_pname):
    print(f'Removing previous {op.basename(outvid_pname)}')
    os.remove(outvid_pname)

# Use psychopy's ffpyplayer-based movie file writer
if output_video:
    writer = MovieFileWriter(
        filename=outvid_pname,
        size=meta['src_vid_size'],
        fps=fps
    )
    writer.open()

for fc in range(90):

    frame, val = player.get_frame()

    if val == 'eof':
        break
    elif frame is None:
        time.sleep(0.01)
    else:

        # Read the next frame in the queue and its estimated play time in seconds
        img_ff, pts = frame

        print(f'Frame {fc:06d}  PTS {pts:0.3f} s')

        # Extract the RGB color image and convert to opencv BGR
        img_bytearray = img_ff.to_bytearray()
        img_rgb = np.reshape(np.array(img_bytearray[0]), [frame_height, frame_width, 3])
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # Do something to img_cv with OpenCV functions

        # Convert back to RGB
        img_rgb = img_bgr[:, :, ::-1]

        # Write the frame to the output file
        if output_video:
            writer.addFrame(img_rgb)

player.close_player()

if output_video:
    writer.close()