import json
import random

def convert(quoref):
    input_dict = json.load(quoref)
    output_dict_val = {}
    output_dict_train = {}

    # Metadata
    output_dict_train["dataset"] = "quoref"
    output_dict_train["config"] = "plain_text"
    output_dict_train["split"] = "train"

    output_dict_val["dataset"] = "quoref"
    output_dict_val["config"] = "plain_text"
    output_dict_val["split"] = "validation"

    # Features
    output_dict_train["features"] = list()
    output_dict_train["features"].append({"feature_idx": 0,
                                    "name": "id",
                                    "type": {"dtype": "string",
                                             "_type": "Value"}})
    output_dict_train["features"].append({"feature_idx": 1,
                                    "name": "title",
                                    "type": {"dtype": "string",
                                             "_type": "Value"}})
    output_dict_train["features"].append({"feature_idx": 2,
                                    "name": "context",
                                    "type": {"dtype": "string",
                                             "_type": "Value"}})
    output_dict_train["features"].append({"feature_idx": 3,
                                    "name": "question",
                                    "type": {"dtype": "string",
                                             "_type": "Value"}})
    output_dict_train["features"].append({"feature_idx": 4,
                                    "name": "answers",
                                    "type": {"feature": {"text": {"dtype": "string",
                                                                  "_type": "Value"}, 
                                                         "answer_start": {"dtype": "int32",
                                                                          "_type": "Value"}},
                                             "_type": "Sequence"}})
    
    output_dict_val["features"] = list()
    output_dict_val["features"].append({"feature_idx": 0,
                                    "name": "id",
                                    "type": {"dtype": "string",
                                             "_type": "Value"}})
    output_dict_val["features"].append({"feature_idx": 1,
                                    "name": "title",
                                    "type": {"dtype": "string",
                                             "_type": "Value"}})
    output_dict_val["features"].append({"feature_idx": 2,
                                    "name": "context",
                                    "type": {"dtype": "string",
                                             "_type": "Value"}})
    output_dict_val["features"].append({"feature_idx": 3,
                                    "name": "question",
                                    "type": {"dtype": "string",
                                             "_type": "Value"}})
    output_dict_val["features"].append({"feature_idx": 4,
                                    "name": "answers",
                                    "type": {"feature": {"text": {"dtype": "string",
                                                                  "_type": "Value"}, 
                                                         "answer_start": {"dtype": "int32",
                                                                          "_type": "Value"}},
                                             "_type": "Sequence"}})

    random.shuffle(input_dict["data"])
    train_data = input_dict["data"][:round(len(input_dict["data"]) * .8)]
    validation_data = input_dict["data"][round(len(input_dict["data"]) * .8):]

    # Rows
    output_dict_train["rows"] = list()
    row_idx = 0
    for datum in train_data:
        title = datum["title"]
        # url = datum["url"]
        for paragraph in datum["paragraphs"]:
            context = paragraph["context"]
            # context_id = paragraph["context_id"]
            for qa in paragraph["qas"]:
                question = qa["question"]
                id = qa["id"]

                answers = list()
                starts = list()
                for answer in qa["answers"]:
                    answers.append(answer["text"])
                    starts.append(answer["answer_start"])

                output_dict_train["rows"].append({"row_idx": row_idx,
                                            "row": {"id": id,
                                                    "title": title,
                                                    "context": context,
                                                    "question": question,
                                                    "answers": {"text": answers,
                                                                "answer_start": starts}},
                                                    "truncated_cells": []
                                            })
                row_idx += 1

    # Rows
    output_dict_val["rows"] = list()
    row_idx = 0
    for datum in validation_data:
        title = datum["title"]
        # url = datum["url"]
        for paragraph in datum["paragraphs"]:
            context = paragraph["context"]
            # context_id = paragraph["context_id"]
            for qa in paragraph["qas"]:
                question = qa["question"]
                id = qa["id"]

                answers = list()
                starts = list()
                for answer in qa["answers"]:
                    answers.append(answer["text"])
                    starts.append(answer["answer_start"])

                output_dict_val["rows"].append({"row_idx": row_idx,
                                            "row": {"id": id,
                                                    "title": title,
                                                    "context": context,
                                                    "question": question,
                                                    "answers": {"text": answers,
                                                                "answer_start": starts}},
                                                    "truncated_cells": []
                                            })
                row_idx += 1

    return output_dict_train, output_dict_val

train, validation = convert(open("quoref/quoref_original_subset_20191206_merged.json"))

with open("quoref/quoref_original_train_formatted.json", "a") as f:
    json.dump(train, f)
with open("quoref/quoref_original_validation_formatted.json", "a") as f:
    json.dump(validation, f)