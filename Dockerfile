# Usa un'immagine Python leggera
FROM python:3.12-alpine

# Imposta la directory di lavoro dentro il container
WORKDIR /app

# Copia il file requirements.txt nel container
COPY requirements.txt .

# Installa Flask dentro il container
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto dei file (app.py) nel container
COPY . .

# Espone la porta 5000 (Flask ascolta qui)
EXPOSE 5000

# Comando per avviare l'app Flask
CMD ["python", "app.py"]
