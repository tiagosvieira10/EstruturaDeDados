# Estrutura de Dados - Projetos em Python

Este repositório contém dois projetos desenvolvidos em Python com foco em estrutura de dados e aplicação prática dos conceitos de **listas encadeadas** e **tabelas hash**. Ambos os projetos simulam cenários reais com regras específicas de negócio.

---

## 📌 Projeto 1: Sistema de Triagem Hospitalar

Simula o processo de atendimento em um hospital com base em **prioridade de urgência**. Os pacientes são classificados com cartões **verdes (V)** ou **amarelos (A)**, sendo os amarelos considerados mais urgentes.

### Regras de Atendimento:

- Pacientes com cartão amarelo são sempre atendidos antes dos pacientes com cartão verde.
- Dentro da mesma cor, os pacientes com **números menores têm prioridade**.
- Numeração:
  - Cartões verdes começam em 1.
  - Cartões amarelos começam em 201.

### Estrutura Utilizada:

- **Lista Encadeada Simples** com inserção em ordem de prioridade:
  - `inserirSemPrioridade()` → insere no final da lista.
  - `inserirComPrioridade()` → insere após os cartões amarelos.
- Interface via **menu interativo** com as opções:
  - Adicionar paciente.
  - Listar fila de espera.
  - Chamar paciente.
  - Sair do sistema.

### Funcionalidades:

- Implementação de nodos com número, cor e ponteiro.
- Inserção automática da numeração.
- Impressão completa da fila.
- Atendimento do primeiro paciente da fila.

---

## 📌 Projeto 2: Sistema de Emplacamento de Veículos por Hash

Sistema baseado em uma **tabela hash de 10 posições** para representar o final das placas dos veículos, relacionando cada número a um estado brasileiro.

### Regras da Função Hash:

- Se a sigla for `DF`, o índice é sempre `7` (exceção por superstição).
- Para os demais estados:



### Estrutura Utilizada:

- **Tabela Hash com Endereçamento em Cadeia**:
- Cada posição é uma lista encadeada simples.
- Inserção sempre no início da lista.

### Funcionalidades:

- Inserção dos 26 estados + Distrito Federal.
- Impressão da tabela antes e depois da inserção.
- Inserção de um estado **fictício** com sigla gerada a partir do nome e sobrenome (ex: "Bruno Kostiuk" → `BK`).

---

## 💻 Tecnologias Utilizadas

- Python 3
- Estruturas: Lista Encadeada, Tabela Hash
- Conceitos: Estrutura de dados, função hash, manipulação de ASCII, controle por menu
