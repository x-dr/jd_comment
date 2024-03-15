from func_spark import SparkApi
from utils import json_load


def test_spark():
    spark_config =  json_load("spark_config.json")
    if spark_config["on"]:
        spark_api = SparkApi(spark_config)
        msg_json = spark_api.get_answer([{"role": "user", "content": "你好"}])
        if msg_json['code'] == 1:
            msg = msg_json['data']
            spark_api.answer = ""
            print(msg)
            return 5, msg.strip()
        else:
            msg = "error"
            return 5, msg.strip()
    else:
        print("1")

print(test_spark()[1])