import ex1
import ex2
import ex3
import ex4

def main():
    # Cridem a la funció per veure els macroblocks i els motion vectors
    ex1.mot_vec()

    # Cridem a la funció per tallar el vídeo un minut
    ex2.cut_video()
    # Cridem a la funció per convertir el vídeo a mp3
    ex2.export_mp3()
    # Cridem a la funció per convertir el vídeo a aac
    ex2.export_aac()
    # Cridem a la funció per juntar-ho tot en un contenidor
    ex2.container()

    # Preguntem a l'usuari si voldrà eliminar el fitxer que es crearà
    delete = int(input('Voldràs esborrar l\'arxiu creat? \n 0-No \n 1-Sí \n'))
    # Cridem a la funció que ens llegirà les tracks del contenidor
    ex3.read_output(delete)

    # Cridem a la funció que ens afegirà els subtítols
    ex4.subtitles()

if __name__ == "__main__":
    main()