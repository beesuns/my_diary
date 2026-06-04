import os
import subprocess

urls_file = r"C:\Users\babys\Music\WORKOUT\1\url.txt"
output_directory = r"C:\Users\babys\Music\WORKOUT\1"

os.makedirs(output_directory, exist_ok=True)


if not os.path.exists(urls_file):
    print(f"Error: {urls_file} not found.")
    exit(1)

with open(urls_file, "r") as file:
    album_urls = [line.strip() for line in file if line.strip()]

if not album_urls:
    print("No URLs found in urls.txt.")
    exit(1)

for url in album_urls:
    print(f"Downloading tracks from: {url}")
    try:
        # Run the spotdl command to download tracks
        subprocess.run(
            ["spotdl", "--output", output_directory, url],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Failed to download tracks from {url}. Error: {e}")

print("Download process completed.")
