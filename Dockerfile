FROM python:3.10

WORKDIR /app

# Copy dependencies first for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the files
COPY . .

# Create logs folder
RUN mkdir -p logs

# Run the app
CMD ["python", "app.py"]
