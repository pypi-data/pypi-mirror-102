# Wrapper for New Relic Insights API

## Avaliable Methods

- get_data(account,query_api_key,query)
    - returns result in JSON format
- insert_data(account,insert_api_key,data_df)
    - return response status as a list

### Sample Code

__Get Request__
```
from NRInsightsApi import get_data
r =  get_data('2929995','JSJW_WKJSJ_192920_192820','SELECT average(duration) FROM PageView')
```

```
{'results': [{'average': None}], 'performanceStats': {'inspectedCount': 0, 'omittedCount': 0, 'matchCount': 0, 'wallClockTime': 1}, 
'metadata': {'eventTypes': ['PageView'], 'eventType': 'PageView', 'openEnded': True, 'beginTime': '2021-03-31T02:48:58Z', 'endTime': '2021-03-31T03:48:58Z', 'beginTimeMillis': 1617158938335, 'endTimeMillis': 1617162538335, 'rawSince': '60 MINUTES AGO', 'rawUntil': 'NOW', 'rawCompareWith': '', 'guid': '4ade46ba-5782-6d40-7627-1411ca37131f', 'routerGuid': '74da0adc-aa35-7d58-a977-667954ca56aa', 'messages': ['No events found -- do you have the correct event type and time range?'], 'info': ['No events found -- do you have the correct event type and time range?'], 'contents': [{'function': 'average', 'attribute': 'duration', 'simple': True}]}}
```


