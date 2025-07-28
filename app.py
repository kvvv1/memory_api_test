from flask import Flask, request, jsonify
from services.supabase_client import supabase_get
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Utilitário para construir filtros Supabase
STR_FILTER = lambda v: f'ilike.*{v}*'
NUM_FILTER = lambda v: f'eq.{v}'

def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None



# /despesas/por-projeto
def build_despesas_por_projeto_params(args):
    params = {}
    if 'des_projetoatividade' in args:
        params['des_projetoatividade'] = STR_FILTER(args['des_projetoatividade'])
    if 'cod_projetoatividade' in args:
        cod = safe_float(args['cod_projetoatividade'])
        if cod is not None:
            params['cod_projetoatividade'] = NUM_FILTER(int(cod))
    return params


@app.route('/despesas/por-projeto', methods=['GET'])
def despesas_por_projeto():
    params = build_despesas_por_projeto_params(request.args)
    data, status = supabase_get('despesa_por_projeto', params)
    return jsonify(data), status

# /despesas/extra
def build_despesas_extra_params(args):
    params = {}
    if 'fornecedor_nome' in args:
        params['fornecedor_nome'] = STR_FILTER(args['fornecedor_nome'])
    if 'valor_extra' in args:
        valor = safe_float(args['valor_extra'])
        if valor is not None:
            params['valor_extra'] = NUM_FILTER(valor)
    if 'numero_extra' in args:
        numero = safe_float(args['numero_extra'])
        if numero is not None:
            params['numero_extra'] = NUM_FILTER(int(numero))
    return params

@app.route('/despesas/extra', methods=['GET'])
def despesas_extra():
    params = build_despesas_extra_params(request.args)
    data, status = supabase_get('despesa_extra', params)
    return jsonify(data), status

# /despesas/por-secretaria

def build_despesas_por_secretaria_params(args):
    params = {}
    if 'codigo_unidade' in args:
        params['codigo_unidade'] = NUM_FILTER(args['codigo_unidade'])
    if 'descricao_unidade' in args:
        params['descricao_unidade'] = STR_FILTER(args['descricao_unidade'])
    if 'valor_pago' in args:
        valor = safe_float(args['valor_pago'])
        if valor is not None:
            params['valor_pago'] = NUM_FILTER(valor)
    return params

@app.route('/despesas/por-secretaria', methods=['GET'])
def despesas_por_secretaria():
    params = build_despesas_por_secretaria_params(request.args)
    data, status = supabase_get('despesa_por_secretaria', params)
    return jsonify(data), status

# despesas/por_elemento

def build_despesas_por_elemento_params(args):
    params = {}
    if 'id_elemento' in args:
        params['id_elemento'] = STR_FILTER(args['id_elemento'])
    if 'descricao' in args:
        params['descricao'] = STR_FILTER(args['descricao'])
    return params

@app.route('/despesas/por-elemento', methods=['GET'])
def despesas_por_elemento():
    params = build_despesas_por_elemento_params(request.args)
    data, status = supabase_get('despesa_por_elemento', params)
    return jsonify(data), status


# /servidores/diarias
def build_servidores_diarias_params(args):
    params = {}
    if 'nome_servidor' in args:
        params['nome_servidor'] = STR_FILTER(args['nome_servidor'])
    if 'valor_pago' in args:
        params['valor_pago'] = NUM_FILTER(args['valor_pago'])
    return params


@app.route('/servidores/diarias', methods=['GET'])
def servidores_diarias():
    params = build_servidores_diarias_params(request.args)
    data, status = supabase_get('pessoal_diaria', params)
    return jsonify(data), status

# /servidores/gastos
def build_servidores_gastos_params(args):
    params = {}
    if 'nome_servidor' in args:
        params['nome_servidor'] = STR_FILTER(args['nome_servidor'])
    if 'mes_referencia' in args:
        params['mes_referencia'] = STR_FILTER(args['mes_referencia'])
    if 'numero_matricula' in args:
        matricula = safe_float(args['numero_matricula'])
        if matricula is not None:
            params['numero_matricula'] = NUM_FILTER(int(matricula))
    return params

@app.route('/servidores/gastos', methods=['GET'])
def servidores_gastos():
    params = build_servidores_gastos_params(request.args)
    data, status = supabase_get('pessoal_gasto', params)
    return jsonify(data), status

def build_servidores_params(args):
    params = {}
    if 'nome_servidor' in args:
        params['nome_servidor'] = STR_FILTER(args['nome_servidor'])
    if 'situacao_atual' in args:
        params['situacao_atual'] = STR_FILTER(args['situacao_atual'])
    if 'numero_matricula' in args:
        params['numero_matricula'] = NUM_FILTER(args['numero_matricula'])
    return params

@app.route('/servidores', methods=['GET'])
def servidores():
    params = build_servidores_params(request.args)
    data, status = supabase_get('pessoal_servidores', params)
    return jsonify(data), status

# /prestacao-de-contas
def build_prestacao_de_contas_params(args):
    params = {}
    if 'ano' in args:
        params['ano'] = NUM_FILTER(args['ano'])
    if 'mes' in args:
        params['mes'] = NUM_FILTER(args['mes'])
    return params

@app.route('/prestacao-de-contas', methods=['GET'])
def prestacao_de_contas():
    params = build_prestacao_de_contas_params(request.args)
    data, status = supabase_get('prestacacaodecontas', params)
    return jsonify(data), status

# /receita
def build_receita_params(args):
    params = {}
    if 'Fornecedor' in args:
        params['Fornecedor'] = STR_FILTER(args['Fornecedor'])
    if 'Empenhado (R$)' in args:
        params['Empenhado (R$)'] = NUM_FILTER(args['Empenhado (R$)'])
    if 'Data Empenho' in args:  
        params['Data Empenho'] = STR_FILTER(args['Data Empenho'])
    return params



@app.route('/receita', methods=['GET'])
def receita():
    params = build_receita_params(request.args)
    data, status = supabase_get('receita', params)
    return jsonify(data), status

@app.route('/receita/total', methods=['GET'])
def receita_total():
    params = build_receita_params(request.args)
    data, status = supabase_get('receita', params)

    try:
        total = sum(float(row.get('Empenhado (R$)', 0)) for row in data)
    except (ValueError, TypeError):
        total = 0

    return jsonify({'total_receita': total}), status


# /licitacoes
def build_licitacoes_params(args):
    params = {}
    if 'fornecedor_nome' in args:
        params['fornecedor_nome'] = STR_FILTER(args['fornecedor_nome'])
    if 'numero_licitacao' in args:
        params['numero_licitacao'] = STR_FILTER(args['numero_licitacao'])
    return params

@app.route('/licitacoes', methods=['GET'])
def licitacoes():
    params = build_licitacoes_params(request.args)
    data, status = supabase_get('licitacao_contrato', params)
    return jsonify(data), status

# Fallback de erro global
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Erro interno do servidor'}), 500

# Configuração do Swagger UI
SWAGGER_URL = '/docs'
API_URL = '/static/swagger_transparencia.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Transparência API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True) 