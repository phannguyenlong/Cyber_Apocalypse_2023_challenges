ct = "bc9bc77a809b7f618522d36ef7765e1cad359eef39f0eaa5dc5d85f3ab249e788c9bc36e11d72eee281d1a645027bd96a363c0e24efc6b5caa552b2df4979a5ad41e405576d415a5272ba730e27c593eb2c725031a52b7aa92df4c4e26f116c631630b5d23f11775804a688e5e4d5624"


text = ""
for i in range(0, len(ct)):
    if (i!=0 and (i%32) == 0):
        print(text)
        text = ""
    else:
        text += ct[i]