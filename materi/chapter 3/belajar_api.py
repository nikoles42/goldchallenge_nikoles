from flask import Flask, request, jsonify
import re

app = Flask(__name__) #deklarasi Flask

def _remove_punct(s):
    return re.sub(r"[^\w\d\s]+", "",s)

@app.route("/clean_text/v1", methods=['POST']) 
def remove_punct_post():
    s = request.get_json()
    non_punct = _remove_punct(s['text'])
    return jsonify({"hasil_bersih":non_punct})

@app.route("/get_text/v1", methods=['GET']) #ini adalah decorator
def return_text():
    name_input = request.args.get('name') #mendapatkan nilai dari query pada url
    nohp_input = request.args.get('nomerhp') #mendapatkan nilai dari query pada url


    return_text = {
        "text":f"halo semuanyaa!!! nama saya adalah {name_input}",
        "no_hape":nohp_input
        #"halo semuanyaa!!! nama saya adalah {}".format(name_input) #versi python lebih lama
    }
    
    return jsonify(return_text) #supaya bisa return dalam bentuk JSON

if __name__ == "__main__":
    app.run(port=1234, debug=True) #debug => kode otomatis update ketika ada perubahan