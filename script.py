import requests
from bs4 import BeautifulSoup

# URL de la página web
url = "https://www.tripadvisor.com.ar/"

# Define un encabezado User-Agent que simula ser Chrome
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1234.0 Safari/537.36"
}

# Realiza la solicitud HTTP con el encabezado configurado
response = requests.get(url, headers=headers)

# Verifica si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # El contenido de la página está en response.text
    # Puedes utilizar BeautifulSoup con 'lxml' para analizarlo
    soup = BeautifulSoup(response.text, 'lxml')

    # Ahora puedes buscar el elemento <footer> en el HTML
    head = soup.find('head')

    # Imprime el contenido del footer
    if head:
        print(head.prettify())
        
        # Puedes realizar más análisis del contenido del footer aquí
        # Por ejemplo, para extraer todos los enlaces dentro del footer:
        head_links = head.find_all('a')
        for link in head_links:
            print("Enlace:", link.get('href'))
            
        # También puedes extraer texto u otros elementos según tus necesidades
        
    else:
        print("No se encontró el elemento <headers> en la página.")

else:
    print("Error.")
