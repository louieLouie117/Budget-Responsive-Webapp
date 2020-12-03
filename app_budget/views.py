from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt



#User Login----------------------------------------------------------
def register_user(request):
    #erros
    errors = User.objects.register_validator(request.POST)
    print("erros found****", errors)

    if len(errors) > 0:
        # if the errors dictionary contains anything,
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        print(key)
        return redirect('/')
    else:
        #hash the password
        hash_browns = bcrypt.hashpw(request.POST['user_password'].encode(),
        bcrypt.gensalt()).decode()
        print('hassing', hash_browns)

        #create user
        print("User was added",request.POST)
        created_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            user_email = request.POST['user_email'],
            # user_password = request.POST['user_password'],replace with hash
            user_password = hash_browns

        )
        print('hash borwns',created_user.user_password)
        #set user in seesion
        request.session['uuid'] = created_user.id

        this_user = User.objects.get(id=request.session['uuid'])
        create_budget1 = Budget.objects.create(
            title = 'Home',
            posted_by = this_user
        )
        create_budget2 = Budget.objects.create(
            title = 'Bills/Utilites',
            posted_by = this_user
        )

        create_budget3 = Budget.objects.create(
            title = 'Personal',
            posted_by = this_user
        )
        create_budget4 = Budget.objects.create(
            title = 'Eating Out',
            posted_by = this_user
        )
        create_budget5 = Budget.objects.create(
            title = 'Transportation',
            posted_by = this_user
        )
        create_budget6 = Budget.objects.create(
            title = 'Giving',
            posted_by = this_user
        )

        print(create_budget1,create_budget2,create_budget3,create_budget4,create_budget5,create_budget6)
      
        return redirect('/app')

def login_user(request):
    #sending to dashboard
    print(request.POST)
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print(key)
        return redirect('/')
    else:
        #check if the email is in the db
        users_list = User.objects.filter(user_email= request.POST['user_email'])
        #set user in session
        request.session['uuid'] = users_list[0].id
        print(users_list[0].user_password)
        return redirect('/app')

def logout(request):
    #send to index
    request.session.flush()
    return redirect('/')



#pages----------------------------------------------------------------
def index(request):
    return render(request, 'index.html')

def show_dashboard(request):
    # check if user is not in session
    if 'uuid' not in request.session:
        return redirect('/')

    userby=User.objects.get(id=request.session['uuid'])

    total = 0
    all_transactions = Transaction.objects.all()
    for transaction in all_transactions:
        total += transaction.amount
    context = {
        'user': userby,
        # 'budget_list': Category.objects.filter(posted_by=userby)
        'budget_list': Category.objects.all(),
        'transactions_list': all_transactions,
        'show_total': total
        # 'amount_list': Transaction.objects.filter()
    }

    # if this_user.bugets.first().title == None:
    #     print("*"*50)
    #     print('there is not data yet')



    return render(request, 'dashboard.html', context)


#from actions-----------------------------------------------------------

def add_budget(request):
    print(request.POST)

    budget_instence = User.objects.get(id=request.session['uuid']).bugets.get(title= request.POST['budget'])
    new_budget = Category.objects.create(
        title = request.POST['budget_title'],
        notes= request.POST['budget_notes'],
        amount= request.POST['budget_amount'],
        budget= budget_instence
        )
    print(new_budget)
    return redirect('/app')


def add_bill(request):
    print(request.POST)
    user_instence = User.objects.get(id=request.session['uuid'])
    new_transcations = Transaction.objects.create(
        category = request.POST['category_budget'],
        title= request.POST['selected_titel'],
        notes= request.POST['user_notes'],
        amount= request.POST['spent_amount'],
        posted_by = user_instence
        )
    print(new_transcations)
    print(user_instence)
    return redirect('/app')



def add_home(request):
    print(request.POST)
    user_instence = User.objects.get(id=request.session['uuid'])
    new_transcations = Transaction.objects.create(
        category = request.POST['category_budget'],
        title= request.POST['selected_titel'],
        notes= request.POST['user_notes'],
        amount= request.POST['spent_amount'],
        posted_by = user_instence
        )
    print(new_transcations)
    print(user_instence)
    return redirect('/app')

    
def add_personal(request):
    print(request.POST)
    user_instence = User.objects.get(id=request.session['uuid'])
    new_transcations = Transaction.objects.create(
        category = request.POST['category_budget'],
        title= request.POST['selected_titel'],
        notes= request.POST['user_notes'],
        amount= request.POST['spent_amount'],
        posted_by = user_instence
        )
    print(new_transcations)
    print(user_instence)
    return redirect('/app')


def add_eating(request):
    print(request.POST)
    user_instence = User.objects.get(id=request.session['uuid'])
    new_transcations = Transaction.objects.create(
        category = request.POST['category_budget'],
        title= request.POST['selected_titel'],
        notes= request.POST['user_notes'],
        amount= request.POST['spent_amount'],
        posted_by = user_instence
        )
    print(new_transcations)
    print(user_instence)

    return redirect('/app')

def add_car(request):
    print(request.POST)
    user_instence = User.objects.get(id=request.session['uuid'])
    new_transcations = Transaction.objects.create(
        category = request.POST['category_budget'],
        title= request.POST['selected_titel'],
        notes= request.POST['user_notes'],
        amount= request.POST['spent_amount'],
        posted_by = user_instence
        )
    print(new_transcations)
    print(user_instence)
    return redirect('/app')



def add_giving(request):
    print(request.POST)
    user_instence = User.objects.get(id=request.session['uuid'])
    new_transcations = Transaction.objects.create(
        category = request.POST['category_budget'],
        title= request.POST['selected_titel'],
        notes= request.POST['user_notes'],
        amount= request.POST['spent_amount'],
        posted_by = user_instence
        )
    print(new_transcations)
    print(user_instence)
    return redirect('/app')


# delete items--------------------------------------
def delete_budget(request, budget_id):
    print(request.POST)
    this_item = Category.objects.get(id=budget_id)
    this_item.delete()
    return redirect('/app')


def delete_transaction(request, transaction_id):
    print(request.POST)
    this_item = Transaction.objects.get(id=transaction_id)
    this_item.delete()
    return redirect('/app')


