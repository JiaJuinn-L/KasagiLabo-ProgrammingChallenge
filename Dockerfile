FROM python:3.9-slim

WORKDIR /app

COPY Challenge_B.py /app/Challenge_B.py
COPY test.txt /app/test.txt

CMD ["python", "Challenge_B.py"]