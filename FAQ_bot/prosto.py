def Chapter8(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    main_text = 'Жатақханаға орналасуға рұқсат алғаннан кейін көре аласыз. Алдын ала тек осы фотоларды көре аласыз'

    # List of photo URLs and their respective captions
    photo_data = [
        {'url': 'https://sdu.edu.kz/wp-content/uploads/elementor/thumbs/Room2-opjtd6cu3vo6orvixzc5imeefs6rhyzumhi5twwssc.jpg', 'caption': 'Бөлмелер'},
        {'url': 'https://sdu.edu.kz/wp-content/uploads/elementor/thumbs/KITCHEN-oqrc5je25n43l8b72skgka3rahoux7a2ibs8f37f3w.png', 'caption': 'Ас үй'},
        {'url': 'https://sdu.edu.kz/wp-content/uploads/elementor/thumbs/canteen-oqqx2g71fnnzk16ec1gfxbs3byi7kv96iacqbog664.jpg', 'caption': 'Асхана'},
        {'url': 'https://sdu.edu.kz/wp-content/uploads/elementor/thumbs/Lounge-area-oqqx2i2ptbqk793o129p2bb0iq8y09gn6jnpa8ddto.jpg', 'caption': 'Демалыс аймағы'},
    ]

    # Send the main text
    bot.send_message(message.chat.id, main_text)

    # Send each photo of its caption
    bot.send_media_group(message.chat.id, [
        types.InputMediaPhoto(media=photo_data[0]['url'], caption=photo_data[0]['caption']),
        types.InputMediaPhoto(media=photo_data[1]['url'], caption=photo_data[1]['caption'])
    ])

    # Send the next two photos on a separate row
    bot.send_media_group(message.chat.id, [
        types.InputMediaPhoto(media=photo_data[2]['url'], caption=photo_data[2]['caption']),
        types.InputMediaPhoto(media=photo_data[3]['url'], caption=photo_data[3]['caption'])
    ])

    # bot.send_message(message.chat.id, 'Жатақханаға орналасуға рұқсат алғаннан кейін көре аласыз ', reply_markup=markup)
    markup.row(button1)



# 'https://sdu.edu.kz/wp-content/uploads/elementor/thumbs/Room2-opjtd6cu3vo6orvixzc5imeefs6rhyzumhi5twwssc.jpg',  # Replace with actual URL
#         'https://sdu.edu.kz/wp-content/uploads/elementor/thumbs/KITCHEN-oqrc5je25n43l8b72skgka3rahoux7a2ibs8f37f3w.png',  # Replace with actual URL
#         'https://sdu.edu.kz/wp-content/uploads/elementor/thumbs/canteen-oqqx2g71fnnzk16ec1gfxbs3byi7kv96iacqbog664.jpg',  # Replace with actual URL
#         'https://sdu.edu.kz/wp-content/uploads/elementor/thumbs/Lounge-area-oqqx2i2ptbqk793o129p2bb0iq8y09gn6jnpa8ddto.jpg',  # Replace with actual URL
