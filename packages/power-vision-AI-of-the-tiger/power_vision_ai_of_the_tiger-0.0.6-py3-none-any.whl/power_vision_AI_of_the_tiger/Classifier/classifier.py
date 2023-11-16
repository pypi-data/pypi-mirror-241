## Classifer
## contains the function to classify the images 

import csv
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
import tqdm

from mediapipe.python.solutions import drawing_utils as mp_drawing
from mediapipe.python.solutions import pose as mp_pose

from PoseClassification.utils import show_image
from PoseClassification.pose_embedding import FullBodyPoseEmbedding
from PoseClassification.pose_classifier import PoseClassifier
from PoseClassification.utils import EMADictSmoothing
from PoseClassification.utils import RepetitionCounter
from PoseClassification.visualize import PoseClassificationVisualizer
from PoseClassification.bootstrap import BootstrapHelper

import pandas as pd

def bootstrap_dataset(bootstrap_images_in_folder='../images_in', bootstrap_images_out_folder='../images_out', 
                      bootstrap_csvs_out_folder='./results/csv_out', per_pose_class_limit=10):
    """
    Function to bootstrap dataset

    Parameters
    ----------
    bootstrap_images_in_folder : str 
        Folder where to find the images (default is '../images_in'). It should contains folders for each class.
    bootstrap_images_out_folder : str
        Folder where to send the output images (default is '../images_out').
    bootstrap_csvs_out_folder : str
        Folder where to find the resulting csv for each class (with landmarks) (default is './results/csv_out').
    per_pose_class_limit : int (or None)
        Limit for number of images per class (e.g. for debug)

    Returns
    -------
    """
    # Initialize helper.
    bootstrap_helper = BootstrapHelper(images_in_folder=bootstrap_images_in_folder,
                                        images_out_folder=bootstrap_images_out_folder,
                                        csvs_out_folder=bootstrap_csvs_out_folder,
                                        )
    
    # Check how many pose classes and images for them are available.
    print('----------------------------------------')
    print('Whole dataset')
    print('----------------------------------------')
    bootstrap_helper.print_images_in_statistics()

    # Bootstrap all images.
    print('----------------------------------------')
    print('Bootstrapping')
    print('----------------------------------------')
    bootstrap_helper.bootstrap(per_pose_class_limit=per_pose_class_limit)

    # Check how many images were bootstrapped.
    bootstrap_helper.print_images_out_statistics()

    # After initial bootstrapping images without detected poses were still saved in
    # the folderd (but not in the CSVs) for debug purpose. Let's remove them.
    print('Remove images without detected pose')
    bootstrap_helper.align_images_and_csvs(print_removed_items=False)
    bootstrap_helper.print_images_out_statistics()

    # Cleaning to remove outliers (eg images without landmarks)
    # Transforms pose landmarks into embedding.
    print('----------------------------------------')
    print('Cleaning and removing outliers')
    print('----------------------------------------')
    pose_embedder = FullBodyPoseEmbedding()

    # Classifies give pose against database of poses.
    pose_classifier = PoseClassifier(
        pose_samples_folder=bootstrap_csvs_out_folder,
        pose_embedder=pose_embedder,
        top_n_by_max_distance=30,
        top_n_by_mean_distance=10)

    outliers = pose_classifier.find_pose_sample_outliers()
    print('Number of outliers: ', len(outliers))
    # Remove all outliers (if you don't want to manually pick).
    bootstrap_helper.remove_outliers(outliers)

    # Align CSVs with images after removing outliers.
    bootstrap_helper.align_images_and_csvs(print_removed_items=False)
    bootstrap_helper.print_images_out_statistics()

def fusion_csv_all_classes(pose_samples_folder='results/csv_out', 
                           pose_samples_csv_path='results/full_csv/poses_csvs_out.csv', 
                           file_extension='csv', file_separator=','):
    """
    Fusion all the csv created for each class into one unique csv (to rule them all)

    Parameters
    ----------
    pose_samples_folder : str
        Folder where to find the csvs for all classes
    pose_samples_csv_path : str
        Path where to save the final csv merging all
    file_extension : str
        Extension of the files
    file_separator : str
        Separator to use in the csv

    """

    # Each file in the folder represents one pose class.
    file_names = [name for name in os.listdir(pose_samples_folder) if name.endswith(file_extension)]

    with open(pose_samples_csv_path, 'w') as csv_out:
        csv_out_writer = csv.writer(csv_out, delimiter=file_separator, quoting=csv.QUOTE_MINIMAL)
        for file_name in file_names:
            # Use file name as pose class name.
            class_name = file_name[:-(len(file_extension) + 1)]

            # One file line: `sample_00001,x1,y1,x2,y2,....`.
            with open(os.path.join(pose_samples_folder, file_name)) as csv_in:
                csv_in_reader = csv.reader(csv_in, delimiter=file_separator)
                for row in csv_in_reader:
                    row.insert(1, class_name)
                    csv_out_writer.writerow(row)

