# Poloniex Info Bot 🤖

[🇬🇧 English](#english) | [🇷🇺 Русский](#русский)

---

## English

A private Telegram bot for real-time monitoring of Poloniex futures trading accounts with automated risk assessment and trade notifications.

### ✨ Features

**Real-Time Monitoring**
- Futures account balance tracking
- Open positions with entry prices and costs
- Active orders status
- Recent fills history

**Dynamic Risk Calculator**
Automatically calculates risk level (1–10) based on balance-to-position ratio:
- **Level 1–3:** Low risk (balance > 2x position)
- **Level 4–6:** Medium risk (balance 0.5–2x position)
- **Level 7–10:** High risk (balance < 0.5x position)

**Automated Notifications**
Sends instant alerts to a Telegram channel when:
- New position opened
- Position closed (with PnL)
- Position size modified

**Privacy Protection**
Bot access restricted to a single authorized Telegram username.

### 🛠 Technical Details

- **Language:** Python 3
- **Libraries:** pyTelegramBotAPI, requests, colorama
- **API:** Poloniex REST API
- **Update Frequency:** Every 15 seconds
- **Tracked Instrument:** BTCUSDTPERP (default)

### 📂 File Structure

```
Bots/Poloniex/InfoBot/
├── fINd_info_bot_polo.py   # Main bot script
├── fINd_poloRq.py          # Poloniex API request handlers
├── fINd_Text_polo.py       # Localized UI texts
├── fINd_conf_polo.env      # Configuration file
└── README.md               # This file
```

### 🚀 Installation

**Prerequisites**
- Python 3.8+
- pip package manager

**Install Dependencies**
```bash
pip install pyTelegramBotAPI requests colorama
```

**Create Poloniex API Credentials**
1. Log in to your Poloniex account
2. Go to the API Keys section
3. Create an API key with read permissions
4. Save the API Key, Secret Key, and Passphrase

**Create a Telegram Bot**
1. Open [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the instructions
3. Save the bot token

**Configure the Bot**

Edit `fINd_conf_polo.env`:
```ini
# Telegram Bot Settings
token=YOUR_TELEGRAM_BOT_TOKEN
userName=YOUR_TELEGRAM_USERNAME
chatId=YOUR_TELEGRAM_CHANNEL_ID  # Optional: for automated alerts

# Poloniex API Credentials
api_key=YOUR_POLONIEX_API_KEY
api_secret=YOUR_POLONIEX_SECRET_KEY
api_passphrase=YOUR_POLONIEX_PASSPHRASE

# Language Settings
language=en  # or 'ru' for Russian
```

### ▶️ Running

```bash
python fINd_info_bot_polo.py
```

Open Telegram, find your bot, and send `/start` to begin monitoring.

### 📡 Channel Notifications

To enable automated trade alerts:
1. Create a Telegram channel
2. Add your bot as an admin
3. Get the channel ID using [@getidsbot](https://t.me/getidsbot)
4. Add `chatId` to your `.env` file

### 🐛 Troubleshooting

**Bot doesn't respond**
- Verify the bot token is correct
- Check that the username matches `userName` in the config
- Ensure the bot is not blocked

**API errors**
- Verify Poloniex API credentials
- Check the API key has read permissions
- Ensure your IP is whitelisted (if enabled)

**Risk level stuck at "01"**
- Normal when no positions are open
- Risk recalculates only with open positions

### 📝 Notes

- Updates every 15 seconds to respect API rate limits
- All calculations are performed locally
- Runs indefinitely until manually stopped
- Default tracked instrument: BTCUSDTPERP
- Logs saved to `{date}_log_auto.log`

### 🔐 Security

- Never commit the `.env` file to version control
- Use IP whitelisting in Poloniex API settings
- Consider running on a dedicated server
- Regularly rotate API keys

### 📄 License

MIT License — free to use, modify, and distribute with attribution to the original source.

---

## Русский

Приватный Telegram-бот для мониторинга фьючерсных торговых счетов Poloniex в реальном времени с автоматической оценкой рисков и уведомлениями о сделках.

### ✨ Возможности

**Мониторинг в реальном времени**
- Отслеживание баланса фьючерсного счёта
- Открытые позиции с ценами входа и затратами
- Состояние активных ордеров
- История последних сделок

**Динамический расчёт рисков**
Автоматически вычисляет уровень риска (1–10) по соотношению баланса к объёму позиции:
- **Уровень 1–3:** низкий риск (баланс более чем в 2 раза превышает позицию)
- **Уровень 4–6:** средний риск (баланс составляет 0,5–2 размера позиции)
- **Уровень 7–10:** высокий риск (баланс менее половины размера позиции)

**Автоматические уведомления**
Мгновенно отправляет оповещения в Telegram-канал при:
- открытии новой позиции;
- закрытии позиции (с расчётом прибыли/убытка);
- изменении размера позиции.

**Защита приватности**
Доступ к боту ограничен одним авторизованным пользователем Telegram.

### 🛠 Технические подробности

- **Язык:** Python 3
- **Библиотеки:** pyTelegramBotAPI, requests, colorama
- **Интерфейс API:** Poloniex REST API
- **Частота обновления:** каждые 15 секунд
- **Отслеживаемый инструмент:** BTCUSDTPERP (по умолчанию)

### 📂 Структура файлов

```
Bots/Poloniex/InfoBot/
├── fINd_info_bot_polo.py   # Основной скрипт бота
├── fINd_poloRq.py          # Обработчики запросов к API Poloniex
├── fINd_Text_polo.py       # Тексты интерфейса с поддержкой нескольких языков
├── fINd_conf_polo.env      # Файл настроек
└── README.md               # Этот файл
```

### 🚀 Установка

**Необходимые условия**
- Python 3.8 или новее
- Менеджер пакетов pip

**Установка зависимостей**
```bash
pip install pyTelegramBotAPI requests colorama
```

**Создание ключей API для Poloniex**
1. Войдите в свой аккаунт Poloniex.
2. Перейдите в раздел «Ключи API».
3. Создайте ключ API с правами на чтение.
4. Сохраните ключ API, секретный ключ и парольную фразу.

**Создание Telegram-бота**
1. Откройте [@BotFather](https://t.me/BotFather).
2. Отправьте команду `/newbot` и следуйте инструкциям.
3. Сохраните токен бота.

**Настройка бота**

Отредактируйте файл `fINd_conf_polo.env`:
```ini
# Настройки Telegram-бота
token=ТОКЕН_ВАШЕГО_TELEGRAM_БОТА
userName=ВАШЕ_ИМЯ_ПОЛЬЗОВАТЕЛЯ_TELEGRAM
chatId=ИДЕНТИФИКАТОР_ВАШЕГО_КАНАЛА  # Необязательно: для автоматических оповещений

# Ключи API Poloniex
api_key=ВАШ_КЛЮЧ_API_POLONIEX
api_secret=ВАШ_СЕКРЕТНЫЙ_КЛЮЧ_POLONIEX
api_passphrase=ВАША_ПАРОЛЬНАЯ_ФРАЗА_POLONIEX

# Настройки языка
language=ru  # или 'en' для английского
```

### ▶️ Запуск

```bash
python fINd_info_bot_polo.py
```

Откройте Telegram, найдите своего бота и отправьте команду `/start`, чтобы начать мониторинг.

### 📡 Оповещения в канал

Чтобы включить автоматические оповещения о сделках:
1. Создайте Telegram-канал.
2. Добавьте своего бота в качестве администратора.
3. Узнайте идентификатор канала, например с помощью [@getidsbot](https://t.me/getidsbot).
4. Укажите параметр `chatId` в файле `.env`.

### 🐛 Решение проблем

**Бот не отвечает**
- Проверьте правильность токена бота.
- Убедитесь, что имя пользователя совпадает с `userName` в настройках.
- Убедитесь, что бот не заблокирован.

**Ошибки API**
- Проверьте правильность ключей API Poloniex.
- Убедитесь, что у ключа есть права на чтение.
- Убедитесь, что ваш IP-адрес добавлен в белый список (если это настроено).

**Уровень риска всегда показывает «01»**
- Это нормально, если открытых позиций нет.
- Риск пересчитывается только при наличии открытых позиций.

### 📝 Примечания

- Данные обновляются каждые 15 секунд, чтобы не превышать лимиты запросов к API.
- Все вычисления выполняются локально.
- Бот работает непрерывно до ручной остановки.
- Отслеживаемый инструмент по умолчанию: BTCUSDTPERP.
- Журналы сохраняются в файлы `{дата}_log_auto.log`.

### 🔐 Безопасность

- Никогда не добавляйте файл `.env` в систему контроля версий.
- Используйте белый список IP-адресов в настройках API Poloniex.
- При возможности запускайте бота на выделенном сервере.
- Регулярно меняйте ключи API.

### 📄 Лицензия

MIT License — свободное использование, изменение и распространение при условии указания источника.