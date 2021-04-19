import numpy as np
FILEPATHS = {'fresh water fish' : '../vectors/fresh_water_fish_vectors.txt',
            'sea fish': '../vectors/sea_fish_vectors.txt',
            'crustaceans': '../vectors/crustacean_vectors.txt',
            'fresh and salt water fish':'../vectors/fresh_and_salt_water_fish_vectors.txt',
            'birds': '../vectors/bird_vectors.txt'}

def main():

    for fp1 in FILEPATHS.keys():
        f1 = loadFileToDict(FILEPATHS[fp1])
        print(f'Varaince of {fp1} is {getSumOfVariances(f1)}')
        esum = 0
        for fp2 in FILEPATHS.keys():
            if fp1 != fp2:
                v1 = getMeanVector(f1)
                v2 = getMeanVector(loadFileToDict(FILEPATHS[fp2]))
                print(f'EclideanDistance between {fp1} and {fp2}:\n', euclideanDistance(v1, v2))
                esum += euclideanDistance(v1, v2)
        print(f'Mean Euclidean distance for {fp1}:\n', esum/(len(FILEPATHS) - 1))

def getMeanVector(fdict : dict):
    ls = list(fdict.values())
    return np.mean(ls, axis = 0).tolist()
def getSumOfVariances(fdict : dict):
    ls = list(fdict.values())
    return np.sum(np.var(ls, axis = 0))

def euclideanDistance(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.linalg.norm(v1-v2)

def loadFileToDict(path):
    fdict = {}
    with open(path, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.split()
            word = line[0]
            line = line[1:]
            vector = list(map(float, line))
            fdict[word] = vector
    return fdict



main()
