import cv2

imagem_frente = cv2.imread('cart_1.jpg')
imagem_verso = cv2.imread('cart_2.jpg')

if imagem_frente is None and imagem_verso is None:
    print('Erro: não foi possível carregar a imagem!')
    exit()

# Definindo dimensões
largura, altura = 508, 321

# Redimensionando a imagem
imagem_redimensionada_frente = cv2.resize(imagem_frente, (largura, altura))
imagem_redimensionada_verso = cv2.resize(imagem_verso, (largura, altura))

# salvar imagem redimensionada
img_salvo_frente = "carteirinha_redimensionada_frente.jpg"
img_salvo_verso = "carteirinha_redimensionada_verso.jpg"
cv2.imwrite(f'{img_salvo_frente}', imagem_redimensionada_frente)
cv2.imwrite(f'{img_salvo_verso}', imagem_redimensionada_verso)

print(f"Imagem redimensionada com sucesso! Salva como "
      f"'{img_salvo_frente}' com largura: {largura} e "
      f"altura: {altura}")

print(f"Imagem redimensionada com sucesso! Salva como "
      f"'{img_salvo_verso}' com largura: {largura} e "
      f"altura: {altura}")
