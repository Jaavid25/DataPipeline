# About:
   Creating a data engineering pipeline to curate a Speech-To-Text dataset from publicly available
lectures on NPTEL, to train speech recognition models.

# Requirements:
   Before you can use this project, you'll need to have the following software installed:  
   
   * MacOS 12 
   * Might work on Ubuntu  
   * Might work on Windows (not tested)  
   * Python 3.8
      
# Setup Instructions:
  ### ***Note:*** Visual studio build tools should be installed in Windows. python3-dev need to be installed in Ubuntu, can be installed by executing the following command.
   ```
   sudo apt install python3-dev
   
   ```
   1. Clone this repository to your local machine.  
   ``` 
   git clone https://github.com/Jaavid25/DataEngineeringPipeline.git
   ```  
   2. Setup a virtual environment by referring to this [documentation.](https://docs.python.org/3/library/venv.html)
      
   3. Install the required Python packages using pip.
   ```
   pip3 install -r requirements.txt 
   ``` 
   
   4. Please ensure to have a good internet connection as the downloads may consume large bandwidth.  
   
# Usage Instructions:  

   ### 1. Downloading the lecture audios:  
   To download all the lecture audios from an NPTEL course webpage, run the **download_audio.py** with the following command,  
   ```
   python3 download_audio.py
   ```  
   * Provide the url for an NPTEL cource page and the destination directory as an user input.  
   * This python script will get links of all lectures and downloads all the lectures as audios in mp3 format in the specified destination directory.
   
   ### 2. Downloading the transcript pdfs:  
   To download all the transcripts from the NPTEL course webpage, run the **download_transcripts.py** with the following command,
   ```
   python3 download_transcripts.py
   ```
   * Provide the url for an NPTEL cource page and the destination directory as an user input.
   * This python script will download all the transcripts as pdfs in the specified destination.
   
   ### 3. Pre-processing audio files:  
   Run the ***bash** script ***convert_audio.sh*** with the following commands,
   ```
   sudo chmod 755 convert_audio.sh
   ./convert_audio.sh
   ```  
   This bash script converts all the downloaded audios from `.mp3` to `.wav` format with a
   16KHz sampling rate, mono channel format. It parallelize the code across 'N' CPUs, where
   * 'N'  
   * path to the directory containing all audio files. 
   * Path to an output directory to store the converted files  
   are user inputs.  
     
   Then, run the python script ***preprocess_audio.py*** by running the following command,
   ```
   python3 preprocess_audio.py
   ```
   This script will trim the first 10 and last 30 seconds from the audio files.  
   Provide, 
   * the directory where the converted WAV files are stored as input directory and 
   * a directory to store the trimmed WAV as output directory 
   as an user input.
   ### 4. Pre-processing transcripts:  
   * Run the python script with the following command,
   ```
   python3 preprocess_transcripts.py
   ```  
   This script will,
   * Convert the PDF to raw text format, and save it as a separate `.txt` file.  
   * Convert all text to lowercase, and remove all punctuations.  
   * Convert all digits to their spoken form using the num2words library.  
   * Removes text segments which are unspoken in actual lecture.  
     
   For this script provide,  
   * Directory having the downloaded transcript pdfs,  
   * Output directory to store the processed `.txt` files,  
   as user inputs.  
   
   ### 5. Creating the training manifest file:  
   
   To create a ***training manifest file***, run the following command,
   ```
   python3 generate_manifest.py
   ```
   this script will create a JSON lines file where every line is a JSON object consisting of the following
   key-value pairs,  
   * audio_filepath: Local path to the audio file.  
   * duration: length of the audio file, in seconds.
   * text: Text corresponding to the audio file.  
     
   Provide,  
   * directory where the processed audio is,  
   * directory where the processed text is,  
   * filname for manifest file, `train_manifest.jasonl` 
   as user inputs.
   
   ### 6. Creating a dashboard:  
   To create a ***dashboard***, run the following command,  
   ```  
   streamlit run create_dashboard.py  
   ```  
   
   To this script, provide  
   * directory where processed audios are,  
   * directory where processed transcripts are  
   as user inputs.  
   
   This script will create a dashboard which will display the following four statistics at the top of the dashboard:
   * Total number of hours
   * Total number of utterances
   * Vocabulary Size
   * Alphabet Size  
   And also displays the,   
   * complete Alphabet list.  
   * plot histograms for the duration per file,  
   * number of words per file,  
   * number of characters per file.  
   
   ***Note :*** An utterance is taken as the segment spoken in one slide of the lecture due to some inconsistency in transcripts by default.  
   ***known issue:*** This can ask for the same input more than once, but works fine.
# Observations on this process:  

The observations in this process are,  
  
* Downloading of audios and transcripts is working well for other courses too. But only the courses with `https://nptel.ac.in/courses/course_id` type of urls but not the older website of NPTEL or archives.  
* In audio preprocesing, firts 10 seconds and last 30 seconds are removed since they had NPTEL introduction clip and credits (scrolling names) are there. It is removed since they are not necessary for further processing and also a considerable amount of space will be reduced.  
* In text preprocessing, there were text segments which are not actully spoken out. Like, The header section of the transcripts which has course title, faculty name, department, institution, lecture and topic. And also in many places time reference for the corresponding slides are given. Such text segments are removed.  
* while downloading transcripts, used selenium in head mode at first. But, at one place I had to scroll down and click to select language. But in head mode, could not acces the content below the screen visibility. Then tried ***headless*** mode to scroll down and click but it didn't work. Then notced that chrome has released new version ***headless==new*** which gives the entire content of the page.  
* In transcripts, noticed that there are many random newline characters (\n) and (\n\n). Hence, found difficult to split proper utterances. So, replaced the time reference of slide in video segments are replaced by (\n\n\n) to differentiate and split the utterances.
* In the webpage, non-uniform class names and more client-side rendering made it a bit challenging task to scrape them.


