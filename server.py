from flask import Flask, request, render_template
from processing import count_pixels

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("res.html", context=count_pixels(request.files.get('file'), request.form.get('hex_color')))
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")