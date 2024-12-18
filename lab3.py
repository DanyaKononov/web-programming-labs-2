from flask import Blueprint, url_for, redirect, render_template, request, make_response
lab3 = Blueprint("lab3", __name__)


@lab3.route('/lab3/')
def labor3():
		name = request.cookies.get('name')
		name_color = request.cookies.get('name_color')
		return render_template('lab3/lab3.html', name=name, name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
		resp = make_response(redirect('/lab3/'))
		resp.set_cookie('name', 'Alex', max_age=1)
		resp.set_cookie('age', '20', max_age=1)
		resp.set_cookie('name_color', 'grey', max_age=1)
		return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
		resp = make_response(redirect('/lab3/'))
		resp.delete_cookie('name')
		resp.delete_cookie('age')
		resp.delete_cookie('name_color')
		return resp


@lab3.route('/lab3/form1')
def formul():
		errors = {}
		user = request.args.get('user')
		if user == '':
			errors['user'] = 'Заполните поле!'
		age = request.args.get('age')
		if age == '':
			errors['age'] = 'Заполните поле!'
		sex = request.args.get('sex')
		return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
		return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
		global price
		drink = request.args.get('drink')
		if drink == 'coffee':
			price = 120
		elif drink == 'black-tea':
			price = 80
		else:
			price = 70
		
		if request.args.get('milk') == 'on':
			price +=30
		if request.args.get('sugar') == 'on':
			price +=10
		return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def	good():
		return render_template('/lab3/success.html', price = price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    backgroundcolor = request.args.get('backgroundcolor')
    fontsize = request.args.get('fontsize')
    if color or backgroundcolor or fontsize:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('color', color)
        resp.set_cookie('backgroundcolor', backgroundcolor)
        resp.set_cookie('fontsize', fontsize)
        return resp
    
    color = request.cookies.get('color')
    backgroundcolor = request.cookies.get('backgroundcolor')
    fontsize = request.cookies.get('fontsize')
    resp = make_response(render_template('lab3/settings.html', color=color, backgroundcolor=backgroundcolor, fontsize=fontsize))
    return resp


@lab3.route('/lab3/ticket')
def ticket():
    return render_template('lab3/ticket.html')


@lab3.route('/lab3/TicketPay')
def pay_ticket():
    price_ticket = 0
    years = request.args.get('years')
    if int(years) > 18:
        price_ticket = 1500
        bilet = 'Взрослый'
    else:
        price_ticket = 750
        bilet = 'Детский'

    if request.args.get('shelf') == 'нижняя' or request.args.get('shelf') == 'нижняя боковая':
        price_ticket += 200
    
    if request.args.get('withunderwear') == 'Да':
        price_ticket += 150

    if request.args.get('withbag') == 'Да':
        price_ticket += 250
    if request.args.get('withinsurance') == 'Да':
        price_ticket += 300
    return render_template('/lab3/TicketPay.html',price_ticket = price_ticket, bilet = bilet )


@lab3.route('/lab3/delete_new')
def delete_n():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('fontsize')
    resp.delete_cookie('backgroundcolor')
    resp.delete_cookie('color')
    return resp
