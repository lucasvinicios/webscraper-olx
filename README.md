# Web Scraper para Anúncios de Carros na OLX

Este projeto é um web scraper desenvolvido em Python que coleta informações de anúncios de carros no site da OLX, especificamente da categoria "GM - Chevrolet Celta" na região de "Grande Goiânia e Anápolis".

## Descrição

O scraper utiliza a biblioteca Selenium para navegar e extrair os seguintes dados de cada anúncio:
- **Descrição do anúncio**
- **Características do carro**
- **Preço do carro**

Os dados extraídos são salvos em dois formatos:
- Arquivo CSV (`anuncios_carros_olx.csv`)
- Arquivo JSON (`data.json`)

## Pré-requisitos

Antes de executar o script, certifique-se de que os seguintes requisitos estão atendidos:

1. **Python instalado**
   - Este projeto foi testado com Python 3.9+.

2. **Bibliotecas necessárias instaladas**
   - Instale as dependências utilizando o comando abaixo:
     ```bash
     pip install selenium pandas
     ```

3. **Driver do Chrome instalado**
   - Baixe o ChromeDriver compatível com a versão do seu navegador Chrome: [ChromeDriver](https://chromedriver.chromium.org/downloads)
   - Certifique-se de especificar o caminho correto para o executável do ChromeDriver no script.

4. **Acesso à Internet**
   - O scraper acessará o site da OLX para coletar os dados.

## Configuração

1. Atualize a variável `path` com o caminho correto do ChromeDriver no seu sistema:
   ```python
   path = 'C:/Users/lucas/Downloads/chromedriver-win64/chromedriver.exe'
   ```

2. Altere a URL do site da OLX, se necessário:
   ```python
   website = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/gm-chevrolet/celta/estado-go/grande-goiania-e-anapolis'
   ```

## Como usar

1. Execute o script no seu ambiente Python:
   ```bash
   python nome_do_script.py
   ```

2. Aguarde enquanto o scraper coleta os dados de todas as páginas disponíveis na URL fornecida.

3. Após a execução, os arquivos `anuncios_carros_olx.csv` e `data.json` serão gerados no mesmo diretório do script.

## Estrutura dos Arquivos Gerados

### CSV (`anuncios_carros_olx.csv`)
| descricao_anuncio         | caracteristicas       | preco   |
|---------------------------|-----------------------|---------|
| "Celta 2012 completo"    | ["4 portas", "1.0"]  | R$ 20.000 |
| ...                       | ...                   | ...     |

### JSON (`data.json`)
```json
[
  {
    "descricao_anuncio": "Celta 2012 completo",
    "caracteristicas": ["4 portas", "1.0"],
    "preco": "R$ 20.000"
  },
  ...
]
```

## Observações

- O script está configurado para funcionar em uma URL específica da OLX. Se desejar modificar a categoria ou a região, basta atualizar a variável `website` com o link apropriado.
- Caso o site da OLX implemente mudanças na estrutura HTML, será necessário ajustar os seletores utilizados no script.

## Licença

Este projeto é de uso livre. Modifique e distribua conforme necessário!
