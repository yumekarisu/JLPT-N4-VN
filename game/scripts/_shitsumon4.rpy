label _shitsumon4:
    N "次の質問です"

# 2nd Question
    scene bg room
    with fade

    voice "4/4-0 N.ogg"
    N "女の人と男の人が写真についてはなしています。女の人は、どの写真をおくりますか。"

    show char2 test at left # Male

    voice "4/4-1 F.ogg"
    F "女の人は話しています。"

    show char1 test at right# Female

    voice "4/4-2 M.ogg"
    M　"男の人は話しています。"

    voice "4/4-3 F.ogg"
    F "女の人は話しています。"

    voice "4/4-4 M.ogg"
    M "男の人は話しています。"

    voice "4/4-5 F.ogg"
    F "女の人は話しています。"

    voice "4/4-6 M.ogg"
    M "男の人は話しています。"

    voice "4/4-7 F.ogg"
    F "女の人は話しています。"

    voice "4/4-8 N.ogg"
    N "女の人は、どの写真をおくりますか。"

menu:

    "正しい答えはどっちですか？"

    "{image=images/kotae4-1.png}":
        jump _Kotae41

    "{image=images/kotae4-2.png}":
        jump _Kotae42

    "{image=images/kotae4-3.png}":
        jump _Kotae43

    "{image=images/kotae4-4.png}":
        jump _Kotae44

label _Kotae41:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan keempat (山と大学の前) \n Keyword:　よく見えない、ダメだね、あまりきれいじゃない"
    jump _shitsumon5

label _Kotae42:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan keempat (山と大学の前) \n Keyword:　よく見えない、ダメだね、あまりきれいじゃない"
    jump _shitsumon5

label _Kotae43:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan keempat (山と大学の前) \n Keyword:　よく見えない、ダメだね、あまりきれいじゃない"
    jump _shitsumon5

label _Kotae44:
    N "はい、そうです。"
    jump _shitsumon5
