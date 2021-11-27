import subprocess
import requests

def subtitles():
    # Aquest és l'enllaç d'on ens descarreguem els subtítols
    url="https://drive.google.com/u/0/" \
        "uc?id=1aY2nY7bXvbM3wAZsS_C-PBGH_SLienvg&export=download"
    # Amb aquesta comanda guardem el contingut de l'enllaç
    url_doc=requests.get(url)

    # Amb aquest bloc obrim l'arxiu on escriurem els subtítols
    # procedents de l'enllaç
    with open("subtitles.srt","w") as file:
        file.write(url_doc.text)

    # Amb aquesta comanda afegim els subtítols al vídeo
    subprocess.call(["ffmpeg", "-i", "BBB_short.mp4", "-vf",
                    "subtitles=subtitles.srt", "BBB_subt.mp4"])

def main():
    # Cridem a la funció que ens afegirà els subtítols
    subtitles()

if __name__ == "__main__":
    main()