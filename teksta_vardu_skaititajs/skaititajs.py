def skaititVardus():
    """Skaita vārdu biežumu tekstā"""
    try:
        with open("teksta_vardu_skaititajs/teksts.txt", "r", encoding="utf-8") as f:
            teksts = f.read()

        vardi = teksts.split()
        for i in range(len(vardi)):
            vardi[i] = vardi[i].strip(".,!-?*'\")(")
            vardi[i] = vardi[i].lower()

        visi_vardi = {}
        for vards in vardi:
            if vards:  # Ignorē tukšus vārdus
                visi_vardi[vards] = visi_vardi.get(vards, 0) + 1

        return visi_vardi

    except Exception as e:
        print(f"Kļūda: {e}")
        return {}

rezultati = skaititVardus()
biezakais_vards = max(rezultati, key=rezultati.get)
varda_skaits = rezultati[biezakais_vards]
print(biezakais_vards, varda_skaits)