FROM python:3.10-slim
EXPOSE 8084
WORKDIR /app/
COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY .  .
ENTRYPOINT [ "executable" ]