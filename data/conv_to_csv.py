with open('KDDTrain+.txt') as infile, open('NSL-KDD.csv', 'w') as outfile:
    for line in infile:
        line = line.strip().replace('\t', ',')
        outfile.write(line + '\n')
