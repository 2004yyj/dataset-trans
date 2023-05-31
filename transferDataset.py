import os
import argparse
import yaml
import sys

def main(args):
    inputArr = []
    outputArr = []
    
    with open(str(sys.path[0] + "\\" + args.input_yaml)) as f:
        inputArr = yaml.load(f, Loader=yaml.FullLoader)['names']

    with open(str(sys.path[0] + "\\" + args.output_yaml)) as f:
        outputArr = yaml.load(f, Loader=yaml.FullLoader)['names']

    dirPath = args.labels_dir
    outputIndexes = []

    for clazz in inputArr:
        if clazz in outputArr:
            outputIndexes.append(outputArr.index(clazz))
        else:
            raise ValueError(f"not included class {clazz}")
    print(outputIndexes)
        
    for (_, _, files) in os.walk(dirPath):
        for f in files:
            path = f"{dirPath}/{f}"
            file = open(path)
            nStr = ""
            lines = file.readlines()
            for l in lines:
                line = l.split()
                print(line[0])
                line[0] = str(outputIndexes[int(line[0])])
                nStr += " ".join(str(e) for e in line) + "\n"
            file.close()
            file = open(path, 'w')
            file.write(nStr)
            file.close()


if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_yaml', required=True, help='input yaml')
    parser.add_argument('--output_yaml', required=True, help='output yaml')
    parser.add_argument('--labels_dir', required=True, help='dataset labels dir')
    args = parser.parse_args()
    main(args)