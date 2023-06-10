label _shitsumon2:
    N "次の質問です"

# 2nd Question
    scene bg school # Art Museum stock image
    with fade

    voice "2/2-0 N.ogg"
    N "男の学生と女の学生が話しています。男の学生は、何を買いますか。"

    show char1 test at left # Male

    voice "2/2-1 M.ogg"
    M "男の学生は話しています。"

    show char2 test at right# Female

    voice "2/2-2 F.ogg"
    F　"女の学生は話しています。"

    voice "2/2-3 M.ogg"
    M "男の学生は話しています。"

    voice "2/2-4 F.ogg"
    F　"女の学生は話しています。"

    voice "2/2-5 M.ogg"
    M "男の学生は話しています。"

    voice "2/2-6 F.ogg"
    F　"女の学生は話しています。"

    voice "2/2-7 M.ogg"
    M "男の学生は話しています。"

    voice "2/2-8 N.ogg"
    N　"男の学生は、何を買いますか。"

menu:

    "正しい答えはどっちですか？"

    "{image=images/kotae2-1.png}":
        jump _Kotae21

    "{image=images/kotae2-2.png}":
        jump _Kotae22

    "{image=images/kotae2-3.png}":
        jump _Kotae23

    "{image=images/kotae2-4.png}":
        jump _Kotae24

label _Kotae21:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan keempat (タオル) \n Keyword: カップはもうたくさん持っているかもしれないな。"
    jump _shitsumon3

label _Kotae22:
    N "いいえ、違います。n Jawaban yang benar adalah pilihan keempat (タオル) \n Keyword: カップはもうたくさん持っているかもしれないな。"
    jump _shitsumon3

label _Kotae23:
    N "いいえ、違います。n Jawaban yang benar adalah pilihan keempat (タオル) \n Keyword: カップはもうたくさん持っているかもしれないな。"
    jump _shitsumon3

label _Kotae24:
    N "はい、そうです。"
    jump _shitsumon3
