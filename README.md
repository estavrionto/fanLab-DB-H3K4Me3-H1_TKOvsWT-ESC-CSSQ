# fanLab-DB-H3K4Me3-H1_TKOvsWT-ESC-CSSQ
Differential Binding sites between H3K4Me3 ChIP-Seq datasets of triple H1 knock-out (H1 TKO) and Wild Type (WT) Embryonic Stem Cells (ESC) found using Chip-seq Signal Quantifier Pipeline (CSSQ)

## Instructions:

1. Clone this repo:
    ```
    gh repo clone estavrionto/fanLab-DB-H3K4Me3-H1_TKOvsWT-ESC-CSSQ 
    ```
2. Create the conda env and activate:
    ```
    <insert command to create the conda env>
    ```
3. Download the reads from SRA:
    ```
    conda run -n assembly python download_reads.py -m download
    ```
4. Perform FastQC quality check:
    ```
    conda run -n assembly fastqc --threads 6 -o ./fastqc/raw/ ./fastq_reads/*.fastq
    conda run -n assembly fastqc --threads 6 -o ./fastqc/trimmed/ ./trimmed_reads/*.fq
    ```
5. Perform MultiQC report:
    ```
    conda run -n assembly multiqc ./fastqc/raw/ -o ./fastqc/raw/
    conda run -n assembly multiqc ./fastqc/trimmed/ -o ./fastqc/trimmed/
    ```
6. Analysis of MultiQC report:
7. Trimming of Adapters:
    ```
    conda run -n trim_galore trim_galore --cores 2 --output_dir ./trimmed_reads/ ./fastq_reads/*.fastq
    ```
9. 

