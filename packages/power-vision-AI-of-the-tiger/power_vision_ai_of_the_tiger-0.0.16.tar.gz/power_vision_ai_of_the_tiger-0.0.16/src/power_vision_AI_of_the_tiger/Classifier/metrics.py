## Functions to compute the metrics of the application

from glob import glob
from mediapipe.python.solutions import drawing_utils as mp_drawing
from mediapipe.python.solutions import pose as mp_pose

from power_vision_AI_of_the_tiger.PoseClassification.pose_embedding import FullBodyPoseEmbedding
from power_vision_AI_of_the_tiger.PoseClassification.pose_classifier import PoseClassifier
from power_vision_AI_of_the_tiger.PoseClassification.utils import EMADictSmoothing

import os
import pandas as pd
import numpy as np
import cv2
from sklearn.metrics import confusion_matrix, roc_curve, auc
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import matplotlib.pyplot as plt




def initialize_tracker(pose_samples_folder):
    '''
    Initialize the pose tracker with the csv_out created after the bootstratping
    
    Parameters
    ----------
    pose_samples_folder : str 
        Folder with pose class CSVs. That should be the same folder you used while
    building classifier to output CSVs.

    Returns
    -------
    pose_tracker : Pose object 
    (from mp_pose)
    pose_classifier : PoseClassifier object
    (from PoseClassification)
    pose_classification_filter : PoseClassifier object with the EMA smoothing
    (from PoseClassification)
    '''

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

    # Initialize EMA smoothing.
    pose_classification_filter = EMADictSmoothing(
        window_size=10,
        alpha=0.2)
    
    return pose_tracker, pose_classifier, pose_classification_filter


def get_class_results(pose_samples_folder, test_image_folder):
    '''
    Compute the classification for the test images

    Parameters
    ----------
    pose_samples_folder : str 
        Folder where to find the csvs_out generated after the model 'training'
    test_image_folder : str
        Folder containing the test images split in folders by class

    Return
    -------
    df_pred_results : pd.DataFrame
    Dataframe containing {'Images':images, 'pose_classification':pose_classification, 'Class':classes}
    '''

    pose_tracker, pose_classifier, pose_classification_filter = initialize_tracker(pose_samples_folder)

    directories = glob(test_image_folder + '/*fall*')

    # Liste des noms de fichiers dans le dossier
    images= []
    pose_classif = []
    classes = []

    # Parcourir tous les fichiers texte dans le répertoire
    for directory in directories :
        image_files = glob(directory + '/*.jpg')
        for image_file in image_files :
        # Lisez l'image avec OpenCV
          input_frame = cv2.imread(image_file)

          # Run pose tracker.
          #input_frame = cv2.cvtColor(input_frame, cv2.COLOR_BGR2RGB)
          result = pose_tracker.process(image=input_frame)
          pose_landmarks = result.pose_landmarks

              # Draw pose prediction.
          output_frame = input_frame.copy()
          if pose_landmarks is not None :
            mp_drawing.draw_landmarks(
                image=output_frame,
                landmark_list=pose_landmarks,
                connections=mp_pose.POSE_CONNECTIONS)

          # Utilisez le classificateur pour prédire les poses
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

            if len(pose_classification_filtered) == 1 :
              if list(pose_classification_filtered.keys())[0] == 'not_fall' :
                classes.append(0)
              elif list(pose_classification_filtered.keys())[0] == 'fall' :
                classes.append(1)
            else :
              if pose_classification_filtered['fall'] > pose_classification_filtered['not_fall'] :
                  classes.append(1)
              elif pose_classification_filtered['fall'] < pose_classification_filtered['not_fall'] :
                  classes.append(0)

            images.append(os.path.basename(image_file))
            pose_classif.append(pose_classification_filtered)

    res = {'Images':images, 'pose_classification':pose_classif, 'Class':classes}
    df_pred_results = pd.DataFrame(res)
    return df_pred_results

