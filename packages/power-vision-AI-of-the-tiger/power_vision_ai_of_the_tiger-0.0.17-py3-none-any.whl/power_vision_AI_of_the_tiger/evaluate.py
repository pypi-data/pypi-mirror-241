import argparse
import os
from power_vision_AI_of_the_tiger.Classifier import metrics

def main():
    # ----------------------------------------------
    # Parser
    # ----------------------------------------------
    parser = argparse.ArgumentParser()

    parser.add_argument("--path_csv_out",
                        default="{}/data/csv_out".format(os.path.dirname(__file__)),
                        help="Path where to save the output csvs")

    parser.add_argument("--images_in", 
                        default='../images_in',
                        help="Path to the folder where to find the images used for testing")

    args = parser.parse_args()

    # ----------------------------------------------
    # Metrics
    # ----------------------------------------------

    metrics.get_metrics(pose_samples_folder=args.path_csv_out, test_image_folder=args.images_in)

if __name__ == "__main__":
    main()