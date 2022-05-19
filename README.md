# fanLab-DB-H3K4Me3-H1_TKOvsWT-ESC-CSSQ
Differential Binding sites between H3K4Me3 ChIP-Seq datasets of triple H1 knock-out (H1 TKO) and Wild Type (WT) Embryonic Stem Cells (ESC) found using Chip-seq Signal Quantifier Pipeline (CSSQ)

## Instructions:
1. Downlaod the reads from SRA:
    ```
    python download_reads.py -m download
    ```
2. Perform FastQC quality check:
    ```
    fastqc --threads 6 -o ./fastqc/ ./fastq_reads/*/*.fastq
    ```
