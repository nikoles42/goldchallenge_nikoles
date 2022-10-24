from flask import Flask, request, jsonify
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from
import re

app = Flask(__name__) #deklarasi Flask
app.json_encoder = LazyJSONEncoder

swagger_template = dict(
info = {
    'title': LazyString(lambda: 'percobaan membuat api swagger'),
    'version': LazyString(lambda: '1'),
    'description': LazyString(lambda: 'coba-coba'),
    },
    host = LazyString(lambda: request.host)
)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)


def _remove_punct(s):
    return re.sub(r"[^\w\d\s]+", "",s)

@swag_from("swagger_config_post.yml", methods=['POST'])
@app.route("/clean_text/v1", methods=['POST']) 
def remove_punct_post():
    s = request.get_json()
    non_punct = _remove_punct(s['text'])
    return jsonify({"hasil_bersih":non_punct})


@swag_from("swagger_config.yml", methods=['GET'])
@app.route("/get_text/v1", methods=['GET'])
def return_text():
    name_input = request.args.get('name')
    nohp_input = request.args.get('nomerhp')
    return_text = {
        "text":f"halo semuanyaa!!! nama saya adalah {name_input}",
        "no_hape":nohp_input
    }
    return jsonify(return_text) 

if __name__ == "__main__":
    app.run(port=1234, debug=True)