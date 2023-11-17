import argparse
import os

from power_vision_AI_of_the_tiger.Classifier import classifier
from power_vision_AI_of_the_tiger.video import video

def main():
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
                        default="{}/data/csv_out".format(os.path.dirname(__file__)),
                        help="Path where to find the output csvs")

    args = parser.parse_args()

    # ----------------------------------------------
    # Classification
    # ----------------------------------------------

    if(args.input == 'stream'):
        stream_video = '/tmp/power_vision_AI_of_the_tiger_stream.mp4'
        video.capturer_et_enregistrer_video(output_path=stream_video)
        classifier.classify_video(video_path=stream_video, class_name='fall',
                                out_video_path =args.output, pose_samples_folder=args.path_csv_out, display=args.display)
    else:
        classifier.classify_video(video_path=args.input, class_name='fall',
                                out_video_path =args.output, pose_samples_folder=args.path_csv_out, display=args.display)

if __name__ == "__main__":
    main()