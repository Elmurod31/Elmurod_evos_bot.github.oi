





import os
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from databese import database as db
from keyboards import evos_btn, evos_btn1, evos_btn2, evos_btnn, evos_btnn1, evos_btnn2

handlers_router = Router()

# O'zbek tili
@handlers_router.message(CommandStart())
async def command_start_handler(message: Message):
    user = db.get_user(message.from_user.id)
    if not user:
        db.insert_user(first_name=message.from_user.first_name,
                            last_name=message.from_user.last_name,
                            telegram_id=message.from_user.id)
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, reply_markup=evos_btn)

@handlers_router.message(F.text == "Kompaniya haqida")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption="Kompaniyamizning birinchi filiali 2006 yilda ochilgan bo’lib, shu kungacha muvaffaqiyatli faoliyat yuritib kelmoqdaligini bilarmidingiz?\n 15 yil davomida kompaniya avtobus bekatidagi kichik ovqatlanish joyidan zamonaviy, kengaytirilgan tarmoqqa aylandi, u bugungi kunda O‘zbekiston bo‘ylab 65 dan ortiq restoranlarni, o‘zining eng tezkor yetkazib berish xizmatini, zamonaviy IT-infratuzilmasini va 2000 dan ortiq xodimlarni o‘z ichiga oladi.")

@handlers_router.message(F.text == "Fililalar")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption="EVOS – O‘zbekistondagi eng yirik tez ovqatlanish restoranlar tarmog‘ining brendi. Kompaniyaning tarixi 2006 yilga borib taqaladi.\n Bugungi kunda butun respublika bo'ylab 70 ta filial o'z eshiklarini ochdi va yaqin kelajakda nafaqat O'zbekistonda, balki uning chegaralaridan tashqarida ham sezilarli kengayish davom etmoqda. Rivojlanish jarayoni doimiy ravishda jadal rivojlanmoqda - buning uchun brendning egasi eng yaxshi QSR mutaxassislarini, shu jumladan xorijiy mutaxassislarni faol ravishda jalb qiladi.", reply_markup=evos_btn1)

@handlers_router.message(F.text == "Menu")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img.png")
    img = FSInputFile(img_path)

    await message.answer_photo(photo=img, caption="Evos saytiga o'tish uchun")

    # HTML formatda link qilish
    caption_text = "<b>Evos ijtimoiy tarmoqlari</b>\n"
    caption_text += '<a href="https://www.instagram.com/evosuzbekistan/">Instagram</a>|'
    caption_text += '<a href="https://t.me/Elmurod_Evos_Bot">Telegram</a>|'
    caption_text += '<a href="https://www.facebook.com/evosuzbekistan">Facebook</a>'

    await message.answer(
        text=caption_text,
        parse_mode="HTML"  # HTML formatni yoqamiz
    )

@handlers_router.message(F.text == "Yangiliklar")
async def command_end_handler(message: Message):
    await message.answer(text="Kompaniya yangiliklari:\n"
                              "Aksiya\n"
                              "Yangi filialar\n"
                              "Yangi to'rta shirinliklar")

@handlers_router.message(F.text == "Kontaktlar/Manzil")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption="Manzil: Furqat Ko'chasi 175, kirish 1, 2-qavat\n"
                                                  "Mo'ljal: MAKRO THE TOWER\n"
                                                  "Kontakt: +998712031212")

    latitude = 41.304632373960224
    longitude = 69.24596245776962
    await message.answer_location(latitude, longitude)

@handlers_router.message(F.text == "Orqaga")
async def command_end_handler(message: Message):
    await message.answer(text="Orqaga qytingiz", reply_markup=evos_btn)


@handlers_router.message(F.text == "til")
async def command_end_handler(message: Message):
    await message.answer(text="Tillar", reply_markup=evos_btn2)

@handlers_router.message(F.text == "Uzbek")
async def command_end_handler(message: Message):
    await message.answer(text="siz o'zbek qilini tanladingiz", reply_markup=evos_btn2)


@handlers_router.message(F.text == "orqaga")
async def command_end_handler(message: Message):
    await message.answer(text="Orqaga qytingiz", reply_markup=evos_btn)


@handlers_router.message(F.text == "Bo'sh ish o'rinlari")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_3.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption="EVOS ® tez xizmat ko‘rsatish restoranlari tarmog‘i bir joyda turmaydi, balki siz bilan va siz uchun doimo o‘sib boradi va rivojlanadi! Biz geografiyamizni kengaytiryapmiz va deyarli har oyda yangi filiallarni ochyapmiz.\nEndi bizning tarmog‘imizda O‘zbekiston bo‘ylab 50 dan ortiq filial mavjud. Shuning uchun, biz doimo jamoamizning bir qismi bo‘lishni xohlaydigan va EVOS ® da o‘z faoliyatini boshlashga tayyor bo‘lgan dinamik va faol odamlarni qidiramiz.")


@handlers_router.message(F.text == "Filiallarni ko'rish")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_4.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img,)

