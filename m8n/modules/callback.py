from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from m8n.config import BOT_USERNAME
from m8n.config import START_PIC
from m8n.config import OWNER_ID
from m8n.config import ASSUSERNAME
from m8n.config import UPDATE
from m8n.config import SUPPORT
from m8n.config import OWNER_USERNAME
from m8n.config import BOT_NAME


@Client.on_callback_query(filters.regex("cbhome"))
async def cbhome(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" ‹ مـࢪحبـا بـك عـزيـزي فـي بـوت **{BOT_NAME}**

- اضـغط علـى زر ‹ الاوامـࢪ › لمـعࢪفـة الأوامـࢪ ›

 - اضغـط عـلى زر ‹ الاعـدادات › لمـعࢪفة الاعـدادات ›""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ الاعـدادات ›", callback_data="cbabout"),
                ],
                [

                    InlineKeyboardButton(
                        "‹ الاوامـࢪ ›", callback_data="cbevery")
                ],
                [
                    InlineKeyboardButton(
                        "‹ اضفـني الـى مجـموعـتك ›", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds_set(_, query: CallbackQuery):
        await query.answer("commands menu")
        await query.edit_message_text(
        f"""‹ مࢪحبـا بـك فـي قـسم الاوامـࢪ  › [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 

- يمكـنك معـࢪفـة الاوامـࢪ عـن طـࢪيق الازرار أدنـاه -""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("‹ اوامـࢪ المطـوريـن ›", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Everyone", callback_data="cbevery"),
                    InlineKeyboardButton("‹ اوامـࢪ المـشرفـين ›", callback_data="cbadmins"),
                ],[
                    InlineKeyboardButton("‹ رجـوع ›", callback_data="cbhome")
                ],
            ]
        ),
    ) 


# Commands for Everyone !!
@Client.on_callback_query(filters.regex("cbevery"))
async def all_set(_, query: CallbackQuery):
    await query.answer("Everyone menu")
    await query.edit_message_text(
    f""" ‹ مرحبا بك في قسم الاوامر ›

- شغل | بالـرد عـلى مـلف او اسـم اغـنية للتـشغـيل  .

- يوت | باسـم الاغنـية لتحـميـل اغنـية من اليـوتيـوب .

- رابط | لـحصـول علـى رابـط اغـنيـة من يوت .

- بنك | لفحـص بـنك البـوت والسـرعة المـمكـنه .

- جراف | لتـحويـل صـورة الى رابـط تلـيجـراف .

- مطور البوت | @{UPDATE}""",
        reply_markup=InlineKeyboardMarkup(
            [
              [
                    InlineKeyboardButton(
                        "‹ اوامـࢪ المـشرفين ›", callback_data="cbadmins"),
                    InlineKeyboardButton(
                        "‹ اوامـࢪ المطـورين ›", callback_data="cbsudo")
                ],
              [InlineKeyboardButton("‹ رجوع ›", callback_data="cbhome")]]
        ),
    )


# Commands for SudoUsers
@Client.on_callback_query(filters.regex("cbsudo"))
async def sudo_set(_, query: CallbackQuery):
    await query.answer("sudo menu")
    await query.edit_message_text(
    f""" ‹ مرحبا بك في قسم اوامر المطورين ›

- الاحصائيات | لرؤية احصائيات البوت اخر شهر .

- ريستارت | اعادة تشغيل البوت وتحسين السرعة .

- اذاعة | لعمل اذاعة في المجموعات بدون تثبيت .

- رسالة | لعمل اذاعة لكل المجموعات مع التثبيت .

- المغادرة | لمغادرة حساب المساعد من المجموعات .

- مطور البوت | @{UPDATE}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("‹ رجوع ›", callback_data="cbevery")
                ],
            ]
        ),
    )


# Commands for Group Admins
@Client.on_callback_query(filters.regex("cbadmins"))
async def admin_set(_, query: CallbackQuery):
    await query.answer("admins menu")
    await query.edit_message_text(
    f""" ‹ مرحبا بك في قسم اوامر المشرفين ›

- كافي | ايقاف تشغيل الاغنية في المجموعة .

- سكب | تخطي التالية الأغنية في المجموعة .

- مؤقتا | لإيقاف تشغيل الأغنية مؤقتا .

- استمر | استمرار التشغيل المتوقف مؤقتا .

- تنظيف | لتنظيف التشغيل وتحسين سرعة البوت .

- انضم | للانضمام حساب المساعد الى المجموعة .

- غادر | لمغادرة حساب المساعد المجموعة .

- مطور البوت | @{UPDATE}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("‹ رجوع ›", callback_data="cbevery")
                ],
            ]
        ),
    )


# Bot about & Information
@Client.on_callback_query(filters.regex("cbabout"))
async def about_set(_, query: CallbackQuery):
    await query.edit_message_text(
    f"""‹ مرحبا بك في قسم الاعدادات  › [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

- يمكنك الانضمام والتواصل مع المطورين عن طريق الازرار أدناه""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("‹ قناة الدعم ›", url=f"https://t.me/{SUPPORT}"),
                    InlineKeyboardButton("‹ قناة المطور ›", url=f"https://t.me/{UPDATE}")
                ],[
                    InlineKeyboardButton("‹ مطور البوت ›", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("‹ حساب المساعد ›", url=f"https://t.me/{ASSUSERNAME}")
                ],[
                    InlineKeyboardButton("‹ السورس ›", url="https://t.me/O_K_Q")
                ],[
                    InlineKeyboardButton("‹ رجوع ›", callback_data="cbhome")
                ],
            ]
        ),
    )


