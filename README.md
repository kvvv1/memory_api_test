# 📊 API de Transparência - Matuzinhos

Sistema de APIs construído com Flask + Supabase para acesso a dados públicos do portal de transparência.

---

## 🔗 Endpoints Disponíveis

### 1. `/despesas/por-projeto`
Busca despesas agrupadas por projeto/atividade.

**Parâmetros disponíveis (GET):**
- `des_projetoatividade`: (texto parcial do projeto)

### 2. `/despesas/extra`
Despesas extras por fornecedor.

**Parâmetros disponíveis:**
- `fornecedor_nome`: nome parcial do fornecedor
- `valor_extra`: valor exato

### 3. `/servidores/diarias`
Consulta de diárias pagas a servidores.

**Parâmetros disponíveis:**
- `nome_servidor`
- `valor_pago`

### 4. `/servidores/gastos`
Consulta de salários e proventos.

**Parâmetros disponíveis:**
- `nome_servidor`
- `mes_referencia`

### 5. `/servidores`
Consulta de cadastro de servidores.

**Parâmetros disponíveis:**
- `nome_servidor`
- `situacao_atual`

### 6. `/prestacao-de-contas`
Arquivos da prestação de contas.

**Parâmetros disponíveis:**
- `ano`
- `mes`

### 7. `/receita`
Empenhos recebidos por fornecedor.

**Parâmetros disponíveis:**
- `Fornecedor`
- `Empenhado (R$)`

### 8. `/licitacoes`
Consulta de licitações e contratos.

**Parâmetros disponíveis:**
- `fornecedor_nome`
- `numero_licitacao`

---

## ✅ Resposta Padrão
Todas as rotas retornam um JSON com os dados filtrados, diretamente do Supabase.

## ❌ Erros
- `500`: Erro interno do servidor
- `400`: Parâmetro inválido

---
