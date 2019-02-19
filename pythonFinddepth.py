import csv
import sys

if len(sys.argv) < 3:
    sys.stderr.write('No Input CSV file and miniconda path\n')
    sys.exit(0)
    
inputFile = sys.argv[1]
minicondaBin = sys.argv[2]
outputFile = "findDepth.sh"
with open(outputFile,'w') as outFile:
    with open(inputFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            outFile.write(f'{minicondaBin}samtools depth -a $WORK/SAEVA-outputs/sortsam/{row[0]}.sorted.sam > $WORK/SAEVA-outputs/depth/{row[0]}.depth\n'}

 
