import imageProcess
from skimage import io
import sys
from os.path import isfile, join
import os.path


def main(path):
    files = os.listdir(path)

    for file in files:
        if not isfile(join(path, file)):
            continue

        image = io.imread(join(path, file))
        nutLabel, success = imageProcess.processImage(image)

        if not success:
            print("processing failed altogether")
            continue

        f = open(join(path, "results\\" + file.split(".")[0] + ".txt"), "w")
        f.write(str(nutLabel))
        f.close()







if __name__ == "__main__":
    if not sys.argv[1]:
        print("no directory was given")
    main(sys.argv[1])