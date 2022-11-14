import datetime

car_all = [
    {
        'Mobil':'Avanza',
        'Warna': 'Putih',
        'Kapasitas': 7,
        'Transmisi': 'Matic',
        'Stok Unit': 3,
        'Harga':290000
    },
    {
        'Mobil':'Calya',
        'Warna': 'Silver',
        'Kapasitas': 7,
        'Transmisi': 'Matic',
        'Stok Unit': 3,
        'Harga':280000
    },
    {
        'Mobil':'Agyaa',
        'Warna': 'Silver',
        'Kapasitas': 7,
        'Transmisi': 'Matic',
        'Stok Unit': 2,
        'Harga':280000
    },
    {
        'Mobil':'Brioo',
        'Warna': 'Putih',
        'Kapasitas': 5,
        'Transmisi': 'Matic',
        'Stok Unit': 2,
        'Harga':270000
    },
    {
        'Mobil':'Ertiga',
        'Warna': 'Hitam',
        'Kapasitas': 7,
        'Transmisi': 'Matic',
        'Stok Unit': 4,
        'Harga':285000
    }
]


def car_spec():
    print('\n========== Spesifikasi Mobil ==========\n')
    print('\tCarID \t| Jenis Mobil  \t\t| Warna\t\t| Kursi\t| Transmisi')

    for car_id, dict in enumerate(car_all):
        print(f"\t{car_id} \t| {dict['Mobil']} \t\t| {dict['Warna']} \t| {dict['Kapasitas']} \t| {dict['Transmisi']}")

def car_available():
    print('\n========== DAFTAR MOBIL TERSEDIA ==========\n')
    print('\tCarID \t| Mobil  \t\t| Transmisi \t| Stok Unit\t| Harga Sewa per Hari')

    for car_id, dict in enumerate(car_all):
        print(f"\t{car_id} \t| {dict['Mobil']} \t\t| {dict['Transmisi']} \t| {dict['Stok Unit']} \t\t| {dict['Harga']}")



def add_carlist():
    car_available()
    while True:
        car_type = input('Masukkan Tipe Mobil: ').capitalize()
        car_color = input('Masukkan Warna Mobil: ').capitalize()
        
        try:
            car_cap = int(input('Masukkan Kapasitas Mobil: '))
        except ValueError:
            print('Input anda invalid, mohon masukan nilai yang sesuai!')
            continue
        else:
            pass

        while True:
            transmission = input('Masukkan jenis transmisi mobil (Manual/Matic): ').capitalize()
            if transmission == 'Manual':
                break
            elif transmission == 'Matic':
                break
            else:
                print('Masukkan jenis transmisi yang sesuai (Manual/Matic)')
                transmission
                continue

        try:
            stok_unit = int(input('Masukkan stok unit mobil: '))
        except ValueError:
            print('Input anda invalid, mohon masukan nilai yang sesuai!')
            continue
        else:
            pass
        
        try:
            price = int(input('Masukkan harga sewa unit mobil: '))
        except ValueError:
            print('Input anda invalid, mohon masukkan nilai yang sesuai!')
            continue
        else:
            break

    while True:
        user_input = input('\nKetik Y jika yakin dan N untuk membatalkan perintah: ').upper()

        if user_input == 'Y':
            break
        elif user_input == 'N':
            add_carlist()
        else:
            user_input

    for car in car_all:
        if (car['Mobil'] == car_type) and (car['Warna'] == car_color) and (car['Kapasitas'] == car_cap) and (car['Transmisi'] == transmission) and (car['Harga'] == price):
            car['Stok Unit'] += stok_unit
            break
    else:
        car_all.append({
            'Mobil': car_type,
            'Warna': car_color,
            'Kapasitas': car_cap,
            'Transmisi': transmission,
            'Stok Unit': stok_unit,
            'Harga': price
        })
    car_available()
    main_menu()

