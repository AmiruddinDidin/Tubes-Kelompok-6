# Kelompok  : 6 (Engineer Mancing)

## Anggota  :

# Shieny Carissa Gembira (16923122)         : Pembuat Laporan
# Reva Elita Nurhaliza (16923126)           : Pembuat Laporan
# Sean Matthew N.H. Hutagaol (16923130)     : Dekomposisi Unit Produk
# Didin Amiruddin (16923134)                : Pembuat Source Code
# Ferdinand Bonar Y.A (16923138)            : Simulasi dan Flowchart
# Nadhifah Apriliani Kurniawan (16923142)   : Pembuat Powerpoint

# Dosen Pengampu    : Jooned Hendrarsakti, Ph.D (KU-1102 - 25)
# Deskripsi         : Program Senjata Pelontar 

## KAMUS

# sudut, percepatan gravitasi, kecepatan_awal, pi, jarak, xmax, ymax : float
# username, password                                                 : list of string
# run, berhasil_login, id_login                                                : boolean


## ALGORITMA

##======================================================DATABASE==========================================================

# DATA UNTUK PERSAMAAAN PARABOLA
pi = 3.14159265359
percepatan_gravitasi = 9.80665 #m/s^2
kecepatan_awal = 90 #m/s

# DATA ARRAY DATABASE
username = ["Shieny", "Reva", "Sean", "Didin", "Ferdinand", "Nadhifah"]
password = ["16923122", "16923126", "16923130", "16923134", "16923138", "16923142"]

#=========================================================================================================================

#FUNGSI UNTUK KESELURUHAN PROGRAM

# Fungsi untuk register user
def register():
    user_register = input("Daftarkan username Anda : ")
    pass_register = input("Daftarkan password Anda : ")
    username.append(user_register)
    password.append(pass_register)
    print("\nUser berhasil didaftarkan!\n")

# Fungsi untuk login user
def login(id_login):
    user_login = input("\nMasukkan username Anda : ")
    pass_login = input("Masukkan password Anda : ")

    id_login = False
    i = 0

    while (id_login == False):
        if (user_login == username[i] and pass_login == password[i]):
            print(f"\nBerhasil login, selamat datang yang mulia {user_login}\n")
            id_login = True
            break

        else:
            i+=1
            if (i == len(username)):
                break

    if (id_login == False):
        print("\nUser belum terdaftar atau password salah, silakan coba lagi!\n")

    return id_login


#-------------------------------------------------------------------------------------------------------------------------

''' ____________________________ '''
'''|    FUNGSI PROGRAM UTAMA    |'''
'''|____________________________|'''

# Import Extension Perhitungan Trigonometri 

import math

# Parabola Bidang Datar Mode 1 (Ketinggian Sama) - Menentukan Sudut Elevasi Penembakan
def parabola_datar1(): ##BELAKANGAN
    jarak = float(input("\nMasukkan jarak target penembakan (m): "))
    sin2sudut = (jarak*percepatan_gravitasi)/kecepatan_awal**2
    sudut = math.asin(sin2sudut)*180/(pi*2)
    ymax = kecepatan_awal**2*(math.sin(math.radians((sudut))))**2/2*percepatan_gravitasi
    t = jarak/(kecepatan_awal*math.cos(math.radians(sudut)))

    print("\n=====================================================================================================================")
    print(f"Dengan jarak target penembakan sebesar {jarak} meter dan kecepatan penembakan sebesar {kecepatan_awal}, maka sudut elevasi penembakannya sebesar {sudut} derajat dengan ketinggian maksimum {ymax} meter dan waktu tempuh {t} detik")
    print("=====================================================================================================================\n")

    return


# Parabola Bidang Datar Mode 2 (Ketinggian Sama) - Menentukan Jarak Maksimum dan Ketinggian Maksimum
def parabola_datar2(): 
    sudut = float(input("\nMasukkan besar sudut elevasi penembakan (derajat): "))
    xmax = ((kecepatan_awal**2)*math.sin(2*math.radians(sudut)))/percepatan_gravitasi
    ymax = ((kecepatan_awal**2)*((math.sin(math.radians(sudut)))**2))/(2*percepatan_gravitasi)
    t = (2*kecepatan_awal*math.sin(math.radians(sudut)))/percepatan_gravitasi

    print("\n=====================================================================================================================")
    print(f"Dengan sudut elevasi tembakan sebesar {sudut} derajat, maka jarak maksimum yang dapat dicapai adalah {xmax} meter dengan waktu tempuh sebesar {t} detik dengan ketinggian maksimum {ymax} meter")
    print("=====================================================================================================================\n")

    return


# Parabola Bidang Miring
def parabola_miring():
    sudut_bidang = float(input("\nMasukkan besar sudut bidang (derajat): "))
    sudut_tembak = float(input("Masukkan besar sudut elevasi penembakan (derajat): "))
    t = (2*kecepatan_awal*math.sin(math.radians(sudut_tembak)))/(percepatan_gravitasi*math.cos(math.radians(sudut_bidang)))
    jarak =(kecepatan_awal*math.cos(math.radians(sudut_tembak))*t)-(0.5*percepatan_gravitasi*math.sin((math.radians(sudut_bidang)))*t**2)

    print("\n=====================================================================================================================")
    print(f"Dengan sudut elevasi tembakan sebesar {sudut_tembak} derajat dan sudut bidang miring {sudut_bidang} derajat, maka jarak maksimum target yang dapat dicapai adalah {jarak} meter dengan waktu tempuh sebesar {t} detik")
    print("=====================================================================================================================\n")

    return


# ----------------------------------------------------------PROGRAM UTAMA----------------------------------------------------------

run = True

while run == True:
    print("Pilih tindakan:\n1. Register \n2. Login \n3. Logout")

    choice = input("Masukkan pilihan (1/2/3): ") # Pilihan Program
    
    if (choice == "1"): # Register User
        register()

    elif (choice == "2"): # Login User
        id_login = False

        if (login(id_login) == True): #Program berjalan ketika berhasil login

            print("-----------Program berjalan-----------")
            bidang = input("\nMasukkan Jenis Bidang Penembakan (Datar/Miring): ")

            if (bidang == "Datar"):
                print("\nKeterangan Mode :\nMode 1 : Atur Jarak Target (Maksimal: 825 m)\nMode 2 : Cari Jarak Maksimum, Tinggi Maksimum, dan Waktu Tempuh")
                mode = int(input("\nMasukkan Jenis Mode (1/2): "))

                if (mode == 1):
                    parabola_datar1()

                elif (mode == 2):
                        parabola_datar2()

            elif (bidang == "Miring"):
                parabola_miring()

    elif (choice == "3"): # Logout User
        print("\nKeluar dari program...")
        run = False

    else: # Salah Input
        print("\nTidak ada di opsi tindakan, silahkan coba lagi\n")

