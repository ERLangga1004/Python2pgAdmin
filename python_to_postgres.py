import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'data_mhs'
username = 'postgres'
pwd = '100403'
port_id = 5432


def create_table():
    try:
        with psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute('DROP TABLE IF EXISTS data_mhs')
                create_script = ''' CREATE TABLE IF NOT EXISTS data_mhs (
                                        id      SERIAL PRIMARY KEY,
                                        nama    VARCHAR(40) NOT  NULL,
                                        asal    VARCHAR(50))'''
                cur.execute(create_script) 
                print("Table berhasil dibuat!")          
    except Exception as error:
        print(f'Gagal membuat table: {error}')


def insert_data(nama, asal):
    try:
        with psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                insert_script = 'INSERT INTO data_mhs (nama, asal) VALUES (%s, %s)'
                cur.execute(insert_script, (nama, asal))
                conn.commit()
                print(f'Data berhasil diinsert: Nama: {nama}, Asal: {asal}')
    except Exception as error:
        print(f'Gagal Insert Data!: {error}')


def read_data():
    try:
        with psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute('SELECT * FROM data_mhs')
                records = cur.fetchall()
                return records
    except Exception as error:
        print(f'Gagal menampilkan data: {error}')
        return []
    

def update_data(id, nama, asal):
    try:    
        with psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                update_script = 'UPDATE data_mhs SET nama = %s, asal = %s WHERE id = %s'
                cur.execute(update_script, (nama, asal, id))
                conn.commit()
                print(f'Data berhasil diupdate')
    except Exception as error:
        print(f'Gagal mengupdate data: {error}')

def delete_data(nama):
    try:
        with psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                delete_script = 'DELETE FROM data_mhs WHERE nama = %s'
                cur.execute(delete_script, (nama,))
                conn.commit()
                print(f'Data berhasil dihapus')
    except Exception as error:
        print(f'Gagal Menghapus data: {error}')

def menu():
    while True:
        print("\nMenu:")
        print("1. Insert Data")
        print("2. Tampilkan Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Keluar")
        menu = input("Pilih Menu (1-5): ")

        if menu == '1':
                nama = input("Masukan Nama: ")
                asal = input("Masukan Asal: ")
                insert_data(nama, asal)

        elif menu == '2':
            data = read_data()
            if data:
                for record in data:
                    print(f"ID: {record['id']}, Nama: {record['nama']}, {record['asal']}")
            else:
                print("Tidak ada data untuk ditampilkan!")

        elif menu == '3':
            try:
                id = int(input("Masukan ID: "))
                nama = input("Masukan Nama Baru: ")
                asal = input("Masukan Asal Baru: ")
                update_data(id, nama, asal)
            except ValueError:
                print("ID harus berupa angka.")

        elif menu == '4':
            nama = input("Masukan Nama yang akan dihapus")
            delete_data(nama)

        elif menu == '5':
            break
        
        else:
            print("Pilihan tidak valid. Silahkan coba lagi")
    
if __name__ == '__main__':
    create_table()
    menu()