# Drone-Ci-Test-Sample
## Start server
docker build -t flask-sample:latest .
docker run -d -p 3000:3000 flask-sample:latest

## Test
python -m pytest
