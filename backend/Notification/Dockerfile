FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY ./notification.py ./invokes.py ./
RUN python -m pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./notification.py"]