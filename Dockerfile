FROM python:3.11-slim  

WORKDIR /bot/
COPY requirements.txt /bot
RUN  pip install --upgrade pip \
    && pip install -r requirements.txt 

VOLUME /bot
# COPY . /bot  

# CMD ["python", "main.py"]
