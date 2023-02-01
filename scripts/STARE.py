import os
import zipfile
import requests
import tqdm
from time import sleep


images_url = "https://cecas.clemson.edu/~ahoover/stare/images/all-images.zip"
diagnoses_url = "https://gist.github.com/OliverMatthews/b3ce29edccdd835ac3719995f2b322ec/archive" \
                "/d6fbd2c69f7e1e0005016e6b2d570722ad7652f4.zip"
optic_nerve_url = "https://cecas.clemson.edu/~ahoover/stare/nerve/GT_NERVES.txt"


def download_images():
    # If the data/STARE/images folder does not exist, create it
    if not os.path.exists("data/STARE/images"):
        os.makedirs("data/STARE/images")

    print("Downloading STARE images from " + images_url)

    # Create a progress bar
    r = requests.get(images_url, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    # Download the data
    with open("data/STARE/all-images.zip", "wb") as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()

    print("Unzipping STARE images.")

    # Create a progress bar
    total_size = os.path.getsize("data/STARE/all-images.zip")
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    # Unzip the data
    with zipfile.ZipFile("data/STARE/all-images.zip", "r") as zip_ref:
        for file in zip_ref.namelist():
            zip_ref.extract(file, "data/STARE/images")
            t.update(os.path.getsize("data/STARE/images/" + file))
    t.close()

    # Delete the zip file
    os.remove("data/STARE/all-images.zip")


def download_diagnoses():
    # If the data/STARE/diagnoses folder does not exist, create it
    if not os.path.exists("data/STARE/"):
        os.makedirs("data/STARE/")

    print("Downloading STARE diagnoses data from " + diagnoses_url)

    # Create a progress bar
    r = requests.get(diagnoses_url, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    # Download the data
    with open("data/STARE/diagnoses.zip", "wb") as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()

    sleep(0.1)

    print("Unzipping STARE diagnoses data.")

    # Create a progress bar
    total_size = os.path.getsize("data/STARE/diagnoses.zip")
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    # Unzip the data from the zip file
    with zipfile.ZipFile("data/STARE/diagnoses.zip", "r") as zip_ref:
        for file in zip_ref.namelist():
            zip_ref.extract(file, "data/STARE/")
            t.update(os.path.getsize("data/STARE/" + file))
    t.close()

    # Delete the zip file
    os.remove("data/STARE/diagnoses.zip")

    # Rename the file
    os.rename("data/STARE/b3ce29edccdd835ac3719995f2b322ec-d6fbd2c69f7e1e0005016e6b2d570722ad7652f4",
              "data/STARE/diagnoses")

    # Move the file to the data/STARE folder
    os.replace("data/STARE/diagnoses/STARE_diagnoses_data.csv", "data/STARE/diagnoses.csv")

    # Delete the folder
    os.rmdir("data/STARE/diagnoses")


def download_optic_nerve():
    # If the data/STARE/optic_nerve folder does not exist, create it
    if not os.path.exists("data/STARE/"):
        os.makedirs("data/STARE/")

    print("Downloading STARE optic nerve data from " + optic_nerve_url)

    # Create a progress bar
    r = requests.get(optic_nerve_url, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024

    # Download the data from the url
    with open("data/STARE/optic_nerve.txt", "wb") as f:
        for data in r.iter_content(block_size):
            f.write(data)

    # Replace all instances of ".jpg" with ".ppm"
    with open("data/STARE/optic_nerve.txt", "r") as f:
        data = f.read()
        data = data.replace(".jpg", ".ppm")
    with open("data/STARE/optic_nerve.txt", "w") as f:
        f.write(data)

    # Convert the data to a csv file
    optic_nerve_to_csv()


# Convert the optic nerve data to a csv file
def optic_nerve_to_csv():
    # Open the optic nerve data file
    with open("data/STARE/optic_nerve.txt", "r") as f:
        # Read the data
        data = f.read()

        # Split the data into lines
        lines = data.split("\n")

        # For each line, split the line into the image name and the x and y coordinates
        lines = [line.split(" ") for line in lines]
        lines = lines[:-1]

        # Write the data to a csv file
        with open("data/STARE/optic_nerve.csv", "w") as f:
            # Write the header
            f.write("ID,y,x\n")

            # Write the data
            for line in lines:
                f.write(line[0] + "," + line[1] + "," + line[2] + "\n")

    # Delete the txt file
    os.remove("data/STARE/optic_nerve.txt")


def download_full():
    download_images()
    download_diagnoses()
    download_optic_nerve()
