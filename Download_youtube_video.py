from pytube import YouTube

link = input("Enter URL :")

yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

# print("Enter video format: ")

dn_option = int(input("Enter ontion: "))

dn_video = videos[dn_option]

dn_video.download()
print("Downloading ...")

print("Download completed.")
