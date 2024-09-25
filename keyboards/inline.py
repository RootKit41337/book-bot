from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

marrcup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Категория 1', callback_data=GoodsCallbackFactory(
                category_id=1,
                subcategory_id=0,
                item_id=0
        ).pack()
        )
        ]
    ]
)