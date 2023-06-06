isim=input("İsminizi girin:")
sifre=input("Şifrenizi girin:")
if isim == sifre:
    print("İsim ve şifre aynı olamaz")
    sifre=input("Şifrenizi girin:")
if isim != sifre:
    isim2=input("İsminizle giriş yapın:")
    if isim2 != isim:
        print("İsminizi yanlış girdiniz tekrar giriniz")
        isim2=input("İsminizle giriş yapınız:")
    if isim2 == isim:
        sifre2=input("Şifrenizle giriş yapın:")
    if  sifre2 != sifre:
        print("Şifrenizi yanlış girdiniz tekrar giriniz")
        sifre2=input("Şifrenizle giriş yapınız:")
    if sifre2 == sifre:
        print("Giriş tamamlandı")