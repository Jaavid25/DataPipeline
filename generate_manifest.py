import json
import audiosegment
import os

def get_audio_duration(input_path):
    input_file = audiosegment.from_file(input_path)
    duration = input_file.duration_seconds
    return duration

def write_to_jsonl(data,file_name):
    with open(file_name, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')

audio_dir = input("Enter the audio directory: ")
transcript_dir = input("Enter the transcript directory: ")
manifest_name  = input("Enter the name of the manifest file: ")
audio_dir_files = os.listdir(audio_dir)
audio_files = list()
durations = list()
for audio_dir_file in audio_dir_files:
    if  audio_dir_file.endswith('.wav'):
        audio_files.append(audio_dir_file)
        durations.append(get_audio_duration(audio_dir + "/" + audio_dir_file))

transcript_dir_files = os.listdir(transcript_dir)
transcripts = list()
for transcript_dir_file in transcript_dir_files:
    if  transcript_dir_file.endswith('.txt'):
        transcripts.append( open(transcript_dir + "/" + transcript_dir_file,"rt").read() )


if len(audio_files) != len(transcripts):
    print("The number of audio files and transcript files do not match. Taking the smaller number of files.")
    print("Number of audio files: ", len(audio_files))
    print("Number of transcript files: ", len(transcripts))
    if len(audio_files) > len(transcripts):
        audio_files = audio_files[:len(transcripts)]
        durations = durations[:len(transcripts)]
    elif len(audio_files) < len(transcripts):
        transcripts = transcripts[:len(audio_files)]

data = list()
for i in range(len(audio_files)):
    data.append({"audio_filepath": audio_files[i], "duration":durations[i], "text": transcripts[i]})

write_to_jsonl(data, manifest_name)