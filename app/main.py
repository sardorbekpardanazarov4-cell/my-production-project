# 1-Bosqich: Build (Kutubxonalarni yig'ish)
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 2-Bosqich: Final (Faqat kerakli narsalar)
FROM python:3.11-slim
WORKDIR /app
# Builder bosqichidan olingan kutubxonalarni nusxalash
COPY --from=builder /root/.local /root/.local
COPY ./app ./app

# Path-ni to'g'irlash
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
