from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user


from .models import Paciente, Profissional, Agendamento
from . import db
from datetime import datetime, date


data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('login.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/paciente')
@login_required
def paciente():
    return render_template('paciente.html', name=current_user.name)


@main.route('/paciente', methods=['GET', 'POST'])
@login_required
def paciente_post():
    if request.method == 'POST':
        nome_paciente = request.form.get('nome_paciente')
        sexo = request.form.get('sexo')
        data_nasc = request.form.get('data_nasc')
        cpf = request.form.get('cpf')
        logradouro = request.form.get('logradouro')
        numero = request.form.get('numero')
        bairro = request.form.get('bairro')
        cep = request.form.get('cep')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        existing_patient = Paciente.query.filter_by(cpf=cpf).first()
        if existing_patient:
            flash('CPF já cadastrado.', 'error')
            return render_template('paciente.html', mensagem_erro='CPF já cadastrado.', **request.form)

        else:
            paciente = Paciente(nome_paciente=nome_paciente, sexo=sexo, data_nasc=data_nasc, cpf=cpf, logradouro=logradouro,
                                numero=numero, bairro=bairro, cep=cep, cidade=cidade, estado=estado, email=email,
                                telefone=telefone)

        db.session.add(paciente)
        db.session.commit()
        return redirect(url_for('main.consulta3'))

    return render_template('paciente.html', name=current_user.name)


@main.route('/profissional')
@login_required
def profissional():
    return render_template('profissional.html', name=current_user.name)


@main.route('/profissional', methods=['GET', 'POST'])
@login_required
def profissional_post():
    if request.method == 'POST':
        nome_profissional = request.form.get('nome_profissional')
        sexo = request.form.get('sexo')
        data_nasc = request.form.get('data_nasc')
        cpf = request.form.get('cpf')
        cro = request.form.get('cro')
        logradouro = request.form.get('logradouro')
        numero = request.form.get('numero')
        bairro = request.form.get('bairro')
        cep = request.form.get('cep')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        existing_profissional = Profissional.query.filter_by(cpf=cpf).first()
        if existing_profissional:
            flash('CPF já cadastrado.', 'error')
            return render_template('profissional.html', mensagem_erro='CPF já cadastrado.', **request.form)

        else:
            profissional = Profissional(nome_profissional=nome_profissional, sexo=sexo, data_nasc=data_nasc, cpf=cpf, cro=cro, logradouro=logradouro,
                                numero=numero, bairro=bairro, cep=cep, cidade=cidade, estado=estado, email=email,
                                telefone=telefone)

        db.session.add(profissional)
        db.session.commit()
        return redirect(url_for('main.consulta4'))

    return render_template('profissional.html', name=current_user.name)


@main.route('/consulta3')  # consulta a entidade
@login_required
def consulta3():
    paciente = Paciente.query.all()
    for dado in paciente:
        # Converte a string da data de nascimento para objeto datetime e formata
        dado.data_nasc = datetime.strptime(dado.data_nasc, '%Y-%m-%d').strftime('%d/%m/%Y')
        return render_template('consulta3.html', name=current_user.name, paciente=paciente)

@main.route('/consulta4')  # consulta o profissional
@login_required
def consulta4():
    profissional = Profissional.query.all()
    for dado in profissional:
        # Converte a string da data de nascimento para objeto datetime e formata
        dado.data_nasc = datetime.strptime(dado.data_nasc, '%Y-%m-%d').strftime('%d/%m/%Y')
        return render_template('consulta4.html', name=current_user.name, profissional=profissional) 


@main.route("/excluir3/<int:id>", methods=['GET', 'POST'])
@login_required
def excluir3(id):
    paciente = Paciente.query.filter_by(id=id).first()
    if request.method == 'POST':
        if paciente:
            db.session.delete(paciente)
            db.session.commit()
            return redirect(url_for('main.consulta3'))
    return render_template('delete.html')


@main.route("/excluir4/<int:id>", methods=['GET', 'POST'])
@login_required
def excluir4(id):
    profissional = Profissional.query.filter_by(id=id).first()
    if request.method == 'POST':
        if profissional:
            db.session.delete(profissional)
            db.session.commit()
            return redirect(url_for('main.consulta4'))
    return render_template('delete.html')


@main.route("/visualizar3/<int:id>", methods= ['GET', 'POST'])
def visualizar3(id):
    paciente = Paciente.query.filter_by(id=id).first()
    if request.method == 'POST':
        if paciente:
            db.session.delete(paciente)
            db.session.commit()

            nome_paciente = request.form.get('nome_paciente')
            data_nasc = request.form.get('data_nasc')
            sexo = request.form.get('sexo')
            cpf = request.form.get('cpf')
            logradouro = request.form.get('logradouro')
            numero = request.form.get('numero')
            bairro = request.form.get('bairro')
            cep = request.form.get('cep')
            cidade = request.form.get('cidade')
            estado = request.form.get('estado')
            email = request.form.get('email')
            telefone = request.form.get('telefone')

            paciente = Paciente(nome_paciente=nome_paciente, sexo=sexo, data_nasc=data_nasc,  cpf=cpf, logradouro=logradouro,
                                numero=numero, bairro=bairro, cep=cep,
                                cidade=cidade, estado=estado, email=email,
                                telefone=telefone)

            db.session.add(paciente)
            db.session.commit()
        return redirect(url_for('main.visualizar3'))
    return render_template('visualizar3.html', paciente=paciente)


