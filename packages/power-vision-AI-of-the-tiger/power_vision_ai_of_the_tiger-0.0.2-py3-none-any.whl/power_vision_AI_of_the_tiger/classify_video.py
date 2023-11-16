import argparse
import os

from Classifier import classifier

# ----------------------------------------------
# Parser
# ----------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", 
                    help="Path to the input video file")

parser.add_argument("-o", "--output", 
                    default='../video/classif_out.mp4',
                    help="Path to the output video file")

parser.add_argument("--display", 
                    help="Display video",
                    action="store_true")

parser.add_argument("--path_csv_out",
                    default="./results/csv_out",
                    help="Path where to find the output csvs")

args = parser.parse_args()

# ----------------------------------------------
# Classification
# ----------------------------------------------

classifier.classify_video(video_path=args.input, class_name='fall',
                          out_video_path =args.output, pose_samples_folder=args.path_csv_out, display=args.display)