from datetime import datetime, timedelta
yesterday = datetime.today() - timedelta(days=1)
today = datetime.now()
tomorrow = datetime.today() + timedelta(days=1)
print( yesterday.strftime('%d/%m/%Y'), today.strftime('%d/%m/%Y'), tomorrow.strftime('%d/%m/%Y'))