import csv
import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description='downloads the reads from SRA using the reads.txt file')
# adding the required arguments using argparse
parser.add_argument( '-m', '--mode', help='mode of running', metavar='test/download', default='test', required=True, type=str )
args = parser.parse_args()

# constants 

reads_dir = './fastq_reads/'

def SVtoLIST(_SVfile,Delimiter):
    with open(_SVfile, 'r') as fo:
            reader = csv.reader(fo, delimiter=Delimiter)
            return list(reader)

def execute(Command_list):
    if args.mode == 'test':
        return f'Dummy execute: {Command_list}'
    elif args.mode == 'download':
        return subprocess.run(Command_list,shell=False,text=True)

def download_reads():
    reads_info = SVtoLIST('reads.txt','\t')
    for i in reads_info:
        print(f'downloading fastq files of {i[1]}')
        'fastq-dump --outdir /opt/fastq/ --split-files /home/[USER]/ncbi/public/sra/SRR925811.sra'
        this_command = ['fasterq-dump','--split-files','--threads','8','--progress','--outdir']
        # print(i)
        this_command.append(f'./{i[3]}/')
        this_command.append(i[1])
        print(execute(this_command))
        # break


if __name__ == "__main__":
    download_reads()