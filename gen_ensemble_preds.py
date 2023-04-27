import json

def gen_preds(bert_output, electra_output, roberta_output):
    bert = json.load(bert_output)
    electra = json.load(electra_output)
    roberta = json.load(roberta_output)
    ballots = {0: roberta,
               1: bert,
               2: electra}
    answers = dict()

    # Ordered from most consistent to least as tiebreaker
    for key in bert:
        candidates = [roberta[key]['predicted_answer'], bert[key]['predicted_answer'], electra[key]['predicted_answer']]
        votes = dict()
        for candidate in candidates:
            if candidate in votes:
                votes[candidate] += 1
            else:
                votes[candidate] = 1
        answer = max(votes, key=votes.get)
        for i in range(len(ballots)):
            if ballots[i][key]['predicted_answer'] == answer:
                answers[key] = ballots[i][key]
                break

    return answers

bert_output = open("bert_model_data/original_eval_output/eval_preds_queried.json")
electra_output = open("electra_model_data/original_eval_output/eval_preds_queried.json")
roberta_output = open("roberta_model_data/original_eval_output/eval_preds_queried.json")
with open('./ensemble_data/ensemble_original_eval_preds.json', 'a') as f:
    json.dump(gen_preds(bert_output, electra_output, roberta_output), f)

bert_output = open("bert_model_data/perturbed_eval_output/eval_preds_queried.json")
electra_output = open("electra_model_data/perturbed_eval_output/eval_preds_queried.json")
roberta_output = open("roberta_model_data/perturbed_eval_output/eval_preds_queried.json")
with open('./ensemble_data/ensemble_perturbed_eval_preds.json', 'a') as f:
    json.dump(gen_preds(bert_output, electra_output, roberta_output), f)

# python3 ./quoref/compute_metrics.py --original_gold_path "./quoref/quoref_original_subset_20191206_merged.json" --original_prediction_path "./ensemble_data/ensemble_original_eval_preds.json" --perturbed_gold_path "./quoref/quoref_test_perturbations_20191206_merged.json" --perturbed_prediction_path "./ensemble_data/ensemble_perturbed_eval_preds.json" > ./metrics/ensemble_metrics.txt