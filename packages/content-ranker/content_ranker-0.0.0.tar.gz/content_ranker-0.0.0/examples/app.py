"""
‫این ماژول یک سرور flask را برای شباهت پرس و جو بالا می آورد.
‫برای اطلاعات بیشتر به README.md پروژه رجوع کنید.
"""
import hashlib
import json
import logging.config
import os
import subprocess

import torch
from flask import Flask, request, jsonify, render_template
from flask_log_request_id import RequestID, current_request_id
from flask_restx import Resource, Api, fields

import sys
from pathlib import Path

sys.path.append((Path(__file__).parent.parent / "src").as_posix())

print((Path(__file__).parent.parent / "src").as_posix())

from content_ranker.exceptions import MissingEnvironmentVariable
from content_ranker.models import MainContentClassificationPredict

APP_NAME = "level-tagger-visualization"
APP_VERSION = "0.0.1"
CWD = Path(__file__).parent
PROJECT_PATH = CWD.parent
LOGGING_CONFIG_PATH = CWD.joinpath("logging.ini")
RESOURCE_PATH = os.path.join(PROJECT_PATH, "src", "content_ranker", "resources")
DOWNLOAD_PATH = os.path.join(CWD, "templates")

app = Flask(__name__)
RequestID(app)

logging.config.fileConfig(LOGGING_CONFIG_PATH, disable_existing_loggers=False)
old_factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    """
    ‫ این تابع تعدادی فیلد را به همه log های سیستم اضافه می کند
    """
    record = old_factory(*args, **kwargs)
    record.app_name = APP_NAME
    record.app_version = APP_VERSION
    record.trace_id = current_request_id()
    return record


logging.setLogRecordFactory(record_factory)
logger = logging.getLogger(__name__)


def get_environment_variable(variable_name, default=None):
    """
    ‫مقدار یک متغیر محیطی را دریافت میکند

    ‫مقدار یک متغیر محیطی را دریافت میکند. در صورت عدم وجود متغیر، مقدار پیش فرض را برمیگرداند
    ‫و اگر مقدار پیش فرضی مشخص نشود، MissingEnvironmentVariable ارورر میدهد.
    Args:
        variable_name: string
        ‫نام متغیر محیطی موردنظر
        default: string, default=None
        ‫مقدار پیشفرض متغیر موردنظر

    Returns: string
    ‫مقدار متغیر محیطی یا در صورت عدم وجود مقدار پیش فرض

    """
    variable_value = os.getenv(variable_name, default)
    if not variable_value:
        logger.error("%s env variable doesn't exists", variable_name)
        raise MissingEnvironmentVariable(
            "{} env variable doesn't exists".format(variable_name))
    return variable_value


MODEL_FILE = get_environment_variable("MODEL_FILE", default="model.pt")
MODEL_ADDRESS = os.path.join(RESOURCE_PATH, MODEL_FILE)
TAG_MAP_FILE = get_environment_variable("TAG_MAP_FILE", default="tags.json")
TAG_MAP_ADDRESS = os.path.join(RESOURCE_PATH, TAG_MAP_FILE)
INPUT_DIM = int(get_environment_variable("INPUT_DIM", default="51"))
DENSE_SIZE = int(get_environment_variable("DENSE_SIZE", default="256"))
HIDDEN_UNITS = int(get_environment_variable("HIDDEN_UNITS", default="128"))
NUM_LAYERS = int(get_environment_variable("NUM_LAYERS", default="1"))
DROPOUT = float(get_environment_variable("DROPOUT", default="0.1"))
TIME_OUT = int(get_environment_variable("TIME_OUT", default="30"))
WAITING_TIME = int(get_environment_variable("WAITING_TIME", default="30"))
SERVER_IP = get_environment_variable("SERVER_IP", default="0.0.0.0")
SERVER_PORT = int(get_environment_variable("SERVER_PORT", default="5000"))

