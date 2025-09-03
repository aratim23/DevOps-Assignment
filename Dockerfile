FROM python:3.11-slim

WORKDIR /app

COPY ACEest_Fitness.py ./
COPY test_workout_manager.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest"]
