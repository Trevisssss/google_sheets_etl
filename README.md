# 📊 Google Sheets ETL with Python

## 🔗 Sobre o Projeto

Este projeto demonstra uma conexão automatizada e segura entre Python e Google Sheets. Utilizando a API oficial do Google e uma conta de serviço, ele realiza a extração (Extract) de dados de uma planilha, transforma-os (Transform) em um DataFrame do Pandas e prepara o terreno para carregá-los (Load) em outro destino, completando um ciclo ETL simples e eficiente.

O foco é apresentar uma solução robusta que pode ser facilmente integrada a pipelines de dados mais complexos.

## ✨ Principais Vantagens

### 🚀 Eficiência e Desempenho
- **Automatização Completa**: Elimina a necessidade de baixar arquivos CSV/Excel manualmente, integrando a fonte de dados diretamente no script.
- **Análise Direta com Pandas**: Os dados são carregados diretamente em um DataFrame do Pandas, a principal ferramenta para análise e manipulação de dados em Python, permitindo uma análise imediata.
- **Leitura Rápida**: A API é otimizada para ler grandes volumes de dados de forma eficiente, como demonstrado no script.

### 🔐 Segurança e Boas Práticas
- **Acesso Seguro via Conta de Serviço**: A autenticação é feita sem expor credenciais de usuário, utilizando um arquivo de credenciais JSON que concede permissões específicas ao script.
- **Gerenciamento de Segredos**: Dados sensíveis, como o nome do arquivo de credenciais e o ID da planilha, são gerenciados fora do código-fonte através de variáveis de ambiente (arquivo `.env`), evitando que informações confidenciais sejam versionadas no Git.

### 💼 Flexibilidade e Escalabilidade
- **Configuração por Ambiente**: O uso do arquivo `.env` facilita a configuração para diferentes ambientes (desenvolvimento, produção) sem alterar o código.
- **Solução Escalável**: A arquitetura é adequada tanto para pequenos projetos quanto para pipelines de dados de grande porte que consomem dados de múltiplas planilhas.
- **Ecossistema Google**: Totalmente compatível com o Google Workspace e Google Cloud Platform, garantindo manutenção e confiabilidade.

## ⚙️ Como Configurar e Executar

Siga os passos abaixo para rodar o projeto localmente.

### 1. Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

### 2. Configuração do Ambiente Google Cloud
1.  **Ative a API do Google Sheets**:

    -   Acesse o Google Cloud Console.
    -   Crie um novo projeto ou selecione um existente.
    -   No menu de navegação, vá para "APIs & Services" > "Library".
    -   Procure por "Google Sheets API" e clique em "Enable".

2.  **Crie uma Conta de Serviço**:
    -   Vá para "APIs & Services" > "Credentials".
    -   Clique em "Create Credentials" > "Service account".
    -   Preencha os detalhes da conta de serviço e conceda a ela um papel apropriado (por exemplo, "Viewer" para acesso de leitura).

3.  **Gere a Chave JSON**:

    -   Após criar a conta de serviço, clique nela na lista de credenciais.
    -   Vá para a aba "KEYS".
    -   Clique em "ADD KEY" > "Create new key".
    -   Selecione "JSON" como o tipo de chave e clique em "Create". O download do arquivo JSON começará automaticamente.

4.  **Compartilhe a Planilha**:
    -   Abra a planilha do Google Sheets que você deseja acessar.
    -   Clique em "Share" (Compartilhar) no canto superior direito.
    -   Copie o endereço de e-mail da conta de serviço (encontrado nos detalhes da credencial no Cloud Console) e cole-o no campo de compartilhamento.
    -   Conceda a permissão apropriada (pelo menos "Viewer" para leitura).

O Código para a conexão com a planilha é encontrado no script `google_sheets.py`

> Esse código pode ser adaptado para retornar apenas um dataframe a partir de uma função, e depois ser utilizada em outro escopo, como uma pipeline de dados, e ser direcionado para outro local, como por exemplo um Banco de Dados.