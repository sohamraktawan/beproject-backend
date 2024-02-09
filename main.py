# import json
# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# from pathlib import Path
# from langchain.text_splitter import Language
# from langchain_community.document_loaders.generic import GenericLoader
# from langchain_community.document_loaders.parsers import LanguageParser

# dotenv_path = Path('.env')
# load_dotenv(dotenv_path=dotenv_path)
# openai_api_key = os.getenv('OPENAI_API_KEY')

# client = OpenAI(api_key=openai_api_key)

# file_path = 'src/server.js'

# try:
#     with open(file_path, 'r') as file:
#         # Read the entire content of the file
#         file_content = file.read()
#         file_content = file_content + "convert this code to python in flask framework"
#         # data_object = json.loads(file_content)

#         # start_path = "src/" + data_object["main"]
#         # print(open(start_path,'r').read())

# except FileNotFoundError:
#     print(f"The file at {file_path} does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")






# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "user", "content": file_content},
#   ]
# )

# print('from flask import Flask, jsonify\nfrom flask_cors import CORS\nfrom flask import request\nimport pymongo\nfrom pymongo import MongoClient\nimport os\n\napp = Flask(__name__)\nCORS(app)\napp.config[\'CORS_HEADERS\'] = \'Content-Type\'\n\nclient = MongoClient(os.getenv("db_connect"))\ndb = client.get_database("database")\n\n@app.route(\'/\')\ndef index():\n    return "Hello, World!"\n\n@app.route(\'/tasks\', methods=[\'GET\'])\ndef get_tasks():\n    tasks = db.tasks.find()\n    tasks_list = []\n    for task in tasks:\n        tasks_list.append({\n            \'id\': str(task[\'_id\']),\n            \'title\': task[\'title\'],\n            \'description\': task[\'description\']\n        })\n    return jsonify(tasks_list)\n\n@app.route(\'/task\', methods=[\'POST\'])\ndef add_task():\n    title = request.json[\'title\']\n    description = request.json[\'description\']\n    task = {\n        \'title\': title,\n        \'description\': description\n    }\n    result = db.tasks.insert_one(task)\n    return f"Task added with id: {result.inserted_id}"\n\nif __name__ == \'__main__\':\n    app.run()')


from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
openai_api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)


file_path = 'src/server.js'
out_path = 'output/server.py'

try:
    with open(file_path, 'r') as file:

        file_content = file.read()
        file_content =  "give me a pseudo code of the code in terms of routes input, output and functionality with exact fields in request and response, specify exact values for the inputs and outputs always, add a description about every step. Provide the same for the functions called inside the routes. Provide models required for database and their definition, database connection type and input for it strictly, server configuration of port,etc. Give python/flask alternative libraries to the libraries used in the code wherever required, avoid deprecated libraries."  + file_content
        # data_object = json.loads(file_content)

        # start_path = "src/" + data_object["main"]
        # print(open(start_path,'r').read())

        # Connect to the database in the same way described in the instructions.

        output_content = llm.invoke(file_content)
        print(output_content.content)
        output_content.content = output_content.content + "\n write a code for all the functions in python flask framework using this information. Follow all the following instructions strictly : Use PyMongo for database connection if mongodb is used. Use the time library for time-related logic. Parse objects returned from database properly, take care that ObjectId is not JSON serializable, use bson library. Import all the libraries used in the output code. Get the necessary environment variables from '.env' file. Solve the tls handshake error in database connection by using certifi library, do not set 'tls_ca_file' in app.config. Never jsonify objects containing ObjectId directly. Never return objects containing ObjectId directly. Give the code only, do not write instructions or anything else."
        output_code = llm.invoke(output_content.content)

        # output_code.content = output_code.content + "\n check if cursor object is accessed properly. give the debugged code only, do not write instructions or anything else. "

        # output_debug = llm.invoke(output_code.content)


except FileNotFoundError:
    print(f"The file at {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


try:
    with open(out_path, 'w') as file:

        # file_content = file.read()
        # file_content = file_content + "convert this code to python in flask framework"
        # data_object = json.loads(file_content)

        # start_path = "src/" + data_object["main"]
        # print(open(start_path,'r').read())

        # output_content = llm.invoke(file_content)

        file.write(output_code.content)


except FileNotFoundError:
    print(f"The file at {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


