<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation - AI based Molecular Similarity App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        footer {
            margin-top: 50px;
            text-align: center;
            color: #777;
        }
        a {
            color: #4CAF50;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Documentation</h1>
        <p>The AI-Driven Molecular Similarity & Visualization Platform app utilizes the trained ChemBERTa model to calculate the similarity between different molecules based on their SMILES representations. This application leverages deep learning to generate embeddings and then calculates pairwise cosine similarity between these embeddings.</p>
        
        <h2>What the App Does</h2>
        <p>This app takes a CSV file containing molecule IDs and SMILES strings, computes ChemBERTa embeddings, and generates a similarity matrix based on cosine similarity between the molecules. The results are presented both as a downloadable CSV file and as a heatmap for easy visualization.</p>
        
        <h2>Impact and Use Cases</h2>
        <p>This tool is essential for chemoinformatics research and drug discovery, where understanding molecular similarity is crucial for tasks such as virtual screening, clustering of molecules, and finding potential lead compounds.</p>
        
        <h2>Features</h2>
        <ul>
            <li>Processes molecular data with ChemBERTa embeddings.</li>
            <li>Generates similarity matrices for up to a significant number of molecules (system dependent).</li>
            <li>Visualizes the results with heatmaps and downloadable CSV outputs.</li>
        </ul>

        <footer>
            <p>For support or further inquiries, contact: <a href="mailto:sharmar@aspire10x.com">sharmar@aspire10x.com</a> or <a href="mailto:support@aspire10x.com">support@aspire10x.com</a></p>
        </footer>
    </div>
</body>
</html>
