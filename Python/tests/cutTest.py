txt = "Ich bin ein\tlanger String der\timmer bei Kommas aufgeteilt\twird und ich bin nur ein Test"
cut = txt.split("\t")

for i in range(len(cut)):
    print('Eintrag',i,':',cut[i])