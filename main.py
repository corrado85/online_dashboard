import time
from datetime import datetime
import pytz

# Imposta la timezone per Roma
timezone = pytz.timezone('Europe/Rome')

# Ottieni l'ora corrente nella timezone di Roma
rome_time = datetime.now(timezone)
current_time = rome_time.strftime("%H:%M:%S")

print(current_time)
