import streamlit as st
from audio_recorder_streamlit import audio_recorder
from source import audio_signal_processing
from source import lottie_animation
from source import rand_no_gen
from source import get_folder_vloume
from streamlit_lottie import st_lottie

import collections
import sys
import os
import shutil

import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title= "Sound Cluster Visualization",
    layout= "wide",
    initial_sidebar_state= "collapsed"
)

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}

            

           
			</style>
			"""

st.markdown(streamlit_style, unsafe_allow_html=True)

st.title("Machine State's Visualization using :sound:")

text = '<p style="font-family:Roboto; color:#fff; font-size: 20px;">This app helps you collect audio data of <b>various states</b> of your machine, in-browser and visualize their similarity/dissimilarity using interactive plots. </p>'
st.markdown(text, unsafe_allow_html=True)


USER_ID = rand_no_gen.generate_16_digit_number()
st.text(USER_ID)


left_col_rowOne, mid_col_rowOne, right_col_rowOne = st.columns(3, gap = 'medium')
with left_col_rowOne:
    lottie_display = lottie_animation.load_lottiefile('assets/animation-select-panda.json')

    st_lottie(
        lottie_display,
        loop= True,
        height = 350,
        width = 350
    )

with mid_col_rowOne:
    no_of_classes = st.slider(
        label = "How many types of machine states do you have?",
        max_value= 3,
        min_value= 2,
        value = 2,
        step =1,
        key= 123,
        help = "For example, if you have data from both NORMAL and MALFUNCTIONING machine, this value is 2."
    )

    if no_of_classes == 2:

        class_names = []
        class_1 = st.text_input(
            label= 'Name the FIRST state of your machine',
            value = "NORMAL",
            max_chars= 20,
            key = 456)

        class_names.append(class_1)

        class_2 = st.text_input(
            label= 'Name the SECOND state of your machine',
            value = "FAULTY",
            max_chars= 20,
            key = 789)

        class_names.append(class_2)

        # This part of the code checks if the class names get repeated, if so, then a error message is thrown back.
        counts_object = collections.Counter(class_names)
        class_freq = list(counts_object.values())
        for value in class_freq:
            if value > 1:
                st.error("Do not repeat names. If you see this error refresh your browser to start again.")
                sys.exit() # If class_names are repeated, we do not let the user proceed any further. Class names has to be unique

    if no_of_classes == 3:
        class_names = []
        class_1 = st.text_input(
            label= 'Name the FIRST state of your machine',
            value = "NORMAL",
            max_chars= 20,
            key = 101112)
        class_names.append(class_1)

        class_2 = st.text_input(
            label= 'Name the SECOND state of your machine',
            value = "FAULTY",
            max_chars= 20,
            key = 131415)
        class_names.append(class_2)

        class_3 = st.text_input(
            label= 'Name the THIRD state of your machine',
            value = "EXTREMELY_FAULTY",
            max_chars= 20,
            key = 161718)
        class_names.append(class_3)

        # This part of the code checks if the class names get repeated, if so, then a error message is thrown back.
        counts_object = collections.Counter(class_names)
        class_freq = list(counts_object.values())
        for value in class_freq:
            if value > 1:
                st.error("Do not repeat names. If you see this error refresh your browser to start again.")
                sys.exit()

with right_col_rowOne:
    pick_DURATION = st.slider(
            label= "Select the duration of recording (in seconds)",
            value = 15,
            min_value= 15,
            max_value= 45,
            step= 15,
            help= 'The more the duration - the better the sound is represented, but more is the time to get the results.',
            key=222324

        )
    pick_DURATION = float(pick_DURATION)

    pick_SR = st.radio(
            label = "Select the sampling rate of the audio",
            options= (4000, 8000,16000),
            horizontal= False,
            label_visibility= "visible",
            key= 192021,
            help= 'The more your sampling rate the better the sound is represented, but more is the time to get the results.'

        )

    pick_SR = int(pick_SR)

count_no_of_wav_files = len([f for f in os.listdir('./recordings_two_class/') if f.endswith('.wav')]) + len([f for f in os.listdir('./recordings_three_class/') if f.endswith('.wav')])

folder_paths = ['./recordings_two_class/', './recordings_three_class/']
total_size = 0
for folder_path in folder_paths:
    total_size += get_folder_vloume.get_total_size(folder_path)


# This is ROW TWO
left_col_rowTwo, first_mid_col_rowTwo, second_right_col_rowTwo, right_col_rowTwo = st.columns(4, gap = 'medium')

with first_mid_col_rowTwo:
    text = '<div style="background-color: black; border-radius: 10px; padding: 14px; border: 2px solid red; font-family:Roboto; color:white; font-size: 18px; text-align: center;">Total no. of files saved till date: <b>' + str(count_no_of_wav_files) + '</b> </div>'
    st.markdown(text, unsafe_allow_html=True)
with second_right_col_rowTwo:
    text = '<div style="background-color: black; border-radius: 10px; padding: 14px; border: 2px solid red; font-family:Roboto; color:white; font-size: 16px; text-align: center;">Total volume (in MB) saved till date: <b>' + str(total_size) + '</b> </div>'
    st.markdown(text, unsafe_allow_html=True)





# This is ROW THREE
if no_of_classes == 2:

    left_col_rowThree, right_col_rowThree = st.columns([1,3], gap = 'small')

    with left_col_rowThree:
        class_name_One = class_names[0]
        text = '<p style="font-family:Roboto; color:#fff; font-size: 24px;"><b>State</b>: </p>'
        st.markdown(text, unsafe_allow_html=True)
        st.warning(class_name_One)

        audio_bytesOne = audio_recorder(
            text=f"Click on the mic to record for {int(pick_DURATION)} secs", 
            recording_color= "#D70040",
            neutral_color= "#F4EA56",
            energy_threshold=(-1.0, 1.0), 
            sample_rate= pick_SR,
            pause_threshold= pick_DURATION,
            key= "abc")  # object audio_recorder inetiated.

        

        if audio_bytesOne:
            st.audio(data=audio_bytesOne, format="audio/wav")

            if st.button("save", key = 252627):
                filename = f"./recordings_two_class/{class_name_One}.wav"
                # st.text("file saved") # dispaly the file name of the saved audio.
                with open(filename, "wb") as file:
                    file.write(audio_bytesOne)
                    st.success("Audio file saved succesfully.")
                    # st.info(filename)

        class_name_Two = class_names[1]
        text = '<p style="font-family:Roboto; color:#fff; font-size: 24px;"><b>State</b>: </p>'
        st.markdown(text, unsafe_allow_html=True)
        st.warning(class_name_Two)

        audio_bytesTwo = audio_recorder(
            text=f"Click on the mic to record for {int(pick_DURATION)} secs", 
            recording_color= "#D70040",
            neutral_color= "#F4EA56",
            energy_threshold=(-1.0, 1.0), 
            sample_rate= pick_SR,
            pause_threshold= pick_DURATION,
            key = 'def')  # object audio_recorder inetiated.

        if audio_bytesTwo:
            st.audio(data=audio_bytesTwo, format="audio/wav")

            
            if st.button("save", key=28293031):
                
                filename = f"./recordings_two_class/{class_name_Two}.wav"
                # st.text("file saved") # dispaly the file name of the saved audio.
                with open(filename, "wb") as file:
                    file.write(audio_bytesTwo)
                    st.text("Audio file saved succesfully.")
                    # st.info(filename)

    with right_col_rowThree:
        text = '<p style="font-family:Roboto; color:#fff; font-size: 24px;"><b>Visualizations</b> </p>'
        st.markdown(text, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["PCA", "T-Sne", "UNET"])

        with tab1: #PCA

            if os.path.exists('./recordings_two_class/NORMAL.wav') and os.path.exists('./recordings_two_class/FAULTY.wav'):

                # Visualize the 3-second segments of the NORMAL.wav file
                
                normal_mfcc_pca = audio_signal_processing.process_signal_PCA('./recordings_two_class/NORMAL.wav')
                faulty_mfcc_pca = audio_signal_processing.process_signal_PCA('./recordings_two_class/FAULTY.wav')

                # Create the scatter plot using Plotly
                normal_df = pd.DataFrame({'x': normal_mfcc_pca[:, 0], 'y': normal_mfcc_pca[:, 1], 'class': 'NORMAL'})
                faulty_df = pd.DataFrame({'x': faulty_mfcc_pca[:, 0], 'y': faulty_mfcc_pca[:, 1], 'class': 'FAULTY'})
                df = pd.concat([normal_df, faulty_df])

                # st.write(df.shape)
                fig = px.scatter(
                    df, 
                    x='x', 
                    y='y', 
                    color='class',
                    labels={"x": "Dimension One", "y": "Dimension Two"})

                st.plotly_chart(fig)

            else:
                text = '<p style="font-family:Roboto; color:red; font-size: 28px;"><b>You have not saved your files from the left</b> </p>'
                st.markdown(text, unsafe_allow_html=True)

                lottie_display = lottie_animation.load_lottiefile('assets/animation-select-file-save.json')

                st_lottie(
                    lottie_display,
                    loop= True,
                    height = 250,
                    width = 400,
                    key = "lottie2"
                )

            # st.header("A cat")
            # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)



        with tab2:
            
            if os.path.exists('./recordings_two_class/NORMAL.wav') and os.path.exists('./recordings_two_class/FAULTY.wav'):
                normal_mfcc_tsne = audio_signal_processing.process_signal_tSNE('./recordings_two_class/NORMAL.wav')

                faulty_mfcc_tsne = audio_signal_processing.process_signal_tSNE('./recordings_two_class/FAULTY.wav')

                # Create the scatter plot using Plotly
                normal_df = pd.DataFrame({'x': normal_mfcc_tsne[:, 0], 'y': normal_mfcc_tsne[:, 1], 'class': 'NORMAL'})
                faulty_df = pd.DataFrame({'x': faulty_mfcc_tsne[:, 0], 'y': faulty_mfcc_tsne[:, 1], 'class': 'FAULTY'})
                df = pd.concat([normal_df, faulty_df])
                # st.title(df.shape)
                fig = px.scatter(
                    df, 
                    x='x', 
                    y='y', 
                    color='class', 
                    labels={"x": "Dimension One", "y": "Dimension Two"})
                # st.write(df.columns)

                st.plotly_chart(fig)

            else:
                text = '<p style="font-family:Roboto; color:red; font-size: 28px;"><b>You have not saved your files from the left</b> </p>'
                st.markdown(text, unsafe_allow_html=True)

                lottie_display = lottie_animation.load_lottiefile('assets/animation-select-file-save.json')

                st_lottie(
                    lottie_display,
                    loop= True,
                    height = 250,
                    width = 400,
                    key = "lottie3"
                )


        with tab3:
            lottie_display = lottie_animation.load_lottiefile('assets/animation-select-coming-soon1.json')

            st_lottie(
                lottie_display,
                loop= True,
                height = 400,
                width = 800,
                key = "lottie4"
            )
            

if no_of_classes ==3:
    lottie_display = lottie_animation.load_lottiefile('assets/animation-select-coming-soon2.json')

    st_lottie(
        lottie_display,
        loop= True,
        height = 300,
        width = 400,
        key = "lottie5"
    )

# left_col_rowFour, mid_col_rowFour, right_col_rowFour = st.columns(3, gap = 'medium')
# with mid_col_rowFour:
#     if st.button("Delete all audio files"):
#         # # Deleting al files from any previous session in both the recordings folders
#         folder_to_del_twoClass = './recordings_two_class/'
#         for filename in os.listdir(folder_to_del_twoClass):
#             file_path = os.path.join(folder_to_del_twoClass, filename)
#             try:
#                 if os.path.isfile(file_path) or os.path.islink(file_path):
#                     os.unlink(file_path)
#                 elif os.path.isdir(file_path):
#                     shutil.rmtree(file_path)
#                     st.info("Button pressed! Running code block...")
#             except Exception as e:
#                 st.write('Failed to delete %s. Reason: %s' % (file_path, e))

#         folder_to_del_threeClass = './recordings_three_class/'
#         for filename in os.listdir(folder_to_del_threeClass):
#             file_path = os.path.join(folder_to_del_threeClass, filename)
#             try:
#                 if os.path.isfile(file_path) or os.path.islink(file_path):
#                     os.unlink(file_path)
#                 elif os.path.isdir(file_path):
#                     shutil.rmtree(file_path)
#                     st.info("Button pressed! Running code block...")
#             except Exception as e:
#                 st.write('Failed to delete %s. Reason: %s' % (file_path, e))


    


# left_col_rowFour, mid_col_rowFour, right_col_rowFour = st.columns(3, gap = 'medium')
    # Code block
    # result = "Code block executed"
    # st.write("Result:", result)

# # # Deleting al files from any previous session
# folder_to_del_twoClass = './recordings_two_class/'
# for filename in os.listdir(folder_to_del_twoClass):
#     file_path = os.path.join(folder_to_del_twoClass, filename)
#     try:
#         if os.path.isfile(file_path) or os.path.islink(file_path):
#             os.unlink(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#     except Exception as e:
#         st.write('Failed to delete %s. Reason: %s' % (file_path, e))


