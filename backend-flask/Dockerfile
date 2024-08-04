FROM python:3.12.4-windowsservercore-1809

WORKDIR C:\\backend-flask

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=4567", "--debug"]