# About:
   Creating a data engineering pipeline to curate a Speech-To-Text dataset from publicly available
lectures on NPTEL, to train speech recognition models.

# Requirements:
   Before you can use this project, you'll need to have the following software installed:  
   
   -> Ubuntu 22.04 (or) MacOS 12  
   -> Might work on Windows (not tested)  
   -> Python 3.8
      
# Setup Instructions:
   1. Clone this repository to your local machine.  
   ``` 
   git clone https://github.com/Jaavid25/DataEngineeringPipeline.git
   ``` 
   2. Install the required Python packages using pip.
   ```
   pip install -r requirements.txt. 
   ```  
   3. Setup a virtual environment by referring to this documentation,
   
      https://docs.python.org/3/library/venv.html
   
   4. Please ensure to have a good internet connection as the downloads may consume large bandwidth.  
   
# To run the scripts:
   ### 1. Downloading the lecture audios:  
   To download all the lecture audios from an NPTEL course webpage, run the **download_audio.py** with the following command,  
   ```
   python3 download_audio.py
   ```  
   Provide the url for an NPTEL cource page and the destination directory as an user input.  
   This python script will get links of all lectures and using **yt-dlp** tool to download all the lectures as audios in mp3 format in the specified        destination directory.
   
   ### 2. Downloading the transcript pdfs:  
   To download all the transcripts from the NPTEL course webpage, run the **download_transcripts.py** with the following command,
   ```
   python3 download_transcripts.py
   ```
   Provide the url for an NPTEL cource page and the destination directory as an user input.
   This python script will download all the transcripts as pdfs in the specified destination.
   
   ### 3. Pre-processing audio files:  
   Run the ***bash** script ***convert_audio.sh*** with the following commands,
   ```
   sudo chmod 755 convert_audio.sh
   ./convert_audio.sh
   ```  
   This bash script converts all the downloaded audios from mp3 to WAV format using ***ffmpeg library*** with a
   16KHz sampling rate, mono channel format. It parallelize the code across N CPUs, where
   N , path to the directory containing all audio files and Path to an output directory to store the converted files are user inputs.  
     
   Then, run the python script ***preprocess_audio.py*** by running the following command,
   ```
   python3 preprocess_audio.py
   ```
   This script will trim the first 10 and last 30 seconds from the audio files.  
   Provide the directory where the converted WAV files are stored as input directory and a directory to store the trimmed WAV as output directory as an      user input.
   ### 4. Pre-processing transcripts:  
   * Run the python script with the
   ### 5. Creating the training manifest file:  
   
   ### 6. Creating a dashboard:
# Observations on this process:
