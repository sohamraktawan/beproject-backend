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


# from langchain_openai import ChatOpenAI
# from langchain.chains import LLMChain, SimpleSequentialChain
# from langchain.prompts.prompt import PromptTemplate
# import os
# from dotenv import load_dotenv
# from pathlib import Path

# dotenv_path = Path('.env')
# load_dotenv(dotenv_path=dotenv_path)
# openai_api_key = os.getenv('OPENAI_API_KEY')

# llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model="gpt-3.5-turbo")
# llm2 = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model="gpt-3.5-turbo")


# file_path = 'src/server.js'
# out_path = 'output/server.py'

# try:
#     with open(file_path, 'r') as file:

        

#         file_content = file.read()
#         src_template = PromptTemplate(input_variables=["code"], template="""give me a pseudo code of the code.\n 
#                                       Provide the same for the functions called inside the routes.\n
#                                      Provide models required for database and their definition, database connection type and input for it strictly, server configuration of port,etc. \n {code}""")


#         # file_content =  "give me a pseudo code of the code. Provide the same for the functions called inside the routes. Provide models required for database and their definition, database connection type and input for it strictly, server configuration of port,etc. "  + file_content
#         # data_object = json.loads(file_content)

#         # start_path = "src/" + data_object["main"]
#         # print(open(start_path,'r').read())

#         # Connect to the database in the same way described in the instructions.
#         chain_one = LLMChain(llm=llm, prompt = src_template)
#         # output_content = llm.invoke(file_content)
#         # print(output_content.content)
#         op_template = PromptTemplate(input_variables=["pseudocode"], template=""" {pseudocode} \n write a code for all the functions in python flask framework using this information. 
#         Follow all the following instructions strictly : 
#         Use PyMongo for database connection if mongodb is used, do not use MongoClient.\n
#         Use the time library for time-related logic.\n
#         Parse objects returned from database properly, take care that ObjectId is not JSON serializable, use bson library. \n 
#         Import all the libraries used in the output code.\n
#         Get the necessary environment variables from '.env' file using dotenv library. \n
#         Solve the tls handshake error in database connection by using certifi library, do not set 'MONGO_TLS_CA_FILE' in app.config.\n 
#         Never jsonify objects containing ObjectId directly. \n
#         Never return objects containing ObjectId directly.\n
#         Give the code only, do not write instructions or anything else, such that I can directly write it to a file. \n """)

#         # output_content.content = output_content.content + "\n write a code for all the functions in python flask framework using this information. Follow all the following instructions strictly : Use PyMongo for database connection if mongodb is used. Use the time library for time-related logic. Parse objects returned from database properly, take care that ObjectId is not JSON serializable, use bson library. Import all the libraries used in the output code. Get the necessary environment variables from '.env' file. Solve the tls handshake error in database connection by using certifi library, do not set 'tls_ca_file' in app.config. Never jsonify objects containing ObjectId directly. Never return objects containing ObjectId directly. Give the code only, do not write instructions or anything else."
#         # output_code = llm.invoke(output_content.content)

#         chain_two = LLMChain(llm=llm2, prompt = op_template)

#         final_chain = SimpleSequentialChain(chains=[chain_one, chain_two])
#         final_output = final_chain.invoke(file_content)

#         # output_code.content = output_code.content + "\n check if cursor object is accessed properly. give the debugged code only, do not write instructions or anything else. "

#         # output_debug = llm.invoke(output_code.content)


# except FileNotFoundError:
#     print(f"The file at {file_path} does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# try:
#     with open(out_path, 'w') as file:

#         # file_content = file.read()
#         # file_content = file_content + "convert this code to python in flask framework"
#         # data_object = json.loads(file_content)

#         # start_path = "src/" + data_object["main"]
#         # print(open(start_path,'r').read())

#         # output_content = llm.invoke(file_content)
#         output = ""
#         print(final_output['output'][0:8])
#         if final_output['output'][0:9] == "```python":
#             end = len(final_output['output'])-3
#             print(end)
#             output = final_output['output'][9:end]
#             print(output)
#         else:
#             file.write(final_output['output'])
#         file.write(output)


