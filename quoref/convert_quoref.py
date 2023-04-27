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

with open("quoref/quoref_original_formatted.json", "a") as f:
    json.dump(convert_original(open("quoref/quoref_original_subset_20191206_merged.json")), f)

with open("quoref/quoref_perturbed_formatted.json", "a") as f:
    json.dump(convert_original(open("quoref/quoref_test_perturbations_20191206_merged.json")), f)