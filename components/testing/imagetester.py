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
        
        count = 0
        for key in nutLabel:
            if nutLabel[key] != None:
                count += 1

        f = open(join(path, "results\\" + file.split(".")[0] + ".json"), "w")
        
        dict = {"file": file, "count": count, "label": nutLabel}
        f.write(str(dict).replace("'", "\""))
        f.close()







if __name__ == "__main__":
    if not sys.argv[1]:
        print("no directory was given")
    main(sys.argv[1])