from flask import Blueprint, render_template, request
from database.models.cliente import Cliente


cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')
def lista_clientes():
    """listar os clientes"""

    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """inserir os dados do cliente"""

    data = request.json
    
    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email']
    )

    return render_template('item_cliente.html', cliente=novo_usuario), {"status": "cliente adicionado com sucesso!"}
    

@cliente_route.route('/new')
def form_cliente():
    """formulário para cadastrar um cliente"""
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """exibir detalhes do cliente"""

    cliente = Cliente.get_by_id(cliente_id)
    # Ou
    # cliente = Cliente.get(Cliente.id == cliente_id)

    return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """formulario para editar um cliente"""

    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """atualizar informações de um cliente"""

    data = request.json

    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()


    return render_template('item_cliente.html', cliente=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):    
    """deletar informações de um cliente"""
    try:
        cliente = Cliente.get_by_id(cliente_id)
        cliente.delete_instance()

        return {'status-delete': 'cliente deletado com sucesso!'}

    except Exception:
        return {'erro': 'cliente_id não encontrado na lista.'}