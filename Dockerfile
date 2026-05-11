# 1-Bosqich: Build
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 2-Bosqich: Final (Yengil va xavfsiz)
FROM python:3.11-slim
WORKDIR /app

# Builder-dan faqat kutubxonalarni olamiz
COPY --from=builder /root/.local /root/.local
COPY ./app ./app

# Python kutubxonalari yo'lini ko'rsatamiz
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]	
