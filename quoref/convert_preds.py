import json

# ELECTRA
with open('./electra_model_data/original_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./electra_model_data/original_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

with open('./electra_model_data/perturbed_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./electra_model_data/perturbed_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

# python3 ./quoref/compute_metrics.py --original_gold_path "./quoref/quoref_original_subset_20191206_merged.json" --original_prediction_path "./electra_model_data/original_eval_output/eval_preds_queried.json" --perturbed_gold_path "./quoref/quoref_test_perturbations_20191206_merged.json" --perturbed_prediction_path "./electra_model_data/perturbed_eval_output/eval_preds_queried.json" > ./metrics/electra_metrics.txt

# BERT
with open('./bert_model_data/original_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./bert_model_data/original_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

with open('./bert_model_data/perturbed_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./bert_model_data/perturbed_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

# python3 ./quoref/compute_metrics.py --original_gold_path "./quoref/quoref_original_subset_20191206_merged.json" --original_prediction_path "./bert_model_data/original_eval_output/eval_preds_queried.json" --perturbed_gold_path "./quoref/quoref_test_perturbations_20191206_merged.json" --perturbed_prediction_path "./bert_model_data/perturbed_eval_output/eval_preds_queried.json" > ./metrics/bert_metrics.txt

# roberta
with open('./roberta_model_data/original_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./roberta_model_data/original_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

with open('./roberta_model_data/perturbed_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./roberta_model_data/perturbed_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

# python3 ./quoref/compute_metrics.py --original_gold_path "./quoref/quoref_original_subset_20191206_merged.json" --original_prediction_path "./roberta_model_data/original_eval_output/eval_preds_queried.json" --perturbed_gold_path "./quoref/quoref_test_perturbations_20191206_merged.json" --perturbed_prediction_path "./roberta_model_data/perturbed_eval_output/eval_preds_queried.json" > ./metrics/roberta_metrics.txt
