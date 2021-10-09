
#!/usr/bin/env python3

# lists all mp4 files in video/ and convert them to mp3 under audio/
# pip3 install pydub
# unfortunately this requires ffmpg installed - sudo apt-get install ffmpeg on Linux.
# some python guru, please find a proper libray that does not have external depedencies


from pydub import AudioSegment
import os

def convert_video_to_audio(input_filename, output_filename):
    mp4 = AudioSegment.from_file(input_filename, "mp4")
    mp4.export(output_filename, format="mp3")

file_list = os.listdir('video/')
file_list_n = len(file_list)
for i in range(0,file_list_n,1):
    file_name = file_list[i]
    file_name_without_extension = os.path.splitext(file_name)[0]
    output_file_name_with_extension = file_name_without_extension + ".mp3"
    input_file_path = os.path.join('video', file_name)
    output_file_path = os.path.join('audio', output_file_name_with_extension)
    if file_name.endswith(".mp4"):
        print(input_file_path)
        convert_video_to_audio(input_file_path, output_file_path)
