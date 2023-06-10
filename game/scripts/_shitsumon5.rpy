label _shitsumon5:
    N "次の質問です"

# 2nd Question
    scene bg park
    with fade

    voice "5/5-0 N.ogg"
    N "男の留学生と女の人が話しています。男の留学生は、何を持っていきますか。"

    show char4 ryuugakusei at left # Male

    voice "5/5-1 M.ogg"
    M "男の留学生は話しています。"

    show char2 test at right# Female

    voice "5/5-2 F.ogg"
    F　"女の人は話しています。"

    voice "5/5-3 M.ogg"
    M "男の留学生は話しています。"

    voice "5/5-4 F.ogg"
    F "男の留学生は話しています。"

    voice "5/5-5 M.ogg"
    M "男の留学生は話しています。"

    voice "5/5-6 N.ogg"
    N "男の留学生は、何を持っていきますか。"

menu:

    "正しい答えはどっちですか？"

    "{image=images/kotae5-1.png}":
        jump _Kotae51

    "{image=images/kotae5-2.png}":
        jump _Kotae52

    "{image=images/kotae5-3.png}":
        jump _Kotae53

    "{image=images/kotae5-4.png}":
        jump _Kotae54

label _Kotae51:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan ketiga (本) \n Keyword:　本もいいと思いますよ、あまり聞きませんから"
    jump _shitsumon6

label _Kotae52:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan ketiga (本) \n Keyword:　本もいいと思いますよ、あまり聞きませんから"
    jump _shitsumon6

label _Kotae53:
    N "はい、そうです。"
    jump _shitsumon6

label _Kotae54:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan ketiga (本) \n Keyword:　本もいいと思いますよ、あまり聞きませんから"
    jump _shitsumon6
