from flask import Flask, render_template, request, redirect, url_for, jsonify
from translate import vi2en, en2vi
app = Flask(__name__)


@app.route("/")
def main():
    return redirect(url_for('en2vi'))


@app.route("/en2vi")
def en2vi():
    return render_template('en2vi.html')


@app.route("/vi2en")
def vi2en():
    return render_template('vi2en.html')


@app.route('/translate', methods=['POST'])
def translate_():
    pass
    # POST request
    if request.method == 'POST':
        respone = request.get_json()['data'][3:]
        input_sentence = respone
        flag = request.get_json()['data'][:3]
        if 'en' in flag:
            result = en2vi_model.tf_translate(input_sentence)
        else:
            result = vi2en_model.tf_translate(input_sentence)

        final_sentences = {"data": result}
        return jsonify(final_sentences)


@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting': 'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        vi = request.get_json()['greeting']  # parse as JSON
        en = vi2en(vi)
        return jsonify(en)
        return 'Sucesss', 200


if __name__ == '__main__':
    app.run()
