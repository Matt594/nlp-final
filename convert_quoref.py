import json
import random

def convert(quoref):
    input_dict = json.load(quoref)
    output_dict = {}

    # random.shuffle(input_dict["data"])
    # train_data = input_dict["data"][:round(len(input_dict["data"]) * .8)]
    # validation_data = input_dict["data"][round(len(input_dict["data"]) * .8):]

    # Rows
    output_dict["data"] = list()
    for datum in input_dict["data"]:
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

                output_dict["data"].append({"id": id,
                                                "title": title,
                                                "context": context,
                                                "question": question,
                                                "answers": {"text": answers,
                                                            "answer_start": starts}})

    return output_dict

output_dict = convert(open("quoref/quoref_original_subset_20191206_merged.json"))

with open("quoref/quoref_original_formatted.json", "a") as f:
    json.dump(output_dict, f)