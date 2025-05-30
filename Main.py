import PyPDF2, fpdf
import socket
from PIL import Image
from googletrans import Translator
from reportlab.pdfgen import canvas
from pdf2image import convert_from_path


def menu():
    scelta = input("Scegli un opzione: \n1. traduci\n2. dividi il pdf\n3.PNG to PDF\n4 PDF to PNG\n5. esci\n")
    if not scelta.isdigit() or (scelta := int(scelta)) < 1 or scelta > 5:
        print("opzione non valida")
        return menu()
    if scelta == 5:
        print("Arrivederci!")
        return

    if(scelta == 1):
        traduci()
    elif(scelta == 2):
        dividi_pdf()
    elif(scelta == 3):
        png_to_pdf()
    elif(scelta == 4):
        pdf_to_png()


def traduci() -> None:

    try:
        socket.gethostbyname("google.com")
    except socket.gaierror:
        print("connettiti a internet per tradurre il file PDF.")
        return menu()

    name = input("inserisci il nome del file:")
    if not name.endswith(".pdf"):
        print("Il file deve essere un PDF.")
        return traduci()    
    
    output = input("inserisci il nome del file di output (senza estensione):")

    with open(name, "rb") as file:
        lettore = PyPDF2.PdfReader(file)
        testo = ""
        for pagina in lettore.pages:
            testo += pagina.extract_text()

    if not testo:
        print("Il file PDF non contiene testo.")
        return traduci()

    lingua = input("inserisci la lingua in cui tradurre (es. 'en' per inglese, 'it' per italiano): ")
    translator = Translator()
    traduzione = translator.translate(testo, dest=lingua)
    print("Traduzione completata:")

    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=traduzione.text, align='L')

    pdf.output(output + ".pdf")
    return menu()


def dividi_pdf() -> None:
    name = input("Inserisci il nome del file PDF: ")
    
    if not name.endswith(".pdf"):
        print("Il file deve essere un PDF.")
        return dividi_pdf()
    
    n_divisione = input("Inserisci il numero di divisioni da effettuare: ")
    if not n_divisione.isdigit() or (n_divisione := int(n_divisione)) < 1:
        print("Numero di divisioni non valido.")
        return dividi_pdf()

    try:
        with open(name, "rb") as file:
            lettore = PyPDF2.PdfReader(file)
            n_pagine = len(lettore.pages) 

            n_tot = n_pagine // n_divisione
            if n_pagine % n_divisione != 0:
                n_tot += 1

            print(f"Numero totale di divisioni: {n_tot}")
            
            for i in range(n_tot):
                writer = PyPDF2.PdfWriter()
                start_page = i * n_divisione
                end_page = min((i + 1) * n_divisione, n_pagine)

                for page_num in range(start_page, end_page):
                    writer.add_page(lettore.pages[page_num])

                output_filename = f"{name[:-4]}_parte_{i + 1}.pdf"
                with open(output_filename, "wb") as output_file:
                    writer.write(output_file)

                print(f"File diviso salvato come: {output_filename}")
    
    except FileNotFoundError:
        print("Il file specificato non esiste. Per favore verifica il nome del file.")
        return dividi_pdf()
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        return dividi_pdf()
    return menu()
    

def png_to_pdf():
    
    print("asscirurati di aver inserito le immagini nella cartella 'PNG'")

    img = input("inserisci il nome dell'immagine (con estensione): ")
    if not img.endswith((".png")):
        print("Il file deve essere un'immagine PNG")
        return png_to_pdf()

    image = Image.open("PNG/" + img)

    width, height = image.size

    c = canvas.Canvas(img + ".pdf", pagesize=(width, height))
    c.drawImage("PNG/" + img, 0, 0, width, height)
    c.save()
    return menu()


def pdf_to_png():
    name = input("Inserisci il nome del file PDF: ")
    
    if not name.endswith(".pdf"):
        print("Il file deve essere un PDF.")
        return pdf_to_png()
    
    convert_from_path(name, output_folder="PNG", fmt="png")
    return menu()

if __name__ == "__main__":

    menu()
