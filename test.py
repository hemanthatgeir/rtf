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
        "anomaliy2"
    ]
}, {
    "connection": "connection1",
    "Batch": "Batch1",
    "job": "JOB1",
    "tests": [
        "test1",
        "test2",
        "test3"
    ],
    "anomalies": [
        "anomaly1",
        "anomaliy2"
    ]
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
            "anomaliy2"
        ]
    }
]

temp_json = {"blocks": []}

divider_json = {"type": "divider"}

tag_list = ["connection", "Batch", "job", "tests", "anomalies"]

temp_dict = {}

global job_no
job_no = 1


def extract_values(dict):
    for tag in tag_list:
        if (tag in dict.keys()):
            if (isinstance(dict[tag], list)):
                flat_list = "\n\t".join(dict[tag])
                temp_dict[tag] = "*```\n\t".join([tag.title(), flat_list])
            else:
                temp_dict[tag] = ":".join([tag, dict[tag]])
        else:
            temp_dict[tag] = ""
    connection = temp_dict[tag_list[0]]
    batch = temp_dict[tag_list[1]]
    job = temp_dict[tag_list[2]]
    tests = temp_dict[tag_list[3]]
    anomalies = temp_dict[tag_list[4]]
    temp_dict.clear()
    return connection, batch, job, tests, anomalies


emoji = True


def json_con_batch(value_0, value_1):
    if (len(value_0) == 0 and len(value_1) == 0):
        sample_json_con_batch = {"type": "header"}
    else:
        sample_json_con_batch = {"type": "header",
                                 "text": {"type": "plain_text", "text": value_0 + "," + value_1, "emoji": emoji}}
        if (sample_json_con_batch in temp_json["blocks"]):
            global job_no
            job_no += 1
            pass
        else:
            temp_json["blocks"].extend([sample_json_con_batch, divider_json])
            job_no = 1


def json_job(value_1, value_2):
    if (len(value_2) == 0):
        sample_json_job = {"type": "section", "text": {"type": "mrkdwn"}}
    else:
        sample_json_job = {"type": "section", "text": {"type": "mrkdwn", "text": "#" + value_1 + value_2}}
    temp_json["blocks"].extend([sample_json_job, divider_json])


def json_test(value_0):
    if (len(value_0) == 0):
        sample_json_test = {"type": "section"}
    else:
        sample_json_test = {"type": "section",
                                      "text": {"type": "mrkdwn", "text": "*" + value_0 + "```"}}
    temp_json["blocks"].extend([sample_json_test])


def json_anomalies(value_0):
    if (len(value_0) == 0):
        sample_json_anomalies = {"type": "section"}
    else:
        sample_json_anomalies = {"type": "section",
                                      "text": {"type": "mrkdwn", "text": "*" + value_0 + "```"}}
    temp_json["blocks"].extend([sample_json_anomalies, divider_json])


for input_dict in input_array:
    values = extract_values(input_dict)
    json_con_batch(values[0], values[1])
    json_job(str(job_no), values[2])
    json_test(values[3])
    json_anomalies(values[4])

final_str_json = json.dumps(temp_json, indent=2)
print(final_str_json)
