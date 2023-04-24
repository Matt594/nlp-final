#!/bin/bash

#SBATCH -J myjob           # Job name
#SBATCH -o myjob.o%j	   # Name of stdout output file
#SBATCH -e myjob.e%j	   # Name of stderr error file
#SBATCH -p gtx             # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 01:30:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=matthew.escobar@utexas.edu
#SBATCH --mail-type=all    # Send email at begin and end of job

# Other commands must follow all #SBATCH directives...

module list
pwd
date

# Launch serial code...

conda init bash
conda activate cs378-nlp-final-project
cd nlp-final
pip install --upgrade pip
pip install -r requirements.txt
python3 run.py --do_train --task qa --dataset ./quoref/quoref_original_formatted.json --output_dir ./trained_model/

# ---------------------------------------------------