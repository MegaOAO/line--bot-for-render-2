from linebot.v3.messaging import (
    StickerMessage,
    ImageMessage,
    TextMessage,
    LocationMessage,
    TemplateMessage,
    CarouselTemplate,
    CarouselColumn,
    QuickReply,
    QuickReplyItem,
    MessageAction,
    URIAction,
)

# 官方文件
# https://github.com/line/line-bot-sdk-python

# 常見問答表
faq = {
    '貼圖': StickerMessage(
        package_id='1',
        sticker_id='1'
    ),
    '門市照片': ImageMessage(
        original_content_url="https://fastly.picsum.photos/id/395/900/400.jpg?hmac=3y0-Ce1YyrujBAT9q2_GVXqC3CIgTSxPOKoLHlmspr0",
        preview_image_url="https://fastly.picsum.photos/id/395/900/400.jpg?hmac=3y0-Ce1YyrujBAT9q2_GVXqC3CIgTSxPOKoLHlmspr0"
    ),
    '交通': TextMessage(text='請問您想使用何種方式前往？',
                          quick_reply=QuickReply(items=[
                              QuickReplyItem(action=MessageAction(
                                  label="搭乘捷運", text="捷運")
                              ),
                              QuickReplyItem(action=MessageAction(
                                  label="搭乘公車", text="公車")
                              )
                          ])
                          ),
    '捷運': TextMessage(
        text="搭乘捷運至木柵線科技大樓站步行5分鐘即可抵達。"
    ),
    '公車': TextMessage(
        text="搭乘公車至科技大樓站步行5分鐘即可抵達。"
    ),
    '營業地址': LocationMessage(
        title='my location',
        address='Tokyo',
        latitude=35.65910807942215,
        longitude=139.70372892916203
    ),
    '查詢匯率': TemplateMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # 匯率選單一圖片網址
                    thumbnail_image_url="https://fastly.picsum.photos/id/352/900/400.jpg?hmac=WTGHcbEoO0_hYEWOE7qNwdFmPC-D7czQpegOKNqpZ0M",
                    title='匯率選單一',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢美金',
                            text='美金'
                        ),
                        MessageAction(
                            label='查詢港幣',
                            text='港幣'
                        ),
                        MessageAction(
                            label='查詢英鎊',
                            text='英鎊'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單二圖片網址
                    thumbnail_image_url="https://fastly.picsum.photos/id/364/900/400.jpg?hmac=70RqcdkXgO-mMYyuGgaFXlB0twshHiFdvzgGhAOZggw",
                    title='匯率選單二',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢澳幣',
                            text='澳幣'
                        ),
                        MessageAction(
                            label='查詢加拿大幣',
                            text='加拿大幣'
                        ),
                        MessageAction(
                            label='查詢新加坡幣',
                            text='新加坡幣'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單三圖片網址
                    thumbnail_image_url="https://fastly.picsum.photos/id/355/900/400.jpg?hmac=G2DG7Nfhf-KOUh0nSEYX7fO7TeC0zN7pkCRkb2Nj0M4",
                    title='匯率選單三',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢瑞士法郎',
                            text='瑞士法郎'
                        ),
                        MessageAction(
                            label='查詢日圓',
                            text='日圓'
                        ),
                        MessageAction(
                            label='查詢瑞典幣',
                            text='瑞典幣'
                        )
                    ]
                )
            ]
        )
    ),
    '抽運勢籤':TextMessage(
        text = "請在心裡想好要詢問的問題後，點選開始抽籤~",
    quick_reply=QuickReply(items=[
                              QuickReplyItem(action=MessageAction(
                                  label="開始抽籤", text="抽籤")
                              ),
                              QuickReplyItem(action=MessageAction(
                                  label="再想一下", text="取消")
                              )
                          ])
    ),
    '取消':TextMessage(text = "好的，有需要時再呼叫小秘書哦~"),
    '功能介紹': TextMessage(
        text="歡迎使用小秘書，目前的功能有查詢今日的星座運勢，以及抽運勢籤唷~其他功能正在開發中"
    ),
    '查詢今日運勢': TemplateMessage(
        altText ='Carousel template',
        template = CarouselTemplate(
            columns = [
                CarouselColumn(
                    thumbnail_image_url = "https://i.pinimg.com/564x/33/f6/5c/33f65c7d1d0fecf6e392890c398fc462.jpg",
                    title='土象星座選單',
                    text = '點選下方星座查詢今日運勢',
                    actions = [
                        MessageAction(
                            label = '魔羯座 Capricorn',
                            text = 'capricorn'
                        ),
                        MessageAction(
                            label = '金牛座 Taurus',
                            text = 'taurus'
                        ),
                        MessageAction(
                            label = '處女座 Virgo',
                            text = 'virgo'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://i.pinimg.com/564x/8b/b7/3c/8bb73c84eb9a4ff89fc969b2b5b148db.jpg",
                    title='風象星座選單',
                    text = '點選下方星座查詢今日運勢',
                    actions = [
                        MessageAction(
                            label = '雙子座 Gemini',
                            text = 'gemini'
                        ),
                        MessageAction(
                            label = '天秤座 Libra',
                            text = 'libra'
                        ),
                        MessageAction(
                            label = '水瓶座 Aquarius',
                            text = 'aquarius'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://i.pinimg.com/564x/a5/92/07/a59207db0b8593184bb4835f9204acf1.jpg",
                    title='火象星座選單',
                    text = '點選下方星座查詢今日運勢',
                    actions = [
                        MessageAction(
                            label = '牡羊座 Aries',
                            text = 'aries'
                        ),
                        MessageAction(
                            label = '獅子座 Leo',
                            text = 'leo'
                        ),
                        MessageAction(
                            label = '射手座 Sagittarius',
                            text = 'sagittarius'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://i.pinimg.com/564x/a5/79/9c/a5799c52d9554bff98e105c4bc8f37d4.jpg",
                    title='水象星座選單',
                    text = '點選下方星座查詢今日運勢',
                    actions = [
                        MessageAction(
                            label = '天蠍座 Scorpio',
                            text = 'scorpio'
                        ),
                        MessageAction(
                            label = '巨蟹座 Cancer',
                            text = 'cancer'
                        ),
                        MessageAction(
                            label = '雙魚座 Pisces',
                            text = 'pisces'
                        )
                    ]
                ),
            ]
        )
    ),
    

}

# 主選單
# Carousel Template
# https://developers.line.biz/en/docs/messaging-api/message-types/#carousel-template
menu = TemplateMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                # 卡片二圖片網址
                thumbnail_image_url="https://i.pinimg.com/564x/5f/b5/0c/5fb50c50dc926c91b07a537ff7e32bf6.jpg",
                title='主選單',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='功能介紹',
                        text='功能介紹'
                    ),
                    MessageAction(
                        label='查詢今日運勢',
                        text='查詢今日運勢'
                    ),
                    MessageAction(
                        label='抽運勢籤',
                        text='抽運勢籤'
                    )
                ]
            ),
        ]
    )
)

horoscope = {"aries", "taurus", "gemini", "cancer", "leo",
             "virgo", "libra", "scorpio","sagittarius", "capricorn",
             "aquarius", "pisces"}