def remove_carlist():
    car_available()
    
    while True:
        car_id = input('Masukkan CarID yang ingin dihapus: ')
        if car_id.isdigit() == False:
            print('Harap masukkan carID yang sesuai')
            car_id
        else:
            car_id = int(car_id)

            if car_id not in range(len(car_all)):
                print(f'CarID {car_id} yang anda masukkan tidak ada dalam database. Mohon masukkan CarID yang sesuai.')
            else:
                print('\Apakah anda ingin menghapus stok unit?')

                while True:
                    user_input = input('\nSilahkan ketik: \n"Y" untuk menghapus stok unit \n"N" untuk batal \nSilahkan Input: ').upper()
                    if user_input == 'Y':
                        del car_all[car_id]
                        break
                    elif user_input == 'N':
                        read_sub3()
                    else:
                        print('Input tidak sesuai. Silahkan ulangi.')
                        user_input
                break   
            
        break

    car_available()
    main_menu()

rent_cart = [] ## keranjang

def rent_car():
    car_available()

    while True:
        car_id = int(input('Masukkan CarID yang ingin di sewa: '))
        car_total = int(input('Masukkan jumlah mobil yang ingin di sewa: '))
        rent_day = int(input('Masukkan jumlah hari sewa: '))
        
        if car_total > car_all[car_id]['Stok Unit']:
            print(f"Stok mobil tidak mencukupi. Stok {car_all[car_id]['Mobil']} tersisa {car_all[car_id]['Stok Unit']} unit")
        else:
            rent_cart.append({
                'Mobil': car_all[car_id]['Mobil'],
                'Jumlah Mobil': car_total,
                'Jumlah Hari': rent_day,
                'Harga/hari': car_all[car_id]['Harga'],
                'CarID': car_id
            })
        
        for car in rent_cart:
            car_all[car['CarID']]['Stok Unit'] -= car['Jumlah Mobil']

            print('Isi Cart:')
            print(f'Mobil\t| Jumlah Mobil\t| Jumlah Hari\t| Harga per hari')

        for car in rent_cart:
            print(f"{car['Mobil']}\t| {car['Jumlah Mobil']}\t| {car['Jumlah Hari']}\t| {car['Harga/hari']}")
        break

    while True:
        check = input('Apakah anda ingin menyewa mobil lain ("Y": ya/"N": tidak): ').upper()

        if check == 'Y':
            car_id = int(input('Masukkan CarID yang ingin di sewa: '))
            print(f"Sisa stok {car_all['Mobil']} adalah {car_all[car_id]['Stok Unit']}.")

            if (car_all[car_id]['Stok Unit'] == 0):
                print('Mohon maaf unit mobil sedang kosong. Silahkan memilih unit mobil yang lain')
                continue
            else:
                add_car_total = int(input('Masukkan jumlah mobil yang ingin disewa: '))
                add_rent_day = int(input('Masukkan jumlah hari sewa: '))
                rent_cart.append([car_all[car_id]['Mobil'], add_car_total, add_rent_day, car_all[car_id]['Harga'], car_id])
                car_all[car_id]['Stok Unit'] -= add_car_total

                if (add_car_total > car_all[car_id]['Stok Unit']):
                    print('Unit mobil tidak cukup.')
                else:
                    rent_cart.append([car_all[car_id]['Mobil'], add_car_total, add_rent_day, car_all[car_id]['Harga'], car_id])
                    car_all[car_id]['Stok Unit'] -= add_car_total
        else:
            break
    
    print('\n========== DAFTAR SEWA MOBIL ==========\n')
    print('Mobil  \t| Jumlah Mobil \t| Jumlah Hari\t| Harga Sewa per Hari\t| Total Harga')

    total_price = 0

    for car in rent_cart:
        print(f"{car['Mobil']}\t\t| {car['Jumlah Mobil']}\t\t| {car['Jumlah Hari']}\t\t| {car['Harga/hari']}\t| {car['Jumlah Mobil'] * car['Jumlah Hari'] * car['Harga/hari']}")
        total_price += car['Harga/hari'] * car['Jumlah Mobil'] * car['Jumlah Hari']
        break

    while True:
        print(f'Total yang harus dibayar = {total_price}')
        if total_price != 0:
            total_money = int(input('Masukkan Jumlah Uang: '))

            if total_money > total_price:
                change = total_money - total_price
                print(f'Uang Kembalian: {change}')
                rent_cart.clear()
                break

            elif total_money < total_price:
                minus = total_price - total_money
                print(f'Maaf, uang kurang sebesar {minus}')
            
            elif total_money == total_price:
                print(f'Terima kasih telah percaya dengan jasa sewa kami')
                rent_cart.clear()
                break
        
        else:
            print(f'Terima kasih atas kunjungannya')
            break
    
    main_menu()

