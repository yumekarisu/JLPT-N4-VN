label _shitsumon3:
    N "次の質問です"

# 2nd Question
    scene bg cafe
    with fade

    voice "3/3-0 N.ogg"
    N "男の人と女の人が話しています。女の人は、チケットを何枚予約しますか。"

    show char1 test at left # Male

    voice "3/3-1 M.ogg"
    M "男の人は話しています。"

    show char2 test at right# Female

    voice "3/3-2 F.ogg"
    F　"女の人は話しています。"

    voice "3/3-3 M.ogg"
    M "男の人は話しています。"

    voice "3/3-4 F.ogg"
    F "女の人は話しています。"

    voice "3/3-5 M.ogg"
    M "男の人は話しています。"

    voice "3/3-6 F.ogg"
    F "女の人は話しています。"

    voice "3/3-7 M.ogg"
    M "男の人は話しています。"

    voice "3/3-8 N.ogg"
    N "女の人は、チケットを何枚予約しますか。"

menu:

    "正しい答えはどっちですか？"

    "２　まい":
        jump _Kotae31

    "３　まい":
        jump _Kotae32

    "５　まい":
        jump _Kotae33

    "６　まい":
        jump _Kotae34

label _Kotae31:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan ketiga (5 まい) \n Keyword:　一人都合が悪くなったら"
    jump _shitsumon4

label _Kotae32:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan ketiga (5 まい) \n Keyword:　一人都合が悪くなったら"
    jump _shitsumon4

label _Kotae33:
    N "はい、そうです。"
    jump _shitsumon4

label _Kotae34:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan ketiga (5 まい) \n Keyword:　一人都合が悪くなったら"
    jump _shitsumon4
