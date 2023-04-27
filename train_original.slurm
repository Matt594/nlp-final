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

# ELECTRA on original

python3 run.py --do_train --task qa --dataset ./quoref/quoref_original_formatted.json --output_dir ./electra_model_data/original_trained_model/
python3 run.py --do_eval --task qa --dataset ./quoref/quoref_original_formatted.json --model ./electra_model_data/original_trained_model/ --output_dir ./electra_model_data/original_eval_output/
python3 run.py --do_eval --task qa --dataset ./quoref/quoref_perturbed_formatted.json --model ./electra_model_data/original_trained_model/ --output_dir ./electra_model_data/perturbed_eval_output/

# ---------------------------------------------------

# BERT on original
python3 run.py --do_train --task qa --dataset ./quoref/quoref_original_formatted.json --output_dir ./bert_model_data/original_trained_model/ --model bert-base-cased
python3 run.py --do_eval --task qa --dataset ./quoref/quoref_original_formatted.json --model ./bert_model_data/original_trained_model/ --output_dir ./bert_model_data/original_eval_output/
python3 run.py --do_eval --task qa --dataset ./quoref/quoref_perturbed_formatted.json --model ./bert_model_data/original_trained_model/ --output_dir ./bert_model_data/perturbed_eval_output/

# ---------------------------------------------------

# roberta on original
python3 run.py --do_train --task qa --dataset ./quoref/quoref_original_formatted.json --output_dir ./roberta_model_data/original_trained_model/ --model roberta-base
python3 run.py --do_eval --task qa --dataset ./quoref/quoref_original_formatted.json --model ./roberta_model_data/original_trained_model/ --output_dir ./roberta_model_data/original_eval_output/
python3 run.py --do_eval --task qa --dataset ./quoref/quoref_perturbed_formatted.json --model ./roberta_model_data/original_trained_model/ --output_dir ./roberta_model_data/perturbed_eval_output/