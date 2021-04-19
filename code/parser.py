
FILE_NAME = 'fresh and salt water fish'
LANGUAGES = ['Da', 'Du', 'F', 'Ge', 'Gr', 'I', 'N', 'P', 'S']
def main():
    with open('../'+ FILE_NAME + '.txt', 'r') as f:
        with open('../' + FILE_NAME + '_parsed.txt', 'w') as wf: 
            found = False
            for line in f.readlines():
                if found and len(line) > 1:
                    if not '-' in line:
                        wf.writelines(line.split(','))
                    found = False
                elif line.strip('\n') in LANGUAGES:
                    found = True

main()