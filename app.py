# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 01:35:40 2024

@author: hp
"""

from flask import Flask, render_template, request, jsonify
import os
from collections import Counter
import math

app = Flask(__name__)

# Step 1: Load documents
def load_documents(folder_path):
    documents = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                documents[filename] = file.read().lower()
    return documents

# Step 2: Keyword Matching Function
def keyword_matching(query, documents):
    query_keywords = query.lower().split()
    doc_ranking = {}

    for doc_name, content in documents.items():
        doc_words = content.split()
        matching_count = sum(1 for word in query_keywords if word in doc_words)
        doc_ranking[doc_name] = matching_count
    
    ranked_docs = sorted(doc_ranking.items(), key=lambda item: item[1], reverse=True)
    return ranked_docs

# Step 3: Term Frequency
def compute_tf(doc):
    words = doc.lower().split()
    # Count occurrences of each word
    word_counts = Counter(words)
    tf = {word: count for word, count in word_counts.items()}
    return tf


def dot_product(vec1, vec2):
    return sum(vec1.get(word, 0) * vec2.get(word, 0) for word in set(vec1.keys()) | set(vec2.keys()))

def magnitude(vec):
    return math.sqrt(sum(val ** 2 for val in vec.values()))

def cosine_similarity(doc_vector1, doc_vector2):
    return dot_product(doc_vector1, doc_vector2) / (magnitude(doc_vector1) * magnitude(doc_vector2))

def rank_by_cosine_similarity(query, documents):
    query_vector = compute_tf(query)
    rankings = {}
    
    for doc_name, content in documents.items():
        documents_vector = compute_tf(content)
        similarity = cosine_similarity(query_vector, documents_vector)
        rankings[doc_name] = similarity
    
    ranked_docs = sorted(rankings.items(), key=lambda item: item[1], reverse=True)
    return ranked_docs

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    search_type = request.form.get('search_type')
    
    docs = load_documents(r"D:\IR UET\Ranking Algo")

    if search_type == 'keyword':
        results = keyword_matching(query, docs)
        return jsonify(results)
    elif search_type == 'cosine':
        results = rank_by_cosine_similarity(query, docs)
        return jsonify(results)
    return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
