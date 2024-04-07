from pytube import YouTube

# recieving the YouTube link 
link = input("Copie aqui o link do vídeo do YouTube que deseja baixar: ")
yt = YouTube(link)




print(f"Title: {yt.title}")