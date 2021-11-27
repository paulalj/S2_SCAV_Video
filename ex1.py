import subprocess

def mot_vec():
    subprocess.call(["ffmpeg", "-flags2", "+export_mvs", "-i", "BBB_short.mp4",
                     "-vf", "codecview=mv=pf+bf+bb", "BBB_motvec.mp4"])


def main():
    # Cridem a la funció per veure els macroblocks i els motion vectors
    mot_vec()

if __name__ == "__main__":
    main()