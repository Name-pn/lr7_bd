from flask import request, Flask
import services

app = Flask(__name__)

@app.route('/blocks', methods=['POST'])
def post_block():
    if request.is_json:
        return services.create_block(request.get_json())
    return {}

@app.route('/countries', methods=['POST'])
def post_block():
    if request.is_json:
        return services.create_country(request.get_json())
    return {}

@app.route('/regions', methods=['POST'])
def post_block():
    if request.is_json:
        return services.create_block(request.get_json())
    return {}

@app.route('/blocks', methods=['GET'])
def get_block():
    return services.get_blocks()

@app.route('/blocks/<pk>', methods=['GET'])
def get_block_detail(pk: int):
    return services.get_block_detail(pk)

@app.route("/post")
def sendDate():
    print(1)