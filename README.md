# Machine States Identification from Audio
The **objective** of this project is to visualise multiple states of machines using the audio emitted by each of the states. Here, by states, we loosely refer to the conditions of the machine such as GOOD vs. MALFUNCTIONING; BRAND NEW vs. WORKS DECENTLY vs.DILIAPIDATED etc.
#### Possible Use Cases: 
* In an industrail setting where you quickly need to compare if one machine is functioning as good as another.

#### Features:
* In browser recording of sound
* Multiple dimensionality reduction techniques to better visualise overlap or seperation between the states.

#### Best suited for:
* Non human sounds, speechs etc and primarily machine sounds.

#### Folder and file structure
1. `main.py`contains the streamlit app.
2. `source` contains the function definitions.
3. **Note**: there are two txt files in the `recordings_three_class` and `recordings_two_class` - do not remove them.


#### Audio feature extraction presently is through
1. MFE
2. Proposed - SPectral Grating

#### Dimensionality reduction:
1. Presently through: PCA and t-SNE
2. Proposed: UNET
