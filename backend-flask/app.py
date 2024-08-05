from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os

log_dir = r"C:\logs"
os.makedirs(log_dir, exist_ok=True)


app = Flask(__name__)
CORS(app)

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

    app.logger.debug(f"environ: {request.environ}")
    
    user = request.environ.get("HTTP_REMOTE_USER")

    if not user:
        user = "jamin"

    response = jsonify(
        {
            "user": f"{user}"
        }
    )

    app.logger.debug(response)
    
    return response

    
if __name__ == "__main__":
    app.run()