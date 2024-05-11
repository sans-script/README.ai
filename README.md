## Editor de README.md Integrado com Inteligência Artificial

### Introdução

Este aplicativo Flet utiliza o modelo de linguagem avançada Gemini Pro da Google para criar README's com base em seus prompts.

Mas por que não usar o próprio site do Gemini para gerar o código Markdown? Muitos sites populares de IA já entregam respostas renderizadas em Markdown. No entanto, ao solicitar o código Markdown para elaborar um README, o modelo pode não oferecer exatamente o que você deseja. O código fornecido pode vir com a renderização já em Markdown, causando confusão. O modelo também pode falhar em fornecer o código completo, resultando em uma renderização incompleta.


![Captura de tela 2024-05-11 110443](https://github.com/sans-script/README.ai/assets/84801905/16463ffd-9a98-401c-a33a-6c6a30c5d130)
**Fig 1.** AI sendo AI.

Você pode obrigar o modelo a fornecer exatamente o código Markdown que você deseja. Boa sorte ao tentar fazer isso, pode levar um certo tempo. Mesmo copiando o texto já renderizado, ele não será idêntico ao texto Markdown original antes da renderização.

Se você, assim como eu, tem preguiça de escrever um README.md, o README.ai chegou para resolver o seu problema e o do Gemini! O README.ai traz uma interface amigável semelhante à dos serviços da Google, graças à biblioteca Flet Python para construção de interfaces gráficas.

O README.ai é uma solução rápida para quem quer gerar README's sem dor de cabeça, oferecendo a possibilidade de editar a resposta da IA em tempo real e adaptar conforme você desejar!

### Funcionalidades:

- **Interface amigável:** Uma caixa de texto simples para inserir seu prompt.
- **Geração de README com IA:** O modelo Gemini Pro gera um README com base no seu prompt.
- **Visualização em tempo real:** Exibe o README gerado em uma janela separada, com formatação Markdown.
- **Edição do README:** Permite editar o README gerado em uma área de texto dedicada.
- **Atualização dinâmica:** As alterações na área de texto editável são refletidas na visualização do README em tempo real.

![Captura de tela 2024-05-11 113613](https://github.com/sans-script/README.ai/assets/84801905/d18af2b7-e0be-420f-879e-5a67f01c2833)
**Fig 2.** Interface do editor

### Como usar:

1. **Insira o prompt:** Digite o que você deseja que o README.ai inclua na caixa de texto "Escreva um README sobre...".
2. **Gere o README:** Clique no botão "+" para enviar o prompt ao modelo Gemini Pro.
3. **Visualize e edite:** O README gerado será exibido na janela de visualização. Você pode editar o README na área de texto ao lado. 
4. **Aproveite seu novo README!**


![Apresentação2](https://github.com/sans-script/README.ai/assets/84801905/e37dda9d-3a5a-40dc-8776-8a6eb29d3eda)
**Fig 3.** As respostas brotam na tela do editor como se fosse mágica ✨ 

### Dependências:

- `flet`: Para construir a interface do usuário. Visite [Flet for Python Docs](https://pypi.org/project/flet/) para mais informações.
- `google.generativeai`: Para acessar o modelo Gemini Pro. Execute ``
- `dotenv e os`: Para gerenciar chaves de API

### Configuração:

1. **Instale as dependências:** `pip install flet python-dotenv google.generativeai` 
2. **Obtenha uma chave de API da Google:** Acesse [https://ai.google.dev/](https://ai.google.dev/) e siga as instruções para criar uma chave de API para o Google Generative AI.
3. **Insira sua chave de API:** Crie um arquivo .env na raiz do seu diretório seguindo o .env.example

### Executando o aplicativo:

1. Basta executar o arquivo `main.py`
2. A linha `ft.app(main, view=ft.WEB_BROWSER)` faz com que a visualização seja no navegador e não em janela como se fosse um programa. Por padrão, ao executar o `main.py`, você terá uma visualização em janela como se fosse um programa. Se quiser visualizar no navegador, basta adicionar o parâmetro`view=ft.WEB_BROWSER` em `ft.app(main)`

```python
ft.app(main, view=ft.WEB_BROWSER) # No navegador
ft.app(main) # Em janela como se fosse um programa
```


### Notas:
- Esta versão ainda está sujeita  à melhorias na interface e funcionalidades.
- Este código usa o modelo `gemini-1.5-pro-latest`. Você pode explorar outros modelos disponíveis na documentação da Google Generative AI.
- O estilo e o conteúdo do README gerado dependerão do seu prompt.
- Certifique-se de ter uma conexão com a internet para usar o modelo Gemini Pro.
- Divirta-se gerando READMEs incríveis! 


#

✨ Made with ❤️ by README.ai