# except FileNotFoundError:
#     print(f"The file at {file_path} does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")

import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts.prompt import PromptTemplate
import os
from dotenv import load_dotenv
from pathlib import Path
import json
import time

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
openai_api_key = os.getenv('OPENAI_API_KEY')





# Define the directory to start traversing
root_dir = 'D:/bepro/backend/src'

# Function to iterate through files
def iterate_js_files(directory):
    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')  # Exclude node_modules directory
        for file in files:
            if file.endswith('.js'):
                yield os.path.join(root, file)

# Function to print text within files
def print_file_content(file_path):
    with open(file_path, 'r') as file:
        print(file.read())

def return_file_content(file_path):
    with open(file_path, 'r') as file:
       return file.read()
complete_code = ""

# Iterate through JavaScript files and print their content
for js_file in iterate_js_files(root_dir):
    # print("\n File:", js_file)
    # print("Content:")
    # print_file_content(js_file)
    # print()

    complete_code = complete_code + "\nFile:" + js_file
    complete_code = complete_code + "\nContent:\n" + return_file_content(js_file)

# print(complete_code)

llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model="gpt-3.5-turbo")

# llm2 = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model="gpt-3.5-turbo")


code_info_template = PromptTemplate(input_variables=["complete_code"], template="""{complete_code} \n I need to convert this code to Python Flask Framework. Just answer the following questions based on it. Which routes, models and controllers are present in the code with filenames?. Give me only the things asked for and nothing else""")

code_info2_template = PromptTemplate(input_variables=["Code_info"], template="""{Code_info} \n DO NOT GENERATE CODE IN JAVASCRIPT. I need to convert this application to Python Flask Framework. Which Blueprints, Models and Controllers should be created based on this information? Give me only the things asked for and nothing else""")

# Do not give me description of this code. Give me which blueprints, models and controllers with code can be made in the flask framework. Use this format to provide the output: 
# <Blueprint-file-name> : <Blueprint-file-code> 
# <Model-file-name> : <Model-file-code>
# <Controller-file-name> : <Controller-file-code>

output = llm.invoke(complete_code + """I need to convert this code to Python Flask Framework. Give me which server, config, blueprints, models and controllers can be made in the flask framework with just the basic code for functions without the implementation, especially for controllers and blueprints. Take into consideration which database is used - MongoDB or SQL. Write complete code, do not cut it short. Use this format to provide the output in JSON format for all files, where "name" field denotes name of the file and "code" field denotes the code to be written in the file. DO NOT GIVE THE WRONG FORMAT. The format contains array of file objects for blueprints, models and controllers as follows: 
{
                    
    {"server": {"name": <file-name>, "code": <server-code>}} ,
                    
    {"config": {"name": <file-name>, "code": <config-code>}},
                    
    {"blueprints":
        [{ "name" : <file-name> , "code" : <blueprint-code>},{"name" : <file-name> , "code" : <blueprint-code> }, ...]
    },
                    
    {"models":
        [{ "name" : <file-name> , "code" : <model-code>},{"name" : <file-name> , "code" : <model-code> }, ...]
    },
                    
    {"controllers":
        [{ "name" : <file-name> , "code" : <controller-code>},{"name" : <file-name> , "code" : <controller-code> }, ...]
    }

}""")
time.sleep(20)
# output2 = llm2.invoke(output.content + "\n I need to convert this application to Python Flask Framework. Which Blueprints, Models and Controllers should be created based on this information? Give me only the things asked for and nothing else")
print(json.loads(output.content)["config"]) 

data = {}

try:
    data = json.loads(output.content)
except Exception as e:
    print("wrong output format")


def create_directory(directory):
    try:
        # Create target Directory if it doesn't exist
        os.makedirs(directory)
        print("Directory ", directory, " Created ")
    except FileExistsError:
        print("Directory ", directory, " already exists")

