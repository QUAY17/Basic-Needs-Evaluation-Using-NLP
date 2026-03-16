# Basic Needs Survey Analysis

NLP analysis platform for a statewide Basic Needs Survey, examining  food and housing insecurity impacts on faculty, staff, and students.

## Overview

This project processes open-ended survey responses using transformer-based NLP models and presents findings through interactive Dash dashboards.

**Analysis capabilities:**
- **Sentiment Analysis** — DistilBERT with custom rule-based classification
- **Topic Modeling** — BERTopic with SentenceTransformer embeddings
- **Keyword Extraction** — KeyBERT with thematic keyword boosting
- **Word Clouds** — Visual keyword frequency representations
- **Institution-Level Analysis** — Response counting and listing by institution

## Project Structure

```
BasicNeeds/
├── data/                          # Survey data (gitignored)
├── scripts/
│   ├── data_processing.py         # Core NLP pipeline
│   ├── split_staff_faculty.py     # Faculty/staff data segmentation
│   ├── all_responses/             # Aggregated analysis + Dash app
│   ├── by_institution/            # Institution-level analysis
│   ├── faculty/                   # Faculty-specific outputs
│   └── staff/                     # Staff-specific outputs
├── student/
│   ├── data_processing.py         # Student NLP pipeline
│   └── split_undergrad_grad.py    # Undergrad/grad segmentation
├── dash_script/                   # Dashboard app (gitignored)
└── requirements.txt
```

## Setup

Key dependencies: `bertopic`, `sentence-transformers`, `keybert`, `transformers`, `spacy`, `dash`, `pandas`, `wordcloud`

## Data Pipeline

1. **Preprocessing** — Lowercase, expand contractions, remove punctuation, filter non-informative responses
2. **Sentiment Analysis** — Classify responses as POSITIVE/NEGATIVE using DistilBERT + context-aware rules
3. **Topic Modeling** — Discover themes via BERTopic with custom stopwords and topic merging
4. **Keyword Extraction** — Extract and rank keywords with domain-specific boosting
5. **Word Cloud Generation** — Visualize keyword frequencies per survey question
6. **Dashboard** — Present results in an authenticated Dash web app

## Survey Questions Analyzed

- How is food or housing insecurity affecting your work?
- What could your college or university do to address food and housing insecurity?
- What are your thoughts about food availability on your campus?
- Please share why you feel unsafe?
- Is there anything else you would like to share?

## Deployment

The Dash dashboard is containerized with Docker and deployed to Kubernetes via Helm charts.