def read_sub1():
    while True:
        print('''
        ========== TREVO CAR RENTAL ========= 

        1. Spesifikasi daftar mobil
        2. Daftar mobil yang tersedia
        3. Kembali ke menu utama
        ''')
        try:
            menu_input = int(input('Masukan nomor menu utama: '))
        except ValueError:
            print('Input anda invalid, mohon hanya masukan angka!')
            continue
 
        if menu_input == 1:
           car_spec() ## daftar semua

        elif menu_input ==2:
            car_available() 
        elif menu_input == 3:
            main_menu()
        else:
            print('Mohon hanya input nomor menu 1 sampai 3!')

def read_sub2():
    while True:
        print('''
        ========== TREVO CAR RENTAL ========= 

        1. Menambah Daftar Mobil
        2. Kembali ke menu utama
        ''')
        try:
            menu_input = int(input('Masukan nomor menu utama: '))
        except ValueError:
            print('Input anda invalid, mohon hanya masukan angka!')
            continue
 
        if menu_input == 1:
           add_carlist()

        elif menu_input == 2:
            main_menu()
        else:
            print('Mohon hanya input nomor menu 1 sampai 2!')

def read_sub3():
    while True:
        print('''
        ========== TREVO CAR RENTAL ========= 

        1. Menghapus Daftar Mobil
        2. Kembali ke menu utama
        ''')
        try:
            menu_input = int(input('Masukan nomor menu utama: '))
        except ValueError:
            print('Input anda invalid, mohon hanya masukan angka!')
            continue
 
        if menu_input == 1:
            remove_carlist()

        elif menu_input == 2:
            main_menu()

        else:
            print('Mohon hanya input nomor menu 1 sampai 2!')

def read_sub4():
    while True:
        print('''
        ========== TREVO CAR RENTAL ========= 

        1. Menyewa Mobil
        2. Kembali ke menu utama
        ''')
        try:
            menu_input = int(input('Masukan nomor menu utama: '))
        except ValueError:
            print('Input anda invalid, mohon hanya masukan angka!')
            continue
 
        if menu_input == 1:
            rent_car()

        elif menu_input ==2:
            main_menu()

        else:
            print('Mohon hanya input nomor menu 1 sampai 2!')

def main_menu():
    time = datetime.datetime.now()
 
    print('\n\tSELAMAT DATANG DI TREVO CAR RENTAL!\n')
    print('\tJasa Rental Mobil Termudah dan Terpecaya\n')
    print(f'\tTanggal dan Waktu: {time}')
 
    while True:
        print('''
        ========== TREVO CAR RENTAL ========= 

        1. Daftar Mobil
        2. Menambahkan daftar mobil
        3. Menghapus daftar mobil
        4. Menyewa Mobil
        5. Keluar program
        ''')
 
        try:
            menu_input = int(input('Masukan nomor menu utama: '))
        except ValueError:
            print('Input anda invalid, mohon hanya masukan angka!')
            continue
 
        if menu_input == 1:
            read_sub1()
 
        elif menu_input == 2:
            read_sub2()
 
        elif menu_input == 3:
            read_sub3()

        elif menu_input == 4:
            read_sub4()

        elif menu_input == 5:
            break
 
        else:
            print('Mohon hanya input nomor menu 1 sampai 3!')

main_menu()
