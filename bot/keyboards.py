from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
web_app = WebAppInfo(url="https://elmurod31.github.io/Elmurod_evos_bot.github.oi/")
# Uzbek tili
evos_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kompaniya haqida"),
            KeyboardButton(text="Fililalar")
        ],
        [
            KeyboardButton(text="Bo'sh ish o'rinlari")
        ],
        [    KeyboardButton(text="Menu", web_app=web_app),
            KeyboardButton(text="Yangiliklar")
        ],
        [
            KeyboardButton(text="Kontaktlar/Manzil"),
            KeyboardButton(text="til"),
        ]
    ],resize_keyboard=True
)

evos_btn1 = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Filiallarni ko'rish")
    ],
    [
        KeyboardButton(text="Bosh ofis"),
        KeyboardButton(text="Toshkent shaxar")
    ],
    [
        KeyboardButton(text="Orqaga")
    ]
    ],resize_keyboard=True
)

evos_btn2 = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="English"),
        KeyboardButton(text="Uzbek")
    ],
    [
        KeyboardButton(text="orqaga"),
    ]
    ],resize_keyboard=True
)








# English language
evos_btnn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="About the Company"),
            KeyboardButton(text="Branches")
        ],
        [
            KeyboardButton(text="Vacancies")
        ],
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text="News")
        ],
        [
            KeyboardButton(text="Contacts/Address"),
            KeyboardButton(text="Language"),
        ]
    ],
    resize_keyboard=True
)

evos_btnn1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="View Branches")
        ],
        [
            KeyboardButton(text="Head Office"),
            KeyboardButton(text="Tashkent City")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)

evos_btnn2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="English"),
            KeyboardButton(text="Uzbek")
        ],
        [
            KeyboardButton(text="Back"),
        ]
    ],
    resize_keyboard=True
)