import audiosegment
import os

# specify the input and output directories
input_dir = input("input directory: ")
output_dir = input("output directory  :")

#check if there's a directory else create one
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


print("Trimming first 10 and last 30 seconds of the audio files...")

# iterate through all .wav files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".wav"):


        # open the input file
        input_file = audiosegment.from_file(input_dir + "/" + filename)

        # calculate the duration of the first 10 and last 30 seconds
        first_10_seconds = 10
        last_30_seconds = input_file.duration_seconds - 30

        # trim the first 10 seconds
        first_trimmed_file = input_file[first_10_seconds * 1000:]  # convert to milliseconds

        # trim the last 10 seconds
        last_trimmed_file = input_file[:last_30_seconds * 1000]  # convert to milliseconds

        # concatenate the remaining audio segments
        remaining_file = first_trimmed_file[:-last_30_seconds * 1000] + last_trimmed_file

        # export the remaining file
        remaining_file.export(output_dir + "/" + filename, format='wav')
        
print("Trimming of audio files completed.")
