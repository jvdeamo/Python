import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Carregamento da imagem
imagem = cv2.imread('src/img/LinguicaCdB.jpg')
if imagem is not None:
    altura, largura, _ = imagem.shape
    print(f'Tamanho da Imagem: largura = {largura}, altura = {altura}')
else:
    print('Erro ao ler a imagem.')

# Detecção e decodificação do código de barras
decoded_objects = decode(imagem)

# Configurar uma fonte que suporta caracteres acentuados
fonte_personalizada = cv2.FONT_HERSHEY_COMPLEX
caminho_fonte = 'src/fonts/Lora-VariableFont_wght.ttf'

escala_fonte = 1
texto = 'CODIGO DE BARRAS: '
texto_cor = (0, 255, 0)  # Verde (para o texto "CÓDIGO DE BARRAS")
tamanho_texto = cv2.getTextSize(texto, fonte_personalizada, escala_fonte, 2)[0]
cor_fonte = (255, 255, 255)  # Branco (para o código de barras)

# Desenhar retângulos ao redor dos códigos de barras detectados
for obj in decoded_objects:
    barcode_data = obj.data.decode('utf-8')
    print(f'Código de Barras: {barcode_data}')

    # Coordenadas para o texto "CODIGO DE BARRAS"
    x_texto = 10
    y_texto = 30

    # Coordenadas para o código de barras
    x_codigo = 10
    y_codigo = y_texto + tamanho_texto[1] + 10

    cv2.putText(imagem, texto, (x_texto, y_texto), fonte_personalizada, escala_fonte, texto_cor, 2)
    cv2.putText(imagem, barcode_data, (x_codigo, y_codigo), fonte_personalizada, escala_fonte, cor_fonte, 2)

    # Obtenha as coordenadas do retângulo delimitador do código de barras
    rect_points = obj.rect

    # Desenhe um retângulo ao redor do código de barras
    cv2.rectangle(imagem, (rect_points[0], rect_points[1]), (rect_points[0] + rect_points[2], rect_points[1] + rect_points[3]), (0, 0, 255), 3)

altura, largura, _ = imagem.shape
nova_largura = int(largura * 0.8)
nova_altura = int(altura * 0.8)
imagem_redimensionada = cv2.resize(imagem, (nova_largura, nova_altura))

cv2.namedWindow('Codigo de Barras Detectado', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Codigo de Barras Detectado', 1000, 720)  # Ajuste o tamanho da janela conforme necessário

# Exibir a imagem na janela com a codificação correta
cv2.imshow('Codigo de Barras Detectado', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
