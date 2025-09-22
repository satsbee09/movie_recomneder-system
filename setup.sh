#!/bin/bash

# Make sure pip is up to date
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# If you don't want a requirements.txt, you can list directly like:
# pip install streamlit scikit-learn pandas numpy requests

# (Optional) Set Streamlit config to avoid browser opening automatically
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
" > ~/.streamlit/config.toml
