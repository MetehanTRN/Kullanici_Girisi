"""KULLANICI GİRİŞ UYGULAMASI"""

kullanici_adi = "MTnaz"
sifre = 76831608
kontrol = 5

print("Lutfen giris yapmak icin bilgilerinizi giriniz")

_kullanici_adi = input("Kullanici Adi : ")
_sifre = int(input("Sifre : "))

while(_kullanici_adi != kullanici_adi or _sifre != sifre):
	
	kontrol -= 1
	if(_kullanici_adi != kullanici_adi and _sifre == sifre):
		print("Kullanici adinizi yanlis girdiniz...")
	
	elif(_kullanici_adi == kullanici_adi and _sifre != sifre):
		print("Sifrenizi yanlis girdiniz...")
		
		if(kontrol == 3):
			print("Sifrenizi mi unuttunuz E/H")
			giris = input()
			
			if(giris == "E"):
				print("Sifrenizi almak icin guvenlik sorusunu cevaplayin")
				print("Annenizin kizlik soyadi nedir? ",end = "")
				soru = input()
				
				if(soru == "yasul"):
					print("Sifreniz : ",sifre)
				
				else:
					print("Guvenlik sorusu hatali...")
					print("Giris alanina yonlendiriliyorsunuz...")			
	else:
		print("Lutfen bilgilerinizi kontrol edin...")
		
	print("Giris hakkiniz : {}".format(kontrol))
		
	_kullanici_adi = input("Kullanici Adi : ")
	_sifre = int(input("Sifre : "))
		
	if(kontrol == 0):
		print("Giris hakkiniz dolmustur, lutfen daha sonra tekrar deneyin")
		break
	
if(_kullanici_adi == kullanici_adi and _sifre == sifre):
	print("Giris Basarili")
	print("Hosgeldiniz")
