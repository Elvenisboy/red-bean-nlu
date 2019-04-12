const json = {
    "nlu_data": {
      "common_examples": [
        {
          "intent": "weather_address_date-time", //意图
          "slots": [
            {
              "start": 2,
              "end": 4,
              "value": "上海",
              "slot": "address"
            },
            {
              "start": 4,
              "end": 6,
              "value": "明天",
              "slot": "date-time"
            }
          ],
          "text": "我要上海明天的天气"
        },
        {
          "intent": "weather_address_date-time",
          "slots": [
            {
              "start": 0,
              "end": 2,
              "value": "上海",
              "slot": "address"
            },
            {
              "start": 2,
              "end": 4,
              "value": "明天",
              "slot": "date-time"
            }
          ],
          "text": "上海明天的天气"
        }]
    }
  }