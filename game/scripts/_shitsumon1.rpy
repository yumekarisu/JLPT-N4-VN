label _shitsumon1:

# 1st Question
    scene bg museum
    with fade

    voice "1/1-0 N.ogg"
    N "男の人と女の人が話しています。男の人は、何で美術館へ行きますか。"

    show char1 test at left # Male

    voice "1/1-1 M.ogg"
    M "男の人は話しています。"

    show char2 test at right# Female

    voice "1/1-2 F.ogg"
    F　"女の人は話しています。"

    voice "1/1-3 M.ogg"
    M "男の人は話しています。"

    voice "1/1-4 F.ogg"
    F "女の人は話しています。"

    voice "1/1-5 M.ogg"
    M "男の人は話しています。"

    voice "1/1-6 F.ogg"
    F "女の人は話しています。"

    voice "1/1-7 M.ogg"
    M "男の人は話しています。"

    voice "1/1-8 N.ogg"
    N "男の人は、何で美術館へ行きますか。"

menu:

    "正しい答えはどっちですか？"

    "{image=images/kotae1-1.png}":
        jump _Kotae11

    "{image=images/kotae1-2.png}":
        jump _Kotae12

    "{image=images/kotae1-3.png}":
        jump _Kotae13

    "{image=images/kotae1-4-resize.png}":
        jump _Kotae14

label _Kotae11:
    N "はい、そうです。"
    jump _shitsumon2


label _Kotae12:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan pertama (自転車) \n Keyword: 時間がかかります、自転車のほうが便利です。"
    jump _shitsumon2


label _Kotae13:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan pertama (自転車) \n Keyword: 時間がかかります、自転車のほうが便利です。"
    jump _shitsumon2


label _Kotae14:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan pertama (自転車) \n Keyword: 時間がかかります、自転車のほうが便利です。"
    jump _shitsumon2
