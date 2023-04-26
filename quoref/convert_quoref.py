import json
import random

def convert_original(quoref):
    input_dict = json.load(quoref)
    output = {}

    # Rows
    output["data"] = list()
    for datum in input_dict["data"]:
        title = datum["title"]
        for paragraph in datum["paragraphs"]:
            context = paragraph["context"]
            for qa in paragraph["qas"]:
                question = qa["question"]
                id = qa["id"]

                answers = list()
                starts = list()
                for answer in qa["answers"]:
                    answers.append(answer["text"])
                    starts.append(answer["answer_start"])

                output["data"].append({"id": id,
                                            "title": title,
                                            "context": context,
                                            "question": question,
                                            "answers": {"text": answers,
                                                        "answer_start": starts}})

    return output

def convert_perturbed(quoref):
    input_dict = json.load(quoref)
    output = {}

    # Rows
    output["data"] = list()
    for datum in input_dict["data"]:
        title = datum["title"]
        for paragraph in datum["paragraphs"]:
            context = paragraph["context"]
            for qa in paragraph["qas"]:
                question = qa["question"]
                id = qa["id"]
                original_id = qa["original_id"]

                answers = list()
                starts = list()
                for answer in qa["answers"]:
                    answers.append(answer["text"])
                    starts.append(answer["answer_start"])

                output["data"].append({"id": id,
                                            "title": title,
                                            "context": context,
                                            "question": question,
                                            "answers": {"text": answers,
                                                        "answer_start": starts},
                                            "original_id": original_id})
                
    return output

original = json.load(open("quoref/quoref_original_subset_20191206_merged.json"))
original_train = dict()
original_test = dict()
original_train["data"] = original["data"][:round(len(original["data"]) * .8)]
original_test["data"] = original["data"][round(len(original["data"]) * .8):]
with open("quoref/train_quoref_original.json", "a") as f:
    json.dump(original_train, f)
with open("quoref/test_quoref_original.json", "a") as f:
    json.dump(original_test, f)

perturbed = json.load(open("quoref/quoref_test_perturbations_20191206_merged.json"))
perturbed_train = dict()
perturbed_test = dict()
perturbed_train["data"] = perturbed["data"][:round(len(perturbed["data"]) * .8)]
perturbed_test["data"] = perturbed["data"][round(len(perturbed["data"]) * .8):]
with open("quoref/train_quoref_perturbed.json", "a") as f:
    json.dump(perturbed_train, f)
with open("quoref/test_quoref_perturbed.json", "a") as f:
    json.dump(perturbed_test, f)

f_original_train = convert_original(open("quoref/train_quoref_original.json"))
with open("quoref/train_quoref_original_formatted.json", "a") as f:
    json.dump(f_original_train, f)
f_original_test = convert_original(open("quoref/test_quoref_original.json"))
with open("quoref/test_quoref_original_formatted.json", "a") as f:
    json.dump(f_original_test, f)

f_perturbed_train = convert_original(open("quoref/train_quoref_perturbed.json"))
with open("quoref/train_quoref_perturbed_formatted.json", "a") as f:
    json.dump(f_perturbed_train, f)
f_perturbed_test = convert_original(open("quoref/test_quoref_perturbed.json"))
with open("quoref/test_quoref_perturbed_formatted.json", "a") as f:
    json.dump(f_perturbed_test, f)