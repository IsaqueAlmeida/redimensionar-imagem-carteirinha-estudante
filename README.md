# Redimensionamento de Imagens de Carteirinha

Este projeto consiste em um script em Python que utiliza a biblioteca OpenCV para redimensionar duas imagens (frente e verso) de carteirinhas. As imagens são carregadas, redimensionadas para dimensões predefinidas e salvas com novos nomes. O processo é automatizado para garantir que a alteração de tamanho seja feita de maneira rápida e eficiente.

## Funcionalidade

- Carregamento de imagens: O script carrega duas imagens de carteirinhas a partir de arquivos locais (cart_1.jpg e cart_2.jpg).
- Verificação de falha no carregamento: Caso não seja possível carregar as imagens, o script imprime uma mensagem de erro e interrompe a execução.
- Redimensionamento: As imagens são redimensionadas para as dimensões especificadas (largura de 508px e altura de 321px).
- Salvamento: As imagens redimensionadas são salvas com novos nomes (`carteirinha_redimensionada_frente.jpg` e `carteirinha_redimensionada_verso.jpg`).
- Mensagem de sucesso: O script imprime mensagens de sucesso após salvar as imagens com as novas dimensões.

## Como Usar

1. **Instalar a Biblioteca OpenCV**: O projeto utiliza a biblioteca OpenCV para o processamento de imagens. Para instalar, use o comando:
    ```bash
    pip install opencv-python
    ```

2. **Prepare as Imagens**: Certifique-se de ter as imagens `cart_1.jpg` e `cart_2.jpg` na mesma pasta onde o script será executado.

3. **Executar o Script**: Execute o script Python da seguinte forma:
    ```bash
    python redimensiona_imagens.py
    ```

4. **Resultado**: As imagens redimensionadas serão salvas com os nomes `carteirinha_redimensionada_frente.jpg` e `carteirinha_redimensionada_verso.jpg` na mesma pasta.

## Explicação do Código

- **Carregamento das Imagens**:
    ```python
    imagem_frente = cv2.imread('cart_1.jpg')
    imagem_verso = cv2.imread('cart_2.jpg')
    ```
    O código utiliza o `cv2.imread()` para carregar as imagens dos arquivos locais.

- **Verificação de Erro**:
    ```python
    if imagem_frente is None and imagem_verso is None:
        print('Erro: não foi possível carregar a imagem!')
        exit()
    ```
    Caso as imagens não sejam carregadas corretamente, o script exibe uma mensagem de erro e interrompe a execução.

- **Redimensionamento**:
    ```python
    imagem_redimensionada_frente = cv2.resize(imagem_frente, (largura, altura))
    imagem_redimensionada_verso = cv2.resize(imagem_verso, (largura, altura))
    ```
    As imagens são redimensionadas para as dimensões definidas (508px de largura e 321px de altura).

- **Salvamento das Imagens**:
    ```python
    cv2.imwrite(f'{img_salvo_frente}', imagem_redimensionada_frente)
    cv2.imwrite(f'{img_salvo_verso}', imagem_redimensionada_verso)
    ```
    As imagens redimensionadas são salvas com novos nomes.

- **Mensagens de Sucesso**:
    O script imprime uma mensagem indicando que as imagens foram redimensionadas e salvas com sucesso.

## Dependências

- Python 3.x
- OpenCV (`opencv-python`)

## Redes Sociais

- GitHub: [https://github.com/IsaqueAlmeida](https://github.com/IsaqueAlmeida)
- LinkedIn: [https://www.linkedin.com/in/isaque-f-s-almeida/](https://www.linkedin.com/in/isaque-f-s-almeida/)

## Contribuições

Contribuições são bem-vindas! Caso queira sugerir melhorias ou corrigir problemas, por favor, faça um fork do projeto, realize as alterações e envie um pull request.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
