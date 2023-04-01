FROM python:3-slim
WORKDIR /usr/src/app
COPY COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./recommendation.py ./invokes.py ./
CMD [ "python", "./recommendation.py" ]