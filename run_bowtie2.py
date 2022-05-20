import csv
import subprocess
import argparse
import os

# constants 

reads_dir = './fastq_reads/'
mode_test = 'test'
mode_actual = 'run'

# command line arguments 
parser = argparse.ArgumentParser(description='runs bowtie2 using the reads.txt file')
# adding the required arguments using argparse
parser.add_argument( '-m', '--mode', help='mode of running', metavar=f'{mode_test}/{mode_actual}', default=f'{mode_actual}', required=False, type=str )
args = parser.parse_args()

def LISTto_SV(LIST,Delimiter, _SVfile):
    with open(_SVfile, 'w') as fo:
        writer = csv.writer(fo, delimiter = Delimiter)
        writer.writerows(LIST)

def runProcess(exe):
    # got from https://stackoverflow.com/a/4760274/577088 
    p = subprocess.Popen(
        exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        universal_newlines=True,bufsize=1
        )
    while(True):
        # returns None while subprocess is running
        retcode = p.poll() 
        line = p.stdout.readline()
        print([line])
        yield line,retcode
        if retcode is not None:
            break

def log_print(in_str):
    print(in_str)
    

# def log_print_output(in_list):
#     for i in in_list[0]:
#         log_print(f'cmd_out: {i}')
#     log_print(in_list[1])

def SVtoLIST(_SVfile,Delimiter):
    with open(_SVfile, 'r') as fo:
            reader = csv.reader(fo, delimiter=Delimiter)
            return list(reader)

def execute(Command_list, var_mode):
    log_print(f'executing: {" ".join(Command_list)}')
    if var_mode == mode_test:
        exitcode = {'args':Command_list, 'returncode':None}
        output_list = [f'Dummy output: {" ".join(Command_list)}']
        for line in output_list:
            log_print(f'cmd_out: {line.rstrip()}')
        log_print(f'exitcode: {exitcode}')
    # elif var_mode == mode_actual:
    #     return subprocess.run(Command_list,shell=False,text=True)
    elif var_mode == mode_actual:
        output_list = []
        for line, rc in runProcess(Command_list):
            if line != '':
                log_print(f'cmd_out: {line.rstrip()}')
                output_list.append(line.rstrip())
            retcode = rc
        exitcode = {'args':Command_list, 'returncode':retcode}
        log_print(f'exitcode: {exitcode}')
    return output_list,exitcode


def run_bowtie2():
    reads_info = SVtoLIST('reads.txt','\t')
    mapped_counts = []
    for i in reads_info:
        print(f'')
        print(f'running assembly of {i}')
        'conda run -n env_bowtie2 bowtie2 --threads 6 -x ../../assembly_indexes/bowtie2/mm9/mm9 -U ./trimmed_reads/SRR2961593_trimmed.fq -S ./assemblies/wt_input.sam'
        cmd_bowtie = [
            'conda','run',
            '--prefix','/storage/home/hcoda1/3/abangaru3/.conda/envs/my_base/envs/env_bowtie2',
            'bowtie2','--threads','12',
            '-x','../../assembly_indexes/bowtie2/mm9/mm9',
            '-U',f'./trimmed_reads/{i[2]}',
            '-S',f'./assemblies/{i[3]}.sam'
            ]
        execute(cmd_bowtie,mode_test)
        # set to dynamic later 

        print(f'running sam to bam conversion of {i}')
        cmd_SAMtoBAM = [

            'conda','run',
            '--prefix','/storage/home/hcoda1/3/abangaru3/.conda/envs/my_base/envs/assembly',
            'samtools','view',
            '--threads','8',
            '-bS',f'./assemblies/{i[3]}.sam',
            '-o',f'./assemblies/{i[3]}.bam'
        ]
        execute(cmd_SAMtoBAM,mode_test)
        # set to dynamic later 

        cmd_test = ['ls','-alh']
        execute(cmd_test,args.mode)

        
        cmd_mapped_count = [
            'samtools','flagstat',f'./assemblies/{i[3]}.bam'

        ]
        
        # cmd_mapped_count = ['echo']
        out_counts,ec = execute(cmd_mapped_count,args.mode)
        for l in out_counts:
            if 'mapped' in l:
                mapped_counts.append(
                    [f'{i[3]}.bam',l.split(" ")[0]])
                break

        
        # break

    LISTto_SV(mapped_counts,'\t','H3K4Me3-H1_TKOvsWT_info.txt')

if __name__ == "__main__":
    run_bowtie2()
    # for i in runProcess(['samtools','flagstat','./assemblies/h1_ip_R2.bam']):
    #     print(i)