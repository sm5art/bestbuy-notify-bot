FROM python:slim
RUN mkdir /bbbot
WORKDIR /bbbot
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "bbbot.bot"]