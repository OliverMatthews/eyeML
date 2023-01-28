import pandas as pd
import scripts.STARE as STARE


# Download the STARE dataset
STARE.download_complete()

# Load the STARE dataset from the image_diagnoses.csv file
data = pd.read_csv("./data/STARE/diagnoses.csv")

# Print the first 5 rows of the dataset
print(data.head())

# Print the number of rows and columns in the dataset
print(data.shape)
