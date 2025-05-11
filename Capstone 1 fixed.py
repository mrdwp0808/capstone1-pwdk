# Capstone 1 

# Data penjualan laptop

#==========No 4=================
print('\n')
print('-'*10,'CAPSTONE 1','-'*10)
print('\n')

from tabulate import tabulate

print('TOKO LAPTOP DUDUNGDUNG')
print('*'*25)
dictLaptop = {
    'pembelian': {
        'id': ['HP01', 'AS02', 'LT03'],
        'merk': ['HP', 'Acer', 'Lenovo'],
        'tipe': ['Pavilion', 'Swift', 'Thinkpad'],
        'jumlah': [10, 8, 12],
        'harga': [9500000, 7000000, 11000000],
        'serial': [
            ['HP01-001', 'HP01-002', 'HP01-003', 'HP01-004', 'HP01-005', 'HP01-006', 'HP01-007', 'HP01-008', 'HP01-009', 'HP01-010'],
            ['AS02-001', 'AS02-002', 'AS02-003', 'AS02-004', 'AS02-005', 'AS02-006', 'AS02-007', 'AS02-008'],
            ['LT03-001', 'LT03-002', 'LT03-003', 'LT03-004', 'LT03-005', 'LT03-006', 'LT03-007', 'LT03-008', 'LT03-009', 'LT03-010', 'LT03-011', 'LT03-012']
        ]
    },
    'penjualan': {
        'id': ['HP01', 'AS02'],
        'merk': ['HP', 'Acer'],
        'tipe': ['Pavilion', 'Swift'],
        'jumlah': [6, 5],
        'harga': [10500000, 7500000],
        'serial': [
            ['HP01-001', 'HP01-002', 'HP01-003', 'HP01-004', 'HP01-005', 'HP01-006'],
            ['AS02-001', 'AS02-002', 'AS02-003', 'AS02-004', 'AS02-005']
        ]
    },
    'stok': {
        'id': ['HP01', 'AS02', 'LT03'],
        'merk': ['HP', 'Acer', 'Lenovo'],
        'tipe': ['Pavilion', 'Swift', 'Thinkpad'],
        'jumlah': [4, 3, 12],  
        'serial': [
            ['HP01-007', 'HP01-008', 'HP01-009', 'HP01-010'],
            ['AS02-006', 'AS02-007', 'AS02-008'],
            ['LT03-001', 'LT03-002', 'LT03-003', 'LT03-004', 'LT03-005', 'LT03-006', 'LT03-007', 'LT03-008', 'LT03-009', 'LT03-010', 'LT03-011', 'LT03-012']
        ]
    }
}


def menu(tinjau):
    dictLaptopNew = []
    for i in range (len(dictLaptop[tinjau]['id'])):
        if tinjau=='stok':
            dictLaptopNew.append([i,dictLaptop[tinjau]['id'][i],dictLaptop[tinjau]['merk'][i],dictLaptop[tinjau]['tipe'][i],dictLaptop[tinjau]['jumlah'][i]])
        else:
            dictLaptopNew.append([i,dictLaptop[tinjau]['id'][i],dictLaptop[tinjau]['merk'][i],dictLaptop[tinjau]['tipe'][i],dictLaptop[tinjau]['jumlah'][i],dictLaptop[tinjau]['harga'][i]])
    if tinjau =='stok':
        header = ['Index','Id','Merk','Tipe','Jumlah_Stok']
    else:
        header = ['Index','Id','Merk','Tipe','Jumlah','Harga']
    print('-'*20,f'DATA {tinjau.upper()}','-'*20)
    print(tabulate(dictLaptopNew,headers=header,tablefmt='fancy_grid',))
    return
def detail(index,tinjauan):
    index = int(index)
    detail = []
    for i in range (len(dictLaptop[tinjauan]['serial'][index])):
        detail.append([i+1,dictLaptop[tinjauan]['serial'][index][i]])
    print(tabulate(detail,headers=['No','Serial Num'],tablefmt='fancy_grid'))
        
def tampilan_menu():
    print('*'*25)
    print('''## Anda masuk kedalam bagian TAMPILAN. Pilih bagian yang ingin ditinjau
1. DATA PEMBELIAN
2. DATA PENJUALAN
3. DATA STOK
4. KEMBALI KE TAMPILAN AWAL
          ''')
    
    pilihan_menu = int(input('Pilih Nomor data yang ingin ditinjau : '))
    print('*'*25)
    if pilihan_menu>0 and pilihan_menu<=3:
        if pilihan_menu ==1:
            peninjauan = 'pembelian'
        elif pilihan_menu ==2:
            peninjauan = 'penjualan'
        else:
            peninjauan = 'stok'
        menu(peninjauan)

        index = input('Masukkan index yang ingin ditinjau : ')
        if index.isdigit():
            detail(index,peninjauan)
        else:
            return tampilan_menu()
    elif pilihan_menu==4:
        return
    else:
        print('Data does not exist')
        return        


