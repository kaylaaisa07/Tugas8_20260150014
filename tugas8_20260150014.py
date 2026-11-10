import modul_sensor

# Struktur data utama: list kosong berisi tuple (suhu, kelembaban)
log_kebun = []


def input_sensor():
    """Meminta input suhu & kelembaban secara aman.
    Mengembalikan tuple (suhu, kelembaban)."""
    while True:
        try:
            suhu = float(input("Masukkan Suhu Udara (C) [0-100]: "))
            lembab = float(input("Masukkan Kelembaban Tanah (%) [0-100]: "))

            if 0 <= suhu <= 100 and 0 <= lembab <= 100:
                return (suhu, lembab)
            else:
                print("Error: Suhu dan kelembaban harus di rentang 0-100!\n")
        except ValueError:
            print("Error: Input harus berupa angka, bukan huruf!\n")


def rekam_data():
    data = input_sensor()
    log_kebun.append(data)
    print(f"Data berhasil direkam: Suhu={data[0]} C, Lembab={data[1]} %")


def analisis_tren():
    if len(log_kebun) == 0:
        print("Belum ada data. Silakan rekam data terlebih dahulu (menu 1).")
        return

    # Slicing: maksimal 3 data terakhir
    data_terakhir = log_kebun[-3:]

    print(f"\nLokasi: {modul_sensor.LOKASI[0]} "
          f"({modul_sensor.LOKASI[1]}, {modul_sensor.LOKASI[2]})")
    print(f"--- {len(data_terakhir)} Data Terakhir ---")
    for i, (suhu, lembab) in enumerate(data_terakhir, start=1):
        print(f"Data {i}: Suhu = {suhu} C | Kelembaban = {lembab} %")

    rata_suhu, rata_lembab = modul_sensor.hitung_tren(data_terakhir)
    status = modul_sensor.evaluasi_irigasi(
        rata_suhu, rata_lembab, modul_sensor.AMBANG_KRITIS
    )

    print(f"\nRata-rata Suhu       : {rata_suhu:.2f} C")
    print(f"Rata-rata Kelembaban : {rata_lembab:.2f} %")
    print(f"Status               : {status}")


def main():
    while True:
        print("\n=== SISTEM MONITORING IoT KAMPUNG ANGGUR ===")
        print("[1] Rekam Data")
        print("[2] Analisis Tren (3 Terakhir)")
        print("[3] Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            rekam_data()
        elif pilihan == "2":
            analisis_tren()
        elif pilihan == "3":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid, pilih 1, 2, atau 3.")


main()
