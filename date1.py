from datetime import datetime
from datetime import timedelta
now = datetime.now()
d = datetime.today() - timedelta(5)
print(d)
print(d.strftime('%d/%m/%Y'))