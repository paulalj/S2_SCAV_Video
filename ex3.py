import subprocess
import sys
from os import remove

def read_output(delete):
    # En aquest bloc creem el fitxer .txt i l'escrivim
    file = open('BBB_tracks.txt', 'w+')
    subprocess.run(["ffmpeg", "-i", "BBB_container.mp4"],
                   stdout=file, stderr=subprocess.STDOUT)
    file.close()

    doc_list=[] # Creem una llista buida on guardarem les paraules del document
    c=0 # Creem un contador que ens servirà per recórrer la llista
    er=0 # Aquesta variable ens servirà per saber si hi ha algun error

    # En aquest bloc obrim el .txt i el llegim paraula per paraula
    file = open('BBB_tracks.txt', 'r')
    for line in file:
        for word in line.split():
            doc_list.append(word)

    # En aquest bloc comparem les paraules del document amb "Video" i "Audio"
    # i imprimim la següent, que és l'standard que busquem. També fem altres
    # coses definides a l'interior.
    for i in doc_list:
        if (i=="Video:"):
            print('Video standard: ', doc_list[c+1])
            er=1
        if (i=="Audio:"):
            print('Audio standard: ', doc_list[c+1])
            er=1

        # En aquesta línia diem per pantalla si l'àudio està en mono o stereo
        if (i=="Hz,"):
            print('L\'àudio està en ', doc_list[c+1])
        # En aquesta línia diem la duració del vídeo
        if (i == "Duration:"):
            print('La duració del vídeo és: ', doc_list[c + 1])
        # En aquesta línia diem el bitrate
        if (i == "kb/s"):
            print('El bitrate és: ', doc_list[c - 1])

        c = c + 1

    # Imprimim el missatge d'ERROR si no ha hagut cap standard
    if (er==0):
        print("ERROR")

    file.close()

    if (delete==1):
        remove('/home/paula/SCAV/BBB_tracks.txt')


def main():
    #Preguntem a l'usuari si voldrà eliminar el fitxer que es crearà
    delete=int(input('Voldràs esborrar l\'arxiu creat? \n 0-No \n 1-Sí \n'))

    # Cridem a la funció que ens llegirà les tracks del contenidor
    read_output(delete)

if __name__ == "__main__":
    main()