from pytube import YouTube
# import os

# recieving the YouTube link 
link = input("Copie aqui o link do vídeo do YouTube que deseja baixar: ")
yt = YouTube(link)

# function to download the video in the highest rsolution
def download_video(yt):
    try:
        # getting the highest resolution
        yd = yt.streams.get_highest_resolution()
        # downloading the video
        yd.download()
        print("Download Concluído!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


download_video(yt)



