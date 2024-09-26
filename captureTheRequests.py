from flask import Flask, request, send_file, jsonify
import logging
import os

#---------------------------------------------------------------------------------
# CONFIGURATION :

app = Flask(__name__)

# App Basic Customization :
PORT = 51951 # port on which the app will be running (for reverse proxy purposes)
LOG_FILE_PATH = "requests.log" # files in which all connections will be stored
DEBUG = True # set false if production environnement
HTTP_SERVER_DIRECTORY_PATH = "http" # directory in which files for the server will be stored (server files not app files)
CUSTOM_HTTP_PATH = "" # leave empty if you want files to be directly accessible at the root / of the server


# Default Logs settings :
logging.basicConfig(level=logging.INFO)
#file on which every requests will be appended
log_file = LOG_FILE_PATH
# some logging magic
file_handler = logging.FileHandler(log_file, mode='a') # append to the log_file
file_handler.setLevel(logging.INFO)  

formatter = logging.Formatter('%(asctime)s - %(message)s') # set timestamps for each request
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
#---------------------------------------------------------------------------------


@app.before_request
# logging function that'll log each and every request received on the endpoints
def log_request():
    app.logger.info(
        "-"*37+"\n\n"+ #formatting
        
        f"Request: {request.method} {request.url}\n"+
        
        f"Headers: {request.headers}"+
        
        f"POST Data: {request.data}\n\n"
        
        +"-"*63+"\n" #formatting
    )


@app.route('/api', methods=['GET', 'POST'])
#simple endpoint to see if the app is running correctly
def checkstatus():
    return jsonify({"status":"The app is running"})


@app.route('/cr', methods=['GET', 'POST'])
# custom request Endpoint
def check_responseGet():
    return jsonify({"status": "success"})


@app.route(CUSTOM_HTTP_PATH + '/<path:filename>', methods=['GET'])
def renfer_file(filename):

    base_directory = os.path.abspath(os.path.join(os.getcwd(), HTTP_SERVER_DIRECTORY_PATH))
    file_path = os.path.join(base_directory, filename)

    print(f"DEBUGGING {file_path}")
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=False)
    else:
        return jsonify({"error": "File not found"}), 404



# run the app on the port
if __name__ == '__main__':
    app.run(port=PORT,debug=DEBUG)