def menambah_data():
    print('*'*25)
    print('## Anda masuk kedalam bagian TAMBAH. ketik "Tidak" untuk membatalkan')
    pilihan_tambah = input('Apakah anda ingin menambahkan data (ya/tidak) ? ').lower()
    if pilihan_tambah == 'tidak':
        return 
    else:
        print('''
Pilihan Penambahan data:
1. Pembelian
2. Penjualan
''')    
        penambahan = input('Masukkan tipe penambahan pilihan anda (pembelian/penjualan) : ').lower()
        menu(penambahan)
        opsi = input('\nApakah anda mau menambahkan jenis laptop baru (ya/tidak) ? ').lower()
        if opsi == 'ya':
            print('\n ***** STOK DALAM GUDANG *****')
            menu('stok')
            print('*'*25)
            id = input('Masukkan Id :').upper()

            if penambahan =='penjualan':
                indx = dictLaptop['stok']['id'].index(id)
                if id in dictLaptop['stok']['id']:
                    print('ID Ditemukan....')
                else:
                    print('Item tidak ada di STOK !!!')
                    return menambah_data()
            
            if id in dictLaptop[penambahan]['id']:
                print('ID Sudah digunakan! Gunakan ID lain ')
                return
            else:
                if penambahan =='penjualan':
                    merk = dictLaptop['stok']['merk'][indx]
                    tipe = dictLaptop['stok']['tipe'][indx]
                    kuantitas = int(input(f'Masukkan Jumlah {penambahan} : '))
                    while kuantitas > dictLaptop['stok']['jumlah'][indx]:
                        print('\nJumlah melebihi stok !!!!!')
                        kuantitas = int(input(f'\nMasukkan Jumlah {penambahan} : '))
                    harga = int(input('Masukkan Harga Satuan Laptop : '))
                    detail(indx,'stok')
                else:
                    merk = input('Masukkan Merk : ').upper()
                    tipe = input('Masukkan Tipe : ').upper()
                    kuantitas = int(input(f'Masukkan Jumlah {penambahan} : '))               
                    harga = int(input('Masukkan Harga Satuan Laptop : '))
            print('-'*15)
            no_seri=[]
            for i in range (kuantitas):
                seri = input(f'Masukkan angka serial {penambahan} ke {i+1} : ')
                no_seri.append(id+'-'+seri)
            save_data = input('SAVE DATA (ya/tidak) ? ').lower()
            if save_data == 'tidak':
                return menambah_data()
            else:
                dictLaptop[penambahan]['id'].append(id)
                dictLaptop[penambahan]['merk'].append(merk)
                dictLaptop[penambahan]['tipe'].append(tipe)
                dictLaptop[penambahan]['jumlah'].append(kuantitas)
                dictLaptop[penambahan]['harga'].append(harga)
                print('-'*15)
                dictLaptop[penambahan]['serial'].append(no_seri)
                print('*'*25)
                list_penambahan = [] 
                for value in [id,merk,tipe,kuantitas,no_seri]:
                    list_penambahan.append(value)

                #Penambahan bagian stok karena adanya pertambahan pembelian
                if penambahan == 'pembelian':
                    i=0
                    for keys,val in dictLaptop['stok'].items():
                        dictLaptop['stok'][keys].append(list_penambahan[i])
                        i+=1
                    return menambah_data()
                else:
                    idx = dictLaptop['stok']['id'].index(id)
                    dictLaptop['stok']['jumlah'][idx] = dictLaptop['stok']['jumlah'][idx] - kuantitas
                    dictLaptop['stok']['serial'][idx] = list(set(dictLaptop['stok']['serial'][idx]) - set(no_seri))
                    return menambah_data()
        elif opsi == 'tidak':
            menu(penambahan)
            return menambah_data()


