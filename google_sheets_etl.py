import time
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas as pd

# Configurações
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS_FILE = 'testingonly-437312-5f259750c35b.json'  # Ex: 'python-sheets-api-123456.json'
SPREADSHEET_ID = '1dnqvufu_NzRGI1sajIfAa7TuZdigTS-ZHUJxLPPCuyU'  # Pegue da URL da planilha

# --- Tempo de autenticação ---
t0 = time.time()
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
t1 = time.time()

# --- Tempo de leitura dos dados ---
result = service.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID,
    range="car_prices!A:P"
).execute()
values = result.get("values", [])
t2 = time.time()

# Converter p/ DataFrame
# OBS: Nessa planilha há 16 colunas e 558838 Linhas.
if values:
    df = pd.DataFrame(values[1:], columns=values[0]) 

# --- Resultados ---
print(f"Tempo autenticação: {t1 - t0:.2f}s") # Meu sistema detectou 0.00s (praticamente instantâneo)
print(f"Tempo leitura dados: {t2 - t1:.2f}s") # Tempo leitura dados: 16.27s
print(f"Tempo total: {t2 - t0:.2f}s")# Tempo total: 16.28s