#!/usr/bin/env python
"""
MIT License

Copyright (c) 2023 Mike Tyszka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import cv2
import time
import argparse

import os.path as op
import numpy as np
import pandas as pd

from ffpyplayer.player import MediaPlayer
from psychopy.tools.movietools import MovieFileWriter

from importlib.resources import files


def face_overlay(frame, faces, frame_count, thickness=1):
    """
    Visualize face detection with bounding box overlays on actual frame

    :param frame: BGR image
    :param faces: list
    :param frame_count: int
    :param thickness: float
    :return:
    """

    if faces[1] is not None:

        for idx, face in enumerate(faces[1]):

            coords = face[:-1].astype(np.int32)

            # Face detection bounding box
            cv2.rectangle(
                frame,
                (coords[0], coords[1]), (coords[0] + coords[2], coords[1] + coords[3]),
                (0, 255, 0),
                thickness
            )

            # Face feature dots
            cv2.circle(frame, (coords[4], coords[5]), 2, (255, 0, 0), thickness)
            cv2.circle(frame, (coords[6], coords[7]), 2, (0, 0, 255), thickness)
            cv2.circle(frame, (coords[8], coords[9]), 2, (0, 255, 0), thickness)
            cv2.circle(frame, (coords[10], coords[11]), 2, (255, 0, 255), thickness)
            cv2.circle(frame, (coords[12], coords[13]), 2, (0, 255, 255), thickness)

    # Add frame counter top left
    cv2.putText(frame, f'{frame_count:06d}', (16, 48), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 1)


def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Create face feature timeseries from movie'
    )

    parser.add_argument('-i', '--input', required=True,
                        help='MP4 video file')

    parser.add_argument('-o', '--output', required=False,
                        help='Output feature CSV file [<video filestub>_faces.csv]')

    parser.add_argument('-subj', '--subjects', nargs='+', default=[],
                        help='List of subject IDs to convert (eg --subjects alpha bravo charlie)')

    parser.add_argument('--overlay', action='store_true', default=False,
                        help='Display face detection overlay on video in real time')

    parser.add_argument('--savevid', action='store_true', default=False,
                        help='Save face detection overlay to a new video (<video filestub>_faces.mp4')

    # Parse command line arguments
    args = parser.parse_args()

    in_pname = op.realpath(args.input)

    if args.output:
        out_pname = args.output
    else:
        out_pname = in_pname.replace('.mp4', '_faces.csv')

    print(f'Input video : {op.basename(in_pname)}')
    print(f'Output CSV  : {op.basename(out_pname)}')

    # Lower face detection score threshold
    score_threshold = 0.75

    # Intersect-over-union ratio (NMS) threshold for face candidates
    nms_threshold = 0.3

    # Candidate faces to retain before NMS
    top_k = 1000

    # Frame resampling scale factor (multiplicative)
    scale = 1.0

    # Full path to pretrained YuNet face detector in models/ directory
    pkg_name = 'featurefilm'
    models_dir = op.join(files(pkg_name), 'models')
    face_detection_model_pname = op.join(models_dir, 'face_detection_yunet_2023mar.onnx')

    # Initialize_FaceDetectorYN
    print(f'Initializing face detector')
    detector = cv2.FaceDetectorYN.create(
        face_detection_model_pname,
        "",
        (320, 320),
        score_threshold,
        nms_threshold,
        top_k
    )

    #
    # Video face analysis
    #

    # Open video player stream
    print(f'Opening video stream from {in_pname}')
    ff_opts = {
        'out_fmt': 'rgb24',
        'fast': True,
        'an': True,  # Ignore audio stream
        'framedrop': False,  # Must be enabled to process all frames
        'sync': 'video'
    }
    player = MediaPlayer(filename=in_pname, ff_opts=ff_opts)

    # Wait for metadata to populate
    while player.get_metadata()['src_vid_size'] == (0, 0):
        time.sleep(0.01)
    meta = player.get_metadata()

    # Pull video parameters from wrapped OpenCV stream
    fps = meta['frame_rate'][0] / float(meta['frame_rate'][1])
    frame_width, frame_height = meta['src_vid_size']
    frame_area = frame_width * frame_height

    print(f'FPS            : {fps}')
    print(f'Frame W x H    : {frame_width} x {frame_height}')
    print(f'Frame area     : {frame_area} pixels')

    # Create a video writer if requested
    if args.savevid:

        outvid_pname = args.input.replace('.mp4', '_faces.mp4')

        if op.isfile(outvid_pname):
            print(f'Removing previous {op.basename(outvid_pname)}')
            os.remove(outvid_pname)

        # Use psychopy's ffpyplayer-based movie file writer
        writer = MovieFileWriter(
            filename=outvid_pname,
            size=meta['src_vid_size'],
            fps=fps
        )
        writer.open()

    # Set video frame size for detector
    detector.setInputSize([frame_width, frame_height])

    # Init frame results list
    res_list = []
    frame_count = 0

    # Progress report every 10 seconds
    progress_interval_s = 10.0
    progress_step = int(progress_interval_s * fps)

    print('\nStarting face detection')
    print('\n{:>6s} {:>10s}'.format('Frame', 'Time'))

    prev_pts = None

    while True:

        frame, val = player.get_frame()

        if val == 'eof':
            break
        elif frame is None:
            time.sleep(0.01)
        else:

            img_ff, pts = frame

            if prev_pts:
                dpts = pts - prev_pts
                # print(f'{frame_count} {pts:0.3f} {dpts:0.3f}')

            # Convert to OpenCV BGR image
            img_bytearray = img_ff.to_bytearray()
            img_rgb = np.reshape(np.array(img_bytearray[0]), [frame_height, frame_width, 3])
            img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

            faces = detector.detect(img_bgr)

            if faces[1] is not None:

                n_faces = len(faces[1])

                total_face_area = 0.0
                min_score = 1.0
                max_score = 0.0

                for face in faces[1]:

                    x0, y0 = face[0], face[1]
                    width, height = face[2], face[3]
                    score = face[-1]
                    area = width * height / float(frame_area)

                    total_face_area += area
                    min_score = score if score < min_score else min_score
                    max_score = score if score > max_score else max_score

            else:

                n_faces = 0
                total_face_area = 0
                min_score = 0.0
                max_score = 0.0

            # Construct frame-wise results dict
            res = {
                'Timestamp': pts,
                'NFaces': n_faces,
                'TotalFaceArea': total_face_area,
                'MinScore': min_score,
                'MaxScore': max_score,
            }

            # Add results to frame results list
            res_list.append(res)

            if np.mod(frame_count, progress_step) == 0:
                print(f'{frame_count:06d} {pts:10.3f}')

            # Increment processed frame counter
            frame_count += 1
            prev_pts = pts

            # Visualize results
            if args.overlay:

                # Overlay face detection bounding boxes on current frame
                face_overlay(img_bgr, faces, frame_count)

                # Show the frame
                cv2.imshow("Live", img_bgr)
                cv2.waitKey(1)

            if args.savevid:

                img_rgb = img_bgr[:, :, ::-1]
                writer.addFrame(img_rgb)

    print('\nFinished face detection')

    # Clean up
    cv2.destroyAllWindows()
    player.close_player()
    if args.savevid:
        writer.close()

    # Convert results list to dataframe and save
    df = pd.DataFrame(res_list)

    print(f'\nSaving face detection results to {out_pname}')
    df.to_csv(out_pname, index=False, float_format='%0.6f')


if "__main__" in __name__:

    main()