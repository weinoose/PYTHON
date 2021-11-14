from datetime import datetime

now = datetime.now()
result = now
result = f"Yıl : {now.year}, Ay : {now.month}, Gün : {now.day}, Saat : {now.hour}, Saniye : {now.second}"
result = datetime.timestamp(now)

now1 = f"{now.day} {now.month} {now.year}"

def fark(d1, d2):
    d1 = datetime.strptime(d1, "%d %m %Y")
    d2 = datetime.strptime(d2, "%d %m %Y")
    return abs((d2-d1).days)

print(fark("17 06 2002", now1)/365)