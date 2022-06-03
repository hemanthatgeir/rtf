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

divider_json = {"type": "divider"}
temp_dict = {"blocks": []}
list_1 = []

for element in range(len(input_array)):
    for k, v in input_array[element].items():
        if (isinstance(v, list)):
            flat_list = ",".join(v)
            list_1.append("%s:%s" % (k,v))
        else:
            list_1.append("%s:%s" % (k,v))

    con = list_1[0] + ',' + list_1[1]
    job = list_1[2]
    test = list_1[3] + ',' + list_1[4]
   

    li = [con,job,test]

    for i in li:
        sample_text_json = {"type": "section", "text": {"type": "mrkdwn", "text": i}}
        temp_dict["blocks"].extend([sample_text_json, divider_json])

    list_1.clear()

temp_json = json.dumps(temp_dict, indent=2)
print(temp_json)
