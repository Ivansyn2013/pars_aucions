FROM python:3.10-buster
WORKDIR /app
COPY req.txt requirements.txt
RUN pip install -r requirements.txt
COPY wsgi.py wsgi.py
COPY app.py app.py
COPY commands ./commands
COPY config ./config
COPY Deploy ./Deploy
COPY logic ./logic
COPY logs ./logs
COPY models ./models
COPY static ./static
COPY templates ./templates
COPY views ./views
EXPOSE 5001
CMD ["python", "wsgi.py"]