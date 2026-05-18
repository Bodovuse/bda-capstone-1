from pathlib import Path
from library import download_video, read_video_urls
import time
from multiprocessing import Pool

Path("videos").mkdir(exist_ok=True)
url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"

videoFile = "data/video_urls.csv"

start = time.perf_counter()

if __name__ == "__main__":
    with Pool() as pool:
        results = pool.map(download_video, read_video_urls(videoFile))
#     #download_video(read_video_urls(videoFile))
#     read_video_urls(videoFile)
#     for url in read_video_urls(videoFile):
#         download_video(url)

end = time.perf_counter()
elapsed = end - start
parallel_time = round(elapsed, 2)
print(f"Parallel execution: {parallel_time}")
# serial_time = round(elapsed, 2)
# print(f"Serial execution: {serial_time}")
