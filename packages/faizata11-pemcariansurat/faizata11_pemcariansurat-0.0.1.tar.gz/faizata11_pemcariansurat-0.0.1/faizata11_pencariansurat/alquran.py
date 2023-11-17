surah_list = [
    {"nama": "Al-Fatihah", "nomor": "1", "asma": "الفاتحة", "ayat": 7},
    {"nama": "Al-Baqarah", "nomor": "2", "asma": "البقرة", "ayat": 286},
    {"nama": "Aali Imran", "nomor": "3", "asma": "آل عمران", "ayat": 200},
    {"nama": "An-Nisa", "nomor": "4", "asma": "النساء", "ayat": 176},
    {"nama": "Al-Ma'idah", "nomor": "5", "asma": "المائدة", "ayat": 120},
    {"nama": "Al-An'am", "nomor": "6", "asma": "الأنعام", "ayat": 165},
    {"nama": "Al-A'raf", "nomor": "7", "asma": "الأعراف", "ayat": 206},
    {"nama": "Al-Anfal", "nomor": "8", "asma": "الأنفال", "ayat": 75},
    {"nama": "At-Taubah", "nomor": "9", "asma": "التوبة", "ayat": 129},
    {"nama": "Yunus", "nomor": "10", "asma": "يونس", "ayat": 109},
    {"nama": "Hud", "nomor": "11", "asma": "هود", "ayat": 123},
    {"nama": "Yusuf", "nomor": "12", "asma": "يوسف", "ayat": 111},
    {"nama": "Ar-Ra'd", "nomor": "13", "asma": "الرعد", "ayat": 43},
    {"nama": "Ibrahim", "nomor": "14", "asma": "إبراهيم", "ayat": 52},
    {"nama": "Al-Hijr", "nomor": "15", "asma": "الحجر", "ayat": 99},
    {"nama": "An-Nahl", "nomor": "16", "asma": "النحل", "ayat": 128},
    {"nama": "Al-Isra'", "nomor": "17", "asma": "الإسراء", "ayat": 111},
    {"nama": "Al-Kahf", "nomor": "18", "asma": "الكهف", "ayat": 110},
    {"nama": "Maryam", "nomor": "19", "asma": "مريم", "ayat": 98},
    {"nama": "Ta Ha", "nomor": "20", "asma": "طه", "ayat": 135},
    {"nama": "Al-Anbiya", "nomor": "21", "asma": "الأنبياء", "ayat": 112},
    {"nama": "Al-Hajj", "nomor": "22", "asma": "الحج", "ayat": 78},
    {"nama": "Al-Mu'minun", "nomor": "23", "asma": "المؤمنون", "ayat": 118},
    {"nama": "An-Nur", "nomor": "24", "asma": "النور", "ayat": 64},
    {"nama": "Al-Furqan", "nomor": "25", "asma": "الفرقان", "ayat": 77},
    {"nama": "Asy-Syu'ara'", "nomor": "26", "asma": "الشعراء", "ayat": 227},
    {"nama": "An-Naml", "nomor": "27", "asma": "النمل", "ayat": 93},
    {"nama": "Al-Qasas", "nomor": "28", "asma": "القصص", "ayat": 88},
    {"nama": "Al-Ankabut", "nomor": "29", "asma": "العنكبوت", "ayat": 69},
    {"nama": "Ar-Rum", "nomor": "30", "asma": "الروم", "ayat": 60},
    {"nama": "Luqman", "nomor": "31", "asma": "لقمان", "ayat": 34},
    {"nama": "As-Sajdah", "nomor": "32", "asma": "السجدة", "ayat": 30},
    {"nama": "Al-Ahzab", "nomor": "33", "asma": "الأحزاب", "ayat": 73},
    {"nama": "Saba'", "nomor": "34", "asma": "سبأ", "ayat": 54},
    {"nama": "Fatir", "nomor": "35", "asma": "فاطر", "ayat": 45},
    {"nama": "Ya Sin", "nomor": "36", "asma": "يس", "ayat": 83},
    {"nama": "As-Saffat", "nomor": "37", "asma": "الصافات", "ayat": 182},
    {"nama": "Sad", "nomor": "38", "asma": "ص", "ayat": 88},
    {"nama": "Az-Zumar", "nomor": "39", "asma": "الزمر", "ayat": 75},
    {"nama": "Ghafir", "nomor": "40", "asma": "غافر", "ayat": 85},
    {"nama": "Fussilat", "nomor": "41", "asma": "فصلت", "ayat": 54},
    {"nama": "Asy-Syura", "nomor": "42", "asma": "الشورى", "ayat": 53},
    {"nama": "Az-Zukhruf", "nomor": "43", "asma": "الزخرف", "ayat": 89},
    {"nama": "Ad-Dukhan", "nomor": "44", "asma": "الدخان", "ayat": 59},
    {"nama": "Al-Jasiyah", "nomor": "45", "asma": "الجاثية", "ayat": 37},
    {"nama": "Al-Ahqaf", "nomor": "46", "asma": "الأحقاف", "ayat": 35},
    {"nama": "Muhammad", "nomor": "47", "asma": "محمد", "ayat": 38},
    {"nama": "Al-Fath", "nomor": "48", "asma": "الفتح", "ayat": 29},
    {"nama": "Al-Hujurat", "nomor": "49", "asma": "الحجرات", "ayat": 18},
    {"nama": "Qaf", "nomor": "50", "asma": "ق", "ayat": 45},
    {"nama": "Az-Zariyat", "nomor": "51", "asma": "الذاريات", "ayat": 60},
    {"nama": "At-Tur", "nomor": "52", "asma": "الطور", "ayat": 49},
    {"nama": "An-Najm", "nomor": "53", "asma": "النجم", "ayat": 62},
    {"nama": "Al-Qamar", "nomor": "54", "asma": "القمر", "ayat": 55},
    {"nama": "Ar-Rahman", "nomor": "55", "asma": "الرحمن", "ayat": 78},
    {"nama": "Al-Waqi'ah", "nomor": "56", "asma": "الواقعة", "ayat": 96},
    {"nama": "Al-Hadid", "nomor": "57", "asma": "الحديد", "ayat": 29},
    {"nama": "Al-Mujadilah", "nomor": "58", "asma": "المجادلة", "ayat": 22},
    {"nama": "Al-Hasyr", "nomor": "59", "asma": "الحشر", "ayat": 24},
    {"nama": "Al-Mumtahanah", "nomor": "60", "asma": "الممتحنة", "ayat": 13},
    {"nama": "As-Saff", "nomor": "61", "asma": "الصف", "ayat": 14},
    {"nama": "Al-Jumu'ah", "nomor": "62", "asma": "الجمعة", "ayat": 11},
    {"nama": "Al-Munafiqun", "nomor": "63", "asma": "المنافقون", "ayat": 11},
    {"nama": "At-Tagabun", "nomor": "64", "asma": "التغابن", "ayat": 18},
    {"nama": "At-Talaq", "nomor": "65", "asma": "الطلاق", "ayat": 12},
    {"nama": "At-Tahrim", "nomor": "66", "asma": "التحريم", "ayat": 12},
    {"nama": "Al-Mulk", "nomor": "67", "asma": "الملك", "ayat": 30},
    {"nama": "Al-Qalam", "nomor": "68", "asma": "القلم", "ayat": 52},
    {"nama": "Al-Haaqqah", "nomor": "69", "asma": "الحاقة", "ayat": 52},
    {"nama": "Al-Ma'arij", "nomor": "70", "asma": "المعارج", "ayat": 44},
    {"nama": "Nuh", "nomor": "71", "asma": "نوح", "ayat": 28},
    {"nama": "Al-Jinn", "nomor": "72", "asma": "الجن", "ayat": 28},
    {"nama": "Al-Muzzammil", "nomor": "73", "asma": "المزمل", "ayat": 20},
    {"nama": "Al-Muddassir", "nomor": "74", "asma": "المدثر", "ayat": 56},
    {"nama": "Al-Qiyamah", "nomor": "75", "asma": "القيامة", "ayat": 40},
    {"nama": "Al-Insan", "nomor": "76", "asma": "الإنسان", "ayat": 31},
    {"nama": "Al-Mursalat", "nomor": "77", "asma": "المرسلات", "ayat": 50},
    {"nama": "An-Naba'", "nomor": "78", "asma": "النبأ", "ayat": 40},
    {"nama": "An-Nazi'at", "nomor": "79", "asma": "النازعات", "ayat": 46},
    {"nama": "'Abasa", "nomor": "80", "asma": "عبس", "ayat": 42},
    {"nama": "At-Takwir", "nomor": "81", "asma": "التكوير", "ayat": 29},
    {"nama": "Al-Infitar", "nomor": "82", "asma": "الإنفطار", "ayat": 19},
    {"nama": "Al-Tatfif", "nomor": "83", "asma": "التطفيف", "ayat": 36},
    {"nama": "Al-Insyiqaq", "nomor": "84", "asma": "الإنشقاق", "ayat": 25},
    {"nama": "Al-Buruj", "nomor": "85", "asma": "البروج", "ayat": 22},
    {"nama": "At-Tariq", "nomor": "86", "asma": "الطارق", "ayat": 17},
    {"nama": "Al-A'la", "nomor": "87", "asma": "الأعلى", "ayat": 19},
    {"nama": "Al-Gasyiyah", "nomor": "88", "asma": "الغاشية", "ayat": 26},
    {"nama": "Al-Fajr", "nomor": "89", "asma": "الفجر", "ayat": 30},
    {"nama": "Al-Balad", "nomor": "90", "asma": "البلد", "ayat": 20},
    {"nama": "Asy-Syams", "nomor": "91", "asma": "الشمس", "ayat": 15},
    {"nama": "Al-Lail", "nomor": "92", "asma": "الليل", "ayat": 21},
    {"nama": "Ad-Duha", "nomor": "93", "asma": "الضحى", "ayat": 11},
    {"nama": "Al-Insyirah", "nomor": "94", "asma": "الشرح", "ayat": 8},
    {"nama": "At-Tin", "nomor": "95", "asma": "التين", "ayat": 8},
    {"nama": "Al-'Alaq", "nomor": "96", "asma": "العلق", "ayat": 19},
    {"nama": "Al-Qadr", "nomor": "97", "asma": "القدر", "ayat": 5},
    {"nama": "Al-Bayyinah", "nomor": "98", "asma": "البينة", "ayat": 8},
    {"nama": "Az-Zalzalah", "nomor": "99", "asma": "الزلزلة", "ayat": 8},
    {"nama": "Al-'Adiyat", "nomor": "100", "asma": "العاديات", "ayat": 11},
    {"nama": "Al-Qari'ah", "nomor": "101", "asma": "القارعة", "ayat": 11},
    {"nama": "At-Takasur", "nomor": "102", "asma": "التكاثر", "ayat": 8},
    {"nama": "Al-'Asr", "nomor": "103", "asma": "العصر", "ayat": 3},
    {"nama": "Al-Humazah", "nomor": "104", "asma": "الهمزة", "ayat": 9},
    {"nama": "Al-Fil", "nomor": "105", "asma": "الفيل", "ayat": 5},
    {"nama": "Quraisy", "nomor": "106", "asma": "قريش", "ayat": 4},
    {"nama": "Al-Ma'un", "nomor": "107", "asma": "الماعون", "ayat": 7},
    {"nama": "Al-Kausar", "nomor": "108", "asma": "الكوثر", "ayat": 3},
    {"nama": "Al-Kafirun", "nomor": "109", "asma": "الكافرون", "ayat": 6},
    {"nama": "An-Nasr", "nomor": "110", "asma": "النصر", "ayat": 3},
    {"nama": "Al-Lahab", "nomor": "111", "asma": "اللهب", "ayat": 5},
    {"nama": "Al-Ikhlas", "nomor": "112", "asma": "الإخلاص", "ayat": 4},
    {"nama": "Al-Falaq", "nomor": "113", "asma": "الفلق", "ayat": 5},
    {"nama": "An-Nas", "nomor": "114", "asma": "الناس", "ayat": 6},
]
def get_surah_info():
    input_type = input("Pilih jenis input (nama/nomor): ")

    if input_type == "nama":
        nama_surat = input("Masukkan nama surah: ").strip()
        for surah in surah_list:
            if surah["nama"].replace("-", "").lower() == nama_surat.lower():
                print_surah_info(surah)
                return
        print("Surah dengan nama '{}' tidak ditemukan.".format(nama_surat))

    elif input_type == "nomor":
        max_surah_number = max(int(surah["nomor"]) for surah in surah_list)
        nomor_surah = int(input("Masukkan nomor surah: "))
        if 1 <= nomor_surah <= max_surah_number:
            for surah in surah_list:
                if surah["nomor"] == str(nomor_surah):
                    print_surah_info(surah)
                    return
            print("Surah dengan nomor '{}' tidak ditemukan.".format(nomor_surah))
        else:
            print("Nomor surah tidak valid.")

    else:
        print("Jenis input tidak valid. Pilih 'nama' atau 'nomor'.")

def print_surah_info(surah):
    print("Informasi Surah:")
    print("Nama Surah:", surah["nama"])
    print("Nomor Surah:", surah["nomor"])
    print("Asma Surah:", surah["asma"])
    print("Jumlah Ayat:", surah["ayat"])

# Example usage:
get_surah_info()
