# Desafio Final: Desenvolvimento de um Sistema de Gerenciamento de Inventário para uma Loja Virtual

## Objetivo

Desenvolver um sistema completo de gerenciamento de inventário para uma loja virtual. Este sistema deverá permitir o cadastro, atualização, exclusão e listagem de produtos, além de realizar vendas e gerar relatórios detalhados em formato CSV. O sistema deve ser robusto, eficiente, e capaz de lidar com erros de forma elegante.

## Descrição do Desafio

Imagine que você foi contratado por uma loja virtual para desenvolver um sistema interno que permita o gerenciamento completo do inventário de produtos. A loja vende uma variedade de produtos que variam em categorias, preços, e quantidades disponíveis. Eles precisam de uma solução que não só gerencie esses produtos, mas que também facilite as operações de venda, armazenamento de dados e geração de relatórios.

## Requisitos do Sistema

1. **Cadastro de Produtos:**

   - O sistema deve permitir o cadastro de novos produtos com as seguintes informações: nome, categoria, preço, quantidade em estoque, e descrição opcional.
   - A estrutura de dados utilizada para armazenar os produtos deve ser escolhida cuidadosamente, utilizando dicionários para indexar os produtos por um identificador único.

2. **Atualização de Produtos:**

   - Deve ser possível atualizar as informações dos produtos cadastrados, como preço, quantidade em estoque, e descrição.
   - Implemente mecanismos de validação para garantir que as atualizações sejam consistentes e que erros comuns (como preços negativos ou estoque insuficiente) sejam evitados.

3. **Exclusão de Produtos:**

   - O sistema deve permitir a exclusão de produtos do inventário. Utilize exceções para lidar com tentativas de exclusão de produtos que não existem.

4. **Realização de Vendas:**

   - O sistema deve permitir a realização de vendas, onde os clientes podem comprar múltiplos produtos em quantidades variáveis.
   - Ao registrar uma venda, o sistema deve atualizar automaticamente a quantidade em estoque de cada produto vendido.
   - Se o estoque for insuficiente para a quantidade desejada, o sistema deve lançar uma exceção específica, informando o usuário do erro.

5. **Relatórios de Vendas:**

   - O sistema deve gerar relatórios de vendas em formato CSV, contendo informações detalhadas como o nome do produto, quantidade vendida, preço unitário, valor total da venda e data/hora da transação.
   - Implemente funções de manipulação de arquivos para gravar esses dados em um arquivo CSV de forma eficiente e segura.

6. **Persistência de Dados:**

   - Os dados do inventário e as informações das vendas devem ser persistidos em arquivos de texto ou CSV, garantindo que nenhuma informação seja perdida entre execuções do programa.
   - Utilize o módulo CSV do Python para manipular os arquivos de dados.

7. **Tratamento de Exceções:**

   - O sistema deve ser capaz de lidar com exceções de forma robusta, lançando e capturando erros relacionados ao cadastro de produtos, atualização de estoque, exclusão de itens, e manipulação de arquivos.
   - Implemente suas próprias exceções personalizadas onde for necessário, por exemplo, para erros de estoque ou manipulação inadequada de dados.

8. **Interface com o Usuário:**

   - A interação com o usuário deve ser clara e amigável, oferecendo menus e opções que guiem o usuário durante o uso do sistema.
   - Utilize funções com diferentes tipos de parâmetros (`*args`, `**kwargs`) para tornar a interface mais flexível e permitir a customização de funcionalidades.

9. **Aplicação de Técnicas Funcionais:**

   - Utilize técnicas de programação funcional, como `map`, `filter` e `reduce`, para manipular e processar as listas de produtos e vendas de maneira eficiente.
   - Implemente funções lambda para operações simples que não necessitem de uma definição completa de função.

10. **Documentação:**
    - Documente detalhadamente o sistema, explicando a arquitetura, as decisões de design, como utilizar o sistema, e como os diferentes componentes interagem.
    - Inclua exemplos de uso para facilitar o entendimento dos usuários.

## Critérios de Avaliação

- **Funcionalidade:** O sistema atende a todos os requisitos especificados? Todas as operações (cadastro, atualização, exclusão, venda, geração de relatórios) funcionam corretamente?
- **Qualidade do Código:** O código está bem estruturado, legível e segue boas práticas de programação Python? As funções estão bem definidas e os nomes são intuitivos?
- **Tratamento de Exceções:** O sistema lida adequadamente com erros, fornecendo feedback claro ao usuário e garantindo que o programa continue funcionando corretamente?
- **Uso de Técnicas Funcionais:** As técnicas de programação funcional foram aplicadas de forma eficaz? As funções lambda, `map`, `filter`, e `reduce` foram utilizadas onde apropriado?
- **Persistência de Dados:** Os dados são armazenados corretamente em arquivos de texto ou CSV? O sistema garante que as informações sejam recuperadas corretamente em execuções subsequentes?
- **Documentação:** A documentação é completa, clara e útil? Inclui explicações sobre o funcionamento do sistema e exemplos práticos de uso?

## Exemplo de Situação Real

Um cliente deseja comprar três itens específicos de categorias diferentes. O estoque de um desses itens está baixo. Seu sistema deve identificar o problema, avisar o cliente sobre o estoque insuficiente, e sugerir alternativas (se houver). O sistema deve então processar a venda para os itens disponíveis, atualizar o estoque, e gerar um recibo detalhado em formato CSV.

Este desafio final visa consolidar e aplicar todos os conceitos aprendidos, promovendo uma experiência prática completa. O sucesso no projeto dependerá da sua capacidade de integrar e aplicar esses conhecimentos de forma eficiente e criativa. Boa sorte!