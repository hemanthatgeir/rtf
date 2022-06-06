import json

input_array = [{
    "connection": "connection1",
    "Batch": "Batch1",
    "job": "JOB2",
    "tests": [
        "test1",
        "test2",
        "test3"
    ],
    "anomalies": [
        "anomaly1",
        "anomaly2"
    ],
},
    {
        "connection": "connection2",
        "Batch": "Batch2",
        "job": "JOB3",
        "tests": [
            "test1",
            "test2",
            "test3"
        ],
        "anomalies": [
            "anomaly1",
            "anomaly2"
        ]
    }
]

temp_json = {"blocks": []}

divider_json = {"type": "divider"}

tag_list = ["connection", "Batch", "job", "tests", "anomalies"]

temp_dict = {}


def extract_values(dict):
    for tag in tag_list:
        if (tag in dict.keys()):

            if (isinstance(dict[tag], list)):
                flat_list = "\n\t".join(dict[tag])
                temp_dict[tag] = ":\n\t".join([tag, flat_list])
            else:
                temp_dict[tag] = ":".join([tag, dict[tag]])  ##temp_dict = {"connection":'connection:connection1'}
        else:
            temp_dict[tag] = ""
    connection = temp_dict[tag_list[0]]
    batch = temp_dict[tag_list[1]]
    job = temp_dict[tag_list[2]]
    tests = temp_dict[tag_list[3]]
    anomalies = temp_dict[tag_list[4]]
    # temp_dict.clear()
    return connection, batch, job, tests, anomalies


def json_con_batch_tests_anomalies(value_0, value_1):
    if (len(value_0) == 0 and len(value_1) == 0):
        sample_json_con_batch = {"type": "section"}
    else:
        if (value_0.startswith("tests") or value_0 == ""):
            sample_json_con_batch = {"type": "section", "text": {"type": "mrkdwn", "text": value_0 + "\n" + value_1}}
        else:
            sample_json_con_batch = {"type": "section", "text": {"type": "mrkdwn", "text": value_0 + "," + value_1}}

    temp_json["blocks"].extend([sample_json_con_batch, divider_json])


def json_job(value_2):
    if (len(value_2) == 0):
        sample_json_job = {"type": "section", "text": {"type": "mrkdwn"}}
    else:
        sample_json_job = {"type": "section", "text": {"type": "mrkdwn", "text": value_2}}
    temp_json["blocks"].extend([sample_json_job, divider_json])


for input_dict in input_array:
    values = extract_values(input_dict)
    json_con_batch_tests_anomalies(values[0], values[1])
    json_job(values[2])
    json_con_batch_tests_anomalies(values[3], values[4])

final_str_json = json.dumps(temp_json, indent=2)
print(final_str_json)
