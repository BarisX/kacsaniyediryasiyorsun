def kaçsaniyediyaşıyorsun():
    kullanıcı_yaşı = input("Yaşını Gir Lütfen: ")
    yaş_saniyesi = int(kullanıcı_yaşı) * 365 * 24 * 60 * 60
    print("Sen {} saniyedir yaşıyorsun oha.".format(yaş_saniyesi))
    