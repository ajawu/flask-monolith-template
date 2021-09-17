poetry export --without-hashes > requirements.txt
docker build -t flask_template:v0.1 .