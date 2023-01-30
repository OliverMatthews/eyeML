import pandas as pd
import skimage as img
import tqdm
from matplotlib import pyplot as plt


# Load the dataset
stare_dataset = pd.read_csv("../data/STARE/diagnoses.csv")

# Print the first 5 rows of the dataset
print(stare_dataset.head())

# Print the number of rows and columns in the dataset
print(stare_dataset.shape)

# Print the number of instances of each class
normal_count = stare_dataset["Normal"].value_counts()[1]
emboli_count = stare_dataset["Emboli"].value_counts()[1]
BRAO_count = stare_dataset["BRAO"].value_counts()[1]
CRAO_count = stare_dataset["CRAO"].value_counts()[1]
BRVO_count = stare_dataset["BRVO"].value_counts()[1]
CRVO_count = stare_dataset["CRVO"].value_counts()[1]
Hemi_count = stare_dataset["Hemi-CRVO"].value_counts()[1]
BDR_NPDR_count = stare_dataset["BDR/NPDR"].value_counts()[1]
PDR_count = stare_dataset["PDR"].value_counts()[1]
ASR_count = stare_dataset["ASR"].value_counts()[1]
HTR_count = stare_dataset["HTR"].value_counts()[1]
Coats_count = stare_dataset["Coats"].value_counts()[1]
Macroaneurism_count = stare_dataset["Macroaneurism"].value_counts()[1]
CNV_count = stare_dataset["CNV"].value_counts()[1]
Other_count = stare_dataset["Other"].value_counts()[1]

print("Normal: " + str(normal_count))
print("Emboli: " + str(emboli_count))
print("BRAO: " + str(BRAO_count))
print("CRAO: " + str(CRAO_count))
print("BRVO: " + str(BRVO_count))
print("CRVO: " + str(CRVO_count))
print("Hemi-CRVO: " + str(Hemi_count))
print("BDR/NPDR: " + str(BDR_NPDR_count))
print("PDR: " + str(PDR_count))
print("ASR: " + str(ASR_count))
print("HTR: " + str(HTR_count))
print("Coats: " + str(Coats_count))
print("Macroaneurism: " + str(Macroaneurism_count))
print("CNV: " + str(CNV_count))
print("Other: " + str(Other_count))

# Split the dataset into training and testing data
train_data = stare_dataset.sample(frac=0.8, random_state=0)
test_data = stare_dataset.drop(train_data.index)

# Print the number of rows and columns in the training and testing data
print(train_data.shape)
print(test_data.shape)

# Using skimage, load all the images in the training data. Use a progress bar to show the progress.
train_images = []
print("Loading training images.")
for i in tqdm.tqdm(range(len(train_data))):
    train_images.append(img.io.imread("../data/STARE/images/" + train_data.iloc[i, 0] + ".ppm"))

# Using skimage, load all the images in the testing data
test_images = []
print("Loading testing images.")
for i in tqdm.tqdm(range(len(test_data))):
    test_images.append(img.io.imread("../data/STARE/images/" + test_data.iloc[i, 0] + ".ppm"))

# Show the first image in the training data
plt.imshow(train_images[0])
plt.show()

