import re
import xml.etree.ElementTree as ET

import pandas as pd


def read_csv(csv_file):
    df_users = pd.read_csv(csv_file)
    df_users['date_joined'] = pd.to_datetime(df_users['date_joined'], unit='s', utc=True)
    df_users = filter_data(df_users)
    return df_users


def read_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    users = list()
    for user in root[0][2]:
        user_id = int(user.get('id'))
        first_name = user.find('first_name').text
        last_name = user.find('last_name').text
        avatar = user.find('avatar').text
        users.append({
            'user_id': user_id,
            'first_name': first_name,
            'last_name': last_name,
            'avatar': avatar
        })
    df_users = pd.DataFrame(users)
    df_users = filter_data(df_users)
    df_users = df_users.set_index('user_id')
    return df_users


def merge_data(csv_data: pd.DataFrame, xml_data: pd.DataFrame):
    data = csv_data.merge(xml_data, how='inner', left_index=True, right_on='user_id')
    data = data.dropna(subset=['username', 'password', 'first_name', 'last_name'])
    return data


def filter_data(data: pd.DataFrame):
    patterns = (r"\(.+\)", r"\[.+\]")
    data = data.to_dict('records')
    bad_records = list()
    for pattern in patterns:
        for user in data:
            for key in user:
                if type(user[key]) == str:
                    if re.search(pattern, user[key]):
                        bad_records.append(user)

    return pd.DataFrame([item for item in data if item not in bad_records])


def data_preparation(csv_file, xml_file):
    csv_data = read_csv(csv_file)
    xml_data = read_xml(xml_file)
    complete_data = merge_data(csv_data, xml_data)
    return complete_data
