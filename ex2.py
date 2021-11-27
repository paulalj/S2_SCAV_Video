import subprocess

def cut_video():
    subprocess.call(
        ["ffmpeg", "-ss", "0:05", "-i", "BBB.mp4", "-c", "copy", "-t",
         "1:00", "BBB_1min.mp4"])

def export_mp3():
    subprocess.call(["ffmpeg", "-i", "BBB_1min.mp4", "-vn", "-c:a",
                     "libmp3lame", "BBB_mp3.mp3"])

def export_aac():
    # El bit rate del mp4 és 128kb per defecte, per això amb la comanda
    # aquesta el baixem a 64kb
    subprocess.call(["ffmpeg","-i", "BBB_1min.mp4", "-c:a", "libfdk_aac",
                     "-b:a", "64k", "BBB_aac.aac"])

def container():
    subprocess.call(["ffmpeg", "-i", "BBB_1min.mp4", "-i", "BBB_mp3.mp3", "-i",
                     "BBB_aac.aac", "-c:v", "copy", "-c:a", "copy", "-map",
                     "0:0", "-map", "1:a", "-map", "2:a", "BBB_container.mp4"])

def main():
    # Cridem a la funció per tallar el vídeo un minut
    cut_video()

    #Cridem a la funció per convertir el vídeo a mp3
    export_mp3()

    #Cridem a la funció per convertir el vídeo a aac
    export_aac()

    #Cridem a la funció per juntar-ho tot en un contenidor
    container()

if __name__ == "__main__":
    main()