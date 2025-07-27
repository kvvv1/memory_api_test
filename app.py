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

# 1. /despesas/por-projeto
def build_despesas_por_projeto_params(args):
    params = {}
    if 'des_projetoatividade' in args:
        params['des_projetoatividade'] = STR_FILTER(args['des_projetoatividade'])
    return params

@app.route('/despesas/por-projeto', methods=['GET'])
def despesas_por_projeto():
    params = build_despesas_por_projeto_params(request.args)
    data, status = supabase_get('despesa_por_projeto', params)
    return jsonify(data), status

# 2. /despesas/extra
def build_despesas_extra_params(args):
    params = {}
    if 'fornecedor_nome' in args:
        params['fornecedor_nome'] = STR_FILTER(args['fornecedor_nome'])
    if 'valor_extra' in args:
        valor = safe_float(args['valor_extra'])
        if valor is not None:
            params['valor_extra'] = NUM_FILTER(valor)
    return params

@app.route('/despesas/extra', methods=['GET'])
def despesas_extra():
    params = build_despesas_extra_params(request.args)
    data, status = supabase_get('despesa_extra', params)
    return jsonify(data), status

# 3. /servidores/diarias
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

# 4. /servidores/gastos
def build_servidores_gastos_params(args):
    params = {}
    if 'nome_servidor' in args:
        params['nome_servidor'] = STR_FILTER(args['nome_servidor'])
    if 'mes_referencia' in args:
        params['mes_referencia'] = STR_FILTER(args['mes_referencia'])
    return params

@app.route('/servidores/gastos', methods=['GET'])
def servidores_gastos():
    params = build_servidores_gastos_params(request.args)
    data, status = supabase_get('pessoal_gasto', params)
    return jsonify(data), status

# 5. /servidores 
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

# 6. /prestacao-de-contas
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

# 7. /receita
def build_receita_params(args):
    params = {}
    if 'Fornecedor' in args:
        params['Fornecedor'] = STR_FILTER(args['Fornecedor'])
    if 'Empenhado (R$)' in args:
        params['Empenhado (R$)'] = NUM_FILTER(args['Empenhado (R$)'])
    return params

@app.route('/receita', methods=['GET'])
def receita():
    params = build_receita_params(request.args)
    data, status = supabase_get('receita', params)
    return jsonify(data), status

# 8. /licitacoes
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