def create_file(directory, filename, content):
    try:
        # Joining directory path and filename
        filepath = os.path.join(directory, filename)
        
        # Writing content into the file
        with open(filepath, 'w') as file:
            file.write(content)
        print("File ", filename, " created and written successfully")
    except Exception as e:
        print("Error creating/writing the file:", e)

# Creating the output directory if it doesn't exist
create_directory("output")

# Creating the subdirectory under the output directory


# # Creating the file within the subdirectory and writing content into it

directories = ["blueprints", "models", "controllers"]


for directory in directories:
    sub_directory_path = os.path.join("output", directory)
    create_directory(sub_directory_path)
    for file in data[directory]:
        create_file(sub_directory_path, file["name"], file["code"])



create_file("output", data["server"]["name"], data["server"]["code"])
create_file("output", data["config"]["name"], data["config"]["code"])

out_dir = 'D:/bepro/backend/output'

data_dict = {}
blueprints = ""
models = ""
controllers = ""
for bp in data["blueprints"]:
    data_dict[bp["name"]] = "blueprint"
    blueprints = blueprints + bp["name"] + " ,"
for md in data["models"]:
    data_dict[md["name"]] = "model"
    models = models + md["name"] + " ,"
for ct in data["controllers"]:
    data_dict[ct["name"]] = "controller"
    controllers = controllers + ct["name"] + " ,"
data_dict[data["server"]["name"]] = "server"
data_dict[data["config"]["name"]] = "config"

blueprints = blueprints[:-1] + '.'
models = models[:-1] + '.'
controllers = controllers[:-1] + '.'

print(blueprints)
print(models)
print(controllers)

def iterate_py_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                yield os.path.join(root, file)

for py_file in iterate_py_files(out_dir):
    # print("\n File:", js_file)
    # print("Content:")
    # print_file_content(js_file)
    # print()
    complete_out_code = ""
    # complete_code = llm.invoke("""The structure of the flask project is as follows : There is a server with the name""" + data["server"]["name"] + """. With the server, there are the "blueprints","models" and "controllers" directories. All the blueprints are present in the "blueprints", models are present in "models" and controllers are present in the "controllers" directories. We need to import all the blueprint files in the server file. We need to import all controller files in the blueprint files. We need to import all the model files in the controller files. This file is a """ + data_dict[os.path.basename(py_file)] + """. The blueprint file names are""" + blueprints + """ The model file names are """ + models + """ The controller file names are """ + controllers + """Modify the code given below and just import all the necessary files as instructed above strictly, without changing previous code strictly. Do not import the file itself. Do not use '.' operator before directory while importing. Use proper project hierarchy while importing files. Give the code only, do not write instructions or anything else. \n""" + return_file_content(py_file))
    

    complete_out_code_raw = llm.invoke(complete_code + """I need to convert this code to Python Flask Framework project, which contains server, config, blueprints, models and controllers. The server file is """ + data["server"]["name"] + """ . The config file is """ + data["config"]["name"] + """ .The blueprint files are """ + blueprints + """ The model files are """ + models + """ The controller files are """ + controllers + """ Write code for the file """ + os.path.basename(py_file) + """". This file is a """ + data_dict[os.path.basename(py_file)] + """ file.
    
    Follow the following instructions while writing code for this file : 
    1) The server file code will import the Flask "app" from config.py file , register flask blueprints and run the imported "app" only and nothing else.
    2) The config file code will create Flask app, establish database connection in app config only and nothing else strictly, get the database connection string from the ".env" file as "MONGO_URI". Use certifi library to solve the SSL Handshake error. Start dabase connection like this - "mongo = Pymongo(app, tlsCAFile=certifi.where())"
    3) Write route names only in the blueprint file code . Use this format strictly for writing all routes - "task_blueprint.route('/create', methods=['POST'])(create_task)" in the blueprint file code.
    DO NOT USE THE FOLLOWING FORMAT STRICTLY :
    format -                                    
    "@auth_blueprint.route('/auth', methods=['POST'])
        def auth():
            return auth()"
    4) Import required python functions from controller files for all the routes in blueprint file code. for example - "from controllers.task_controller import create_task, get_tasks, complete_task, delete_task"
    4) Do not write any route implementation in server, config, blueprint and model file codes strictly. 
    5) Blueprints should contain route names which are present in above code only, do not add extra route names. 
    6) The model file code contains database models only and should not contain any implementation.
    7) Do not declare controller file code as a Flask Blueprint, they just contain python functions strictly and should not mention anything about routes. 
    8) The controller file code will contain python functions for specific elaborate implementation for example "def signup()" and should contain the elaborate code for each function.
    9) Use PyMongo for database connection if mongodb is used. Follow this project structure strictly. 
                         
    Give the code for this file only, do not write instructions or anything else strictly, so that it can be directly written in a python file.""")
    
    time.sleep(20)

    complete_out_code = llm.invoke(complete_out_code_raw.content + """Extract the code from this and return. Give the code only, do not write instructions or anything else strictly. """)
    print(complete_out_code.content)
    with open(py_file, 'w') as file:
        if complete_out_code.content[0:9] == "```python":
            end = len(complete_out_code.content)-3
            print(end)
            output =complete_out_code.content[9:end]
            file.write(output)
        else:
            file.write(complete_out_code.content)

    
