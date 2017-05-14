FROM python:3.6
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

EXPOSE 4000
CMD ["python", "src/__init__.py"]
