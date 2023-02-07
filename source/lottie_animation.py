import json
import streamlit as st

@st.cache()
def load_lottiefile(filepath: str) ->json:
    '''
    Objective: The objective of this fn. is to load a lottie animation (json) file 
    ---------

    Input: relative filepath to the animation json file
    -----

    Output: Json object
    ------
    
    '''
    with open(filepath, "r") as f:
        return json.load(f)

