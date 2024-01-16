# 1. Data
flight_list = ['A1', '1B','2A','2B','3A','3B']
ticket_type = {'A1': 5000,'1B':5000, '2A':75000, '3A': 100000,'3B':100000}
booked_seats = {}

def penjualan_tiket_pesawat():
    for seat in flight_list:
        booked_seats[seat] = 0

    while True:
        print("\nMenu:")
        print("1. Lihat Daftar Tiket Tersedia")
        print("2. Beli Tiket")
        print("3. Lihat Jumlah Penumpang Yang Sudah Di Pesankan")
        print("4. Hapus Jumlah Penumpang Yang Di Pesankan")
        print("5. Exit")
        pilihan = int(input("Silakan Masukkan Pilihan Anda: "))

        if pilihan == 1:
            print("\nDaftar Tiket Tersedia:")
            for seat, booked in booked_seats.items():
                print(f"{seat}: {ticket_type[seat] - booked} tiket tersisa")

        elif pilihan == 2:
            seat_number = input("masukkan nomor kursi (misal 1A): ")
            if seat_number in flight_list:
                seat_type = seat_number[:1]
                number_of_tickets = int(input(f"masukkan jumlah tiket yang ingin di beli (max {ticket_type[seat_number] - booked_seats[seat_number]} tiket): "))
            if number_of_tickets <= ticket_type[seat_number]-booked_seats[seat]:
                booked_seats[seat_number] += number_of_tickets
                print(f"f Anda telah berhasil membeli {number_of_tickets} tiket {seat_type}")
            else:
                print(f"Maaf, nomor kursi {seat_number} tidak tersedia")

        elif pilihan == 3:
            print("\nJumlah penumpang yang sudah di pesankan:")
            for seat, booked in booked_seats.items():
                print(f"f{seat}: {booked} penumpang")

        elif pilihan == 4:
            seat_number = input("Masukkan nomor kursi (misal A1): ")
            for seat_number in flight_list:
                booked_seats[seat_number] = 0
                print(f"jumlah penumpang yang sudah di pesankan untuk nomor kursi {seat_number} telah di hapus")
            else:
                print(f"Maaf , nomor kursi {seat_number} tidak tersedia")

        elif pilihan == 5:
            print("Terima Kasih telah menggunakan  aplikasi ini!")
            break
        else:
            print("pilihan Anda tidak valid, silakan coba lagi")