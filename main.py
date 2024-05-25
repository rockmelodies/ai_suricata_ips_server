#!/usr/bin/env python
# encoding: utf-8
# @author: rockmelodies
# @license: (C) Copyright 2013-2024, 360 Corporation Limited.
# @contact: rockysocket@gmail.com
# @software: garner
# @file: main.py
# @time: 2024/5/25 下午5:53
# @desc:

import json
import pandas as pd


def preprocess_eve_log(eve_log_file):
    '''
    提取suricata規則日志2
    :param eve_log_file:
    :return:
    '''
    records = []
    with open(eve_log_file, 'r') as f:
        for line in f:
            record = json.loads(line)
            if 'alert' in record:
                records.append(record)

    df = pd.DataFrame(records)
    df = df[['timestamp', 'src_ip', 'src_port', 'dest_ip', 'dest_port', 'proto', 'alert']]
    df['alert'] = df['alert'].apply(lambda x: x['signature'] if isinstance(x, dict) else None)
    return df


df = preprocess_eve_log('/var/log/suricata/eve.json')
df.to_csv('preprocessed_eve_log.csv', index=False)

