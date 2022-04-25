from datetime import datetime, timezone, timedelta

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today.strftime('%d-%m-%Y %H:%M'), tomorrow, sep='\n')
