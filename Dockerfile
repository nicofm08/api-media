FROM python:3.9-alpine
# Instala dependencias necesarias para compilar
RUN apk add --no-cache gcc musl-dev linux-headers

COPY ./ /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
