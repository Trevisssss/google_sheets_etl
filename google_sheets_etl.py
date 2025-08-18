import time
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas as pd
import dotenv

# Carrega as variáveis de ambiente do arquivo .env
dotenv.load_dotenv()

# Configurações
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

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
    print(f"DataFrame criado com {df.shape[0]} linhas e {df.shape[1]} colunas.")
# --- Resultados ---
print(f"Tempo de autenticação: {t1 - t0:.2f}s")
print(f"Tempo de leitura dos dados: {t2 - t1:.2f}s")
print(f"Tempo total: {t2 - t0:.2f}s")