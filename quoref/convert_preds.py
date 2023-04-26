import json

with open('./original_model_data/original_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./original_model_data/original_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

with open('./original_model_data/perturbed_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./original_model_data/perturbed_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

# python3 ./quoref/compute_metrics.py --original_gold_path "./quoref/test_quoref_original.json" --original_prediction_path "./original_model_data/original_eval_output/eval_preds_queried.json" --perturbed_gold_path "./quoref/test_quoref_perturbed.json" --perturbed_prediction_path "./original_model_data/perturbed_eval_output/eval_preds_queried.json"

with open('./perturbed_model_data/original_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./perturbed_model_data/original_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

with open('./perturbed_model_data/perturbed_eval_output/eval_predictions.jsonl', 'r') as json_file:
    json_list = list(json_file)
json_eval = dict()
for json_str in json_list:
    result = json.loads(json_str)
    json_eval[result['id']] = {i:result[i] for i in result if i!='id'}
with open('./perturbed_model_data/perturbed_eval_output/eval_preds_queried.json', 'a') as f:
    json.dump(json_eval, f)

# python3 ./quoref/compute_metrics.py --original_gold_path "./quoref/test_quoref_original.json" --original_prediction_path "./perturbed_model_data/original_eval_output/eval_preds_queried.json" --perturbed_gold_path "./quoref/test_quoref_perturbed.json" --perturbed_prediction_path "./perturbed_model_data/perturbed_eval_output/eval_preds_queried.json"
