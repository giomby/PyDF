# 🐍 PyPDF Toolkit

Un semplice ma potente toolkit in Python per lavorare con file PDF e immagini.
Include funzionalità di traduzione, conversione e manipolazione di PDF, il tutto da riga di comando!

## ✨ Funzionalità

* 📄 **Traduzione di PDF**: Estrae e traduce il testo del PDF in una lingua a scelta.
* ✂️ **Divisione di PDF**: Divide un PDF in più parti specificando il numero di pagine per ogni parte.
* 🖼️ **PNG to PDF**: Converte un'immagine `.png` in un file PDF mantenendo le dimensioni originali.
* 📄➞️🖼️ **PDF to PNG**: Converte ogni pagina di un PDF in una o più immagini PNG.
* 📶 **Controllo connessione**: Verifica se sei connesso a Internet prima di usare la traduzione.

## 🧰 Requisiti

Installa le dipendenze con:

```bash
pip install PyPDF2 fpdf pillow googletrans==4.0.0-rc1 reportlab pdf2image
```

oppure:

```bash
pip install -r requirements.txt
```

> ⚠️ Per `pdf2image` potrebbe essere necessario installare [poppler](https://github.com/oschwartz10612/poppler-windows) su Windows o usare `apt install poppler-utils` su Linux.

## 📁 Struttura Cartelle

Assicurati di avere una cartella `PNG` nella stessa directory del file Python, usata per salvare o leggere le immagini:

```
📁 tuo_progetto/
🔼── main.py
🔼── PNG/
```

## 🚀 Come si usa

Lancia il programma con:

```bash
python main.py
```

Ti verrà mostrato un semplice menu:

```
Scegli un opzione:
1. traduci
2. dividi il pdf
3. PNG to PDF
4. PDF to PNG
5. esci
```

### 🗌️ Traduzione

* Il file PDF deve contenere **testo estraibile**, non solo immagini o scansioni.
* È richiesta la connessione a Internet.
* Supporta codici lingua standard (es. `'en'`, `'it'`, `'fr'`, etc.).

## 📜 Licenza

Questo progetto è rilasciato sotto licenza MIT.
Vedi il file [LICENSE](./LICENSE) per maggiori dettagli.

---

👨‍💻 Creato con ❤️ in Python da **Giomby**
