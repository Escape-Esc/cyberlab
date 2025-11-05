
print("      =====AI BY : ESCAPE=====")
print("       ______your hope_______")
print("              v 0.01")



# Script AI sederhana

def ai_harapan(pertanyaan):
    pertanyaan = pertanyaan.lower()
    if "aku ingin dia" in pertanyaan:
        return "Jika sesuatu yang kamu harapkan tidak dapat dimiliki. Maka jawabanya besok, mungkin lusa. Bisa jadi tahun depan"
    else:
        return " Kamu punya harapan?"

# Program utama
print("        === MINI PROGRAM ===")
while True:
    user_input = input("Kamu: ")
    if user_input.lower() in ["exit", "keluar", "quit"]:
        print("AI: Sampai jumpa, ingat. Dirimu adalah harapan terbaik, hari ini gagal? masih ada besok dan tahun depan. hahahaha")
        break
    jawaban = ai_harapan(user_input)
    print("AI:", jawaban)
