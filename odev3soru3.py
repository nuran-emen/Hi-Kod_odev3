from datetime import datetime
def YasHesaplama(dogumYili):
    mevcutYil = datetime.now().year
    yas = mevcutYil-dogumYili
    return yas 

dogumYili = int(input("Doğum yılınızı girin:"))
print(f"Yaşınız : {YasHesaplama(dogumYili)}")