complete_output_code = ""



#Correct the import statements in the code given below based on the code given above and add import statements for all the necessary entities as instructed strictly, keeping the existing code same.
for py_file in iterate_py_files(out_dir):

    complete_output_code = complete_output_code + "\nFile:" + py_file
    complete_output_code = complete_output_code + "\nContent:\n" + return_file_content(py_file)


for py_file in iterate_py_files(out_dir):
    # complete_output_code = ""

    if(data_dict[os.path.basename(py_file)] != "server" ):
        continue
    
    import_code = llm.invoke(complete_output_code + """The structure of the flask project is as follows : There is a server with the name""" + data["server"]["name"] + """ . There is a config file with name """ + data["config"]["name"] + """and the project contains server, config, blueprints, models and controllers. With the server and config, there are the "blueprints","models" and "controllers" directories. All the blueprint files are present in the "blueprints" directory, model files are present in "models" directory and controller files are present in the "controllers" directory. The blueprint file names are""" + blueprints + """ The model file names are """ + models + """ The controller file names are """ + controllers + """ 
    
    Modify the code given below to import the appropriate entities in the existing code.
                             
    Instructions for modifying code are: 
    1) Do not remove or change any existing code or implementation from the below code strictly. 
    2) Import Blueprints and register Blueprints in server file code. Import the Flask app from config file in server file code.
    3) Import python modules required in the code. 
    4) Do not import the file inside itself. Use proper project hierarchy while importing files. 
    
     \n""" + """
     The below code is of """+ os.path.basename(py_file) + """ The below code is of a  """ + data_dict[os.path.basename(py_file)] + """ file. \n Code : \n""" + return_file_content(py_file) + """Give the modified code only, do not write instructions or anything else strictly.""")

    time.sleep(20)
    

    with open(py_file, 'w') as file:
        if import_code.content[0:9] == "```python":
            end = len(import_code.content)-3
            print(end)
            output = import_code.content[9:end]
            file.write(output)
        else:
            file.write(import_code.content)

    
function_content =  llm.invoke(complete_output_code + """Provide the names of the functions imported from controller files to the blueprint with the controller file name.
Give the names in this format :
{
"<controller-file-name>.py" : "<name1> , <name2> , <name3>" , 
"<controller-file-name>.py" : " <name1> , <name2> , <name3>"
}""")

print(function_content.content)

function_data = json.loads(function_content.content)

pseudo_code = ""

pseudo_code = llm.invoke(complete_code + """Write an elaborate line-by-line pseudo-code with all the logic for the controller functions given below based on the above code.""" +  function_content.content)

print(pseudo_code.content)

