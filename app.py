from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import os
import torch
from transformers import RobertaTokenizer, RobertaModel

app = Flask(__name__)

# Load the pre-trained ChemBERTa model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")
model = RobertaModel.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")

# Function to calculate similarity
def calculate_similarity(smiles_list):
    embeddings = []
    for smiles in smiles_list:
        input_ids = torch.tensor(tokenizer.encode(smiles)).unsqueeze(0)
        with torch.no_grad():
            outputs = model(input_ids)[0]
        embeddings.append(outputs.mean(1).numpy())

    # Calculate similarity matrix
    sim_matrix = np.zeros((len(smiles_list), len(smiles_list)))
    for i in range(len(embeddings)):
        for j in range(len(embeddings)):
            sim_matrix[i, j] = np.dot(embeddings[i], embeddings[j].T) / (np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[j]))

    return np.round(sim_matrix, 2)  # Limit to two decimal places

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return redirect(url_for('index'))

    # Read the uploaded CSV
    df = pd.read_csv(file)
    smiles_list = df['SMILES'].tolist()
    ids_list = df['ID'].tolist()

    # Calculate the similarity matrix
    sim_matrix = calculate_similarity(smiles_list)

    # Create heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(sim_matrix, annot=True, fmt=".2f", cmap="coolwarm", xticklabels=ids_list, yticklabels=ids_list)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Save the matrix to CSV
    sim_df = pd.DataFrame(sim_matrix, index=ids_list, columns=ids_list)
    csv_file = 'similarity_matrix.csv'
    sim_df.to_csv(csv_file)

    return render_template('result.html', matrix=sim_df.to_html(classes="table table-striped"), 
                           heatmap=url_for('heatmap'), csv_file=csv_file)

# New route for documentation
@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/heatmap')
def heatmap():
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/download/<csv_file>')
def download_csv(csv_file):
    return send_file(csv_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
