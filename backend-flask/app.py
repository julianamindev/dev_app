from flask import Flask, request
import logging
import os

log_dir = r"C:\logs"
os.makedirs(log_dir, exist_ok=True)


app = Flask(__name__)

file_handler = logging.FileHandler(os.path.join(log_dir, "app.log"))
stream_handler = logging.StreamHandler()

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [file_handler, stream_handler]
)

@app.route("/")
def home():
    app.logger.debug("flask started")

    # headers = request.headers

    # app.logger.debug(f"headers: {headers}")
    
    # user = request.headers.get("X-Auth-User")
    app.logger.debug(f"environ: {request.environ}")
    
    # app.logger.debug(f"user: {user}")
    
    # str = f"hi there {user}"
    return f"hi {request.environ.get("HTTP_REMOTE_USER")}"
    # user = request.environ.get("REMOTE_USER")
    # # app.logger.debug(f"User access: {user}")
    # if user:
    #     return f"Logged in as {user}"
    # else:
    #     return "No user logged in"
    
if __name__ == "__main__":
    app.run()