# coding=utf-8
import json
import os
import sys

import requests

config = {}
config_uri = os.path.expanduser('~') + '/.trello_tool.json'


def create_card_list(id_list, id_card_source, name):
    url = "https://api.trello.com/1/cards"
    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': config['key'],
        'token': config['token'],
        'idList': id_list,
        'idCardSource': id_card_source,
        'name': name
    }
    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    return json.loads(response.text)


def get_card_from_list(list_of_card_id):
    url = "https://api.trello.com/1/lists/{0}/cards".format(list_of_card_id)
    print(url)
    query = {
        'key': config['key'],
        'token': config['token'],
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )
    return json.loads(response.text)


def create_check_list_for_work_flow(card_id):
    url = "https://api.trello.com/1/checklists"

    query = {
        'key': config['key'],
        'token': config['token'],
        'idCard': card_id,
        'name': 'Work Flow',
        'pos': 'top'
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )
    return json.loads(response.text)


def create_check_list_item(check_list_id, name):
    url = "https://api.trello.com/1/checklists/{0}/checkItems".format(check_list_id)

    query = {
        'key': config['key'],
        'token': config['token'],
        'name': name
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )
    return response.text


def update_card_desc(card_id, desc):
    url = "https://api.trello.com/1/cards/{0}".format(card_id)

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': config['key'],
        'token': config['token'],
        'desc': desc
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )
    return response


def get_card_list_from_broad():
    url = "https://api.trello.com/1/boards/{0}/lists".format(config['broad_id'])

    query = {
        'key': config['key'],
        'token': config['token']
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )

    return json.loads(response.text)


def get_stay_stuck_id():
    card_lists = get_card_list_from_broad()
    stay_stuck_id = ''
    for card_list in card_lists:
        if card_list['name'] == config['stay_stuck_name']:
            stay_stuck_id = card_list['id']
    if stay_stuck_id == '':
        print("stay_stuck_name error")
        sys.exit(1)
    else:
        return stay_stuck_id


def get_template_card_id():
    template_card_list_name = config['template_card_list_name']
    template_card_name = config['template_card_name']
    card_lists = get_card_list_from_broad()
    template_card_list_id = ''
    template_card_id = ''
    for card_list in card_lists:
        if card_list['name'] == template_card_list_name:
            template_card_list_id = card_list['id']
    if template_card_list_id == '':
        print("template_card_name error")
        sys.exit(1)
    else:
        cards_in_template_list = get_card_from_list(template_card_list_id)
        for card in cards_in_template_list:
            if card['name'] == template_card_name:
                template_card_id = card['id']
        if template_card_id == '':
            print("template_card_name error")
            sys.exit(1)
        else:
            return template_card_id


def create_new_card_for_story(name, url, stay_stuck_id, template_card_id):
    new_card = create_card_list(stay_stuck_id, template_card_id, name.split(".")[0])
    new_card_id = new_card['id']
    work_flow_check_list = create_check_list_for_work_flow(new_card_id)
    work_flow_check_list_id = work_flow_check_list['id']
    fo = open(url + '/' + name, "r")
    work_flow_file_content = fo.read()
    work_flow_file_list = work_flow_file_content.split("######")
    update_card_desc(new_card_id, new_card['desc'] + work_flow_file_content)
    for i in range(1, len(work_flow_file_list)):
        print(i)
        print(work_flow_file_list[i])
        work_step = work_flow_file_list[i]
        work_flows = work_step.split(">")
        for work_flow in work_flows:
            create_check_list_item(work_flow_check_list_id, work_flow)
    fo.close()


def read_config():
    config_file = open(config_uri, 'r')
    config_json = config_file.read()
    global config
    config = json.loads(config_json)
    config['file_base_uri'] = config['file_base_uri'].replace("~", os.path.expanduser('~'))
    return config


def main(args=None):
    """The main routine."""
    read_config()
    stay_stuck_id = get_stay_stuck_id()
    template_card_id = get_template_card_id()
    print(len(sys.argv))
    publish_type = len(sys.argv) == 3
    print(publish_type)
    if len(sys.argv) == 3 :
        file_url = config['file_base_uri'] + sys.argv[1]
        file_name = sys.argv[2] + ".md"
        create_new_card_for_story(file_name, file_url, stay_stuck_id, template_card_id)
        return 0
    else:
        file_url = config['file_base_uri'] + sys.argv[1]
        files = os.listdir(file_url)  # 得到文件夹下的所有文件名称
        for file_name in files:  # 遍历文件夹
            if not os.path.isdir(file_name):
                create_new_card_for_story(file_name, file_url, stay_stuck_id, template_card_id)
    return 0


if __name__ == "__main__":
    sys.exit(main())
