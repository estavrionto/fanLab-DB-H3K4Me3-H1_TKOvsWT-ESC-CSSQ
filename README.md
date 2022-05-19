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
    conda activate assembly
    ```
3. Download the reads from SRA:
    ```
    python download_reads.py -m download
    ```
4. Perform FastQC quality check:
    ```
    fastqc --threads 6 -o ./fastqc/ ./fastq_reads/*/*.fastq
    ```
5. Perform MultiQC report:
    ```
    multiqc ./fastqc/ -o ./fastqc/
    ```
6. Analysis of MultiQC report:
7. Trimming of Adapters:
8. 

