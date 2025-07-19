import streamlit as st import random

# ========== DATA PENGERTIAN ESTER MOON ==========
pengertian_estermoon = [
   {Ester Moon adalah aplikasi web yang bergerak dalam menyediakan bahan ajar berupa kumpulan materi praktikum analisis titrimetri dan kimia organik. Materi praktikum yang tersedia merupakan materi dasar yang dapat mengasah skill analis dalam bidang analitik. Selain materi praktikum, aplikasi web ini menyediakan fitur berupa kalkulator perhitungan konsentrasi dan normalitas larutan untuk standardisasi. Dengan adanya aplikasi web ini analis akan lebih mudah dalam mengakses bahan ajar praktikum, karena bahan ajar yang tersedia sangat fleksibel dan bisa diakses kapan saja.}
]

# ========== DATA PENGERTIAN GOLONGAN SENYAWA ==========
pengertian_senyawa = [
    {"Golongan": "Hidrokarbon", "Pengertian": "Senyawa organik yang hanya terdiri dari karbon (C) dan hidrogen (H). Dibagi menjadi: Alkana (jenuh), Alkena (tak jenuh dengan ikatan rangkap dua), Alkuna (ikatan rangkap tiga), Aromatik (cincin benzena)."},
    {"Golongan": "Alkohol Primer", "Pengertian": "OH terikat pada karbon yang hanya terhubung ke satu atom C lain (contoh: etanol)."},
    {"Golongan": "Alkohol Sekunder", "Pengertian": "OH terikat pada karbon yang terhubung ke dua atom C lain (contoh: isopropanol)."},
    {"Golongan": "Alkohol Tersier", "Pengertian": "OH terikat pada karbon yang terhubung ke tiga atom C lain (contoh: tert-butanol)."},
    {"Golongan": "Fenol", "Pengertian": "Senyawa aromatik dengan gugus -OH langsung terikat pada cincin benzena. Lebih asam dari alkohol biasa."},
    {"Golongan": "Eter", "Pengertian": "Senyawa dengan struktur R-O-R′, di mana R dan R′ adalah gugus alkil atau aril. Tidak memiliki gugus -OH bebas."},
    {"Golongan": "Aldehida", "Pengertian": "Mengandung gugus karbonil (C=O) di ujung rantai karbon, yaitu -CHO. Contoh: formaldehida."},
    {"Golongan": "Keton", "Pengertian": "Mengandung gugus karbonil (C=O) di tengah rantai karbon, bukan di ujung. Contoh: aseton."},
    {"Golongan": "Karbohidrat", "Pengertian": "Senyawa organik dengan rumus umum Cₙ(H₂O)ₙ. Contoh: glukosa, fruktosa. Sumber energi."},
    {"Golongan": "Asam Karboksilat", "Pengertian": "Mengandung gugus -COOH. Bersifat asam dan dapat membentuk garam atau ester. Contoh: asam asetat."},
    {"Golongan": "Amina Primer", "Pengertian": "Satu gugus alkil/aril terikat pada nitrogen (R-NH₂)."},
    {"Golongan": "Amina Sekunder", "Pengertian": "Dua gugus alkil/aril terikat pada nitrogen (R₂NH)."},
    {"Golongan": "Amina Tersier", "Pengertian": "Tiga gugus alkil/aril terikat pada nitrogen (R₃N)."},
    {"Golongan": "Amina", "Pengertian": "Senyawa yang mengandung atom nitrogen dengan gugus alkil/aril."},
    {"Golongan": "Protein", "Pengertian": "Polimer asam amino dengan ikatan peptida. Fungsi: enzim, transport, struktural, dsb."},
    {"Golongan": "Lemak & Minyak", "Pengertian": "Lemak: padat pada suhu ruang (dari hewan). Minyak: cair pada suhu ruang (dari tumbuhan). Cadangan energi."},
]