@handlers_router.message(F.text == "Bosh ofis")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_5.png")
    img = FSInputFile(img_path)

    await message.answer_photo(photo=img, caption="EVOS — O‘zbekistonda mashhur fast-food tarmog‘i bo‘lib, 2007-yilda tashkil etilgan. Kompaniya 15 yillik tajribaga ega bo‘lib, mamlakat bo‘ylab 62 ta filialga ega . EVOS o‘zining tezkor va sifatli xizmatlari bilan mijozlar orasida keng tarqalgan.​")

    latitude = 41.31144724359285
    longitude = 69.24363513827315

    await message.answer_location(latitude, longitude)

@handlers_router.message(F.text == "Toshkent shaxar")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_6.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption="Toshkent shahrida EVOS kompaniyasining ko‘plab filiallari mavjud bo‘lib, ular shaharning deyarli barcha tumanlarida joylashgan.\n Mirzo-Ulug'bek tumanida Muxammad Yusuf ko‘chasi 1A va Temur Malik ko‘chasi 3A manzillarida, Chilonzor tumanida Chilonzor-8 mavzesi Qatortol ko‘chasi 21A, Katta Ka'ni ko‘chasi Chilonzor-D20 mavzesi va Furqat ko‘chasi 174 manzillarida EVOS filiallari faoliyat ko‘rsatmoqda. Uchtepa tumanida esa Chilonzor-12 mavzesi, Lutfiy ko‘chasi 41A da EVOS mavjud.")










# English Language
@handlers_router.message(CommandStart())
async def command_start_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, reply_markup=evos_btnn)

@handlers_router.message(F.text == "About the Company")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    img = FSInputFile(img_path)
    await message.answer_photo(
        photo=img,
        caption="Did you know that our company's first branch was opened in 2006 and has been operating successfully ever since?\n"
                "Over 15 years, the company has grown from a small snack stop at a bus station into a modern and expansive network "
                "that now includes over 65 restaurants across Uzbekistan, the fastest delivery service, a modern IT infrastructure, "
                "and more than 2000 employees."
    )

@handlers_router.message(F.text == "Branches")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    img = FSInputFile(img_path)
    await message.answer_photo(
        photo=img,
        caption="EVOS is the brand of the largest fast-food restaurant chain in Uzbekistan. The company’s history dates back to 2006.\n"
                "Today, 70 branches have opened across the country, and the company is rapidly expanding not only in Uzbekistan but also beyond its borders. "
                "The development process is progressing rapidly – the brand owner is actively engaging the best QSR experts, including foreign specialists.",
        reply_markup=evos_btnn1
    )

@handlers_router.message(F.text == "Menu")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img.png")
    img = FSInputFile(img_path)

    await message.answer_photo(photo=img, caption="Click the links below to visit our social platforms:")

    caption_text = "<b>EVOS Social Media</b>\n"
    caption_text += '<a href="https://www.instagram.com/evosuzbekistan/">Instagram</a> | '
    caption_text += '<a href="https://t.me/Elmurod_Evos_Bot">Telegram</a> | '
    caption_text += '<a href="https://www.facebook.com/evosuzbekistan">Facebook</a>'

    await message.answer(
        text=caption_text,
        parse_mode="HTML"
    )

@handlers_router.message(F.text == "News")
async def command_end_handler(message: Message):
    await message.answer(text="Company News:\n"
                              "- Promotions\n"
                              "- New Branches\n"
                              "- Four New Desserts")

@handlers_router.message(F.text == "Contacts/Address")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    img = FSInputFile(img_path)
    await message.answer_photo(
        photo=img,
        caption="Address: 175 Furqat Street, Entrance 1, 2nd Floor\n"
                "Landmark: MAKRO THE TOWER\n"
                "Contact: +998712031212"
    )

    latitude = 41.304632373960224
    longitude = 69.24596245776962
    await message.answer_location(latitude, longitude)

@handlers_router.message(F.text == "Back")
async def command_end_handler(message: Message):
    await message.answer(text="You went back.", reply_markup=evos_btnn)

@handlers_router.message(F.text == "Language")
async def command_end_handler(message: Message):
    await message.answer(text="Lenguages", reply_markup=evos_btnn2)

@handlers_router.message(F.text == "English")
async def command_end_handler(message: Message):
    await message.answer(text="You have selected English.", reply_markup=evos_btnn2)

@handlers_router.message(F.text == "Vacancies")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_3.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption="EVOS ® fast service restaurant chain never stands still but constantly grows and develops with you and for you! We are expanding our geography and opening new branches almost every month.\nCurrently, we have more than 50 branches across Uzbekistan. Therefore, we are constantly looking for dynamic and active individuals who are willing to become part of our team and start their career at EVOS ®.")

@handlers_router.message(F.text == "View Branches")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_4.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img)

@handlers_router.message(F.text == "Head Office")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_5.png")
    img = FSInputFile(img_path)

    await message.answer_photo(photo=img, caption="EVOS is a popular fast-food chain in Uzbekistan, established in 2007. With 15 years of experience, the company has 62 branches across the country. EVOS has become widely known among customers for its fast and high-quality services.")

    latitude = 41.31144724359285
    longitude = 69.24363513827315

    await message.answer_location(latitude, longitude)

@handlers_router.message(F.text == "Tashkent City")
async def command_end_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_6.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption="In Tashkent City, EVOS has many branches located in almost all districts of the city.")
