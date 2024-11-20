# Document Ranking System

This project is a **Document Ranking System** built using **Flask**, designed to rank text documents based on user queries. The system utilizes two ranking algorithms: **Keyword Matching** and **Cosine Similarity**. Users can submit a query, and the system will return the most relevant documents from a collection of text files.

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Features](#features)
4. [System Architecture](#system-architecture)
5. [Algorithms Used](#algorithms-used)
    - [Keyword Matching](#keyword-matching)
    - [Cosine Similarity](#cosine-similarity)
6. [File Structure](#file-structure)
7. [Installation and Setup](#installation-and-setup)
8. [Usage](#usage)
9. [License](#license)
10. [Acknowledgements](#acknowledgements)

## Introduction

The **Document Ranking System** ranks a collection of text documents based on a user-provided query. The system supports two methods for ranking documents:
1. **Keyword Matching:** Ranks documents by counting how many keywords from the query appear in the document.
2. **Cosine Similarity:** Ranks documents based on the cosine of the angle between the query vector and the document vectors in a high-dimensional space.

This system is built as a web application using the **Flask** framework. It supports easy interaction with users, allowing them to submit queries and receive ranked results.

## Technologies Used

- **Python 3.x**
- **Flask** (for creating the web application)
- **Jinja2** (for HTML templating)
- **Matplotlib** (for visualizing data)
- **Natural Language Processing (NLP)** tools like `Counter` and `math` libraries for text processing and cosine similarity calculations.

## Features

- **Keyword-based Ranking:** Simple method of document ranking based on query keywords.
- **Cosine Similarity-based Ranking:** Advanced method of ranking using vector space models to calculate similarities.
- **Web Interface:** User-friendly Flask-based interface for interacting with the system.
- **File Uploads:** Ability to load text documents from the specified folder path for ranking.
- **Real-Time Ranking:** Instantaneous ranking of documents as per user input queries.

## System Architecture

The system consists of the following key components:
1. **Web Interface (Flask App):** The front-end interface where users submit queries and view results.
2. **Processing Modules:**
   - **Load Documents:** A module to load and read documents from the filesystem.
   - **Keyword Matching:** A module that compares query keywords with document words and ranks documents accordingly.
   - **Cosine Similarity:** A module that calculates cosine similarity between document vectors and the query vector.
3. **Document Repository:** A directory containing text files that are used as the documents for ranking.

### Data Flow:
- **User submits a query** through the web interface.
- The query is processed by the **Search Endpoint**, which determines whether the **Keyword Matching** or **Cosine Similarity** method will be used.
- The relevant documents are loaded from the **Document Repository**.
- Documents are ranked and the results are returned and displayed to the user.

## Algorithms Used

### Keyword Matching

The **Keyword Matching** algorithm works by checking how many words in the user's query appear in the document. The document with the highest number of matching words is ranked the highest.

- **Approach:**
  - Convert both the query and documents to lowercase.
  - Split both the query and documents into words.
  - Count how many words in the query appear in the document.
  - Rank documents based on the count of matched words.

### Cosine Similarity

**Cosine Similarity** is used to calculate the similarity between two vectors based on the angle between them. The formula is:

\[
\text{Cosine Similarity} = \frac{A \cdot B}{\|A\| \|B\|}
\]

Where:
- \(A\) is the vector representation of the query.
- \(B\) is the vector representation of the document.
- \(A \cdot B\) is the dot product of the vectors.
- \(\|A\|\) and \(\|B\|\) are the magnitudes (or lengths) of the vectors.

This algorithm helps in measuring the relevance of a document with respect to the user's query in a more nuanced way than keyword matching.

## File Structure

The project directory structure looks like this:

```
DocumentRankingSystem/
│
├── app.py                  # Main Flask application
├── static/                 # Static files (CSS, JS, etc.)
│   └── style.css           # CSS file for styling the web page
├── templates/              # HTML templates
│   └── index.html          # The main page template
├── documents/              # Directory containing the text documents
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

- **app.py:** Contains the Flask application logic and routing.
- **static/:** Stores static files like CSS and JavaScript.
- **templates/:** Stores HTML templates used to render web pages.
- **documents/:** Contains the text files (documents) that will be used for ranking.

## Installation and Setup

### Prerequisites:
Ensure that Python 3.x is installed on your system.

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/DocumentRankingSystem.git
cd DocumentRankingSystem
```

### Step 2: Install Dependencies
Create a virtual environment and install the required libraries:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```

### Step 3: Run the Flask Application
To start the web application, run:
```bash
python app.py
```
The application will run on `http://127.0.0.1:5000/` by default.

### Step 4: Access the Web Interface
Open your browser and navigate to `http://127.0.0.1:5000/`. You can now submit queries and see the ranked document results.

## Usage

1. **Submit a Query:** Enter your query in the search bar.
2. **Choose Search Type:** Select between **Keyword Matching** or **Cosine Similarity** for ranking.
3. **View Results:** The system will display the documents ranked by relevance according to the chosen search method.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Flask:** Lightweight web framework for building the application.
- **Python Libraries:** `collections` for counting word frequencies, `math` for performing vector operations.
