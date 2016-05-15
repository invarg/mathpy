from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate as auth, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect   # Add this
# import html helper
from ..function.html_h import set_template, content


def account(request, view=''):
    fl = request.user.is_authenticated()
    if fl:
        # user is logged in
            # change password
        if request.method == 'POST':
            user_name = request.POST['user_name']
            password = request.POST['password']
            user = auth(username=user_name, password=password)
            if view == 'password' and user is not None:
                if user.is_active:
                    pass
                    #login(request, user)
                    msg = 'Redirect to a success page'
                else:
                    msg = "Return a 'disabled account' error message"
                    pass
                l = set_template('account', 'signup', request.user.is_authenticated())
                return render(request, 'account/password.html', {'msg': msg, 'm': l})
            else:
                pass
            # Return an 'invalid login' error message.
        else:
            if view == 'logoff':    # log off
                from django.contrib.auth import logout
                logout(request)
                msg = 'signed out'
                fl = False
            elif view == 'password':    # change password
                msg = 'change password'
                l = set_template('account', view, request.user.is_authenticated())
                return render(request, 'account/password.html', {'msg': msg, 'm': l})
            else:                       # user info
                view = 'edit'
                msg = 'account info'
    else:
        # user is not logged in
            # login event
        if request.method == 'POST':
            if view == 'login':
                user_name = request.POST['user_name']
                password = request.POST['password']
                user = auth(username=user_name, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        msg = "User is valid, active and authenticated"
                        view = 'edit'
                        return redirect('/account/edit/')
                    else:
                        msg = "The password is valid, but the account has been disabled!"
                else:
                    msg = "The username and password were incorrect."
            elif view == 'signup':
                msg = "Sign up."
            else:
                msg = "Something else."
        else:
                # show sign up form
            if view == 'signup':
                msg = 'sign up'
                l = set_template('account', 'signup', request.user.is_authenticated())
                return render(request, 'account/signup.html', {'msg': msg, 'm': l})
            else:
                # show login form
                msg = 'log in' #a
                l = set_template('account', 'login', request.user.is_authenticated())
                return render(request, 'account/login.html', {'msg': msg, 'm': l})
    l = set_template('account', view, request.user.is_authenticated())
    return render(request, 'account/account.html', {'msg': msg, 'm': l})


@csrf_exempt    # This skips csrf validation. Use csrf_protect to have validation
def user_check(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    user = auth(username=user_name, password=password)
    if user is not None:
        if user.is_active:
            msg = "" #"User is valid, active and authenticated"
        else:
            msg = "The password is valid, but the account has been disabled!"
    else:
        msg = "The username and password were incorrect."
    #response = JsonResponse({'msg': msg})
    return JsonResponse({'res': msg})