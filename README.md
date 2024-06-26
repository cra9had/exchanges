# Бот для обмена валюты

## Тех задание

**Цель проекта:** Создать Telegram-бота для криптообменника с возможностью дальнейшего масштабирования.

**Функциональные требования:**

1. **Кабинет пользователя:**
    - Доступен для выполнения операций по обмену криптовалюты и фиатных денег.
    - Имеет две кнопки: "Купить" и "Поддержка".
2. **Операция "Купить":**
    - По нажатию кнопки "Купить" открывается меню выбора валюты для оплаты (в текущей версии - рубль).
    - После выбора валюты пользователем, отображается меню с валютами для обмена (криптовалюты, евро, доллар).
    - Пользователь вводит сумму для обмена в рублях.
    - Бот использует интеграцию с сервисами для получения актуального курса и расчета комиссии, формируя сумму для обмена.
    - После нажатия кнопки "Продолжить", пользователь должен ввести реквизиты для получения валюты (адрес кошелька или номер иностранной карты).
    - Пользователю предлагается выбрать способ доставки (быстрая или стандартная).
3. **Подтверждение операции:**
    - После выбора способа доставки, бот предоставляет реквизиты для оплаты и кнопку "Я оплатил".
    - После нажатия кнопки "Я оплатил", пользователю предлагается загрузить скриншот оплаты или чек.
4. **Кабинет оператора:**
    - Доступен для верификации информации и совершения обмена.
    - Оператор будет оповещаться о новых заявках на обмен
    - Оператор сможет отменять/совершать сделку
    - Оператор может

**Технические требования:**

- Бот должен быть реализован на платформе Telegram, используя Telegram Bot API.
- Для интеграции с сервисами для получения актуального курса необходимо найти сервис, с наиболее выгодными условиями

**Дополнительные требования:**

- Реализация защиты данных пользователей и безопасности операций обмена.
- Логирование всех операций

Ориентир: https://t.me/BULBA_BTC_BOT
