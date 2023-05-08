# import pandas as pd

import os
import audiosegment
import pandas as pd
import streamlit as st


# set the path to your directory of WAV files
audio_directory = input("audio directory path:")
text_directory = input("transcript directory path:")

# loop through all the WAV files in the directory
audio_files = os.listdir(audio_directory)
audio_files.sort()

# loop through all the text files in the directory
transcript_files = os.listdir(text_directory)
transcript_files.sort()

if len(audio_files) != len(transcript_files):
    print("The number of audio files and transcript files do not match. Taking the smaller number of files.")
    print("Number of audio files: ", len(audio_files))
    print("Number of transcript files: ", len(transcript_files))
    if len(audio_files) > len(transcript_files):
        audio_files = audio_files[:len(transcript_files)]
    elif len(audio_files) < len(transcript_files):
        transcript_files = transcript_files[:len(audio_files)]


def audio_insights(audio_directory):
    total_duration_seconds = 0
    duration_per_file = list()
    #dict1 = dict()
    global audio_files

    for filename, i in zip( audio_files, range(len(audio_files))):
        if filename.endswith(".wav"):
            # load the WAV file and get its duration in seconds
            filepath = os.path.join(audio_directory, filename)
            wav_file = audiosegment.from_file(filepath)
            duration_seconds = wav_file.duration_seconds
            #dict1.update({i: duration_seconds})
            duration_per_file.append(duration_seconds)
            # add the duration of the current file to the total duration
            total_duration_seconds += duration_seconds

    #print(dict1)
    # convert the total duration to hours
    total_duration_hours = total_duration_seconds / 3600

    return total_duration_hours, duration_per_file


def transcript_insights(text_directory):
    total_word_set = set()
    total_char_set = set()
    total_utterances = 0
    no_of_words_per_file = list()
    no_of_char_per_file = list()
    global transcript_files
  
    for filename in  transcript_files:
        if filename.endswith(".txt"):
            # open the text file and read its contents
            filepath = os.path.join(text_directory, filename)
            with open(filepath, 'r') as file:
                text = file.read()

            # split the text into words and add them to the set
            word_list = text.split()
            word_set = set(word_list)
            total_word_set = total_word_set.union(word_set)
            word_count = len(word_list)
            no_of_words_per_file.append(word_count)

            # add the characters to the character set
            char_set = set(text) - {'\n', '\x0c', '\uf0b6', '\uf061', '\uf071', '\uf02b', '\uf0b4', '\uf073', '–', 'ˆ', '“', '‘'}
            total_char_set = total_char_set.union(char_set)
            char_count = len(char_set)
            no_of_char_per_file.append(char_count)

            # split the text into paragraphs based on double newline characters
            paragraphs = text.split('\n\n\n')

            # count the number of paragraphs
            num_paragraphs = len(paragraphs)

            # add up the total number of utterances
            total_utterances += num_paragraphs

    # count the number of unique words in all the text files
    total_vocab_size = len(total_word_set)

    # count the number of unique characters in all the text files
    # print(total_char_set)
    total_alphabet_size = len(total_char_set)

    return total_char_set, total_utterances, total_vocab_size, total_alphabet_size, no_of_words_per_file, no_of_char_per_file


duration, duration_per_file = audio_insights(audio_directory)
char_set, utterance, vocabulary, alphabet, words_per_file, char_per_file = transcript_insights(text_directory)

global_statistics = [{'Total Number of hours': duration,
             'Total Number of utterances': utterance,
             'Vocabulary size': vocabulary,
             'Alphabet size': alphabet}]

global_statistics_df = pd.DataFrame(global_statistics)
per_file_statistics_df = pd.DataFrame(duration_per_file, columns=['Duration(secs)'])
per_file_statistics_df['words'] = words_per_file
per_file_statistics_df['ch'] = char_per_file
print(global_statistics_df)
print(per_file_statistics_df)


st.write("# Global Statistics")
st.write(global_statistics_df)
st.write("# Alphabhets")
st.write(char_set)
st.write("# Histograms")
st.write("## Duration per file")
st.bar_chart(per_file_statistics_df["Duration(secs)"])
st.write("## words per file")
st.bar_chart(per_file_statistics_df["words"])
st.write("## characters per file")
st.bar_chart(per_file_statistics_df["ch"])
