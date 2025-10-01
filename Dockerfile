# Use Python image for nbconvert
FROM python:3.13-slim

# Copy requirements first
COPY requirements.txt requirements.txt

# Install Python deps, Nginx, and unrar-free
RUN apt-get update && \
    apt-get install -y nginx unrar-free && \
    rm -rf /var/lib/apt/lists/*

# Copy project notebooks and data.rar
COPY projects /projects
COPY data.rar data.rar

# Extract data.rar using unrar-free
RUN unrar-free x data.rar /

# Install Python dependencies (nbconvert, etc.)
RUN pip install -r requirements.txt

# Convert all notebooks to HTML
RUN jupyter nbconvert --to html /projects/*.ipynb

# Clean Nginx default files and copy converted HTMLs
RUN rm -rf /var/www/html/* && \
    cp /projects/*.html /var/www/html/

# Copy index page generator script
COPY generate_index.py /tmp/generate_index.py

# Generate index page
RUN python3 /tmp/generate_index.py

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
