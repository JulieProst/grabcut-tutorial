from pathlib import Path

import cv2
import streamlit as st

IMAGES_FOLDER = Path(__file__).parent / "images"
RAW_KEY = "raw"
BINARIZED_KEY = "binarized"
MASK_KEY = "mask"
SEGMENTED_KEY = "segmented"

st.set_page_config(
    page_title="Segmentation Visualization",
    layout="wide",
)

st.title("Segmentation Visualization")

image_names = [file.name for file in Path(IMAGES_FOLDER / "raw").glob("**/*")]
selected_image_name = st.sidebar.selectbox(
    "Which image do you want to analyze?", image_names
)

(
    raw_column,
    binarized_column,
    mask_column,
    segmented_column,
) = st.columns(4)

columns = [
    {
        "column": raw_column,
        "name": RAW_KEY,
    },
    {
        "column": binarized_column,
        "name": BINARIZED_KEY
    },
    {
        "column": mask_column,
        "name": MASK_KEY
    },
    {
        "column": segmented_column,
        "name": SEGMENTED_KEY
    },
]


for column_dict in columns:
    column_name = column_dict['name']
    with column_dict["column"]:
        st.title(f"{column_name}")
        selected_image = cv2.imread(str(IMAGES_FOLDER / column_name / selected_image_name))
        st.image(selected_image)