def get_ground_truth(test_image_folder):
    '''
    Create a dataframe with the ground truth class fro the test images

    Parameters
    ----------
    test_image_folder : str
        Folder containing the test images split in folders by class

    Return
    -------
    df_gt_results : pd.DataFrame
    Dataframe containing {'Images':images, 'Class':classes}
    '''

    directories = glob(test_image_folder + '/*fall*')

    # Initialiser un dataframe
    data = []

    # Parcourir tous les fichiers texte dans le répertoire
    for directory in directories :
        if os.path.basename(directory) == 'fall':
            fall_images = glob(directory+'/*.jpg')
            for fall_image in fall_images:
                data.append({"Images": os.path.basename(fall_image), "Class": 1})
        elif os.path.basename(directory) == 'not_fall':
            not_fallen_images = glob(directory+'/*.jpg')
            for not_fallen_image in not_fallen_images:
                data.append({"Images": os.path.basename(not_fallen_image), "Class": 0})

    # Afficher le dataframe résultant
    df_gt_results = pd.DataFrame(data)
    return df_gt_results


def compute_final_results(pose_samples_folder, test_image_folder):
    '''
    Create a dataframe containing ground truth and predicted class

    Parameters
    ----------
    pose_samples_folder : str 
        Folder where to find the csvs_out generated after the model 'training'
    test_image_folder : str
        Folder containing the test images split in folders by class

    Return
    -------
    df_final : pd.DataFrame
    Dataframe containing {'Images':images, 'Class_gt': ground truth class for the test images, 'Class_pred': predicted class for the test images}
    '''

    df_pred = get_class_results(pose_samples_folder, test_image_folder)
    df_gt = get_ground_truth(test_image_folder)
    df_final = df_pred.drop(columns=['pose_classification']).merge(df_gt, left_on=df_pred.Images, right_on=df_gt.Images, suffixes=('_gt', '_pred'))
    
    return df_final

def get_metrics(pose_samples_folder, test_image_folder):
    '''
    Compute the metrics for the classification 

    Parameters
    ----------
    pose_samples_folder : str 
        Folder where to find the csvs_out generated after the model 'training'
    test_image_folder : str
        Folder containing the test images split in folders by class
    labels_folder : str
        Folder containing the labels of the test images split in folders by class
    Return
    -------
    None
    '''

    df_results = compute_final_results(pose_samples_folder, test_image_folder)
    ground_truth = df_results.Class_gt
    predictions = df_results.Class_pred

    # Matrice de confusion
    cm = confusion_matrix(ground_truth, predictions)

    # Calcul des métriques de classification
    accuracy = accuracy_score(ground_truth, predictions)
    precision = precision_score(ground_truth, predictions)
    recall = recall_score(ground_truth, predictions)
    f1 = f1_score(ground_truth, predictions)

    # Courbe ROC
    #fpr, tpr, _ = roc_curve(ground_truth, predictions)
    #roc_auc = auc(fpr, tpr)

    # Affichage de la matrice de confusion

    print('----------------------------------------')
    print('Matrice de confusion')
    print('----------------------------------------')
    print(cm)

    # Affichage des métriques de classification
    print('----------------------------------------')
    print('Metrics')
    print('----------------------------------------')
    print(f"Accuracy : {accuracy:.2f}")
    print(f"Precision : {precision:.2f}")
    print(f"Recall : {recall:.2f}")
    print(f"F1 Score : {f1:.2f}")

    # Affichage de la courbe ROC
    #plt.figure()
    #plt.plot(fpr, tpr, color='darkorange', lw=2, label='Courbe ROC (AUC = {:.2f})'.format(roc_auc))
    #plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    #plt.xlabel('Taux de faux positifs')
    #plt.ylabel('Taux de vrais positifs')
    #plt.title('Courbe ROC')
    #plt.legend(loc="lower right")
    #plt.show()

    # Affichez un rapport de classification détaillé
    print('----------------------------------------')
    print('Classification report')
    print('----------------------------------------')
    print(classification_report(ground_truth, predictions))