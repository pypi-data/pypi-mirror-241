# functions to stream, record and display the video

import cv2
from moviepy.editor import VideoFileClip

#############################
#    CAPTURE & STREAM       #
#############################

def stream_video(video_path):
    # j'ouvre la vidéo depuis le fichier
    cap = cv2.VideoCapture(video_path)

    # je vérifie si la vidéo est ouverte correctement
    if not cap.isOpened():
        print("Erreur: Impossible d'ouvrir la vidéo.")
        return

    # je regarde les propriétés de la vidéo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # je crée une fenêtre OpenCV pour le streaming
    cv2.namedWindow('Video Stream', cv2.WINDOW_NORMAL)

    while True:
        # je lis le prochain frame de la vidéo
        ret, frame = cap.read()

        # je vérifie si la vidéo est terminée
        if not ret:
            print("Fin de la vidéo.")
            break

        # j'affiche le frame dans la fenêtre
        cv2.imshow('Video Stream', frame)

        # j'attends 30 millisecondes (j'ai mis cette valeur au hasard)
        if cv2.waitKey(30) & 0xFF == 27:  
            break

    # je libère la vidéo et j'efface la fenêtre
    cap.release()
    cv2.destroyAllWindows()


def enregistrer_video(output_path, capture_source=0, resolution=(640, 480), fps=30.0):
    cap = cv2.VideoCapture(capture_source)

    if not cap.isOpened():
        print("Attention, vous n'avez pas branché votre webcam.")
        return

    # je définis la résolution et le FPS
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
    cap.set(cv2.CAP_PROP_FPS, fps)

    # je définis le codec et je crée l'objet VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  
    out = cv2.VideoWriter(output_path, fourcc, fps, resolution)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Fin de la capture vidéo.")
            break

        out.write(frame)

        cv2.imshow('Enregistrement vidéo', frame)

        # j'attends 1 milliseconde 
        if cv2.waitKey(1) & 0xFF == 27:  
            break

    # je libère la capture vidéo et le VideoWriter
    cap.release()
    out.release()

    # j'efface la fenêtre d'affichage 
    cv2.destroyAllWindows()


def afficher_video(video_path):
    
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Erreur: Impossible d'ouvrir la vidéo.")
        return

    # propriétés de la vidéo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # je crée une fenêtre OpenCV pour afficher la vidéo
    cv2.namedWindow('Lecture de la vidéo', cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Fin de la vidéo.")
            break

        cv2.imshow('Lecture de la vidéo', frame)

        if cv2.waitKey(30) & 0xFF == 27:  
            break

    cap.release()
    cv2.destroyAllWindows()

def capturer_et_enregistrer_video(output_path=None, capture_source=0, resolution=(640, 480), fps=30.0):
    # début de la capture vidéo
    cap = cv2.VideoCapture(capture_source)

    # vérification de la capture vidéo est ouverte correctement
    if not cap.isOpened():
        print("Erreur: Impossible d'ouvrir la capture vidéo.")
        return

    # définition de la résolution et du FPS
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
    cap.set(cv2.CAP_PROP_FPS, fps)

    if output_path:
        # définition du codec et création de l'objet VideoWriter
        fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
        out = cv2.VideoWriter(output_path, fourcc, fps, resolution)

    while True:
        ret, frame = cap.read()

        # vérification de la fin de la capture vidéo
        if not ret:
            print("Fin de la capture vidéo.")
            break

        # enregistrement de la frame dans le chemin de sortie
        if output_path:
            out.write(frame)

        # affichage de la frame dans une fenêtre
        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()

    # si un chemin de sortie est spécifié on libère le VideoWriter
    if output_path:
        out.release()

    # on détruit la fenêtre d'affichage
    cv2.destroyAllWindows()



#############################
#         CONVERT           #
#############################

def convertir_webm_en_mp4(input_path, output_path):
    
    clip = VideoFileClip(input_path)

    clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    print(f"Conversion de {input_path} vers {output_path} effectuée avec succès.")


def convertir_mp4_en_avi(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("Erreur: Impossible d'ouvrir la vidéo.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # définition du codec et création de l'objet VideoWriter pour le fichier AVI
    fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Fin de la vidéo.")
            break

        out.write(frame)

    cap.release()
    out.release()

    print(f"Conversion de {input_path} vers {output_path} effectuée avec succès.")


# execution
# if __name__ == '__main__':
    
#     #stream_video('/home/alexandre.appolaire@Digital-Grenoble.local/Documents/ACV/Partie_2/data/fall.mp4')
#     capturer_et_enregistrer_video('/home/alexandre.appolaire@Digital-Grenoble.local/Documents/ACV/Partie_2/data/fall_test.mp4')