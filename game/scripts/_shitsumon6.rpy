label _shitsumon6:
    N "次の質問です"

# 2nd Question
    scene bg office
    with fade

    voice "6/6-0 N.ogg"
    N "会社で男の人と女の人が話しています。女の人は今日、このあと何をしますか。"

    show char1 test at left # Male

    voice "6/6-1 M.ogg"
    M "男の人は話しています。"

    show char2 test at right# Female

    voice "6/6-2 F.ogg"
    F　"女の人は話しています。"

    voice "6/6-3 M.ogg"
    M "男の人は話しています。"

    voice "6/6-4 F.ogg"
    F "女の人は話しています。"

    voice "6/6-5 M.ogg"
    M "男の人は話しています。"

    voice "6/6-6 F.ogg"
    F "女の人は話しています。"

    voice "6/6-7 M.ogg"
    M "男の人は話しています。"

    voice "6/6-8 N.ogg"
    N "女の人は今日、このあと何をしますか。"

menu:

    "正しい答えはどっちですか？"

    "{image=images/kotae6-1.png}":
        jump _Kotae61

    "{image=images/kotae6-2.png}":
        jump _Kotae62

    "{image=images/kotae6-3.png}":
        jump _Kotae63

    "{image=images/kotae6-4.png}":
        jump _Kotae64

label _Kotae61:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan kedua (コピー) \n Keyword:　明日のかいぎ、それは明日ですね。"
    jump _shitsumon7

label _Kotae62:
    N "はい、そうです。"
    jump _shitsumon7

label _Kotae63:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan kedua (コピー) \n Keyword:　明日のかいぎ、それは明日ですね。"
    jump _shitsumon7

label _Kotae64:
    N "いいえ、違います\n Jawaban yang benar adalah pilihan kedua (コピー) \n Keyword:　明日のかいぎ、それは明日ですね。。"
    jump _shitsumon7
