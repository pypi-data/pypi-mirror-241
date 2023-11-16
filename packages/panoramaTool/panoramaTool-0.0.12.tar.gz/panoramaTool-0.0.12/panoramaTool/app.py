import concurrent.futures
import os

import csv

from flask import Flask, render_template, request
from dotenv import load_dotenv

from panoramaTool.panorama_api.api_request import APICall
from panoramaTool.panorama_api.post_rules import PostRulesManager

load_dotenv()

app = Flask(__name__)
template_path = os.path.join(os.path.dirname(__file__), 'templates')
app.template_folder = template_path
app.static_folder = os.path.join(os.path.dirname(__file__), 'static')
csv_folder = os.path.join(os.path.dirname(__file__), 'csv')
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        panorama_url = request.form['url']
        username = request.form['username']
        password = request.form['password']
        rule_name = request.form['rule_name']
        csv_file = request.files['csv_file']

        save_path = os.path.join(csv_folder, 'upload.csv')

        if os.path.exists(save_path):
            os.remove(save_path)

        csv_file.save(save_path)
        apikey = APICall.get_api_key(user=username, password=password, panorama_url=panorama_url)
        post_rules_manager = PostRulesManager(panorama_url=panorama_url, apikey=apikey, verify=False)
        response = create_post_rules_from_csv(read_csv(save_path), post_rules_manager, rule_name=rule_name)
        print(response)
        return "Done!"


def create_post_rules_from_csv(csv, post_rules_manager, rule_name):
    response = ["No CSV"]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for counter, csv_data in enumerate(csv):
            futures.append(executor.submit(create_post_rule, csv_data, post_rules_manager, rule_name, counter))

        concurrent.futures.wait(futures)

        for future in futures:
            response.append(future.result())

    return response


def create_post_rule(csv_data, post_rules_manager, rule_name, counter):
    return post_rules_manager.create_post_rule(action=csv_data.get('Action'),
                                               source_address=csv_data.get('Source address'),
                                               source_zone=csv_data.get('Source Zone'),
                                               destination_address=csv_data.get('Destination address'),
                                               destination_zone=csv_data.get('Destination Zone'),
                                               protocol=csv_data.get('IP Protocol').upper(),
                                               destination_port=csv_data.get('Destination Port'),
                                               name=f"{rule_name}{counter}",
                                               application="any")


def read_csv(file_path):
    csv_data = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_data.append(row)
    return csv_data


if __name__ == '__main__':
    app.run()
