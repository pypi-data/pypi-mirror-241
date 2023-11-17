import argparse
import os

from power_vision_AI_of_the_tiger.Classifier import classifier

def main():
    # ----------------------------------------------
    # Parser
    # ----------------------------------------------
    parser = argparse.ArgumentParser()

    parser.add_argument("--images_in", 
                        default='../images_in',
                        help="Path to the folder where to find the images used for training")

    parser.add_argument("--images_out", 
                        default='../images_out',
                        help="Path to the folder where to save the classified images")

    parser.add_argument("--path_csv_out",
                        default="{}/data/csv_out".format(os.path.dirname(__file__)),
                        help="Path where to save the output csvs")

    parser.add_argument("--per_pose_class_limit",
                        default=None,
                        help="Limit on the number of images to bootstrap by class")

    args = parser.parse_args()

    # ----------------------------------------------
    # Classification
    # ----------------------------------------------
    if args.per_pose_class_limit is not None:
        per_pose_class_limit = int(args.per_pose_class_limit)
    else:
        per_pose_class_limit = None

    classifier.bootstrap_dataset(bootstrap_images_in_folder=args.images_in, bootstrap_images_out_folder=args.images_out, 
                                bootstrap_csvs_out_folder=args.path_csv_out, per_pose_class_limit=per_pose_class_limit)
    classifier.fusion_csv_all_classes()

if __name__ == "__main__":
    main()
