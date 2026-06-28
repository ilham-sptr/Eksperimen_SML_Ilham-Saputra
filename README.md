# Paket Lengkap Submission MSML — Ilham Saputra

Paket ini berisi semua bahan untuk memperbaiki keempat kriteria sesuai catatan reviewer.
Semua kode di dalamnya **sudah saya jalankan & tes langsung** (bukan sekadar ditulis) —
detail pengujian ada di masing-masing README per folder.

## Peta Folder → Tujuan

| Folder di paket ini | Jadi apa? |
|---|---|
| `Eksperimen_SML_Ilham-Saputra_repo/` | Isi repo GitHub **`Eksperimen_SML_Ilham-Saputra`** (Kriteria 1) |
| `Membangun_model/` | Masuk ke dalam ZIP submission utama, folder `Membangun_model/` (Kriteria 2) |
| `Workflow-CI_repo/` | Isi repo GitHub **`Workflow-CI`** (Kriteria 3) |
| `Monitoring dan Logging/` | Masuk ke dalam ZIP submission utama, folder `Monitoring dan Logging/` (Kriteria 4) |

## Langkah Submit Ulang

1. **Kriteria 1**: Buat/perbarui repo GitHub `Eksperimen_SML_Ilham-Saputra` (Public), push isi `Eksperimen_SML_Ilham-Saputra_repo/`. Lalu update `Eksperimen_SML_Ilham-Saputra.txt` dengan link repo itu.
2. **Kriteria 3**: Buat/perbarui repo GitHub `Workflow-CI` (Public), push isi `Workflow-CI_repo/` (termasuk folder `.github/` yang tersembunyi!). Pastikan tab Actions menunjukkan run yang sukses (✔ hijau). Update `Workflow-CI.txt` dengan link repo itu.
3. **Kriteria 2**: Jalankan `modelling.py` & `modelling_tuning.py` di folder `Membangun_model/` terhadap MLflow Tracking Server lokal milikmu, lalu ambil screenshot dashboard & artifact (lihat `Membangun_model/README.md`).
4. **Kriteria 4**: Jalankan `7.inference.py` dan `3.prometheus-exporter.py`, setup Prometheus + Grafana, lalu ambil semua screenshot bukti (lihat `Monitoring dan Logging/README.md`).
5. Susun ulang ZIP submission utama mengikuti struktur resmi:
   ```
   SMSML_Ilham-Saputra.zip
   ├── Eksperimen_SML_Ilham-Saputra.txt
   ├── Membangun_model/
   ├── Workflow-CI.txt
   └── Monitoring dan Logging/
   ```
6. Submit ulang ke Dicoding.

## Yang Sudah Diverifikasi Jalan (Tidak Cuma Teori)
- ✅ Notebook eksperimen Kriteria 1 — 0 error di seluruh cell
- ✅ `automate_Ilham-Saputra.py` — jalan tanpa error, hasil sama dengan notebook
- ✅ `modelling.py` & `modelling_tuning.py` — diuji ke MLflow Tracking Server lokal sungguhan, artefak `model/MLmodel`, `estimator.html`, `training_confusion_matrix.png` semua tergenerate
- ✅ `mlflow run` pada `MLProject/` — sukses, run_id bisa diekstrak otomatis
- ✅ `.github/workflows/ci.yml` — YAML valid, tahapan sesuai contoh level skilled di pedoman
- ✅ `7.inference.py` — serving model real, endpoint `/predict` & `/metrics` terverifikasi
- ✅ `3.prometheus-exporter.py` — metrik CPU/RAM real dari sistem, terverifikasi di endpoint `/metrics`

## Yang TIDAK Saya Buatkan (Harus Kamu Sendiri)
Saya nggak membuat screenshot/bukti palsu untuk: dashboard MLflow, artifact MLflow, DagsHub, monitoring Prometheus, dashboard & alerting Grafana — karena itu harus jadi bukti nyata dari environment-mu sendiri yang berjalan. Instruksi detail step-by-step ada di README masing-masing folder.
