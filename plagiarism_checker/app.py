import os
from flask import Flask, render_template, request, redirect, url_for
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Path to temporarily store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Vectorize text using TF-IDF
def vectorize(texts):
    return TfidfVectorizer().fit_transform(texts).toarray()

# Calculate cosine similarity
def similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])

# Route to handle file upload
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')  # Get all files from the form
        if files:
            filenames = []
            for file in files:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)  # Save the uploaded file
                filenames.append(filepath)

            # Read the files and check for plagiarism
            student_notes = [open(file, encoding='utf-8').read() for file in filenames]
            vectors = vectorize(student_notes)
            plagiarism_results = check_plagiarism(vectors, filenames)

            return render_template('results.html', plagiarism_results=plagiarism_results)

    return render_template('index.html')

# Check plagiarism between files
def check_plagiarism(vectors, filenames):
    plagiarism_results = set()
    for idx_a, vector_a in enumerate(vectors):
        for idx_b, vector_b in enumerate(vectors):
            if idx_a != idx_b:
                sim_score = similarity(vector_a, vector_b)[0][1]
                student_pair = sorted([filenames[idx_a], filenames[idx_b]])
                plagiarism_results.add((student_pair[0], student_pair[1], sim_score))
    
    return plagiarism_results

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
