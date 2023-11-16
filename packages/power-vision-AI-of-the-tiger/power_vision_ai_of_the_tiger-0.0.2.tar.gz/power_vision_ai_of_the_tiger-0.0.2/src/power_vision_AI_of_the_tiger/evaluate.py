import argparse
from Classifier import metrics


# ----------------------------------------------
# Parser
# ----------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--path_csv_out",
                    default="./results/csv_out",
                    help="Path where to save the output csvs")

parser.add_argument("--images_in", 
                    default='../images_in',
                    help="Path to the folder where to find the images used for testing")

args = parser.parse_args()

# ----------------------------------------------
# Metrics
# ----------------------------------------------

metrics.get_metrics(pose_samples_folder=args.path_csv_out, test_image_folder=args.images_in)