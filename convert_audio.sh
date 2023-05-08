#!/bin/bash

# Set the source and destination directories
echo "Please type the path to the source directory:"
read source_dir
echo "Please type the path to the deoostination directory:"
read dest_dir
echo "Please type the number of threads:"
read N

# Check if the source directory exists
if [ ! -d "$source_dir" ]; then
    echo "The source directory doesn't exist."
    exit 1
fi

# Check if the destination directory exists, create it if it doesn't
if [ ! -d "$dest_dir" ]; then
    mkdir -p "$dest_dir"
fi

echo "Converting audio files"

# Convert all MP3 files in the source directory to WAV and save them in the destination directory
for file in "$source_dir"/*.mp3; do
    if [ -f "$file" ]; then
        # Get the base filename without the extension
        filename=$(basename -- "$file")
        filename="${filename%.*}"

        # Convert the file to WAV format and save it in the destination directory
        ffmpeg -threads "$N" -i "$file" -ar 16000 "$dest_dir/$filename.wav"
    fi
done

echo "Convertion of audio files from mp3 to WAV completed"
