from datetime import datetime
def YasHesaplama(dogumYili):
    mevcutYil = datetime.now().year
    yas = mevcutYil-dogumYili
    return yas 

dogumYili = int(input("Doğum yılınızı girin:"))
print(f"Yaşınız : {YasHesaplama(dogumYili)}")


def emeklilik(isim) :
    yas = YasHesaplama(dogumYili)
    kalanYil = 65 - yas
    if yas >= 65 :
        print("Emekli oldunuz.")
    else :
        print(f"{isim} emekliliğine {kalanYil} yıl kaldı ")
   
emeklilik("Elif")