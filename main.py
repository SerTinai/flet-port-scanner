"""y=40
x=52

print(id(x), id(y))"""

"""port =input("port input")
port.strip()
print(int(port))"""

"""total_kota=100000
harcanan_kota=int(input("harcanan kota"))
kalan_kota=total_kota-harcanan_kota
print(f"kalan kota: {kalan_kota}")"""

"""server_active = True
print(type(server_active))"""

"""hava_durumu = "yağmurlu"
if hava_durumu == "yağmurlu":
    print("Şemsiyeni almayı unutma!")
elif hava_durumu == "güneşli":
    print("Güneş gözlüğünü takmayı unutma!")
elif hava_durumu == "karlı":
    print("Sıcak giyinmeyi unutma!")
elif hava_durumu == "rüzgarlı":
    print("Rüzgar geçirmez bir ceket giymeyi unutma!")
elif hava_durumu == "sisli":
    print("Sis lambalarını açmayı unutma!")
elif hava_durumu == "bulutlu":
    print("Hafif bir yağmur olabilir, şemsiye almayı düşünebilirsin!") """

"-----------------------------------------"

"""coming_Ip = input("Gelen IP adresini girin: ")
blacklist_Ip = input("Engellenmiş IP adresini girin: ")
istek_sayisi = int(input("Bu IP adresinden gelen istek sayısını girin: "))  
if coming_Ip == blacklist_Ip and istek_sayisi > 10:
    print("Bu IP adresi engellenmiş. Erişim reddedildi.")
else:    
    print("Bu IP adresi engellenmemiş. Erişim sağlandı.")"""

"""kalan_sorgu =40
sorgulanan_bilet = int(input("Sorgulanan bilet sayısını girin: "))
sorgulanan_bilet_sayisi = sorgulanan_bilet.strip()
if sorgulanan_bilet_sayisi.isdigit():
    sorgulanan_bilet_sayisi = int(sorgulanan_bilet_sayisi)
    if sorgulanan_bilet_sayisi <= kalan_sorgu:
        print(f"{sorgulanan_bilet_sayisi} bilet sorgulandı. Kalan sorgu hakkınız: {kalan_sorgu - sorgulanan_bilet_sayisi}")
    else:
        print("Sorgulanan bilet sayısı kalan sorgu hakkını aşıyor. Lütfen daha az bilet sorgulayın.")"""

"""port = int(input("Port numarasını girin: "))
port=port.strip()
if port.isdigit():
    port = int(port)
    if 0 <= port <= 65535:
        print(f"Geçerli bir port numarası girdiniz: {port}")
    else:
        print("Port numarası 0 ile 65535 arasında olmalıdır.")"""


"""start_port = int(input("Başlangıç port numarasını girin: ")).strip()
end_port = int(input("Bitiş port numarasını girin: ")).strip()
if start_port.isdigit() and end_port.isdigit():
    start_port = int(start_port)
    end_port = int(end_port)
for port in range(start_port, end_port + 1):
    if 0 <= port <= 65535:
        print(f" port taranıyor {port} ")
    else:
        print(f"Port numarası {port} geçersiz. Port numarası 0 ile 65535 arasında olmalıdır.")"""

"""true_password = "Cyber12345"

while True:
    password = input("Şifreyi girin: ").strip()
    if password == true_password:
        print("Şifre doğru! Erişim sağlandı.")
        break
    else:
        print("Şifre yanlış! Lütfen tekrar deneyin.")"""

"""number =1
while number < 4:
    if number == 2:
        number = number + 1
        continue
    print(number)
    number = number + 1
    print(number)"""

import flet as ft
import socket

def main(page: ft.Page):
    # Panel Ayarları
    page.title = "Siber Güvenlik Port Tarayıcı"
    page.theme_mode = ft.ThemeMode.DARK # Hacker modu: Karanlık tema 😎
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Arayüz Elemanları
    baslik = ft.Text(value="🛡️ PORT TARAMA İSTASYONU", size=28, weight=ft.FontWeight.BOLD, color="green")
    ip_input = ft.TextField(label="Hedef IP veya Alan Adı (Örn: 127.0.0.1)", width=350, border_color="green")
    durum_yazisi = ft.Text(value="Sistem Hazır. Hedef girip taramayı başlatın.", size=16, color="white")
    
    # Sonuçların akacağı liste paneli
    sonuc_kutusu = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True)
    sonuc_konteyner = ft.Container(
        content=sonuc_kutusu,
        border=ft.Border.all(1, "green"),
        border_radius=10,
        width=400,
        height=200,
        bgcolor="#1e1e1e"
    )

    # Arka Plandaki Siber Güvenlik Motoru (Soket Taraması)
    def taramayi_baslat(e):
        hedef_ip = ip_input.value.strip()
        
        if not hedef_ip:
            durum_yazisi.value = "❌ Lütfen geçerli bir IP veya domain girin!"
            durum_yazisi.color = "red"
            page.update()
            return
        
        durum_yazisi.value = f"⚡ {hedef_ip} taranıyor... Lütfen bekleyin..."
        durum_yazisi.color = "yellow"
        sonuc_kutusu.controls.clear() # Eski sonuçları temizle
        page.update()
        
        # En popüler siber güvenlik portları
        hedef_portlar = [21, 22, 23, 25, 53, 80, 443, 8080, 9999]
        acik_port_bulundu = False
        
        for port in hedef_portlar:
            # Soket bağlantısı denemesi (TCP SYN gibi düşünebilirsin)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5) # Port başına yarım saniye süre tanı (hızlı olması için)
            
            result = s.connect_ex((hedef_ip, port)) # 0 dönerse port açıktır
            
            if result == 0:
                sonuc_kutusu.controls.append(
                    ft.Text(f"🔓 Port {port} : AÇIK !", color="green", weight=ft.FontWeight.BOLD)
                )
                acik_port_bulundu = True
            s.close()
            page.update() # Her port kontrolünde arayüzü canlı güncelle
            
        if not acik_port_bulundu:
            sonuc_kutusu.controls.append(ft.Text("🔒 Belirlenen portlarda açık bulunamadı.", color="red"))
            
        durum_yazisi.value = "✅ Tarama Tamamlandı!"
        durum_yazisi.color = "green"
        page.update()

    # Yeni Flet buton standardı
    tarama_butonu = ft.Button("Taramayı Başlat", on_click=taramayi_baslat, icon=ft.Icons.PLAY_ARROW)
    
    # Elemanları Ekrana Diz
    page.add(
        baslik,
        ft.Divider(height=20, color="transparent"),
        ip_input,
        tarama_butonu,
        ft.Divider(height=10, color="transparent"),
        durum_yazisi,
        ft.Divider(height=10, color="transparent"),
        sonuc_konteyner
    )

# Yeni Flet çalıştırma standardı
ft.run(main, view=ft.AppView.WEB_BROWSER)