DESC = "این سرویس، نتایج level tagger را برای یک url داده شده نشان می دهد."
api = Api(app, title='level tagger visualization', description=DESC)
name_space_levelـtaggerـvisualization = api.namespace('level-tagger-visualization')
levelـtaggerـvisualization_request_body = name_space_levelـtaggerـvisualization.model(
    "request body",
    {
        "url": fields.String(
            description="url of page",
            required=True,
            name="url",
            example="https://www.farsnews.ir/news/14001018000246/%D9%85%D8%B0%D8%A7%DA%A9%D8%B1%D8%A7%D8%AA-%D9%88%DB%8C%D9%86-%D8%A7%D8%B2-%D8%B3%D9%81%D8%B1-%D8%AF%DB%8C%D9%BE%D9%84%D9%85%D8%A7%D8%AA%E2%80%8C-%DA%A9%D8%B1%D9%87%E2%80%8C%D8%A7%DB%8C-%D9%88-%D8%B1%D8%A7%DB%8C%D8%B2%D9%86%DB%8C%E2%80%8C%D9%87%D8%A7%DB%8C-%D9%86%D9%85%D8%A7%DB%8C%D9%86%D8%AF%D9%87-%D8%B3%D8%B9%D9%88%D8%AF%DB%8C-%D8%AA%D8%A7-%D8%A7%D8%A8%D8%B1%D8%A7%D8%B2")},
)


def prepare_model():
    """
    ‫نمونه ای از کلاس  MainContentClassificationPredict تولید می کند.

    Returns: MainContentClassificationPredict model
    """
    device = torch.device(0 if torch.cuda.is_available() else 'cpu')
    print(f'device : {device}')
    kwargs = {'input_dim': INPUT_DIM,
              'dense_size': DENSE_SIZE,
              'hid_dim': HIDDEN_UNITS,
              'num_layer': NUM_LAYERS,
              'num_classes': 6,
              'dropout': DROPOUT,
              'seed': 1234}
    MCP = MainContentClassificationPredict(MODEL_ADDRESS, TAG_MAP_ADDRESS, kwargs, device)
    return MCP


def validate_request_data(data):
    """
    ‫داده های درخواست کاربر را چک میکند و در صورت valid نبودن داده، exception تولید میکند

    Args:
        data: string
        ‫داده request body

    Returns: string
    ‫خروجی، url است.
    """
    try:
        parsed_data = json.loads(data)
    except json.JSONDecodeError as e:
        logger.error("cannot decode request json body", exc_info=e)
        raise json.JSONDecodeError
    url = parsed_data.get("url")
    if not url:
        logger.error("request body doesnt contain required field url")
        raise ValueError
    return url


def get_all_files_of_url(url):
    url_bytes = bytes(url, encoding='utf-8')
    file_name = hashlib.sha1(url_bytes).hexdigest()
    file_name = file_name + ".html"
    save_address = os.path.join(DOWNLOAD_PATH, file_name)
    subprocess.run(["wget", '-O', save_address, "-k", url])
    return save_address


@app.route('/level_tagger_visualization/', methods=['POST'])
def level_tagger_visualization():
    """
    ‫این تابع درخواست کاربر را دریافت میکند و نتیجه را برای یک url نشان می دهد.
    """
    logger.info("show level tagger results", extra={"body": request.data})
    try:
        url = validate_request_data(request.data)
    except json.JSONDecodeError:
        logger.info("response with status code 400, invalid json body")
        return "invalid json request body", 400
    except ValueError:
        logger.info("response with status code 400, invalid request arguments")
        return "invalid request arguments", 400
    try:
        save_address = get_all_files_of_url(url)
    except:
        logger.info("response with status code 400, can not get the page")
        return "problem in loading the webpage of the url", 400
    try:
        MCP.make_colored_html(save_address)
    except:
        logger.info("response with status code 400, can not score texts of page")
        return "problem in scoring texts of the webpage of the url", 400
    filename = os.path.basename(save_address)
    output_url = f"http://{SERVER_IP}:{SERVER_PORT}/show_page/{filename}"
    logger.info("response with status code 200", extra={"output_url": output_url})
    return jsonify({"output_url": output_url})


@app.route('/show_page/<filename>', methods=['GET'])
def show_page(filename):
    logger.info("show the html : %s" % (filename))
    return render_template(filename)


@name_space_levelـtaggerـvisualization.route(
    "/",
    doc={
        "description": "‫نتایج level tagger را برای url ورودی نشان می دهد."})
class MainClass(Resource):
    @name_space_levelـtaggerـvisualization.doc(
        body=levelـtaggerـvisualization_request_body, responses={
            200: 'Success', 400: 'Invalid Request Body'})
    def post(self):
        return level_tagger_visualization()


if __name__ == "__main__":
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)
    MCP = prepare_model()
    app.run(host=SERVER_IP, port=SERVER_PORT)
