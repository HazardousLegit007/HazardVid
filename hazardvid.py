import requests
from tqdm import tqdm
import pyfiglet

text = "HazardVid"
result = pyfiglet.figlet_format(text)
print(result)

social_handles = {
    "Twitter": "@HazardousLegit",
    "Facebook": "@HazardousLegit",
    "Instagram": "@HazardousLegit",
    "LinkedIn": "@HazardousLegit"
}

welcome_message = "Welcome to HazardousLegit Video Downloader!"

print(welcome_message)
print("You can find us on:")
for platform, handle in social_handles.items():
    print(f"{platform}: {handle}")

print ( ''' [ Coded By HazardousLegit ] ''' )
def download_video(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("Content-Length", 0))
    block_size = 1024  # 1 Kibibyte
    t = tqdm(total=total_size, unit='iB', unit_scale=True)

    with open(filename, "wb") as f:
        for data in response.iter_content(block_size):
            t.update(len(data))
            f.write(data)

    t.close()
    if total_size != 0 and t.n != total_size:
        print("ERROR, something went wrong")

url = input("Enter video url to download:")
filename = input("Enter the filename to save as:")
download_video(url, filename)









































