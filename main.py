# Solo i tickers che ho in portafoglio

prtf = ['1MC', '500', 'ANX', 'AAPL', 'CHIP', 'CFR', 'META', 'MSFT', 'MWRD', 'NVDA', 'STLA', 'TRMD']

symbol_list = prtf

all_tickers_filtered = prtf

all_tickers = prtf













# 6500 ticker ci mette un paio di minuti
def fetch_fundamental_data(symbol):
    try:
        stock = yf.Ticker(symbol).info
        return stock
    except Exception as e:
        print(f"Ignorato errore per il simbolo {symbol}: {e}")
        return None

# Specify the maximum number of threads (adjust according to your needs)
max_threads = 10

# Utilizza tqdm per aggiungere una progress bar al ciclo
with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
    # Use executor.map to parallelize the fetching of data
    fundamental_data = list(tqdm(executor.map(fetch_fundamental_data, all_tickers), total=len(all_tickers), desc="Fetching data"))

# Remove None values (symbols that had errors)
fundamental_data = [data for data in fundamental_data if data is not None]

# Visualizza il DataFrame finale
df_fundamental = pd.DataFrame(fundamental_data)








# Definisci la funzione che esegue la moltiplicazione
def multiply_columns(df):
    df['dividendYield'] *= 1
    df['ebitdaMargins'] *= 1
    df['returnOnEquity'] *= 1
    df['priceToHighRatio'] = df['currentPrice'] / df['fiftyTwoWeekHigh'] * 100
    return df.drop(columns=['currentPrice', 'fiftyTwoWeekHigh'])  #non mi interessa portarmi dietro df['currentPrice'] / df['fiftyTwoWeekHigh']


# Filtra e seleziona il DataFrame, applica la funzione e ordina
df_filtered = (
    df_fundamental[
        #(df_fundamental['industry'] == 'Oil & Gas Midstream') &
    (df_fundamental['marketCap'] > 2000000000)]
    [['shortName', 'marketCap', 'industry','dividendYield', 'ebitdaMargins', 'recommendationKey','totalCashPerShare',
      'returnOnEquity', 'currentPrice', 'fiftyTwoWeekHigh'
      #'priceToHighRatio'
      ]]
    .pipe(multiply_columns)
    .sort_values(by='dividendYield', ascending=False)
)

#df_filtered = df_fundamental[(df_fundamental['industry'] == 'Oil & Gas Midstream') & (df_fundamental['marketCap'] > 2000000000)][['shortName', 'marketCap','52WeekChange','dividendYield','ebitdaMargins','recommendationKey']].assign(dividendYield=lambda x: x[['dividendYield','ebitdaMargins']] * 100).sort_values(by='dividendYield', ascending=False)
df_filtered

