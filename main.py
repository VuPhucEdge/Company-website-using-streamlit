import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some orther text
st.header("The Best Company")
st.write(
    """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
)
st.subheader("Our Team")

# Prepare the columns
col1, col2, col3 = st.columns(3)

# make a dataframe with the company members
df = pandas.read_csv("data.csv")

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for infrc, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f"{row['first name'].title()} {row['last name']}.title()")
        # Add member's role in the company
        st.write(row['role'])
        # Add member's photo
        st.image("images/"+row['image'])

# Add content to the first column
with col2:
    # Iterate over only the first four rows
    for infrc, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(f"{row['first name'].title()} {row['last name']}.title()")
        # Add member's role in the company
        st.write(row['role'])
        # Add member's photo
        st.image("images/"+row['image'])

# Add content to the first column
with col3:
    # Iterate over only the first four rows
    for infrc, row in df[8:].iterrows():
        # Add member's first and last names
        st.subheader(f"{row['first name'].title()} {row['last name']}.title()")
        # Add member's role in the company
        st.write(row['role'])
        # Add member's photo
        st.image("images/"+row['image'])
