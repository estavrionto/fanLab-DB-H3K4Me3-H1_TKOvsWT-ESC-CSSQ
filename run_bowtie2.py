import csv
import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description='runs bowtie2 using the reads.txt file')
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
        return f'Dummy execute: {" ".join(Command_list)}'
    elif args.mode == 'download':
        return subprocess.run(Command_list,shell=False,text=True)

def run_bowtie2():
    reads_info = SVtoLIST('reads.txt','\t')
    for i in reads_info:
        print(f'running assembly of {i}')
        'conda run -n env_bowtie2 bowtie2 --threads 6 -x ../../assembly_indexes/bowtie2/mm9/mm9 -U ./trimmed_reads/SRR2961593_trimmed.fq -S ./assemblies/wt_input.sam'
        this_command = [
            'conda','run','-n','env_bowtie2',
            'bowtie2','--threads','6',
            '-x','../../assembly_indexes/bowtie2/mm9/mm9',
            '-U',f'./trimmed_reads/{i[2]}',
            '-S',f'./assemblies/{i[3]}.sam'
            ]
        print(execute(this_command))
        # break


if __name__ == "__main__":
    run_bowtie2()