# ========== DATA UJI SENYAWA ==========
senyawa_data = {
    "Hidrokarbon": [
        {"Nama Uji": "Uji Pembakaran", "Hasil Positif": "Nyala kuning berasap", "Keterangan": "Aromatik"},
        {"Nama Uji": "Uji Bromin", "Hasil Positif": "Warna hilang", "Keterangan": "Adisi ikatan rangkap"},
        {"Nama Uji": "Uji Baeyer", "Hasil Positif": "Ungu hilang jadi coklat", "Keterangan": "Ikatan rangkap"},
    ],
    "Alkohol Primer": [
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Tidak keruh / lambat", "Keterangan": "Reaksi lambat"},
        {"Nama Uji": "Uji Kromik (Jones)", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi → asam karboksilat"},
        {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"},
    ],
    "Alkohol Sekunder": [
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Keruh sedang (~5 menit)", "Keterangan": "Reaksi sedang"},
        {"Nama Uji": "Uji Kromik", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi → keton"},
        {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"},
    ],
    "Alkohol Tersier": [
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Cepat keruh", "Keterangan": "Cepat bereaksi"},
        {"Nama Uji": "Uji Kromik", "Hasil Positif": "Negatif", "Keterangan": "Tidak teroksidasi"},
        {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"},
    ],
    "Fenol": [
        {"Nama Uji": "Uji Ferri Klorida", "Hasil Positif": "Ungu/biru", "Keterangan": "Kompleks fenolat"},
        {"Nama Uji": "Uji Bromin", "Hasil Positif": "Endapan putih tribromofenol", "Keterangan": "Substitusi elektrofilik"},
    ],
    "Aldehida": [
        {"Nama Uji": "Uji Tollens", "Hasil Positif": "Cermin perak", "Keterangan": "Aldehida teroksidasi"},
        {"Nama Uji": "Uji Fehling", "Hasil Positif": "Endapan merah bata", "Keterangan": "Aldehida positif"},
        {"Nama Uji": "Uji DNP", "Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Gugus karbonil"},
    ],
    "Keton": [
        {"Nama Uji": "Uji Tollens", "Hasil Positif": "Negatif", "Keterangan": "Tidak teroksidasi"},
        {"Nama Uji": "Uji Fehling", "Hasil Positif": "Negatif", "Keterangan": "Tidak bereaksi"},
        {"Nama Uji": "Uji DNP", "Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Gugus karbonil"},
    ],
    "Karbohidrat": [
        {"Nama Uji": "Uji Molisch", "Hasil Positif": "Cincin ungu", "Keterangan": "Dehidrasi furfural"},
        {"Nama Uji": "Uji Benedict", "Hasil Positif": "Endapan merah bata", "Keterangan": "Gula pereduksi"},
    ],
    "Asam Karboksilat": [
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus merah", "Keterangan": "Bersifat asam"},
        {"Nama Uji": "Uji NaHCO₃", "Hasil Positif": "Gelembung CO₂", "Keterangan": "Reaksi dengan basa lemah"},
    ],
    "Amina Primer": [
        {"Nama Uji": "Uji Hinsberg", "Hasil Positif": "Larut setelah basa", "Keterangan": "Gugus -NH₂"},
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus biru", "Keterangan": "Basa"},
    ],
    "Amina Sekunder": [
        {"Nama Uji": "Uji Hinsberg", "Hasil Positif": "Tidak larut setelah basa", "Keterangan": "Tidak membentuk garam"},
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus biru", "Keterangan": "Basa"},
    ],
    "Amina Tersier": [
        {"Nama Uji": "Uji Hinsberg", "Hasil Positif": "Tidak bereaksi", "Keterangan": "Tidak membentuk derivat"},
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus biru", "Keterangan": "Basa"},
    ],
    "Protein": [
        {"Nama Uji": "Uji Biuret", "Hasil Positif": "Ungu", "Keterangan": "Ikatan peptida"},
        {"Nama Uji": "Uji Xantoprotein", "Hasil Positif": "Kuning", "Keterangan": "Gugus aromatik"},
    ],
    "Lemak & Minyak": [
        {"Nama Uji": "Uji Kertas", "Hasil Positif": "Noda transparan", "Keterangan": "Ciri lipid"},
        {"Nama Uji": "Uji Baeyer", "Hasil Positif": "Ungu hilang", "Keterangan": "Ikatan tak jenuh"},
    ],
}

# ========== DATA KELARUTAN, KEBASEAN, TITIK DIDIH ==========
data_senyawa = [
    {"nama_jenis": "Hidrokarbon (contoh: heksana)", "kelarutan": "Tidak larut dalam air, larut dalam pelarut non-polar", "kebasaan": "Netral (pH ~7)", "titik_didih": 68.7},
    {"nama_jenis": "Alkohol Primer (contoh: etanol)", "kelarutan": "Larut dalam air dan etanol", "kebasaan": "Netral (pH ~7)", "titik_didih": 78.4},
    {"nama_jenis": "Alkohol Sekunder (contoh: isopropanol)", "kelarutan": "Larut dalam air", "kebasaan": "Netral (pH ~7)", "titik_didih": 82.6},
    {"nama_jenis": "Alkohol Tersier (contoh: tert-butanol)", "kelarutan": "Larut dalam air", "kebasaan": "Netral (pH ~7)", "titik_didih": 82.2},
    {"nama_jenis": "Fenol", "kelarutan": "Sedikit larut dalam air", "kebasaan": "Sedikit asam (pH ~5.5)", "titik_didih": 181.7},
    {"nama_jenis": "Eter (contoh: dietil eter)", "kelarutan": "Sedikit larut dalam air", "kebasaan": "Netral (pH ~7)", "titik_didih": 34.6},
    {"nama_jenis": "Aldehida (contoh: asetaldehida)", "kelarutan": "Larut dalam air", "kebasaan": "Netral (pH ~7)", "titik_didih": 20.2},
    {"nama_jenis": "Keton (contoh: aseton)", "kelarutan": "Larut dalam air", "kebasaan": "Netral (pH ~7)", "titik_didih": 56.1},
    {"nama_jenis": "Karbohidrat (contoh: glukosa)", "kelarutan": "Sangat larut dalam air", "kebasaan": "Netral (pH ~7)", "titik_didih": "Terurai sebelum mendidih"},
    {"nama_jenis": "Asam Karboksilat (contoh: asam asetat)", "kelarutan": "Sangat larut dalam air", "kebasaan": "Asam (pH ~2–4)", "titik_didih": 118.1},
    {"nama_jenis": "Amina Primer (contoh: metilamina)", "kelarutan": "Larut dalam air", "kebasaan": "Basa lemah (pH ~10–11)", "titik_didih": -6.3},
    {"nama_jenis": "Amina Sekunder (contoh: dimetilamina)", "kelarutan": "Larut dalam air", "kebasaan": "Basa lemah (pH ~10–11)", "titik_didih": 7.4},
    {"nama_jenis": "Amina Tersier (contoh: trimetilamina)", "kelarutan": "Larut dalam air", "kebasaan": "Basa lemah (pH ~10–11)", "titik_didih": 3.5},
    {"nama_jenis": "Amina (umum)", "kelarutan": "Larut dalam air, larut dalam asam", "kebasaan": "Basa lemah (pH ~9–11)", "titik_didih": "Bervariasi"},
    {"nama_jenis": "Protein (contoh: albumin)", "kelarutan": "Larut dalam air (larutan koloid)", "kebasaan": "Netral–sedikit asam (pH ~6–7)", "titik_didih": "Terdenaturasi sebelum mendidih"},
    {"nama_jenis": "Lemak & Minyak (contoh: trigliserida)", "kelarutan": "Tidak larut dalam air", "kebasaan": "Netral (pH ~7)", "titik_didih": ">300 (dekomposisi)"},
]

# ========== FAKTA MENARIK ==========
fakta_menarik = [
    "🧴 Lemak tak jenuh bereaksi dengan larutan Baeyer.",
    "🧪 Fenol memberikan warna ungu dengan FeCl₃.",
    "⚗ Uji Lucas membedakan alkohol primer, sekunder, tersier.",
    "💨 NaHCO₃ bereaksi dengan asam karboksilat membebaskan CO₂.",
    "🔬 Uji Biuret positif jika ada ikatan peptida.",
]

========== KONFIGURASI HALAMAN ==========

st.set_page_config(page_title="Uji Senyawa Kimia Lengkap", layout="wide")

tab1, tab2, tab3, tab4, tab5 = st.tabs([ "📘 Pengertian EsterMoon", "📘 Pengertian Senyawa", "🔬 Uji Senyawa", "📊 Kelarutan, Kebasaan & Titik Didih", "🧠 Quiz Golongan Senyawa" ])

========== TAB 1: ESTER MOON ==========

with tab1: st.header("Apa Itu Ester Moon?") st.write(""" Ester Moon adalah aplikasi web yang bergerak dalam menyediakan bahan ajar berupa kumpulan materi praktikum analisis titrimetri dan kimia organik.
Materi dasar ini mengasah skill analis dalam bidang analitik.
Web juga menyediakan kalkulator konsentrasi dan normalitas larutan.
Materi fleksibel dan bisa diakses kapan saja. """) st.subheader("👩‍🔬 Kelompok 03:") for nama in ["Anita", "Dwita", "Marsya", "Najwa", "Shella"]: st.write(f"- {nama}")

========== TAB 2: PENGERTIAN SENYAWA ==========

with tab2: st.title("📘 Pengertian Golongan Senyawa Kimia") selected = st.selectbox("Pilih Golongan Senyawa", [x["Golongan"] for x in pengertian_senyawa]) for item in pengertian_senyawa: if item["Golongan"] == selected: st.info(item["Golongan"]) st.write(item["Pengertian"])

if st.checkbox("Tampilkan Semua Pengertian"):
    st.table({
        "Golongan": [x["Golongan"] for x in pengertian_senyawa],
        "Pengertian": [x["Pengertian"] for x in pengertian_senyawa]
    })

========== TAB 3: UJI SENYAWA ==========

with tab3: st.title("🔬 Uji Golongan Senyawa Kimia") selected = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()), key="uji") st.subheader(f"📋 Hasil Uji untuk: {selected}") for uji in senyawa_data[selected]: with st.expander(uji["Nama Uji"]): st.markdown(f"Hasil Positif: {uji['Hasil Positif']}") st.markdown(f"Keterangan: {uji['Keterangan']}")

========== TAB 4: KELARUTAN, PH, TITIK DIDIH ==========

with tab4: st.title("📊 Data Kelarutan, Kebasaan, dan Titik Didih Senyawa") tab_kel, tab_pH, tab_td = st.tabs(["Uji Kelarutan", "Kebasaan (pH)", "Titik Didih"])

with tab_kel:
    for s in data_senyawa:
        st.subheader(s["nama_jenis"])
        st.write(s["kelarutan"])
        st.write("---")

with tab_pH:
    for s in data_senyawa:
        st.subheader(s["nama_jenis"])
        st.write(s["kebasaan"])
        st.write("---")

with tab_td:
    for s in data_senyawa:
        st.subheader(s["nama_jenis"])
        st.write(f"{s['titik_didih']} °C")
        st.write("---")

========== TAB 5: QUIZ ==========

with tab5: st.title("🧠 Quiz Golongan Senyawa Kimia") semua_uji = [] for gol, daftar_uji in senyawa_data.items(): for uji in daftar_uji: semua_uji.append({**uji, "Golongan": gol})

jumlah_soal = min(15, len(semua_uji))

if "soal_kuis" not in st.session_state:
    st.session_state["soal_kuis"] = random.sample(semua_uji, jumlah_soal)
    st.session_state["opsi_kuis"] = []
    for soal in st.session_state["soal_kuis"]:
        semua_golongan = list(senyawa_data.keys())
        opsi = random.sample(semua_golongan, min(4, len(semua_golongan)))
        if soal["Golongan"] not in opsi:
            opsi[random.randint(0, len(opsi) - 1)] = soal["Golongan"]
        random.shuffle(opsi)
        st.session_state["opsi_kuis"].append(opsi)

soal_kuis = st.session_state["soal_kuis"]
opsi_kuis = st.session_state["opsi_kuis"]
jawaban_pengguna = {}

for i, soal in enumerate(soal_kuis, 1):
    st.markdown(f"Soal {i}: {soal['Nama Uji']} → Hasil: {soal['Hasil Positif']}")
    opsi = opsi_kuis[i - 1]
    jawaban = st.radio("Pilih Golongan:", opsi, key=f"kuis_{i}")
    jawaban_pengguna[f"soal_{i}"] = {"jawaban": jawaban, "benar": soal["Golongan"]}

if st.button("📤 Submit Jawaban"):
    benar = sum(1 for k in jawaban_pengguna if jawaban_pengguna[k]["jawaban"] == jawaban_pengguna[k]["benar"])
    skor = (benar / jumlah_soal) * 100

    st.success(f"✅ Kamu menjawab {benar} dari {jumlah_soal} soal dengan benar.")
    st.info(f"🎯 Skor akhir: {skor:.2f}%")

    salah = [(k, v["jawaban"], v["benar"]) for k, v in jawaban_pengguna.items() if v["jawaban"] != v["benar"]]
    if salah:
        st.warning("❌ Jawaban yang salah:")
        for s in salah:
            st.markdown(f"- {s[0]}: Jawabanmu {s[1]}, seharusnya *{s[2]}")

    st.markdown("---")
    st.subheader("💡 Fakta Menarik Kimia")
    st.info(random.choice(fakta_menarik))

========== FOOTER ==========

st.markdown("---") st.caption("© 2025 | Uji Senyawa Kimia Interaktif by Streamlit 🎓")
