poetry export --without-hashes > requirements.txt
docker build -t flask_template:v0.1 .
docker run -p 127.0.0.1:8000:8000 flask_template:v0.1 sh -c "export FLASK_APP=app.main:app && flask db init && flask db migrate && flask db upgrade"