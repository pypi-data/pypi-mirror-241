import streamlit as st
import os
from power_vision_AI_of_the_tiger.Classifier import classifier


st.title("Fall Detection Web App")

# Upload de la vidéo
uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])

# Widget pour choisir l'emplacement de sauvegarde de la vidéo
#save_path = st.file_uploader("Choose where to save the output video", type="", key="save_path")

# chemin vers les csv
pose_sample_folder = f"data/csv_out"

if uploaded_file is not None:
    # Temp video
    temp_video_path = os.path.join("/tmp", uploaded_file.name)
    with open(temp_video_path, "wb") as temp_video:
        temp_video.write(uploaded_file.getvalue())

    #get the name of the video
    filename = os.path.splitext(temp_video_path)[0] + '_out.mp4'

    # video process
    results_df = classifier.classify_video(video_path=temp_video_path, out_video_path=filename, pose_samples_folder=pose_sample_folder, display=False)

    # Affichage de la vidéo résultante
    video_file = open(temp_video_path, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    # Affichage du tableau de résultats
    st.write("Fall Detection Results:")
    st.write(results_df)