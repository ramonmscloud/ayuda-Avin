from PyPDF2 import PdfReader

try:
    pdf = PdfReader('PARA SALTAR CON RED 4y5.pdf')
    text = ''
    for page in pdf.pages:
        text += page.extract_text() + '\n\n'
    
    with open('pdf_content.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    
    print('Contenido del PDF extraído correctamente a pdf_content.txt')
except Exception as e:
    print(f'Error al procesar el PDF: {e}')