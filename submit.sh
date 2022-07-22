#!/bin/bash -l
#SBATCH -p batch 
#SBATCH -J y6-analysis
#SBATCH -o job.%j.o
#SBATCH -N 1
#SBATCH -n 16 
#SBATCH -w node3
#SBATCH -t 200:00:00

conda activate morphct 

# PUT YOUR CODE IN HERE!
python -u y6-script.py
