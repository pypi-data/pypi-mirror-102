# NPDChecker

Инструмент для проверки статуса плательщика налога на профессиональный доход (НПД) по ИНН

---

### Синхронный режим:
```python
from npdchecker import NPDChecker

checker = NPDChecker()
inn = 144075719327

status = checker(inn) # проверка актуального статуса
status = checker(inn, "2020-07-25") # Проверка статуса на 25 июля 2020 года
```

---

### Асинхронный режим:
```python
from npdchecker import NPDChecker

checker = NPDChecker()
inn = 144075719327

async def check():
	async with checker:
		status = await checker.a(inn)
        status = await checker.a(inn, "2019-12-31")

checker.run(check())
```

---

### Ошибки

Все ошибки API идут классом `NPDError`. Класс имеет атрибуты `code` и `message`
согласно [Документации](https://npd.nalog.ru/html/sites/www.npd.nalog.ru/api_statusnpd_nalog_ru.pdf 'Ссылка на документацию').