def sub_pilihan_edit(edit,keys,pilihan_edit):
    
    if type(dictLaptop[edit][keys][pilihan_edit]) != int:
        nilai = input(f'Masukkan {keys} Baru : ')
        if keys == 'id':
            nilai = nilai.upper()
        else:
            nilai = nilai.title()
        save_data = save_data = input('SAVE DATA (ya/tidak) ? ').lower()
        if save_data == 'tidak':
            return edit_data()
        else:
            dictLaptop[edit][keys][pilihan_edit] = nilai
            if edit == 'pembelian':
                dictLaptop['stok'][keys][pilihan_edit] = dictLaptop[edit][keys][pilihan_edit]
            else:
                dictLaptop['stok'][keys][pilihan_edit] = dictLaptop[edit][keys][pilihan_edit]
            print('Data Tersimpan! ')
            menu(edit)
            lanjut = input('Edit data lagi di index yang sama (ya/tidak)?').lower()
            if lanjut=='tidak':
                return edit_data()
            else:
                key = input('Masukkan nama kolom yang mau diedit : ').lower()
                # print(edit, key,pilihan_edit)
                return sub_pilihan_edit(edit,key,pilihan_edit)
    else :
        if keys == 'harga':
            nilai = int(input(f'Masukkan {keys} Baru : '))
        else: 
            nilai = int(input(f'Masukkan penambahan {keys} : '))
        save_data = save_data = input('SAVE DATA (ya/tidak) ? ').lower()
        if save_data == 'tidak':
            return edit_data()
        else:
            detail(pilihan_edit,edit)
            dictLaptop[edit][keys][pilihan_edit] = nilai
            if edit == 'pembelian' or edit == 'penjualan' and keys =='jumlah':
                list_penambahan_noseri = [] 
                for i in range (nilai):
                    seri = input(f'Masukkan angka serial {edit} ke {i+1}  : ')
                    list_penambahan_noseri.append(seri)
                if edit == 'pembelian':
                    dictLaptop[edit][keys][pilihan_edit] = dictLaptop[edit][keys][pilihan_edit] + nilai
                    dictLaptop['stok'][keys][pilihan_edit] = dictLaptop['stok'][keys][pilihan_edit] + nilai
                    dictLaptop['stok']['serial'][pilihan_edit].extend(list_penambahan_noseri)
                else:
                    dictLaptop[edit][keys][pilihan_edit] = dictLaptop[edit][keys][pilihan_edit] - nilai
                    dictLaptop['stok'][keys][pilihan_edit] = dictLaptop['stok'][keys][pilihan_edit] - nilai
                    dictLaptop['stok']['serial'][pilihan_edit] = list(set(dictLaptop['stok']['serial'][pilihan_edit]) - set(list_penambahan_noseri))
            else:
                dictLaptop['stok'][keys][pilihan_edit] = dictLaptop[edit][keys][pilihan_edit]
            lanjut = input('Edit data lagi di index yang sama (ya/tidak)?').lower()
            if lanjut=='tidak':
                return edit_data()
            else:
                key = input('Masukkan nama kolom yang mau diedit : ').lower()
                # print(edit, key,pilihan_edit)
                return sub_pilihan_edit(edit,key,pilihan_edit)

        
def edit_data():
    print('*'*25)
    print('## Anda masuk kedalam bagian EDIT. ketik "Tidak" untuk membatalkan')

    #####PERLU DILANJUTIN LAGI OKEE, BARU NAMBAHIN YG PRINT DIATS
    pilihan_edit = input('Apakah anda ingin mengEDIT data (ya/tidak)?: ').lower()
    if pilihan_edit == 'tidak':
        return
    else:
        print('''Pilihan Edit data:
1. Pembelian
2. Penjualan
''')    
        edit = input('Masukkan tipe edit pilihan anda (pembelian/penjualan) : ').lower()
        menu(edit)
        opsi = input('\nMasukkan No index yang ingin anda edit : ').lower()
        if opsi.isdigit():
            opsi = int(opsi)
            if opsi<=len(dictLaptop[edit]['id']) and opsi>=0:
                keys = input('Masukkan nama kolom yang ingin diedit :').lower()
                if keys in dictLaptop[edit]:
                    sub_pilihan_edit(edit,keys,opsi)
                else :
                    print('Nama kolom tidak tersedia !!!!')
                return edit_data()

            else :
                print('Input Anda Tidak Valid ! Anda akan dilempar ke halaman utama')
                return
        else:
            print('Input Anda Tidak Valid ! Anda akan dilempar ke halaman utama')
            return edit_data()
        

def hapus_data():
    print('*'*25)
    print('## Anda masuk kedalam bagian HAPUS. ketik "Tidak" untuk membatalkan')
    print('''Pilihan HAPUS data:
1. Pembelian
2. Penjualan
3. Stok
4. Exit
''') 
    pilihan_hapus = input('Masukkan Bagian yang ingin dihapus (Pembelian/Penjualan/Stok/Exit): ').lower()
    if pilihan_hapus == 'exit':
        return
    else:
        menu(pilihan_hapus)
        hapus = input('Masukkan Index yang ingin dihapus : ').lower()
        if hapus.isdigit():
            hapus = int(hapus)
            if hapus<len(dictLaptop[pilihan_hapus]['id']) and hapus>=0:
                verifikasi = input('\nApakah anda yakin ingin mengHAPUS data tersebut (ya/tidak)?').lower()
                if verifikasi == 'tidak':
                    return hapus_data()
                else:
                    for keys in dictLaptop[pilihan_hapus]:  
                        del dictLaptop[pilihan_hapus][keys][hapus]
                    print('\n')
                    print(f'***  Tampilan Menu {pilihan_hapus.capitalize()} Terbaru ***')
                    menu(pilihan_hapus)
                    return hapus_data()
            else:
                print('Input Anda Tidak Valid ! DATA tidak ditemukan ')
                return hapus_data()
        else:
            print('Input Anda Tidak Valid ! Data tidak ditemukan ')
            return hapus_data()

def menu_awal():
    print('''
List Menu :
1. Menampilkan daftar pembelian/penjualan/stok laptop
2. Menambah data 
3. Mengedit data 
4. Menghapus data 
5. Keluar sistem
''')

while True:
    print('*'*25)
    menu_awal()
    pilihan = int(input('Masukkan Pilihan Anda : '))
    if pilihan == 1:
        tampilan_menu()
    elif pilihan == 2:
        menambah_data()
    elif pilihan == 3:
        edit_data()
    elif pilihan == 4:
        hapus_data()
    elif pilihan == 5:
        print('\n----------Terimakasih----------')
        break
    else :
        print('Angka tidak valid')

