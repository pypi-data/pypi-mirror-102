# koronavirus
Koronavirüs (Covid-19) verilerine erişmenizi sağlayan bir Python modülü.
Verilerin kaynağı: [NovelCOVID API](https://disease.sh/)

## Örnek Kullanım
```python
# modülü içeri aktar
from koronavirus import *

# Türkiye'nin koronavirüs verilerini al
veriler =  korona("Turkey") # veya korona()
print(veriler)

# async hâli
veriler = await async_korona("Turkey") # veya async_korona()
print(veriler)
```
