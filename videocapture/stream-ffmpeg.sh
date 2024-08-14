 ffmpeg -re -stream_loop -1 -i 2024-08-14_09-55-05.mkv -c:v libx264 -bf 0 -b:v 2M -profile:v main  -f rtsp rtsp://localhost:8554/mystream
