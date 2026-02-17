import random 
sayi=random.randint(1,100)
hak = 5
puan=120

while hak>0:
  hak-=1
  puan-=20
  tahmin=  int(input('Tahmin giriniz:'))
  if sayi==tahmin: 
   print(f'bravo {tahmin} doğru tahmin puanınız{puan}')
   break
  elif sayi<tahmin:
   print('asagi ininiz')
  else:
   print('Yukari cikiniz')
  if hak==0:
   print(f'hakkınız btti sayi {sayi} idi puanınız {puan}')
 

