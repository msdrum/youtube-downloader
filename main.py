from pytube import YouTube
import threading

# recieving the YouTube link 
link = input("Copie aqui o link do vídeo do YouTube que deseja baixar: ")
yt = YouTube(link)

print(f"Baixando: {yt.title}  por favor, aguarde.")

# function to download the video in the highest rsolution
def download_video(yt):
    try:
        # getting the highest resolution
        yd = yt.streams.get_highest_resolution()

        
        # function to improve the download time
        def download():
            yd.download()
            print("Download Concluído!")

        download_thread = threading.Thread(target=download)
        download_thread.start()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


download_video(yt)