for py_file in iterate_py_files(out_dir):
    # complete_output_code = ""

    if(data_dict[os.path.basename(py_file)] != "controller"):
        continue
    
    import_code = llm.invoke(pseudo_code.content + """ Write the complete elaborate code for the following python functions in Flask Framework based on the above pseudo-code.
    Follow the following instructions while writing the code:
    1) Do not create a Flask blueprint for the controller file code, controller file code should contain the python functions only.
    2) Import "mongo" database connection object from config.py and use it in this code.
    3) Do not use database models for accessing the database, access database objects directly using "mongo" object. 
    4) Use the time library for time-related logic. 
    5) Parse objects returned from database properly, take care that ObjectId is not JSON serializable, use bson library. 
    6) Import all the libraries used in the output code. 
    7) This is the controller file code, the database connection and Flask "app" is initialized in config.py file, import the Flask "app" from config.py file. 
    8) Write code for python functions called inside these functions as well.
     Functions : """ + function_data[os.path.basename(py_file)] + """. Give the code only, do not write instructions or anything else strictly.""")

    time.sleep(20)
    

    with open(py_file, 'w') as file:
        if import_code.content[0:9] == "```python":
            end = len(import_code.content)-3
            print(end)
            output = import_code.content[9:end]
            file.write("from config import mongo \n")
            file.write(output)
        else:
            file.write("from config import mongo \n")
            file.write(import_code.content)
            



for py_file in iterate_py_files(out_dir):
    # complete_output_code = ""

    if(data_dict[os.path.basename(py_file)] != "blueprint"):
        continue
    
    import_code = llm.invoke(return_file_content(py_file) + """Write all these routes in this format -  "<blueprint_name>.route('<route-endpoint>', methods=['<method>'])(<controller-function>)" and import all the required python function from the controller files. Remove the "@" before blueprint name in the format.  Give the code for this file only, do not write instructions or anything else strictly, so that it can be directly written in a python file.""")

    time.sleep(20)
    

    with open(py_file, 'w') as file:
        if import_code.content[0:9] == "```python":
            end = len(import_code.content)-3
            print(end)
            output = import_code.content[9:end]
            # file.write("import mongo from config \n")
            file.write(output)
        else:
            file.write(import_code.content)





# pseudo_code = ""

# pseudo_code = llm.invoke(complete_code + """Give me a pseudo code of the code for all the controller functions in this code. Do not include model co"""" )


# for py_file in iterate_py_files(out_dir):
#     # complete_output_code = ""

#     if(data_dict[os.path.basename(py_file)] != "server"):
#         continue
    
#     import_code = llm.invoke(complete_output_code + """The structure of the flask project is as follows : There is a server with the name""" + data["server"]["name"] + """ . There is a config file with name """ + data["config"]["name"] + """and the project contains server, config, blueprints, models and controllers. With the server and config, there are the "blueprints","models" and "controllers" directories. All the blueprint files are present in the "blueprints" directory, model files are present in "models" directory and controller files are present in the "controllers" directory. The blueprint file names are""" + blueprints + """ The model file names are """ + models + """ The controller file names are """ + controllers + """ 
    
#     Modify the code given below to import the appropriate entities in the existing code.
                             
#     Instructions for modifying code are: 
#     1) Do not remove or change any existing code or implementation from the below code strictly. 
#     2) Import all python functions present in controller files in blueprint file code.
#     3) Do not remove or change the existing python functions present in controller file code strictly, do not create flask Blueprint in controller file code.
#     4) Import Blueprints and register Blueprints in server file code. Import the Flask app from config file in server file code. 
#     5) Do not make any changes to config file code strictly.
#     6) Import python modules required in the code. 
#     7) Do not change anything in the model file code.
#     8) Do not import the file inside itself. Use proper project hierarchy while importing files. 
    
#      \n""" + """
#      The below code is of """+ os.path.basename(py_file) + """ The below code is of a  """ + data_dict[os.path.basename(py_file)] + """ file. \n Code : \n""" + return_file_content(py_file) + """Give the modified code only, do not write instructions or anything else strictly.""")

#     time.sleep(20)
    

#     with open(py_file, 'w') as file:
#         if import_code.content[0:9] == "```python":
#             end = len(import_code.content)-3
#             print(end)
#             output = import_code.content[9:end]
#             file.write(output)
#         else:
#             file.write(import_code.content)
