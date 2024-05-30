import streamlit as st
import numpy as np
import pandas as pd
import os

accueil = "Bonjour " + os.environ["USERNAME"]

st.write(accueil)

st.markdown("""# Toto en short
## sous titre de Totot
Toto et tata sont dans un bateau""")

df = pd.DataFrame({
    'first column': list(range(1, 1000)),
    'second column': np.arange(1, 1000, 1)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Selectionne le nb de lignes', 1, 1000, 42)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df
print(f"Tu as selectionne : {line_count} lignes.")