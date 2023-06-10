label _shitsumon8:
    N "次の質問です"

# 2nd Question
    scene bg library
    with fade

    voice "8/8-0 N.ogg"
    N "図書館で男の人と係りの人が話しています。男の人はこのあとどのボタンを押しますか。"

    show char1 test at left # Male

    voice "8/8-1 M.ogg"
    M "男の人は話しています。"

    show char2 test at right# Female

    voice "8/8-2 F.ogg"
    F　"係りの人は話しています。"

    voice "8/8-3 M.ogg"
    M "男の人は話しています。"

    voice "8/8-4 F.ogg"
    F "係りの人は話しています。"

    voice "8/8-5 M.ogg"
    M "男の人は話しています。"

    voice "8/8-6 N.ogg"
    N "男の人はこのあとどのボタンを押しますか。"

menu:

    "正しい答えはどっちですか？"

    "あかと　きいろ":
        jump _Kotae81

    "あかと　しろ":
        jump _Kotae82

    "あおと　きいろ":
        jump _Kotae83

    "あおと　しろ":
        jump _Kotae84

label _Kotae81:
    N "はい、そうです。"
    jump _recap

label _Kotae82:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan pertama (あかと　きいろ) \n Keyword:　押したんですが、薄くする時は。"
    jump _recap

label _Kotae83:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan pertama (あかと　きいろ) \n Keyword:　押したんですが、薄くする時は。"
    jump _recap

label _Kotae84:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan pertama (あかと　きいろ) \n Keyword:　押したんですが、薄くする時は。"
    jump _recap