def classify_video(video_path='../video/abhi_pushups.mp4', class_name='fall', 
                    out_video_path = '../video/classif_out.mp4', pose_samples_folder='results/csv_out',
                    display=True):
    """
    Classify the video and display it

    video_path : str
        Path to the incoming video
    class_name : str
        Name of the class for which counting the fall
    out_video_path : str
        Path to the output video (with counts etc.)
    pose_samples_folder : str
        Folder where to find the csvs
    display : bool
        If we display some snapshots of the output video or not
    """
    video_cap = cv2.VideoCapture(video_path)

    # Get some video parameters to generate output video with classificaiton.
    video_n_frames = video_cap.get(cv2.CAP_PROP_FRAME_COUNT)
    video_fps = video_cap.get(cv2.CAP_PROP_FPS)
    video_width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #print(f"video_n_frames: {video_n_frames}")
    #print(f"video_fps: {video_fps}")
    #print(f"video_width: {video_width}")
    #print(f"video_height: {video_height}")

    # Initialize tracker.
    pose_tracker = mp_pose.Pose()

    # Initialize embedder.
    pose_embedder = FullBodyPoseEmbedding()

    # Initialize classifier.
    # Check that you are using the same parameters as during bootstrapping.
    pose_classifier = PoseClassifier(
        pose_samples_folder=pose_samples_folder,
        pose_embedder=pose_embedder,
        top_n_by_max_distance=30,
        top_n_by_mean_distance=10)

    # # Uncomment to validate target poses used by classifier and find outliers.
    # outliers = pose_classifier.find_pose_sample_outliers()
    # print('Number of pose sample outliers (consider removing them): ', len(outliers))

    # Initialize EMA smoothing.
    pose_classification_filter = EMADictSmoothing(
        window_size=10,
        alpha=0.2)

    # Initialize counter.
    repetition_counter = RepetitionCounter(
        class_name=class_name,
        enter_threshold=7,
        exit_threshold=5)

    # Initialize renderer.
    pose_classification_visualizer = PoseClassificationVisualizer(
        class_name=class_name,
        plot_x_max=video_n_frames,
        # Graphic looks nicer if it's the same as `top_n_by_mean_distance`.
        plot_y_max=10)
    
    # Open output video.
    out_video = cv2.VideoWriter(out_video_path, cv2.VideoWriter_fourcc(*'mp4v'), video_fps, (video_width, video_height))

    frame_idx = 0
    output_frame = None
    with tqdm.tqdm(total=video_n_frames, position=0, leave=True) as pbar:
        while True:
            # Get next frame of the video.
            success, input_frame = video_cap.read()
            if not success:
                print("unable to read input video frame, breaking!")
                break

            # Run pose tracker.
            input_frame = cv2.cvtColor(input_frame, cv2.COLOR_BGR2RGB)
            result = pose_tracker.process(image=input_frame)
            pose_landmarks = result.pose_landmarks

            # Draw pose prediction.
            output_frame = input_frame.copy()
            if pose_landmarks is not None:
                mp_drawing.draw_landmarks(
                    image=output_frame,
                    landmark_list=pose_landmarks,
                    connections=mp_pose.POSE_CONNECTIONS)
            
            if pose_landmarks is not None:
                # Get landmarks.
                frame_height, frame_width = output_frame.shape[0], output_frame.shape[1]
                pose_landmarks = np.array([[lmk.x * frame_width, lmk.y * frame_height, lmk.z * frame_width]
                                            for lmk in pose_landmarks.landmark], dtype=np.float32)
                assert pose_landmarks.shape == (33, 3), 'Unexpected landmarks shape: {}'.format(pose_landmarks.shape)

                # Classify the pose on the current frame.
                pose_classification = pose_classifier(pose_landmarks)

                # Smooth classification using EMA.
                pose_classification_filtered = pose_classification_filter(pose_classification)

                # Count repetitions.
                video_timestamp = video_cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0  # Convert milliseconds to seconds
                repetitions_count = repetition_counter(pose_classification_filtered, video_timestamp)
            else:
                # No pose => no classification on current frame.
                pose_classification = None

                # Still add empty classification to the filter to maintaing correct
                # smoothing for future frames.
                pose_classification_filtered = pose_classification_filter(dict())
                pose_classification_filtered = None

                # Don't update the counter presuming that person is 'frozen'. Just
                # take the latest repetitions count.
                repetitions_count = repetition_counter.n_repeats

            # Draw classification plot and repetition counter.
            output_frame = pose_classification_visualizer(
                frame=output_frame,
                pose_classification=pose_classification,
                pose_classification_filtered=pose_classification_filtered,
                repetitions_count=repetitions_count)

            # Save the output frame.
            out_video.write(cv2.cvtColor(np.array(output_frame), cv2.COLOR_RGB2BGR))

            # Show intermediate frames of the video to track progress.
            if display:
                if frame_idx % 50 == 0:
                    show_image(output_frame)

            frame_idx += 1
            pbar.update()

    # Close output video.
    out_video.release()
    print('\n')
    print('----------------------------------------')
    print(f'Fall report for the {os.path.basename(video_path)} video')
    print('----------------------------------------')
    fall_list = {'Fall':repetition_counter.fall_list, 'Timestamp':repetition_counter.fall_timestamp}
    df_fall_list = pd.DataFrame(fall_list)
    df_fall_list = df_fall_list.to_string(index=False)
    print(df_fall_list)
    print('\n')
    print(f'Video {out_video_path} saved \n')
    # Release MediaPipe resources.
    # pose_tracker.close()

    # Show the last frame of the video.
    if display:
        if output_frame is not None:
            show_image(output_frame)
