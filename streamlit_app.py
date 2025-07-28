import streamlit as st
import random
import pandas as pd

# ========== SETUP HALAMAN ==========
st.set_page_config(page_title="Uji Senyawa Kimia Lengkap", layout="wide")

# ========== DATA PENGERTIAN ORGOVERSE ==========
pengertian_orgoverse = [
    {
        "deskripsi": "OrgoVerse (Organik Universe) adalah website yang berisi materi kimia organik khusus tentang senyawa kimia. Website ini dilengkapi fitur fakta menarik dan kuis untuk mengasah pengetahuan, serta menyediakan antarmuka interaktif dan responsif agar pembelajaran dapat berlangsung fleksibel dan mudah diakses kapan saja dan di mana saja."
    }
]

# ========== DATA PENGERTIAN GOLONGAN SENYAWA ==========
pengertian_senyawa = [
    {"Golongan": "Hidrokarbon", "Pengertian": "Senyawa organik yang hanya terdiri dari karbon (C) dan hidrogen (H). Dibagi menjadi: Alkana (jenuh), Alkena (tak jenuh dengan ikatan rangkap dua), Alkuna (ikatan rangkap tiga), Aromatik (cincin benzena)."},
    {"Golongan": "Alkohol Primer", "Pengertian": "OH terikat pada karbon yang hanya terhubung ke satu atom C lain (contoh: etanol)."},
    {"Golongan": "Alkohol Sekunder", "Pengertian": "OH terikat pada karbon yang terhubung ke dua atom C lain (contoh: isopropanol)."},
    {"Golongan": "Alkohol Tersier", "Pengertian": "OH terikat pada karbon yang terhubung ke tiga atom C lain (contoh: tert-butanol)."},
    {"Golongan": "Fenol", "Pengertian": "Senyawa aromatik dengan gugus -OH langsung terikat pada cincin benzena. Lebih asam dari alkohol biasa."},
    {"Golongan": "Eter", "Pengertian": "Senyawa dengan struktur R‑O‑R′, di mana R dan R′ adalah gugus alkil atau aril. Tidak memiliki gugus ‑OH bebas."},
    {"Golongan": "Aldehida", "Pengertian": "Mengandung gugus karbonil (C=O) di ujung rantai karbon, yaitu ‑CHO. Contoh: formaldehida."},
    {"Golongan": "Keton", "Pengertian": "Mengandung gugus karbonil (C=O) di tengah rantai karbon, bukan di ujung. Contoh: aseton."},
    {"Golongan": "Karbohidrat", "Pengertian": "Senyawa organik dengan rumus umum Cₙ(H₂O)ₙ. Contoh: glukosa, fruktosa. Sumber energi."},
    {"Golongan": "Asam Karboksilat", "Pengertian": "Mengandung gugus ‑COOH. Bersifat asam dan dapat membentuk garam atau ester. Contoh: asam asetat."},
    {"Golongan": "Amina Primer", "Pengertian": "Satu gugus alkil/aril terikat pada nitrogen (R‑NH₂)."},
    {"Golongan": "Amina Sekunder", "Pengertian": "Dua gugus alkil/aril terikat pada nitrogen (R₂NH)."},
    {"Golongan": "Amina Tersier", "Pengertian": "Tiga gugus alkil/aril terikat pada nitrogen (R₃N)."},
    {"Golongan": "Amina", "Pengertian": "Senyawa yang mengandung atom nitrogen dengan gugus alkil/aril."},
    {"Golongan": "Protein", "Pengertian": "Polimer asam amino dengan ikatan peptida. Fungsi: enzim, transport, struktural, dsb."},
    {"Golongan": "Lemak & Minyak", "Pengertian": "Lemak: padat pada suhu ruang (dari hewan). Minyak: cair pada suhu ruang (dari tumbuhan). Cadangan energi."},
]
properti_senyawa = [
    {"nama_jenis": "Hidrokarbon (contoh: heksana)", "kelarutan": "Tidak larut dalam air, larut dalam pelarut non-polar", "kebasaan": "Netral (pH ~7)", "titik_didih": 68.7},
    {"nama_jenis": "Alkohol Primer (contoh: etanol)", "kelarutan": "Larut dalam air dan etanol", "kebasaan": "Netral (pH ~7)", "titik_didih": 78.4},
    {"nama_jenis": "Alkohol Sekunder (contoh: isopropanol)", "kelarutan": "Larut dalam air", "kebasaan": "Netral (pH ~7)", "titik_didih": 82.6},
    {"nama_jenis": "Alkohol Tersier (contoh: tert‑butanol)", "kelarutan": "Larut dalam air", "kebasaan": "Netral (pH ~7)", "titik_didih": 82.2},
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

# ========== DATA UJI SENYAWA ==========
senyawa_data = {
    "Hidrokarbon": [
        {"Nama Uji": "Uji Pembakaran", "Penjelasan": "Uji ini digunakan untuk mengidentifikasi jenis serat atau material berdasarkan sifat pembakaran, bau yang dihasilkan, warna asap, dan sisa pembakaran. Sering digunakan dalam penentuan golongan serat tekstil atau material organik.", "Hasil Positif": "Nyala kuning berasap", "Keterangan": "Aromatik"},
        {"Nama Uji": "Uji Bromin", "Penjelasan": "Uji ini untuk mendeteksi adanya ikatan rangkap dua atau tiga (ketidakjenuhan) pada senyawa organik seperti alkena, alkuna, fenol, dan anilina.", "Hasil Positif": "Warna hilang", "Keterangan": "Adisi ikatan rangkap"},
        {"Nama Uji": "Uji Baeyer", "Penjelasan": "Menggunakan larutan kalium permanganat (KMnO₄) untuk mengidentifikasi senyawa yang memiliki ikatan rangkap, seperti alkena.", "Hasil Positif": "Ungu hilang jadi coklat", "Keterangan": "Ikatan rangkap"},
    ],
    "Alkohol Primer": [
        {"Nama Uji": "Uji Lucas", "Penjelasan": "Uji kualitatif untuk membedakan alkohol primer, sekunder, dan tersier berdasarkan kecepatan reaksi dengan reagen Lucas (campuran ZnCl₂ dan HCl pekat). Alkohol tersier bereaksi cepat (seketika keruh), sekunder lebih lambat, dan primer biasanya tidak menunjukkan perubahan", "Hasil Positif": "Tidak keruh / lambat", "Keterangan": "Reaksi lambat"},
        {"Nama Uji": "Uji Kromik (Jones)", "Penjelasan": "Uji untuk mendeteksi alkohol primer dan sekunder atau aldehida menggunakan reagen Jones (larutan kromium trioxide dalam asam sulfat).", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi → asam karboksilat"},
        {"Nama Uji": "Uji Natrium", "Penjelasan": "untuk mendeteksi keberadaan ion natrium dalam suatu sampel.", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"},
    ],
    "Alkohol Sekunder": [
        {"Nama Uji": "Uji Lucas", "Penjelasan": "Uji kualitatif untuk membedakan alkohol primer, sekunder, dan tersier berdasarkan kecepatan reaksi dengan reagen Lucas (campuran ZnCl₂ dan HCl pekat). Alkohol tersier bereaksi cepat (seketika keruh), sekunder lebih lambat, dan primer biasanya tidak menunjukkan perubahan", "Hasil Positif": "Keruh sedang (~5 menit)", "Keterangan": "Reaksi sedang"},
        {"Nama Uji": "Uji Kromik", "Penjelasan": "Uji untuk mendeteksi alkohol primer dan sekunder atau aldehida menggunakan reagen Jones (larutan kromium trioxide dalam asam sulfat).", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi → keton"},
        {"Nama Uji": "Uji Natrium", "Penjelasan": "untuk mendeteksi keberadaan ion natrium dalam suatu sampel.", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"},
    ],
    "Alkohol Tersier": [
        {"Nama Uji": "Uji Lucas", "Penjelasan": "Uji kualitatif untuk membedakan alkohol primer, sekunder, dan tersier berdasarkan kecepatan reaksi dengan reagen Lucas (campuran ZnCl₂ dan HCl pekat). Alkohol tersier bereaksi cepat (seketika keruh), sekunder lebih lambat, dan primer biasanya tidak menunjukkan perubahan", "Hasil Positif": "Cepat keruh", "Keterangan": "Cepat bereaksi"},
        {"Nama Uji": "Uji Kromik", "Penjelasan": "Uji untuk mendeteksi alkohol primer dan sekunder atau aldehida menggunakan reagen Jones (larutan kromium trioxide dalam asam sulfat).", "Hasil Positif": "Negatif", "Keterangan": "Tidak teroksidasi"},
        {"Nama Uji": "Uji Natrium", "Penjelasan": "untuk mendeteksi keberadaan ion natrium dalam suatu sampel.", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"},
    ],
    "Fenol": [
        {"Nama Uji": "Uji Ferri Klorida", "Penjelasan": "Uji untuk mendeteksi fenol.", "Hasil Positif": "Ungu/biru", "Keterangan": "Kompleks fenolat"},
        {"Nama Uji": "Uji Bromin", "Penjelasan": "Uji ini untuk mendeteksi adanya ikatan rangkap dua atau tiga (ketidakjenuhan) pada senyawa organik seperti alkena, alkuna, fenol, dan anilina.", "Hasil Positif": "Endapan putih tribromofenol", "Keterangan": "Substitusi elektrofilik"},
    ],
    "Aldehida": [
        {"Nama Uji": "Uji Tollens", "Penjelasan": "Uji ini digunakan untuk mendeteksi gugus karbonil pada aldehida dan keton.", "Hasil Positif": "Cermin perak", "Keterangan": "Aldehida teroksidasi"},
        {"Nama Uji": "Uji Fehling", "Penjelasan": "Uji untuk mendeteksi gula pereduksi atau aldehida", "Hasil Positif": "Endapan merah bata", "Keterangan": "Aldehida positif"},
        {"Nama Uji": "Uji DNPH", "Penjelasan": " Uji ini digunakan untuk mendeteksi gugus karbonil pada aldehida dan keton.", "Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Gugus karbonil"},
    ],
    "Keton": [
        {"Nama Uji": "Uji Tollens", "Penjelasan": "Uji ini digunakan untuk mendeteksi gugus karbonil pada aldehida dan keton.", "Hasil Positif": "Negatif", "Keterangan": "Tidak teroksidasi"},
        {"Nama Uji": "Uji Fehling", "Penjelasan": "Uji untuk mendeteksi gula pereduksi atau aldehida", "Hasil Positif": "Negatif", "Keterangan": "Tidak bereaksi"},
        {"Nama Uji": "Uji DNPH", "Penjelasan": " Uji ini digunakan untuk mendeteksi gugus karbonil pada aldehida dan keton.", "Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Gugus karbonil"},
    ],
    "Karbohidrat": [
        {"Nama Uji": "Uji Molisch", "Penjelasan": "Merupakan uji umum karbohidrat berdasarkan reaksi dehidrasi membentuk furfural yang berinteraksi dengan α-naftol menghasilkan cincin ungu di antara dua lapisan reagen.", "Hasil Positif": "Cincin ungu", "Keterangan": "Dehidrasi furfural"},
        {"Nama Uji": "Uji Benedict", "Penjelasan": "untuk deteksi gula pereduksi. Larutan biru dari tembaga(II) sulfat akan berubah warna hingga endapan merah bata menunjukkan keberadaan gula pereduksi.", "Hasil Positif": "Endapan merah bata", "Keterangan": "Gula pereduksi"},
        {"Nama Uji": "Uji Barfoed", "Penjelasan": "untuk membedakan monosakarida dari disakarida. Monosakarida akan mereduksi reagen Barfoed membentuk endapan merah bata dalam waktu singkat.", "Hasil Positif": "Endapan merah bata cepat", "Keterangan": "Monosakarida positif"},
        {"Nama Uji": "Uji Seliwanoff", "Penjelasan": "untuk membedakan antara aldosa dan ketosa. Ketosa akan memberi warna merah dengan reagen Seliwanoff, sedangkan aldosa menghasilkan warna lambat atau tidak berwarna.", "Hasil Positif": "Warna merah cepat", "Keterangan": "Ketosa positif"},
    ],
    "Asam Karboksilat": [
        {"Nama Uji": "Uji Lakmus", "Penjelasan": "Menggunakan kertas lakmus untuk mengetahui sifat asam/basa suatu larutan.", "Hasil Positif": "Lakmus merah", "Keterangan": "Bersifat asam"},
        {"Nama Uji": "Uji NaHCO₃", "Penjelasan": "Untuk identifikasi senyawa asam karboksilat, di mana terbentuk gelembung CO₂ sebagai hasil reaksi positif.", "Hasil Positif": "Gelembung CO₂", "Keterangan": "Reaksi dengan basa lemah"},
    ],
    "Amina Primer": [
        {"Nama Uji": "Uji Hinsberg", "Penjelasan": "Uji kualitatif untuk membedakan amina primer, sekunder, dan tersier memakai reagen Hinsberg (benzensulfonil klorida) berdasarkan kelarutan produk reaksi dalam basa.", "Hasil Positif": "Larut setelah basa", "Keterangan": "Gugus -NH₂"},
        {"Nama Uji": "Uji Lakmus", "Penjelasan": "Menggunakan kertas lakmus untuk mengetahui sifat asam/basa suatu larutan.", "Hasil Positif": "Lakmus biru", "Keterangan": "Basa"},
    ],
    "Amina Sekunder": [
        {"Nama Uji": "Uji Hinsberg", "Penjelasan": "Uji kualitatif untuk membedakan amina primer, sekunder, dan tersier memakai reagen Hinsberg (benzensulfonil klorida) berdasarkan kelarutan produk reaksi dalam basa.","Hasil Positif": "Tidak larut setelah basa", "Keterangan": "Tidak membentuk garam"},
        {"Nama Uji": "Uji Lakmus", "Penjelasan": "Menggunakan kertas lakmus untuk mengetahui sifat asam/basa suatu larutan.", "Hasil Positif": "Lakmus biru", "Keterangan": "Basa"},
    ],
    "Amina Tersier": [
        {"Nama Uji": "Uji Hinsberg", "Penjelasan": "Uji kualitatif untuk membedakan amina primer, sekunder, dan tersier memakai reagen Hinsberg (benzensulfonil klorida) berdasarkan kelarutan produk reaksi dalam basa.","Hasil Positif": "Tidak bereaksi", "Keterangan": "Tidak membentuk derivat"},
        {"Nama Uji": "Uji Lakmus", "Penjelasan": "Menggunakan kertas lakmus untuk mengetahui sifat asam/basa suatu larutan.", "Hasil Positif": "Lakmus biru", "Keterangan": "Basa"},
    ],
    "Protein": [
        {"Nama Uji": "Uji Biuret", "Penjelasan": "Uji protein yang didasarkan pada reaksi senyawa peptida dengan ion tembaga(II), menghasilkan warna ungu sebagai tanda adanya ikatan peptida.", "Hasil Positif": "Ungu", "Keterangan": "Ikatan peptida"},
        {"Nama Uji": "Uji Xantoprotein", "Penjelasan": "Uji untuk mengenali asam amino aromatik (fenilalanin, tirosin, triptofan) berdasarkan reaksi nitrasi menghasilkan warna kuning yang berubah menjadi jingga dengan alkali.", "Hasil Positif": "Kuning", "Keterangan": "Gugus aromatik"},
        {"Nama Uji": "Uji Ninhidrin", "Penjelasan": "Uji untuk mendeteksi asam amino bebas dan peptida; bereaksi menghasilkan warna ungu atau biru.", "Hasil Positif": "Warna ungu/biru", "Keterangan": "Asam amino bebas"},
    ],
    "Lemak & Minyak": [
        {"Nama Uji": "Uji Kertas", "Penjelasan": "Biasanya digunakan untuk menguji keberadaan lemak; kertas diusap bahan, bila meninggalkan noda transparan, menandakan adanya lemak.", "Hasil Positif": "Noda transparan", "Keterangan": "Ciri lipid"},
        {"Nama Uji": "Uji Baeyer", "Penjelasan": "Menggunakan larutan kalium permanganat (KMnO₄) untuk mengidentifikasi senyawa yang memiliki ikatan rangkap, seperti alkena.", "Hasil Positif": "Ungu hilang", "Keterangan": "Ikatan tak jenuh"},
        {"Nama Uji": "Uji Saponifikasi", "Penjelasan": "Digunakan untuk mengamati proses hidrolisis ester (misal lemak) membentuk garam asam lemak (sabun) dan gliserol dalam suasana basa.", "Hasil Positif": "Sabun terbentuk", "Keterangan": "Hidrolisis trigliserida"},
    ],
}

# ========== TABS ==========
tab1, tab2, tab3, tab4 = st.tabs([
    "📙 Tentang OrgoVerse",
    "📘 Pengertian Senyawa",
    "🔬 Uji Senyawa",
    "🧠 Quiz Golongan Senyawa"
])

# ===== Tab 1 =====
with tab1:
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.image("orgoverse_logo.png", width=200)
    st.markdown("""
        <h1 style='margin-top: 20px;'>Selamat Datang di <span style="color:#6c63ff;">OrgoVerse!</span></h1>
        <p style='font-size: 18px;'><strong>Platform interaktif</strong> untuk memahami <em>golongan senyawa kimia</em> secara menyenangkan dan mudah diakses.</p>
        <p style='font-size: 16px;'>🔍 Jelajahi pengertian senyawa, uji-uji kimia, data kelarutan, dan tantang dirimu lewat kuis interaktif!</p>
        <hr style='margin-top: 40px;'>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.header("Apa Itu OrgoVerse?")
    st.write(pengertian_orgoverse[0]["deskripsi"])
    st.subheader("👩‍🔬 Kelompok 04:")
    anggota = [
        "ANITA TIARA ANGEL (2460328)",
        "DWITA WIDYA PUTRI (2460361)",
        "MARSYA MADINA MUNIR (2460413)",
        "NAJWA ANANDA EFENDI (2460457)",
        "SHELLA RIVANA AULIYA (2460516)"
    ]
    for nama in anggota:
        st.write(f"- {nama}")

# ===== Tab 2 =====
with tab2:
    st.title("📘 Pengertian Golongan Senyawa Kimia")
    sel = st.selectbox("Pilih Golongan Senyawa", [x["Golongan"] for x in pengertian_senyawa])

    # Tampilkan Pengertian
    for item in pengertian_senyawa:
        if item["Golongan"] == sel:
            st.subheader(f"📖 {item['Golongan']}")
            st.write(item["Pengertian"])

            # Cari properti senyawa yang cocok
            match = next((p for p in properti_senyawa if sel.lower() in p["nama_jenis"].lower()), None)
            if match:
                st.markdown("### ⚗️ Properti Fisik:")
                st.write(f"**Kelarutan:** {match['kelarutan']}")
                st.write(f"**Kebasaan:** {match['kebasaan']}")
                st.write(f"**Titik Didih:** {match['titik_didih']} °C" if isinstance(match["titik_didih"], (int, float)) else f"**Titik Didih:** {match['titik_didih']}")
            else:
                st.info("Properti fisik tidak tersedia untuk golongan ini.")
            break

    if st.checkbox("Tampilkan Semua Pengertian"):
        st.dataframe(pd.DataFrame(pengertian_senyawa))

# ===== Tab 3 =====
with tab3:
    st.title("🔬 Uji Golongan Senyawa Kimia")
    sel2 = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()))
    st.subheader(f"Hasil Uji untuk: {sel2}")
    for uji in senyawa_data[sel2]:
        with st.expander(uji["Nama Uji"]):
            st.markdown(f"**Hasil Positif:** {uji['Hasil Positif']}")
            st.markdown(f"**Keterangan:** {uji['Keterangan']}")
            if "Penjelasan" in uji:
                st.markdown(f"**Penjelasan:** {uji['Penjelasan']}")

# ========== TAB 4: QUIZ ==========
with tab4:
    st.title("🧠 Quiz Golongan Senyawa Kimia")
    semua_uji = []
    for golongan, daftar_uji in senyawa_data.items():
        for uji in daftar_uji:
            semua_uji.append({**uji, "Golongan": golongan})

    jumlah_soal = min(15, len(semua_uji))

    if "soal_kuis" not in st.session_state:
        st.session_state["soal_kuis"] = random.sample(semua_uji, k=jumlah_soal)
        st.session_state["opsi_kuis"] = []
        for soal in st.session_state["soal_kuis"]:
            opsi = random.sample(list(senyawa_data.keys()), 4)
            if soal["Golongan"] not in opsi:
                opsi[random.randint(0, 3)] = soal["Golongan"]
            random.shuffle(opsi)
            st.session_state["opsi_kuis"].append(opsi)

    soal_kuis = st.session_state["soal_kuis"]
    opsi_kuis = st.session_state["opsi_kuis"]

    st.markdown("Jawab semua soal terlebih dahulu, lalu klik Submit Jawaban.")

    jawaban_pengguna = {}
    for i, soal in enumerate(soal_kuis, 1):
        st.markdown(f"Soal {i}: {soal['Nama Uji']} → {soal['Hasil Positif']}")
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
                st.markdown(f"- {s[0]}: Jawabanmu {s[1]}, seharusnya **{s[2]}")

        st.markdown("---")
        st.subheader("💡 Fakta Menarik Kimia")
        st.info(random.choice(fakta_menarik))

# ===== FOOTER =====
st.markdown("---")
st.caption("© 2025 | Uji Senyawa Kimia Interaktif by Streamlit 🎓")
