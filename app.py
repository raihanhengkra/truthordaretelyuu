import random
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, FlexSendMessage, 
    TemplateSendMessage, ConfirmTemplate, PostbackTemplateAction, MessageTemplateAction,
    ButtonsTemplate, URITemplateAction, TextSendMessage, CarouselTemplate, CarouselColumn, ImageSendMessage, StickerSendMessage,
    ImageCarouselTemplate, ImageCarouselColumn
)

app = Flask(__name__)

ACCESS_TOKEN = 'OQRq5Ec52wUzfWjBTUYoE7knj86fHUs2Abn9tazxpM36GCtfeNiOMF360bkCEhDKt7Jd1XmgKVsFb1ejMoc3nzZwFv2JYLDEW55WjahHmHMu5sbGaZbds3p1nx/HDEcfSqaRAHkTJzT7/K/KYb2QVgdB04t89/1O/w1cDnyilFU='
SECRET = '2257f71766f9bde0b2e569ea9e699e28'

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    t = {'Kalau kamu bisa jadi tidak terlihat, apa hal pertama yang akan kamu lakukan?':1, 
        'Apa rahasia yang kamu sembunyikan dari orangtuamu?':2,
        'Siapa orang yang diam-diam kamu sukai?' :3,
        'Siapa orang terakhir yang kamu kepoin di media sosial?':4,
        'Kalau ada jin yang memberikanmu tiga permohonan, apa yang kamu inginkan?':5,
        'Jika kamu kembali ke masa lalu, apa yang akan kamu lakukan?':6,
        'Apa tontonan favoritmu saat masih kecil?': 7,
        'Siapa orang yang paling sering kamu chat?':8,
        'Apa kebohongan terbesar yang pernah kamu katakan kepada orangtuamu?':9,
        'Apa mimpi paling aneh yang pernah kamu alami?':10,
        'Ceritakan detail ciuman pertamamu…':11,
        'Kapan terakhir kali kamu ngompol atau eek di celana?':12,
        'Menurutmu, hewan apa yang terlihat paling mirip denganmu?':13,
        'Di antara temanmu, siapa orang yang paling kamu suka dalam konteks romantis?':15,
        'Di antara temanmu, siapa orang yang menurutmu paling baik dan paling buruk sifatnya?':16,
        'Siapa mantan terindahmu?':16,
        'Siapa orang yang ingin kamu jadikan istri/suami?':17,
        'Apakah kamu pernah melakukan ghosting?':18,
        'Apa aib yang kamu sembunyikan dari teman-temanmu?':19,
        'Berapa jumlah mantanmu? sebutkan!':20,
        }
    tth = random.choice(list(t.keys()))

    d = {'Lakukan rap gaya bebas selama 3 menit!':1, 
        'Biarkan orang lain membuat status menggunakan akun sosial mediamu!':2,
        'Berikan ponselmu kepada salah satu di antara kita dan biarkan orang tersebut mengirim satu pesan kepada siapapun yang dia mau!' :3,
        'Cium salah satu kaus kaki di antara temanmu!':4,
        'Makan satu gigitan kulit pisang!':5,
        'Peragakan salah satu orang di antara kita sampai ada yang bisa menebak siapa orang yang diperagakan!':6,
        'Nyanyikanlah salah lagu lagu dari Rossa!': 7,
        'Tirukan seorang selebriti sampai ada yang bisa menebak!':8,
        'Bertingkahlah seperti Hotman Paris selama 2 menit!':9,
        'Biarkan satu orang menggambar tato di wajahmu!':10,
        'Tutuplah mata lalu raba muka salah satu di antara kita sampai kamu bisa menebak siapa orang itu!':11,
        'Ungkapkan persaanmu kepada gebetanmu!':12,
        'Push up 20 kali!':13,
        'Kayang selama satu menit!':15,
        'Plank selama satu menit!.':16,
        'Coba teriak “aku sayang kamu” sekarang juga!':16,
        'Baca dengan lantang pesan yang terakhir kali kamu kirim ke gebetanmu!':17,
        'Telepon seorang teman dan katakan selamat ulang tahun sambil menyanyikan lagu!':18,
        'Tunjukkan gerakan dance terbaikmu!':19,
        'Parodikan adegan di film India kesukaanmu!':20,
        }
    dare = random.choice(list(d.keys()))

    
    g = {'https://i.pinimg.com/564x/d4/d0/4c/d4d04ca608a791e769fcef88c2435d6b.jpg':1, 
        'https://i.pinimg.com/564x/d5/00/4f/d5004fa2ded59ce5285a1eb7b9f00576.jpg':2,
        'https://i.pinimg.com/564x/53/ac/45/53ac458033d5f840800df3cd0b2ff55e.jpg' :3,
        'https://i.pinimg.com/564x/e4/4d/2b/e44d2b46ace72839f413ecd2505acd3d.jpg':4,
        'https://i.pinimg.com/564x/1e/13/53/1e13536611cda462baa82113f9cadb3c.jpg':5,
        'https://i.pinimg.com/564x/9a/b7/6a/9ab76a96e274ebf97a1b74e53ae99a70.jpg':6,
        'https://i.pinimg.com/564x/76/10/1a/76101ab14bace1803bb37988c825e42a.jpg':7,
        'https://i.pinimg.com/564x/fe/61/5c/fe615cf92a1c99bfce7302adc44f4379.jpg':8,
        'https://i.pinimg.com/564x/d4/b7/3f/d4b73f7c2c470b02f1f1c3417fe616f7.jpg':9,
        'https://i.pinimg.com/564x/80/b6/c8/80b6c83d13ad4401ae92add70c393324.jpg':10,
        }
    gambar = random.choice(list(g.keys()))

    s = {52002734:1, 
        52002735:2,
        52002736:3,
        52002737:4,
        52002738:5,
        52002740:6,
        52002748:7,
        52002745:8}
    stiker = random.choice(list(s.keys()))

    if msg_from_user == 'mulai':
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='Selamat datang di Line Chatbot games truth or dare',
                actions=[
                    MessageTemplateAction(
                        label='Aturan cara bermain',
                        text='aturan'
                    ),
                    MessageTemplateAction(
                        label='Mulai gamesnya',
                        text='start'
                    )
                ]
            )
        )   
        line_bot_api.reply_message(event.reply_token, message)


    if msg_from_user == 'start':
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='Mau pilih apa?',
                actions=[
                    MessageTemplateAction(
                        label='Truth',
                        text='t'
                    ),
                    MessageTemplateAction(
                        label='Dare',
                        text='d'
                    )
                ]
            )
        )   
        line_bot_api.reply_message(event.reply_token, message)

    if msg_from_user == 'selesai':
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='Mau lanjut?',
                actions=[
                    MessageTemplateAction(
                        label='berhenti',
                        text='berhenti'
                    ),
                    MessageTemplateAction(
                        label='lanjut',
                        text='mulai'
                    )
                ]
            )
        )   
        line_bot_api.reply_message(event.reply_token, message)


    if msg_from_user == 't':
        message = TextSendMessage(tth + "\n" + "Apakah bisa menjawabnya? Ketik 'bisa' jika memang bisa dan ketik 'gabisa' jika tidak mampu melakukannya")
        line_bot_api.reply_message(event.reply_token, message)

    if msg_from_user == 'd':
        message = TextSendMessage(dare + "\n" + "Apakah bisa melakukan tantangan ini? Ketik 'bisa' jika memang bisa dan ketik 'gabisa' jika tidak mampu melakukannya")
        line_bot_api.reply_message(event.reply_token, message)

    if msg_from_user == 'bisa':
        message = TextSendMessage("coba ceritakan jawabanmu jika kamu memilih truth atau peragarakan langsung/videokan jika kamu memilih dare")
        line_bot_api.reply_message(event.reply_token, message)

    if msg_from_user == 'gabisa':
        image_message = ImageSendMessage(
            original_content_url=gambar,
            preview_image_url='https://i.pinimg.com/564x/40/1e/cf/401ecf89c1d2cbac56d26cc95c3f9fb2.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)

    if msg_from_user == 'aturan':
        image_message = ImageSendMessage(
            original_content_url='https://i.pinimg.com/564x/a2/cd/eb/a2cdeb2f9f29dd0f2717f0a3d04ddecc.jpg',
            preview_image_url='https://i.pinimg.com/564x/a2/cd/eb/a2cdeb2f9f29dd0f2717f0a3d04ddecc.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    
    if msg_from_user == 'berhenti':
        sticker_message = StickerSendMessage(
            package_id='11537',
            sticker_id=stiker)
        line_bot_api.reply_message(event.reply_token, sticker_message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
