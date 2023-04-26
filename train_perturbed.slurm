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
python3 run.py --do_train --task qa --dataset ./quoref/train_quoref_perturbed_formatted.json --output_dir ./perturbed_model_data/perturbed_trained_model/
python3 run.py --do_eval --task qa --dataset ./quoref/test_quoref_original_formatted.json --model ./perturbed_model_data/perturbed_trained_model/ --output_dir ./perturbed_model_data/original_eval_output/
python3 run.py --do_eval --task qa --dataset ./quoref/test_quoref_perturbed_formatted.json --model ./perturbed_model_data/perturbed_trained_model/ --output_dir ./perturbed_model_data/perturbed_eval_output/
# python3 ./quoref/compute_metrics.py --original_gold_path "./quoref/quoref_original_subset_20191206_merged.json" --original_prediction_path "./perturbed_model_data/original_eval_output/eval_predictions.jsonl" --perturbed_gold_path "./quoref/quoref_test_perturbations_20191206_merged.json" --perturbed_prediction_path "./perturbed_model_data/perturbed_eval_output/eval_predictions.jsonl"
# ---------------------------------------------------