# Plagiarism Checker Tool

This is a plagiarism checker tool that detects similarities between text documents. It uses the **TF-IDF** (Term Frequency-Inverse Document Frequency) vectorization technique and **Cosine Similarity** to measure the similarity between different student notes stored in text files. The tool is built using Python and can be used to scan a collection of `.txt` files and identify potential instances of plagiarism.

## Features

- **TF-IDF Vectorization**: Transforms text into numerical data that represents the frequency of words across documents.
- **Cosine Similarity**: Compares the vectorized representation of documents to calculate how similar two documents are.
- **File Processing**: Automatically processes all `.txt` files in a directory and compares them.
- **Results**: Outputs pairs of documents with their similarity scores, indicating possible plagiarized content.

## Requirements

- Python 3.x
- `scikit-learn` library (for TF-IDF and Cosine Similarity)
- Basic Python libraries (`os`, `math`, etc.)

You can install the required Python packages using `pip`:

```bash
pip install scikit-learn
