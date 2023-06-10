label _shitsumon7:
    N "次の質問です"

# 2nd Question
    scene bg school
    with fade

    voice "7/7-0 N.ogg"
    N "教室で、先生が話しています。学生は明日、何時にどこに集まらなければならなりませんか。"

    show char3 sensei at center # Male

    voice "7/7-1 M.ogg"
    M "先生は話しています。"


    voice "7/7-2 N.ogg"
    N "学生は明日、何時にどこに集まらなければならなりませんか。"

menu:

    "正しい答えはどっちですか？"

    "8時半に　きょうしつ":
        jump _Kotae71

    "8時半に　たいいくかんの　前":
        jump _Kotae72

    "９時半に　きょうしつ":
        jump _Kotae73

    "９時半に　たいいくかんの　前":
        jump _Kotae74

label _Kotae71:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan kedua (８時半に　たいいくかんの　前) \n Keyword:　までに来てください、集まってきださい。"
    jump _shitsumon8

label _Kotae72:
    N "はい、そうです。"
    jump _shitsumon8

label _Kotae73:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan kedua (８時半に　たいいくかんの　前) \n Keyword:　までに来てください、集まってきださい。"
    jump _shitsumon8

label _Kotae74:
    N "いいえ、違います。\n Jawaban yang benar adalah pilihan kedua (８時半に　たいいくかんの　前) \n Keyword:　までに来てください、集まってきださい。"
    jump _shitsumon8