@main.route("/atualizar3/<int:id>", methods=['GET', 'POST'])
@login_required
def atualizar3(id):
    paciente = Paciente.query.filter_by(id=id).first()
    if request.method == 'POST':
        if paciente:
            db.session.delete(paciente)
            db.session.commit()

            nome_paciente = request.form.get('nome_paciente')
            data_nasc = request.form.get('data_nasc')
            sexo = request.form.get('sexo')
            cpf = request.form.get('cpf')
            logradouro = request.form.get('logradouro')
            numero = request.form.get('numero')
            bairro = request.form.get('bairro')
            cep = request.form.get('cep')
            cidade = request.form.get('cidade')
            estado = request.form.get('estado')
            email = request.form.get('email')
            telefone = request.form.get('telefone')

            paciente = Paciente(nome_paciente=nome_paciente, sexo=sexo, data_nasc=data_nasc,  cpf=cpf, logradouro=logradouro,
                                numero=numero, bairro=bairro, cep=cep,
                                cidade=cidade, estado=estado, email=email,
                                telefone=telefone)

            db.session.add(paciente)
            db.session.commit()
        return redirect(url_for('main.consulta3'))
    return render_template('atualizar3.html', paciente=paciente)

@main.route("/visualizar4/<int:id>", methods= ['GET', 'POST'])
def visualizar4(id):
    profissional = Profissional.query.filter_by(id=id).first()
    if request.method == 'POST':
        if profissional:
            db.session.delete(profissional)
            db.session.commit()

            nome_profissional = request.form.get('nome_profissional')
            data_nasc = request.form.get('data_nasc')
            sexo = request.form.get('sexo')
            cpf = request.form.get('cpf')
            cro = request.form.get('cro')
            logradouro = request.form.get('logradouro')
            numero = request.form.get('numero')
            bairro = request.form.get('bairro')
            cep = request.form.get('cep')
            cidade = request.form.get('cidade')
            estado = request.form.get('estado')
            email = request.form.get('email')
            telefone = request.form.get('telefone')

            profissional = Profissional(nome_profissional=nome_profissional, sexo=sexo, data_nasc=data_nasc,  cpf=cpf, cro=cro, logradouro=logradouro,
                                numero=numero, bairro=bairro, cep=cep,
                                cidade=cidade, estado=estado, email=email,
                                telefone=telefone)

            db.session.add(profissional)
            db.session.commit()
        return redirect(url_for('main.visualizar4'))
    return render_template('visualizar4.html', profissional=profissional)


@main.route("/atualizar4/<int:id>", methods=['GET', 'POST'])
@login_required
def atualizar4(id):
    profissional = Profissional.query.filter_by(id=id).first()
    if request.method == 'POST':
        if profissional:
            db.session.delete(profissional)
            db.session.commit()

            nome_profissional = request.form.get('nome_profissional')
            sexo = request.form.get('sexo')
            data_nasc = request.form.get('data_nasc')
            cpf = request.form.get('cpf')
            cro = request.form.get('cro')
            logradouro = request.form.get('logradouro')
            numero = request.form.get('numero')
            bairro = request.form.get('bairro')
            cep = request.form.get('cep')
            cidade = request.form.get('cidade')
            estado = request.form.get('estado')
            email = request.form.get('email')
            telefone = request.form.get('telefone')

            profissional = Profissional(nome_profissional=nome_profissional, data_nasc=data_nasc, sexo=sexo,  cpf=cpf, cro=cro, logradouro=logradouro,
                            numero=numero, bairro=bairro, cep=cep,
                            cidade=cidade, estado=estado, email=email,
                            telefone=telefone)

            db.session.add(profissional)
            db.session.commit()
            return redirect(url_for('main.consulta4'))
    return render_template('atualizar4.html', profissional=profissional)

@main.route('/agendamento', methods=['GET', 'POST'])
def agendamento():
    profissionais = Profissional.query.all()
    pacientes = Paciente.query.all()

    if request.method == 'POST':
        data_string = request.form['data']
        data = datetime.strptime(data_string, '%Y-%m-%d').date()
        horario = request.form['horario']
        profissional_id = request.form['profissional']
        paciente_id = request.form['paciente']

        horarios_agendados = Agendamento.query.filter_by(data=data, horario=horario, profissional_id=profissional_id).all()
        if horarios_agendados:
            flash('Horário indisponível para o profissional selecionado.', 'error')
        else:
            novo_agendamento = Agendamento(data=data, horario=horario, profissional_id=profissional_id, paciente_id=paciente_id)
            db.session.add(novo_agendamento)
            db.session.commit()
            flash('Agendamento realizado com sucesso.', 'success')
            return redirect(url_for('main.agendamento'))  # Corrigido para redirecionar para 'main.agendamento'

    return render_template('agendamento.html', profissionais=profissionais, pacientes=pacientes)



@main.route('/lista_atendimento', methods=['GET', 'POST'])
def lista_atendimento():
    data_filtrada = None
    if request.method == 'POST':
        data_selecionada = request.form['data']
        data_filtrada = Agendamento.query.filter_by(data=data_selecionada).all()
    else:
        data_atual = date.today()
        data_filtrada = Agendamento.query.filter_by(data=data_atual).all()

    # Carregar dados dos profissionais
    profissionais = Profissional.query.all()

    # Carregar dados dos pacientes
    pacientes = Paciente.query.all()

    return render_template('lista_atendimento.html', data_filtrada=data_filtrada, profissionais=profissionais, pacientes=pacientes)

