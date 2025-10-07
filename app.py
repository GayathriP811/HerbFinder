# app.py
from flask import Flask, render_template, request
import os, random

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

herb_data = {
    "Tulsi": "Tulsi is known for its medicinal properties. It boosts immunity and relieves stress.",
    "Neem": "Neem leaves are antibacterial and antifungal.",
    "Aloe Vera": "Aloe Vera soothes the skin and aids digestion.",
    "Mint": "Mint adds freshness and helps digestion.",
    "Turmeric": "Turmeric is rich in curcumin with anti-inflammatory effects."
}

@app.route('/', methods=['GET','POST'])
def index():
    uploaded_image = None
    herb_name = None
    herb_description = None

    if request.method == 'POST':
        file = request.files.get('image')
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            uploaded_image = file.filename
            herb_name = random.choice(list(herb_data.keys()))
            herb_description = herb_data[herb_name]

    return render_template('index.html',
                           uploaded_image=uploaded_image,
                           herb_name=herb_name,
                           herb_description=herb_description)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
