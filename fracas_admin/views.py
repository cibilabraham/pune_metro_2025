
from tracemalloc import start
from django.shortcuts import render, redirect
from numpy import product

from fracas.models import *
from fracas_admin.models import *
from django.views import View
from datetime import datetime, date, timedelta
import calendar
from pandas.tseries import offsets
from django.http import HttpResponse,JsonResponse
from urllib.parse import unquote
from nested_inline.admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline
from django.db.models import Count
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User,Group
from django.contrib import auth

import os
import xlrd

from django.db import connection
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.


class Index(View):
    template_name = 'indexPage.html'
    
    def get(self, request, *args, **kwargs):
        if 'login' in request.session:
            return redirect('/dashboard/')
        return render(request, self.template_name)
    
class UserLogin(View):
    template_name = 'indexHome.html'
    
    def get(self, request, *args, **kwargs):
        if 'login' in request.session:
            return redirect('/dashboard/')
        return render(request, self.template_name)
    
class Login(View):
    """ It was a view for the comp login view """
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if 'login' in request.session:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        if id != 1:
            return redirect('index')
        return render(request, self.template_name,{'id':id})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        message = ''
        if request.method == 'POST':
            req = self.request.POST
            email = req.get('email')
            password = req.get('password')
            auth_user = auth.authenticate(username=email, password=password, is_active=True)
            if auth_user:
                User_data =User.objects.filter(username=email)
                for UsersData in User_data:
                    if UserProfile.objects.filter(user_id=UsersData.id,is_disable=0,is_active=0).exists():
                        user_data = UserProfile.objects.filter(user_id=UsersData.id)
                        for u_data in user_data:
                            if 1 == u_data.user_role_id:
                                auth.login(request, auth_user)
                                request.session['P_id'] = 0
                                request.session['login'] = 'true'
                                request.session['email'] = email
                                request.session['user_Role'] = id
                                request.session['user_ID'] = u_data.user_id
                                now = datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                h = history(user_id=u_data.id,P_id=0,date=date.today(),time=current_time,message="Login",function_name="Manage Users")
                                h.save()
                                return redirect('/dashboard/')
                            else:
                                auth.login(request, auth_user)
                                request.session['P_id'] = u_data.product_id_id
                                x=Product.objects.filter(product_id=u_data.product_id_id)
                                request.session['P_name'] = x[0].product_name
                                request.session['login'] = 'true'
                                request.session['email'] = email
                                request.session['user_Role'] = u_data.user_role_id
                                request.session['user_ID'] = u_data.user_id
                                now = datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                h = history(user_id=u_data.id,P_id=u_data.product_id_id,date=date.today(),time=current_time,message="Login",function_name="Manage Users")
                                h.save()
                                return redirect('/dashboard/')
                    else:
                        message = 'Invalid credentials given'
                        return render(request, self.template_name, {"message": message,'id':id})
            else:
                message = 'Invalid credentials given'
        return render(request, self.template_name, {"message": message,'id':id})
    
class Logout(View):
    def get(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message="Logout",function_name="Manage Users")
        h.save()
        auth.logout(request)
        for key in request.session.keys():
            del request.session[key]
        return redirect('index')
    
class Dashboard(View):
    template_name = 'dashboard.html'
    
    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        return render(request, self.template_name)
    
class ListUsers(View):
    template_name = 'list_user.html'
    
    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4:
            return redirect('/dashboard/')
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        #print(user_Role)
        # print(req)
        if user_Role == 1:
            User_data =User.objects.filter(is_active=True).exclude(is_superuser=True)
            for UsersData in User_data:
                user_data =UserProfile.objects.filter(user_id=UsersData.id)
                for u_data in user_data:
                    product_data =Product.objects.filter(product_id=u_data.product_id_id)
                    userRole_data =Group.objects.filter(id=u_data.user_role_id)
                    for p_data in product_data:
                        for ur_data in userRole_data:
                            data.append({ 
                                'email' :  UsersData.username,
                                'first_name' : u_data.first_name,
                                'last_name' : u_data.last_name,
                                'user_role' : ur_data.name,
                                'product' : p_data.product_name,
                                'is_disable' : u_data.is_disable,
                                'id':UsersData.id,
                            })
        else:
            user_data =UserProfile.objects.filter(product_id_id=P_id,user_role_id__gte = user_Role,is_active=0).exclude(user_role_id=1)
            for u_data in user_data:
                User_data =User.objects.filter(id=u_data.user_id)
                for UsersData in User_data:
                    product_data =Product.objects.filter(product_id=u_data.product_id_id)
                    userRole_data =Group.objects.filter(id=u_data.user_role_id)
                    for p_data in product_data:
                        for ur_data in userRole_data:
                            data.append({ 
                                'email' :  UsersData.username,
                                'first_name' : u_data.first_name,
                                'last_name' : u_data.last_name,
                                'user_role' : ur_data.name,
                                'user_role_id' : ur_data.id,
                                'user_IDS' : u_data.user_id,
                                'user_ID' : user_ID,
                                'product' : p_data.product_name,
                                'is_disable' : u_data.is_disable,
                                'role' : user_Role,
                                'id':UsersData.id,
                            })
        return JsonResponse({'data':data})
                
            
    
class DeleteUsers(View):
    template_name = 'list_user.html'
    
    def post(self, request, *args, **kwargs):
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4:
            return redirect('/dashboard/')
        req = self.request.POST
        id = req.get('id')
        p = User.objects.get(id=id)
        p.is_active = False
        p.save()
        UserProfile.objects.filter(user_id=id).update(is_active=1)
        FindDelete = User.objects.filter(id=id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete user"
        meg ="USERNAME: "+FindDelete[0].username +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Manage Users")
        h.save()
        return JsonResponse({'status':'1'})
    
class DisableUsers(View):
    template_name = 'list_user.html'
    
    def post(self, request, *args, **kwargs):
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4:
            return redirect('/dashboard/')
        req = self.request.POST
        id = req.get('id')
        is_disable = req.get('is_disable')
        if is_disable == '1':
            UserProfile.objects.filter(user_id=id).update(is_disable=0)
        else:
            UserProfile.objects.filter(user_id=id).update(is_disable=1)
        FindUserDis = User.objects.filter(id=id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if is_disable == '1':
            meg ="Enable user "
        else:
            meg ="Disable user "
        meg ="USERNAME: "+FindUserDis[0].username +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Manage Users")
        h.save()
        return JsonResponse({'status':'1'})
    
class AddUsers(View):
    template_name = 'add_user.html'
    
    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        id = kwargs.get("id")
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4:
            return redirect('/dashboard/')
        if id==None:
            data={ 
            'firstName' : '',
            'lastName' : '',
            'user_role' : '',
            'product' : '',
            'email' : '',
            'id' :'',
            'password' :'',
            }
            if user_Role == 1:
                products = Product.objects.filter(is_active=0)
            else:
                products = Product.objects.filter(product_id=P_id,is_active=0)
            user_roles = Group.objects.filter(id__gte=user_Role+1)
        else:
            User_data =User.objects.filter(id=id)
            for UsersData in User_data:
                user_data =UserProfile.objects.filter(user_id=UsersData.id)
                for u_data in user_data:
                    data={ 
                        'email' :  UsersData.username,
                        'firstName' : u_data.first_name,
                        'lastName' : u_data.last_name,
                        'user_role' : u_data.user_role_id,
                        'product' : u_data.product_id_id,
                        'id':UsersData.id,
                        'password' :'XXXXXXXXXXXXXX',
                    }
            if user_Role == 1:
                products = Product.objects.filter(is_active=0)
            else:
                products = Product.objects.filter(product_id=P_id,is_active=0)
            if user_ID == UsersData.id:
                user_roles = Group.objects.filter(id=u_data.user_role_id)
            else:
                user_roles = Group.objects.filter(id__gte=user_Role+1)
        return render(request, self.template_name,{'products':products,'user_roles':user_roles,'data':data})
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        message = ''
        req = self.request.POST
        first_name = req.get('firstName')
        last_name = req.get('lastName')
        user_role_id = req.get('user_role')
        product_id = req.get('product')
        email = req.get('email')
        password = req.get('password')
        conf_password = req.get('conf_password')
        id = req.get('id')
        if id == "":
            if password != conf_password:
                message = 'Password does not match..!'
                return JsonResponse({'message': message,'status':'0'})
            else:
                if User.objects.filter(username=email).exists():
                    message = 'Email address already exists..!'
                    return JsonResponse({'message': message,'status':'0'})
                else:
                    q = User.objects.create_user(username=email,password=password)
                    q.save()
                    u = UserProfile(user_id=q.id,product_id_id=product_id,user_role_id=user_role_id,first_name=first_name,last_name=last_name)
                    u.save()
                    message = 'Successfully add new user..!'
                    FindUser = UserProfile.objects.filter(user_id=user_ID)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    meg ="Add new user "
                    meg ="USERNAME: "+email +"=> "+meg
                    h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Manage Users")
                    h.save()
                    return JsonResponse({'message': message,'status':'1'})
        else:
            AFTER = UserProfile.objects.filter(user_id=id)
            AFTER1 = User.objects.filter(id=id)
            meg =''
            if first_name != str(AFTER[0].first_name):
                meg = meg +'first_name: '+ str(AFTER[0].first_name) +' to '+str(first_name)+', '
            if last_name != str(AFTER[0].last_name):
                meg = meg +'last_name: '+ str(AFTER[0].last_name) +' to '+str(last_name)+', '
            if email != str(AFTER1[0].username):
                meg = meg +'email: '+ str(AFTER1[0].username) +' to '+str(email)+', '
            if product_id != str(AFTER[0].product_id_id):
                prd = Product.objects.filter(product_id=AFTER[0].product_id_id)
                prd1 = Product.objects.filter(product_id=product_id)
                meg = meg +'project: '+ str(prd[0].product_name) +' to '+str(prd1[0].product_name)+', '
            if user_role_id != str(AFTER[0].user_role_id):
                user_roles = Group.objects.filter(id=AFTER[0].user_role_id)
                user_roles1 = Group.objects.filter(id=user_role_id)
                meg = meg +'user_role_id: '+ str(user_roles[0].name) +' to '+str(user_roles1[0].name)+', '
            if password != 'XXXXXXXXXXXXXX' or conf_password != 'XXXXXXXXXXXXXX':
                meg = meg +'password: password changed '

            if password == 'XXXXXXXXXXXXXX' and conf_password == 'XXXXXXXXXXXXXX':
                if User.objects.filter(username=email).exists():
                    if User.objects.filter(username=email,id=id).exists():
                        UserProfile.objects.filter(user_id=id).update(product_id_id=product_id,user_role_id=user_role_id,first_name=first_name,last_name=last_name)
                        message = 'Successfully update user..!'
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+id +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Manage Users")
                            h.save()
                        return JsonResponse({'message': message,'status':'1'})
                    else:
                        message = 'Email address already exists..!'
                        return JsonResponse({'message': message,'status':'0'})
                else:
                    User.objects.filter(id=id).update(username=email)
                    UserProfile.objects.filter(user_id=id).update(product_id_id=product_id,user_role_id=user_role_id,first_name=first_name,last_name=last_name)
                    message = 'Successfully update user..!'
                    if meg !='':
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="ID: "+id +"=> "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Manage Users")
                        h.save()
                    return JsonResponse({'message': message,'status':'1'})
            else:
                if password != conf_password:
                    message = 'Password does not match..!'
                    return JsonResponse({'message': message,'status':'0'})
                else:
                    if User.objects.filter(username=email).exists():
                        if User.objects.filter(username=email,id=id).exists():
                            p = User.objects.get(id=id)
                            p.set_password(password)
                            p.save()
                            UserProfile.objects.filter(user_id=id).update(product_id_id=product_id,user_role_id=user_role_id,first_name=first_name,last_name=last_name)
                            message = 'Successfully update user..!'
                            if meg !='':
                                FindUser = UserProfile.objects.filter(user_id=user_ID)
                                now = datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                meg ="ID: "+id +"=> "+meg
                                h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Manage Users")
                                h.save()
                            return JsonResponse({'message': message,'status':'1'})
                        else:
                            message = 'Email address already exists..!'
                            return JsonResponse({'message': message,'status':'0'})
                    else:
                        p = User.objects.get(id=id)
                        p.set_password(password)
                        p.username = email
                        p.save()
                        UserProfile.objects.filter(user_id=id).update(product_id_id=product_id,user_role_id=user_role_id,first_name=first_name,last_name=last_name)
                        message = 'Successfully update user..!'
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+id +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Manage Users")
                            h.save()
                        return JsonResponse({'message': message,'status':'1'})
        return JsonResponse({'message': message,'status':'1'})
        




class ChangePassword(View):
    template_name = 'password_reset.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        # user_ID = request.session['user_ID']
        # email = request.session['email']
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        
        message = ''
        req = self.request.POST
        # id = req.get('id')
        # email = req.get('email')
        email = request.session['email']
        user_ID = request.session['user_ID']
        password = req.get('password')
        password1 = req.get('password1')
        conf_password = req.get('conf_password')
        auth_user = auth.authenticate(username=email, password=password, is_active=True)
        # auth_user = auth.authenticate(id=id, password=password, is_active=True)
        if auth_user:
            if password1 != conf_password:
                message = 'New Password does not match..!'
                return JsonResponse({'message': message,'status':'0'})
            else:
                # update auth_user set password=password where id=1;
                p = User.objects.get(id=user_ID)
                p.set_password(conf_password)
                p.save()
                message='Password Updated Successfully..!'
                P_id = request.session['P_id']
                FindUser = UserProfile.objects.filter(user_id=user_ID)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message="Password changed",function_name="Manage Users")
                h.save()  
                auth.logout(request)
                for key in request.session.keys():
                    del request.session[key] 
                return JsonResponse({'message': message,'status':'1'})

        else:
            message = 'Old password does not match...!'
            return JsonResponse({'message': message,'status':'0'})
            

class PBSMasterView(View):
    template_name = 'pbsmaster.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 1:
            project = Product.objects.filter(is_active=0)
            system = PBSMaster.objects.filter(is_active=0).distinct('system')
            subsystem = PBSMaster.objects.filter(is_active=0).distinct('subsystem')
            product_id = PBSMaster.objects.filter(is_active=0).distinct('product_id')
            asset_type = PBSMaster.objects.filter(is_active=0).distinct('asset_type')
        else:
            project = Product.objects.filter(product_id=P_id,is_active=0)
            system = PBSMaster.objects.filter(project_id=P_id,is_active=0).distinct('system')
            subsystem = PBSMaster.objects.filter(project_id=P_id,is_active=0).distinct('subsystem')
            product_id = PBSMaster.objects.filter(project_id=P_id,is_active=0).distinct('product_id')
            asset_type = PBSMaster.objects.filter(project_id=P_id,is_active=0).distinct('asset_type')
        units = PBSUnit.objects.all()
        MTBFMTBSAF = units[0].MTBFMTBSAF
        MTTR = units[0].MTTR
        return render(request, self.template_name,{'MTBFMTBSAF':MTBFMTBSAF,'MTTR':MTTR,'asset_type':asset_type,'project':project,'system':system,'subsystem':subsystem,'product_id':product_id})
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        data=[]
        req = request.POST
        project = req.get('project')
        system = req.get('system')
        subsystem = req.get('subsystem')
        product_id = req.get('product_id')
        asset_type = req.get('asset_type')
        print(system)
        # print(req)
        if user_Role == 1:
            PBSMaster_data =PBSMaster.objects.filter(is_active=0)
            if project != "all":
                 PBSMaster_data = PBSMaster_data.filter(project_id=project)
            if system != "all":
                PBSMaster_data = PBSMaster_data.filter(system=system)
            if subsystem != "all":
                 PBSMaster_data = PBSMaster_data.filter(subsystem=subsystem)
            if product_id != "all":
                PBSMaster_data = PBSMaster_data.filter(product_id=product_id)
            if asset_type != "all":
                PBSMaster_data = PBSMaster_data.filter(asset_type=asset_type)
            for PBSMasters in PBSMaster_data:
                project_data =Product.objects.filter(product_id=PBSMasters.project_id)
                for sub in project_data:
                    data.append({ 
                        'id' :  PBSMasters.id,
                        'system' : PBSMasters.system,
                        'project' : sub.product_name,
                        'subsystem' : PBSMasters.subsystem,
                        'product_id' : PBSMasters.product_id,
                        'product_description' : PBSMasters.product_description,
                        'asset_type' : PBSMasters.asset_type,
                        'asset_description' : PBSMasters.asset_description,
                        'MTBF' : PBSMasters.MTBF,
                        'MTBSAF':PBSMasters.MTBSAF,
                        'MTTR':PBSMasters.MTTR,
                        'MART' : PBSMasters.MART,
                        'asset_quantity':PBSMasters.asset_quantity,
                        'user_Role':user_Role,
                        'availability_target':PBSMasters.availability_target,
                    })
        else:
            PBSMaster_data =PBSMaster.objects.filter(project_id=P_id,is_active=0)
            if system != 'all':
                PBSMaster_data = PBSMaster_data.filter(system=system)
            if subsystem != "all":
                 PBSMaster_data = PBSMaster_data.filter(subsystem=subsystem)
            if product_id != "all":
                PBSMaster_data = PBSMaster_data.filter(product_id=product_id)
            if asset_type != "all":
                PBSMaster_data = PBSMaster_data.filter(asset_type=asset_type)
            for PBSMasters in PBSMaster_data:
                project_data =Product.objects.filter(product_id=PBSMasters.project_id)
                for sub in project_data:
                    data.append({ 
                        'id' :  PBSMasters.id,
                        'system' : PBSMasters.system,
                        'project' : sub.product_name,
                        'subsystem' : PBSMasters.subsystem,
                        'product_id' : PBSMasters.product_id,
                        'product_description' : PBSMasters.product_description,
                        'asset_type' : PBSMasters.asset_type,
                        'asset_description' : PBSMasters.asset_description,
                        'MTBF' : PBSMasters.MTBF,
                        'MTBSAF':PBSMasters.MTBSAF,
                        'MTTR':PBSMasters.MTTR,
                        'MART' : PBSMasters.MART,
                        'asset_quantity':PBSMasters.asset_quantity,
                        'user_Role':user_Role,
                        'availability_target':PBSMasters.availability_target,
                    }) 
        return JsonResponse({'data':data})
    
class DeletePBSMaster(View):
    template_name = 'add_pbsmaster.html'
    
    def post(self, request, *args, **kwargs):
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4 or user_Role == 2:
            return redirect('/dashboard/')
        req = self.request.POST
        id = req.get('id')
        PBSMaster.objects.filter(id=id).update(is_active=1)
        FindDelete = PBSMaster.objects.filter(id=id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete PBSMaster"
        # FindDelete[0].asset_type
        meg ="ID: "+id +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="PBS Master")
        h.save()
        return JsonResponse({'status':'1'})
    
class DeleteAllPBSMaster(View):
    template_name = 'add_pbsmaster.html'
    
    def get(self, request, *args, **kwargs):
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4 or user_Role == 2:
            return redirect('/dashboard/')
        req = self.request.GET
        ASST = ''
        print(req.get('ids', ''))
        ids=[int(x) for x in req.get('ids', '').split(',')]
        for id in ids:
            PBSMaster.objects.filter(id=id).update(is_active=1)
            FindDelete = PBSMaster.objects.filter(id=id)
            if ASST == '':
                ASST = FindDelete[0].asset_type
            else:
                ASST = ASST +', '+ FindDelete[0].asset_type
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete PBSMaster"
        # ASST
        meg ="ID: "+str(ids) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="PBS Master")
        h.save()
        return JsonResponse({'status':'1'})


    
class PBSMasterAdd(View):
    template_name = 'add_pbsmaster.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        if user_Role == 2 or user_Role == 3:
            if id ==None:
                return redirect('/dashboard/')
        if id==None:
            data={ 
            'system' : '',
            'subsystem' : '',
            'product_id' : '',
            'product_description' : '',
            'asset_type' : '',
            'id' :'',
            'asset_description' : '',
            'MTBF' : 0,
            'MTBSAF' : 0,
            'MTTR' : 0,
            'MART' : 0,
            'asset_quantity':0,
            'availability_target':0,
            'project':'',
            }
        else:
            PBSMaster_data =PBSMaster.objects.filter(id=id)
            for PBSMastersData in PBSMaster_data:
                data={ 
                    'system' : PBSMastersData.system,
                    'subsystem' : PBSMastersData.subsystem,
                    'product_id' : PBSMastersData.product_id,
                    'product_description' : PBSMastersData.product_description,
                    'asset_type' : PBSMastersData.asset_type,
                    'id' :PBSMastersData.id,
                    'asset_description' : PBSMastersData.asset_description,
                    'MTBF' : PBSMastersData.MTBF,
                    'MTBSAF' : PBSMastersData.MTBSAF,
                    'MTTR' : PBSMastersData.MTTR,
                    'MART' : PBSMastersData.MART,
                    'asset_quantity':PBSMastersData.asset_quantity,
                    'availability_target':PBSMastersData.availability_target,
                    'project':PBSMastersData.project_id,
                }
        project = Product.objects.filter(is_active=0)
        system = PBSMaster.objects.filter().distinct('system')
        subsystem = PBSMaster.objects.filter().distinct('subsystem')
        units = PBSUnit.objects.all()
        MTBFMTBSAF = units[0].MTBFMTBSAF
        MTTR = units[0].MTTR
        return render(request, self.template_name,{'MTBFMTBSAF':MTBFMTBSAF,'MTTR':MTTR,'data':data,'project':project,'system':system,'subsystem':subsystem})
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        message = ''
        req = self.request.POST
        system = req.get('system')
        subsystem = req.get('subsystem')
        product_id = req.get('product_id')
        product_description = req.get('product_description')
        asset_type = req.get('asset_type')
        asset_description = req.get('asset_description')
        MTTR = req.get('MTTR')
        MTBF = req.get('MTBF')
        MTBSAF = req.get('MTBSAF')
        MART = req.get('MART')
        cursor = connection.cursor()
        asset_quantity = req.get('asset_quantity')
        availability_target = req.get('availability_target')
        project = req.get('project')
        id = req.get('id')
        if MTTR == '':
            MTTR = 0
        if MTBSAF == '':
            MTBSAF = 0
        if MART == '':
            MART = 0
        if availability_target == '':
            availability_target = 0
            
        DATA = []
        HEAD = ["system",'subsystem','project_id','product_id','product_description','asset_type','asset_description','asset_quantity']
        for f in HEAD:
            if f == 'project_id':
                DATA.append({
                    'field':f,
                    'value':project
                })
            else:
                DATA.append({
                    'field':f,
                    'value':req.get(f)
                })
        # print(DATA)


        if id == "":
            if PBSMaster.objects.filter(asset_type=asset_type,is_active=0).exists():
                message = 'Asset name already exists..!'
                return JsonResponse({'message': message,'status':'0'})
            else:
                u = PBSMaster(availability_target=availability_target,project_id=project,system=system,subsystem=subsystem,product_id=product_id,product_description=product_description,asset_type=asset_type,asset_description=asset_description,MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,MART=MART,asset_quantity=asset_quantity)
                u.save()
                message = 'Successfully add new PBS Master..!'
                FindUser = UserProfile.objects.filter(user_id=user_ID)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                meg ="Add new PBSMaster"
                # asset_type
                meg ="ID: "+str(u.id) +"=> "+meg
                h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="PBS Master")
                h.save()
                return JsonResponse({'message': message,'status':'1','id':u.id})
        else:
            AFTER = PBSMaster.objects.filter(id=id)
            meg =''
            for i in DATA:
                cursor.execute("SELECT * FROM fracas_pbsmaster WHERE id='{0}' and {1}='{2}'".format(id,i['field'],i['value']))
                row = cursor.fetchone()
                if row == None:
                    cursor.execute("SELECT {0} FROM fracas_pbsmaster WHERE id='{1}'".format(i['field'],id))
                    row1 = cursor.fetchone()
                    if i['field'] == 'project_id':
                        prd =Product.objects.filter(product_id=row1[0])
                        prd1 =Product.objects.filter(product_id=project)
                        meg = meg +'Project: '+ str(prd[0].product_name) +' to '+str(prd1[0].product_name)+', '
                    else:
                        meg = meg +i['field']+': '+ str(row1[0]) +' to '+str(i['value'])+', '

            if MTBF != str(AFTER[0].MTBF):
                meg = meg +'MTBF: '+ str(AFTER[0].MTBF) +' to '+str(MTBF)+', '
            if MTBSAF != str(AFTER[0].MTBSAF):
                meg = meg +'MTBSAF: '+ str(AFTER[0].MTBSAF) +' to '+str(MTBSAF)+', '
            if MTTR != str(AFTER[0].MTTR):
                meg = meg +'MTTR: '+ str(AFTER[0].MTTR) +' to '+str(MTTR)+', '
            if availability_target != str(AFTER[0].availability_target):
                meg = meg +'availability_target: '+ str(AFTER[0].availability_target) +' to '+str(availability_target)+', '


            if PBSMaster.objects.filter(asset_type=asset_type,id=id,is_active=0).exists():
                PBSMaster.objects.filter(id=id).update(availability_target=availability_target,project_id=project,product_id=product_id,system=system,subsystem=subsystem,product_description=product_description,asset_description=asset_description,MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,MART=MART,asset_quantity=asset_quantity)
                message = 'Successfully update PBS Master..!'
                if meg !='':
                    FindUser = UserProfile.objects.filter(user_id=user_ID)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    meg ="ID: "+id +" => "+meg
                    h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="PBS Master")
                    h.save()
                return JsonResponse({'message': message,'status':'1','id':id})
            else:
                if PBSMaster.objects.filter(asset_type=asset_type,is_active=0).exists():
                    message = 'Asset name already exists..!'
                    return JsonResponse({'message': message,'status':'0'})
                else:
                    PBSMaster.objects.filter(id=id).update(availability_target=availability_target,project_id=project,product_id=product_id,asset_type=asset_type,system=system,subsystem=subsystem,product_description=product_description,asset_description=asset_description,MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,MART=MART,asset_quantity=asset_quantity)
                    message = 'Successfully update PBS Master..!'
                    if meg !='':
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="ID: "+id +"=> "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="PBS Master")
                        h.save()
                    return JsonResponse({'message': message,'status':'1','id':id})   
        return JsonResponse({'message': message,'status':'0'})
        


class PBSMasterImport(View):
    template_name = 'import_pbsmaster_page.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4 or user_Role == 2:
            return redirect('/dashboard/')
        user_ID = request.session['user_ID']
        temp_table_import_file.objects.filter(updated_by=user_ID).delete()
        return render(request, self.template_name,)
    
    def post(self, request, *args, **kwargs):
        
        user_ID = request.session['user_ID']
        ExcelFile = request.FILES['import_file'] 
        data=[]  
        ExcelFile_name = ExcelFile.name
        fn=ExcelFile_name.split('.')
        df=fn[0]
        count = 0
        for a in df:
            if (a.isspace()) == True:
                count+=1
        if count != 0:
            message="Don't include space for the uploaded filename"
            return render(request, self.template_name, {"message": message})
        extension = os.path.splitext(ExcelFile_name)[-1].lower()
        if extension=='.xlsx' or extension=='.xls':
            fs = FileSystemStorage()
            filename = fs.save('excelFile/'+ExcelFile.name, ExcelFile)
            ExcelFileloc = fs.url(filename)
           
            # wb=xlrd.open_workbook('excelFile/imppbs_SFZqfeF.xlsx')
            wb = xlrd.open_workbook(filename)
            sheet = wb.sheet_by_index(0)
            row_count = sheet.nrows
            cols_count = sheet.ncols
            if(cols_count is not 14):
                message='The excel file is not in the required format'
                return render(request, self.template_name, {"message": message})


            A1= sheet.cell_value(0,0) 
            B1= sheet.cell_value(0,1)
            C1= sheet.cell_value(0,2)
            D1= sheet.cell_value(0,3)
            E1= sheet.cell_value(0,4)
            F1= sheet.cell_value(0,5)
            G1= sheet.cell_value(0,6)
            H1= sheet.cell_value(0,7)
            I1= sheet.cell_value(0,8)
            J1= sheet.cell_value(0,9)
            K1= sheet.cell_value(0,10)
            L1= sheet.cell_value(0,11)
            M1= sheet.cell_value(0,12)
            N1= sheet.cell_value(0,13)
            # return render(request, self.template_name, {"message": B1})

            asset_type_array=[]

            if(B1=='Project' and C1=='System'  and D1=='Subsystem' and E1=='Product id' and F1=='Product description' and G1=='Asset name' and H1=='Asset description' and I1=='MTBF' and J1=='MTBSAF' and K1=='MTTR' and L1=='MART' and M1=='Asset quantity' and N1=='Availability target' ):
                # return render(request, self.template_name, {"message": 'required format'})
                for row in range(1, row_count):
                    project=sheet.cell_value(row,1)
                    system= sheet.cell_value(row,2)
                    subsystem= sheet.cell_value(row,3)
                    product_id= sheet.cell_value(row,4)
                    product_description= sheet.cell_value(row,5)
                    asset_type= sheet.cell_value(row,6)
                    asset_description= sheet.cell_value(row,7)
                    MTBF = sheet.cell_value(row,8)
                    MTBSAF = sheet.cell_value(row,9)
                    MTTR = sheet.cell_value(row,10)
                    MART = sheet.cell_value(row,11)
                    if isinstance(sheet.cell_value(row,12), str):
                        asset_quantity = sheet.cell_value(row,12)
                    else:
                        asset_quantity = int(sheet.cell_value(row,12))
                    if isinstance(sheet.cell_value(row,13), str):
                        availability_target = sheet.cell_value(row,13)
                    else:
                        availability_target = int(sheet.cell_value(row,13))
                    
                    project_err = '1'
                    system_err = '1'
                    subsystem_err = '1'
                    product_id_err = '1'
                    product_description_err = '1'
                    asset_type_err = '1'
                    asset_description_err = '1'
                    MTBF_err = '1'
                    MTBSAF_err = '1'
                    MTTR_err = '1'
                    MART_err = '1'
                    asset_quantity_err = '1'
                    availability_target_err = '1'
                    err_status = '1'
                    
                    if not Product.objects.filter(product_name=project,is_active=0).exists():
                        project_err = 'Project not avalable'
                        
                    if not isinstance(MTBF, float) and not isinstance(MTBF, int):
                        MTBF_err='Value error'
                    if not isinstance(asset_quantity, int) :
                        asset_quantity_err='Value error'
                        
                    if MTBF_err == '1':
                        if MTBF == 0:
                            MTBF_err='Value error'
                    
                        
                    if system == "":
                        system_err = 'Empty'
                    if subsystem == "":
                        subsystem_err = 'Empty'
                    if product_id == "":
                        product_id_err = 'Empty'
                    if product_description == "":
                        product_description_err = 'Empty'
                    if asset_description == "":
                        asset_description_err = 'Empty'
                    if asset_type == "":
                        asset_type_err = 'Empty'
                    if MTBF == "":
                        MTBF_err = 'Empty'
                    if MTBSAF == "":
                        MTBSAF = 0
                    else:
                        if not isinstance(MTBSAF, float) and not isinstance(MTBSAF, int) :
                            MTBSAF_err='Value error'
                    if MTTR == "":
                        MTTR = 0
                    else:
                        if not isinstance(MTTR, float) and not isinstance(MTTR, int) :
                            MTTR_err='Value error'
                    if MART == "":
                        MART = 0
                    else:
                        if not isinstance(MART, float) and not isinstance(MART, int) :
                            MART_err='Value error'
                    if asset_quantity == "":
                        asset_quantity_err = 'Empty'
                    if availability_target == "":
                        availability_target = 0
                    else:
                        if not isinstance(availability_target, int) :
                            availability_target_err='Value error'
                        
                    if project_err != '1' or system_err != '1' or subsystem_err != '1' or product_id_err != '1' or product_description_err != '1' or asset_type_err != '1' or asset_description_err != '1' or MTBF_err != '1' or MTBSAF_err != '1' or MTTR_err != '1' or MART_err != '1' or asset_quantity_err != '1' or availability_target_err != '1':
                        err_status = '0'
                    asset_type_array = {asset_type,}
                    
                    data.append({
                        'id':row,
                        'project':project,
                        'project_err':project_err,
                        'system':system,
                        'system_err':system_err,
                        'subsystem':subsystem,
                        'subsystem_err':subsystem_err,
                        'product_id':product_id,
                        'product_id_err':product_id_err,
                        'product_description':product_description,
                        'product_description_err':product_description_err,
                        'asset_type':asset_type,
                        'asset_type_err':asset_type_err,
                        'asset_description':asset_description,
                        'asset_description_err':asset_description_err,
                        'MTBF':MTBF,
                        'MTBF_err':MTBF_err,
                        'MTBSAF':MTBSAF,
                        'MTBSAF_err':MTBSAF_err,
                        'MTTR':MTTR,
                        'MTTR_err':MTTR_err,
                        'MART':MART,
                        'MART_err':MART_err,
                        'asset_quantity':asset_quantity,
                        'asset_quantity_err':asset_quantity_err,
                        'availability_target':availability_target,
                        'availability_target_err':availability_target_err,
                        'err_status':err_status,
                    })
            else:
                message='The excel file is not in the required format'
                return render(request, self.template_name, {"message": message})
        else:
            message='The file selected is not excel document'
            return render(request, self.template_name, {"message": message})
        return render(request, self.template_name, {"data": data,"status":"1"})
    
    # def post(self, request, *args, **kwargs):
    #     temp_table_import_file1 =temp_table_import_file.objects.filter()
    #     temp_table_import_file1 =''
    #     if temp_table_import_file1:
    #         return render(request, self.template_name, {"message": 'please Wait an excel sheet is in progress'})
    #     else:
    #         user_ID = request.session['user_ID']
    #         ExcelFile = request.FILES['import_file']   
            
    #         ExcelFile_name = ExcelFile.name
    #         fn=ExcelFile_name.split('.')
    #         df=fn[0]
    #         count = 0
    #         for a in df:
    #             if (a.isspace()) == True:
    #                 count+=1
    #         if count != 0:
    #             message='The excel file name contain space '
    #             return render(request, self.template_name, {"message": message})
            
    #         extension = os.path.splitext(ExcelFile_name)[-1].lower()
    #         if extension=='.xlsx' or extension=='.xls':
    #             fs = FileSystemStorage()
    #             filename = fs.save('excelFile/'+ExcelFile.name, ExcelFile)
    #             ExcelFileloc = fs.url(filename)
                
    #             wb = xlrd.open_workbook(ExcelFileloc)
    #             sheet = wb.sheet_by_index(0)
    #             row_count = sheet.nrows
    #             cols_count = sheet.ncols
    #             if(cols_count is not 12):
    #                 message='The excel file is not in the required format'
    #                 return render(request, self.template_name, {"message": message})


    #             A1= sheet.cell_value(0,0) 
    #             B1= sheet.cell_value(0,1)
    #             C1= sheet.cell_value(0,2)
    #             D1= sheet.cell_value(0,3)
    #             E1= sheet.cell_value(0,4)
    #             F1= sheet.cell_value(0,5)
    #             G1= sheet.cell_value(0,6)
    #             H1= sheet.cell_value(0,7)
    #             I1= sheet.cell_value(0,8)
    #             J1= sheet.cell_value(0,9)
    #             K1= sheet.cell_value(0,10)
    #             L1= sheet.cell_value(0,11)
    #             # return render(request, self.template_name, {"message": B1})

    #             asset_type_array=[]

    #             if(B1=='System' and C1=='Subsystem'  and D1=='Product id' and E1=='Product description' and F1=='Asset name' and G1=='Asset description' and H1=='MTBF' and I1=='MTBSAF' and J1=='MTTR' and K1=='MART' and L1=='Asset quantity' ):
    #                 # return render(request, self.template_name, {"message": 'required format'})
    #                 for row in range(1, row_count):
    #                     system= sheet.cell_value(row,1)
    #                     subsystem= sheet.cell_value(row,2)
    #                     product_id= sheet.cell_value(row,3)
    #                     product_description= sheet.cell_value(row,4)
    #                     asset_type= sheet.cell_value(row,5)
    #                     asset_description= sheet.cell_value(row,6)
                        
    #                     MTBF=''
    #                     MTBSAF=''
    #                     MTTR=''
    #                     MART=''
    #                     asset_quantity=''
    #                     c_asset_quantity=int(sheet.cell_value(row,11))
                        
    #                     if isinstance(sheet.cell_value(row,7), float) or isinstance(sheet.cell_value(row,7), int) :
    #                         MTBF=sheet.cell_value(row,7)
    #                     if isinstance(sheet.cell_value(row,8), float) or isinstance(sheet.cell_value(row,8), int) :
    #                         MTBSAF=sheet.cell_value(row,8)
    #                     if isinstance(sheet.cell_value(row,9), float) or isinstance(sheet.cell_value(row,9), int) :
    #                         MTTR=sheet.cell_value(row,9)
    #                     if isinstance(sheet.cell_value(row,10), float) or isinstance(sheet.cell_value(row,10), int) :
    #                         MART=sheet.cell_value(row,10)
    #                     if isinstance(sheet.cell_value(row,11), float) and sheet.cell_value(row,11)==c_asset_quantity :
    #                         asset_quantity=c_asset_quantity
                       
                       

    #                     if asset_type in asset_type_array:
    #                         asset_type=''
    #                     else:  
    #                         asset_type_array.append(asset_type)

    #                     updated_by = user_ID
    #                     if Product.objects.filter(product_name=subsystem).exists():
    #                         subsystem_data =Product.objects.filter(product_name=subsystem)
    #                         subsystem_id= subsystem_data[0].product_id
    #                     else:
    #                         subsystem_id=0
    #                     # print('system' +system)
    #                     if system=="" or subsystem=="" or subsystem_id==0 or product_id=="" or product_description=="" or asset_type=="" or asset_description=="" or MTBF=="" or MTBSAF=="" or MTTR=="" or MART=="" or asset_quantity==""  : 
    #                         error_list ='1'
    #                     else:
    #                         error_list ='0'

    #                     u = temp_table_import_file(system=system,subsystem=subsystem,subsystem_id=subsystem_id,product_id=product_id,product_description=product_description,asset_type=asset_type,asset_description=asset_description,MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,MART=MART,asset_quantity=asset_quantity,error_list=error_list,updated_by=updated_by )
    #                     u.save()
    #                     # return render(request, self.template_name, {"message": 'format'})


                    
    #             else:
    #                 message='The excel file is not in the required format'
    #                 return render(request, self.template_name, {"message": message})
    #         else:
    #             message='The file selected is not excel document'
    #             return render(request, self.template_name, {"message": message})

    #         importfile2 =temp_table_import_file.objects.filter(updated_by=user_ID)
    #         if importfile2:
    #             data='1'
    #             dataUpdate=[]
    #             dataAdd=[]
    #         else:
    #             data=''
            
    #         asset_data = PBSMaster.objects.filter()
    #         asset_type_array=[]
    #         for a1 in asset_data:
    #             asset_type_array.append(a1.asset_type )
                
    #         # return render(request, self.template_name, { "message":asset_type_array[0]})

    #         for imp in importfile2:
    #             if imp.asset_type in asset_type_array:
    #                 dataUpdate.append({ 
    #                     'id' :imp.id,
    #                     'system' :imp.system,
    #                     'subsystem' :imp.subsystem,
    #                     'product_id' :imp.product_id,
    #                     'product_description' :imp.product_description ,
    #                     'asset_type' :imp.asset_type ,
    #                     'asset_description' :imp.asset_description ,
    #                     'MTBF' :imp.MTBF ,
    #                     'MTBSAF':imp.MTBSAF,
    #                     'MTTR':imp.MTTR,
    #                     'MART' :imp.MART ,
    #                     'asset_quantity':imp.asset_quantity,
    #                     'updated_by':imp.updated_by,
    #                     'error_list':imp.error_list,
    #                 })
    #             else:

    #                 dataAdd.append({ 
    #                     'id' :imp.id,
    #                     'system' :imp.system,
    #                     'subsystem' :imp.subsystem,
    #                     'product_id' :imp.product_id,
    #                     'product_description' :imp.product_description ,
    #                     'asset_type' :imp.asset_type ,
    #                     'asset_description' :imp.asset_description ,
    #                     'MTBF' :imp.MTBF ,
    #                     'MTBSAF':imp.MTBSAF,
    #                     'MTTR':imp.MTTR,
    #                     'MART' :imp.MART ,
    #                     'asset_quantity':imp.asset_quantity,
    #                     'updated_by':imp.updated_by,
    #                     'error_list':imp.error_list,
    #                 })
    #         return render(request, self.template_name, {"data":data ,"dataUpdate":dataUpdate,"dataAdd":dataAdd})



class PBSMasterAddImport(View):
    template_name = 'import_pbsmaster_page.html'
    
    def post(self, request, *args, **kwargs):
        req = self.request.POST
        # ids = req.get('ids')
        user_ID = request.session['user_ID']
        updated=0
        inserted=0
        ids=[int(x) for x in req.get('ids', '').split(',')]
        datas= req.get('datas')
        data=json.loads(datas)
        if data !="":
            for items in data:
                itemId=items['id']
                if itemId in ids:
                    itemAssetType = items['asset_type']
                    itemProject = items['project']
                    Project = Product.objects.filter(product_name=itemProject)
                    if PBSMaster.objects.filter(asset_type=itemAssetType,is_active=0).exists():
                        PBSMaster.objects.filter(asset_type=itemAssetType).update(availability_target=items['availability_target'],project_id=Project[0].product_id,system=items['system'],subsystem=items['subsystem'],product_id=items['product_id'],product_description=items['product_description'],asset_description=items['asset_description'],MTBF=items['MTBF'],MTBSAF=items['MTBSAF'],MTTR=items['MTTR'],MART=items['MART'],asset_quantity=items['asset_quantity'],is_active=0)
                        updated+=1
                    else:
                        u = PBSMaster(asset_type=itemAssetType,availability_target=items['availability_target'],project_id=Project[0].product_id,system=items['system'],subsystem=items['subsystem'],product_id=items['product_id'],product_description=items['product_description'],asset_description=items['asset_description'],MTBF=items['MTBF'],MTBSAF=items['MTBSAF'],MTTR=items['MTTR'],MART=items['MART'],asset_quantity=items['asset_quantity'])
                        u.save()
                        inserted+=1
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Insert "+str(inserted)+" record and Update "+str(updated)+" record to PBSMaster"
        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Import PBS Master")
        h.save()
        return JsonResponse({'status':'1','inserted': inserted,'updated': updated})

   
    # def post(self, request, *args, **kwargs):
    #     req = self.request.POST
    #     # ids = req.get('ids')
    #     user_ID = request.session['user_ID']

    #     ids=[int(x) for x in req.get('ids', '').split(',')]
    #     imported_data = temp_table_import_file.objects.filter(id__in=ids)
    #     # message=imported_data[0].asset_type
        
    #     asset_data = PBSMaster.objects.filter()
    #     asset_type_array=[]
    #     for a1 in asset_data:
    #         asset_type_array.append(a1.asset_type )
        
    #     updated=0
    #     inserted=0
    #     for imp in imported_data:
    #         if imp.asset_type in asset_type_array:
    #             updated+=1
    #             PBSMaster_1=PBSMaster.objects.filter(asset_type=imp.asset_type)
    #             id=PBSMaster_1[0].id
    #             PBSMaster.objects.filter(id=id).update(system=imp.system, subsystem_id=imp.subsystem_id,  product_description=imp.product_description,asset_description=imp.asset_description,  MTBF=imp.MTBF,  MTBSAF=imp.MTBSAF, MTTR=imp.MTTR, MART=imp.MART, asset_quantity=imp.asset_quantity )
            
    #         else:
    #             inserted+=1
    #             u = PBSMaster(system=imp.system, subsystem_id=imp.subsystem_id,  product_description=imp.product_description,asset_type=imp.asset_type,asset_description=imp.asset_description,  MTBF=imp.MTBF,  MTBSAF=imp.MTBSAF, MTTR=imp.MTTR, MART=imp.MART, asset_quantity=imp.asset_quantity )
    #             u.save()
    #     temp_table_import_file.objects.filter(updated_by=user_ID).delete()
    #     # return render(request, self.template_name, {"message":message,'status':1 })
    #     P_id = request.session['P_id']
    #     user_ID = request.session['user_ID']
    #     FindUser = UserProfile.objects.filter(user_id=user_ID)
    #     now = datetime.now()
    #     current_time = now.strftime("%H:%M:%S")
    #     meg ="Insert "+str(inserted)+" record and Update "+str(updated)+" record to PBSMaster"
    #     h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg)
    #     h.save()
    #     return JsonResponse({'status':'1','inserted': inserted,'updated': updated})






class AdminReviewBoardView(View):
    template_name = 'fracas-review-board.html'

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            req = request.GET
            asset_type = req.get('asset_type')          
            if not asset_type:
                review_board = ReviewBoard.objects.all().order_by('-meeting_date')
            else:
                review_board = ReviewBoard.objects.filter(asset_type=asset_type)
            asst = PBSMaster.objects.filter(id=asset_type)
            asset_distinct_review_board = ReviewBoard.objects.all().distinct('asset_type')
            asset_data = Asset.objects.all().distinct('asset_type')
        # print(url,'DDDDDD')
        print(asst[0].asset_type)

        return render(request, self.template_name, {'asst':asst[0].asset_type,'review_boards' : review_board, 'asset_datas':asset_data, 'asset_distinct_review_boards':asset_distinct_review_board})

    def post(self, request, *args, **kwargs):

        req = request.POST
        asset_type = req.get('asset_type')
        start_date = req.get('start_date')
        end_date = req.get('end_date')

        if asset_type and start_date and end_date:
            formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
            formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')

        meeting_id = ''
        meeting_date = '2020-08-01'
        meeting_status = ''
        review_board = ReviewBoard.objects.create(
                            asset_type=asset_type,
                            from_date=formated_start_date,
                            to_date=formated_end_date,
                            meeting_id=meeting_id,
                            meeting_date=meeting_date,
                            meeting_status=meeting_status,
                            )
        request.session['review_board_id'] = review_board.id
        # return render(request, self.template_name, {'review_board' : review_board})
        return JsonResponse({'message': 'success', 'asset_type':asset_type.replace(" ","_"), 'start_date':formated_start_date,'end_date':formated_end_date, 'review_board_id':review_board.id}, safe=False)
        # return redirect('review_board_details')

class AdminReviewBoardDetailsView(View):
    template_name = 'fracas_review_board_details.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        user_ID = request.session['user_ID']
        req = request.GET
        asset_type = unquote(req.get('asset_type'))
        start_date = req.get('start_date')
        end_date = req.get('end_date')
        review_board_id = req.get('r_id')
       
        
        if ReviewBoard.objects.filter(id=review_board_id,is_active=1).exists():
            return redirect('/forms/review_board/')
        review_board = ReviewBoard.objects.get(id=review_board_id)
        meeting_date = review_board.meeting_date
        PBSMaster_datas=PBSMaster.objects.filter(id=asset_type)
        for PBSMaster_data in PBSMaster_datas:
        # defects = Defect.objects.filter(asset_type=asset_type, defect_open_date=start_date, defect_closed_date=end_date)
            employees = UserProfile.objects.filter(is_active=0,product_id_id=PBSMaster_data.project).exclude(user_role_id=1)
            asst = PBSMaster_data.asset_type
        defects = Defect.objects.filter(asset_type=asset_type,is_active=0)
        defects_count = len(defects)
        return render(request, self.template_name, {'defects_count':defects_count,'meeting_date':meeting_date,'review_board' : review_board, 'defects':defects, 'employees':employees, 'asset_type':asset_type ,'asst':asst})

class ReviewBoardDefectDiscussionView(View):
    template_name = 'fracas_review_board_details.html'

    def get(self, request, *args, **kwargs):
        
        data=[]
        
        req = request.GET
        review_board_id = req.get('review_board_id')
        discussion_id = req.get('discussion_id')
        review_board = ReviewBoard.objects.get(id=req.get('review_board_id'))
        # defects = Defect.objects.filter(asset_type=asset_type, defect_open_date=start_date, defect_closed_date=end_date)
        
        defect_discussions = DefectDiscussion.objects.filter(review_board=review_board)
        for discussion in defect_discussions:
            employees = discussion.attendees.all()
            print(employees)
            attendees=[]
            for employee in employees:
                attendees.append({'employee_id':employee.id, 'name':employee.first_name+" "+employee.last_name})
            data.append({'review_board_id':discussion.review_board.id,
                         'defect_id':discussion.defect.defect_id,
                         'defect_name':discussion.defect.defect_description,
                         'meeting_date':discussion.meeting_date,
                         'attendees':attendees,
                         'discussion_id':discussion.defect_discussion_id
                })
        return JsonResponse({'success':'success', 'data':data})

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        # asset_type = unquote(req.get('asset_type'))
        attendees = req.getlist('attendees[]')
        defect_id = req.get('defect')
        review_board_id = req.get('review_board_id')
        
        
        review_board = ReviewBoard.objects.get(id=review_board_id)
        # defects = Defect.objects.filter(asset_type=asset_type, defect_open_date=start_date, defect_closed_date=end_date)
        defect = Defect.objects.get(defect_id=defect_id)
        employees = UserProfile.objects.filter(id__in=attendees)
        defect_discussion = DefectDiscussion.objects.create(review_board=review_board, defect=defect)
        defect.defect_status = review_board.meeting_status
        defect.save()
        for employee in employees:
            defect_discussion.attendees.add(employee)

        return JsonResponse({'success':'success'})

class AdminReviewBoardUpdateView(View):
    # template_name = 'fracas_review_board_details.html'

    def post(self, request, *args, **kwargs):
                
        req = request.POST
        review_board_id = req.get('review_board_id')
        delete_action = req.get('delete_action')
        meeting_status = req.get('meeting_status')
        meeting_outcome = req.get('meeting_outcome')
        
        review_board = ReviewBoard.objects.get(id=review_board_id)
        discussions = DefectDiscussion.objects.filter(review_board=review_board)
        
        
        if review_board_id and delete_action:
            
            # discussions = DefectDiscussion.objects.filter(review_board=review_board)
            if discussions:
                print(discussions,")))))))))")
                for discussion in discussions:
                    actions = Action.objects.filter(defect_discussion_id=discussion.defect_discussion_id)
                    actions.delete()
                discussions.delete()
            review_board.delete()
        else:
            review_board.meeting_status = meeting_status
            review_board.meeting_outcome = meeting_outcome
            review_board.save()
        if meeting_status:
            for discussion in discussions:
                discussion.defect.defect_status = meeting_status
                discussion.defect.save()
                discussion.save()
        print(review_board,"SSSSSSSSSSSS")
        print('success')
        return JsonResponse({'success':'success'})


class ReviewBoardDefectDiscussionUpdateView(View):
    template_name = 'fracas_review_board_details.html'

    def get(self, request, *args, **kwargs):
        
        data=[]
        
        req = request.GET
        review_board_id = req.get('review_board_id')
        discussion_id = req.get('discussion_id')

        discussion = DefectDiscussion.objects.get(defect_discussion_id=discussion_id)

        employees = discussion.attendees.all()
        print(employees)
        attendees=[]
        for employee in employees:
            attendees.append({'employee_id':employee.id, 'name':employee.first_name+" "+employee.last_name})
        data.append({'review_board_id':discussion.review_board.id,
                     'defect_name':discussion.defect.defect_description,
                     'defect_id':discussion.defect.defect_id,
                     'meeting_date':discussion.meeting_date,
                     'attendees':attendees,
                     'discussion_id':discussion.defect_discussion_id
            })
        return JsonResponse({'success':'success', 'data':data})

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        discussion_id = req.get('discussion_id')
        delete_action = req.get('delete_action')
        if discussion_id and delete_action:
            Action.objects.filter(defect_discussion_id=discussion_id).delete()
            DefectDiscussion.objects.filter(defect_discussion_id=discussion_id).delete()
        else:
            defect_id = req.get('defect')
            attendees = req.getlist('attendees[]')
            discussion = DefectDiscussion.objects.get(defect_discussion_id=discussion_id)
            defect = Defect.objects.get(defect_id=defect_id)
            
            employees = UserProfile.objects.filter(id__in=attendees)
            discussion.defect = defect
            discussion.save()
            for attendee in discussion.attendees.all():
                discussion.attendees.remove(attendee)
            for employee in employees:
                discussion.attendees.add(employee)


        return JsonResponse({'success':'success'})

class ReviewBoardDiscussionActionView(View):
    template_name = 'fracas_review_board_details.html'


    def get(self, request, *args, **kwargs):
        
        data=[]
        
        req = request.GET
        discussion_id = req.get('discussion_id')
        print(discussion_id,"DDDDDDDD")      
        defect_discussion = DefectDiscussion.objects.get(defect_discussion_id=discussion_id)
        actions = Action.objects.filter(defect_discussion_id=defect_discussion.defect_discussion_id)
        for action in actions:
            data.append({'action_description':action.action_description,
                         'action_owner':action.action_owner,
                         'action_status':action.action_status,
                         'action_due_dat':(action.action_due_date).strftime('%d/%m/%Y'),
                         'progress_log':action.progress_log,
                         'action_id':action.action_id
                })
        return JsonResponse({'success':'success', 'data':data})

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        # asset_type = unquote(req.get('asset_type'))

        discussion_id = req.get('discussion_id')
        action_description = req.get('action_description')
        action_owner = req.get('action_owner')
        action_status = req.get('action_status')
        action_date = req.get('action_due_dat')
        progress_log = req.get('progress_log')
        action_due_dat = datetime.strptime(action_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        print(action_due_dat,"mmmmmmmmmmm")
        defect_discussion = DefectDiscussion.objects.get(defect_discussion_id=discussion_id)
        
        action = Action.objects.create(
                      action_description = action_description,
                      action_owner = action_owner,
                      action_status = action_status,
                      action_due_date = action_due_dat,
                      progress_log = progress_log,
                      defect_discussion_id = defect_discussion    
            )

        return JsonResponse({'success':'success'})

class ReviewBoardDiscussionActionUpdateView(View):
    template_name = 'fracas_review_board_details.html'


    def get(self, request, *args, **kwargs):
        req = request.GET

        action_id = req.get('action_id')
        print(action_id,"mlooooooooo")
        data=[]
        action = Action.objects.get(action_id=action_id)
        # action_due_dat = datetime.strptime(action.action_due_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        data.append({'action_description':action.action_description,
                         'action_owner':action.action_owner,
                         'action_status':action.action_status,
                         'action_due_dat':(action.action_due_date).strftime('%d/%m/%Y'),
                         'progress_log':action.progress_log,
                         'action_id':action.action_id
                })

        return JsonResponse({'success':'success', 'data':data})

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        # asset_type = unquote(req.get('asset_type'))

        action_id = req.get('action_id')
        delete_action = req.get('delete_action')

        print(action_id,"mlooooooooo")

        action = Action.objects.get(action_id=action_id)
        if action_id and delete_action:
            Action.objects.filter(action_id=action_id).delete()
        else:
            action_description = req.get('action_description')
            action_owner = req.get('action_owner')
            action_status = req.get('action_status')
            action_due_date = datetime.strptime(req.get('action_due_dat'), "%d/%m/%Y").strftime("%Y-%m-%d") 
            progress_log = req.get('progress_log')
        
            action.action_description = action_description
            action.action_owner = action_owner
            action.action_status = action_status
            action.action_due_date = action_due_date
            action.progress_log = progress_log

            action.save()

        return JsonResponse({'success':'success'})

class ReviewBoardGraphView(View):
    template_name = 'fracas_review_board_details.html'


    def get(self, request, *args, **kwargs):

        req = request.GET
        object_id = req.get('review_board_id')

        review_board=ReviewBoard.objects.filter(id=object_id,is_active=0)

        # Add graph to view
        
        if ReviewBoard.objects.filter(id=object_id,is_active=0).first().from_date and ReviewBoard.objects.filter(is_active=0,id=object_id).first().to_date:
            data = FailureData.objects.filter(is_active=0,asset_config_id__asset_type=ReviewBoard.objects.filter(is_active=0,id=object_id).first().asset_type, date__gte=ReviewBoard.objects.filter(is_active=0,id=object_id).first().from_date, date__lte=ReviewBoard.objects.filter(is_active=0,id=object_id).first().to_date).values("date").annotate(y=Count("id")).order_by("date")
        elif ReviewBoard.objects.filter(is_active=0,id=object_id).first().from_date and not ReviewBoard.objects.filter(is_active=0,id=object_id).first().to_date:
            data = FailureData.objects.filter(is_active=0,asset_config_id__asset_type=ReviewBoard.objects.filter(is_active=0,id=object_id).first().asset_type, date__gte=ReviewBoard.objects.filter(is_active=0,id=object_id).first().from_date).values("date").annotate(y=Count("id")).order_by("date")
        elif ReviewBoard.objects.filter(is_active=0,id=object_id).first().to_date and not ReviewBoard.objects.filter(is_active=0,id=object_id).first().from_date:
            data = FailureData.objects.filter(is_active=0,asset_config_id__asset_type=ReviewBoard.objects.filter(is_active=0,id=object_id).first().asset_type, date__lte=ReviewBoard.objects.filter(is_active=0,id=object_id).first().to_date).values("date").annotate(y=Count("id")).order_by("date")
        else:
            data = FailureData.objects.filter(is_active=0,asset_config_id__asset_type=ReviewBoard.objects.filter(is_active=0,id=object_id).first().asset_type).values("date").annotate(y=Count("id")).order_by("date")
            print(data, "44444444444")
        cumulative = 0
        data1=[]
        for d in data:
            data1.append({'x':d['date'], 'y':d['y']})
        print(data1, "44444444444")
        for datum in data1:
            cumulative = cumulative + datum['y']
            datum['y'] = cumulative

        chart_data = (
            data1
        )
        asset_type = ReviewBoard.objects.filter(is_active=0,id=object_id).first().asset_type
        asset_data = PBSMaster.objects.filter(is_active=0,id=asset_type).first()

        expected = []
        if(asset_data and FailureData.objects.filter(is_active=0,).exists()):
            MTBF = asset_data.MTBF
            findUnit = PBSUnit.objects.filter()
            if findUnit[0].MTBFMTBSAF == 'days':
                MTBF = round(MTBF/24,2)                        
            elif findUnit[0].MTBFMTBSAF == 'mins':
                MTBF = MTBF *60
            else:
                MTBF = MTBF

            if ReviewBoard.objects.filter(is_active=0,id=object_id).first().from_date:
                first_failure_date = ReviewBoard.objects.filter(is_active=0,id=object_id).first().from_date
            else:
                first_failure_date = FailureData.objects.filter(is_active=0,asset_config_id__asset_type=asset_type).order_by("date").first().date
            if ReviewBoard.objects.filter(is_active=0,id=object_id).first().to_date:
                last_failure_date = ReviewBoard.objects.filter(is_active=0,id=object_id).first().to_date
            else:            
                last_failure_date = FailureData.objects.filter(is_active=0,asset_config_id__asset_type=asset_type).order_by("date").last().date

            increment = (last_failure_date - first_failure_date)/10
            expected = []
            dates = [0]*11
            print('======== LOOP START ==========')
            print('MTBF',MTBF)
            for i in range(11):
                dates[i] = first_failure_date + i*increment
                time_window = ((dates[i] - first_failure_date)*24).days
                print('=========================')
                Start_date = datetime.strptime(str(first_failure_date), '%Y-%m-%d')
                End_date = datetime.strptime(str(last_failure_date), '%Y-%m-%d')
                # number_of_days = (End_date-Start_date).days
                number_of_days = i*32
                print('number_of_days',number_of_days)
                hrs = number_of_days*24*asset_data.asset_quantity
                print(hrs,'   hrs')

                expected_failure = hrs/MTBF
                print('expected_failure',expected_failure)
                print('expected_failure',round(expected_failure))
                # expected_failure = time_window*asset_data.asset_quantity/MTBF
                # print(time_window, 'x', asset_data.asset_quantity, '/', MTBF, '=', round(expected_failure) )
                expected.append({'x': dates[i], 'y': round(expected_failure)})

        # cumulative = 0
        # for datum in expected:
        #     cumulative = cumulative + datum['y']
        #     datum['y'] = round(cumulative)

        # expected_data = (
        #     expected
        # )

        # Serialize and attach the chart data to the template context

        as_json_chart_data = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        as_json_expected_data = json.dumps(list(expected), cls=DjangoJSONEncoder)


        return JsonResponse({'success':'success', "expected_data":as_json_expected_data, "chart_data": as_json_chart_data})

class ReviewBoardDiscussionActionAttendeesView(View):
    template_name = 'fracas_review_board_details.html'

    def get(self, request, *args, **kwargs):
        
        req = request.GET
        discussion_id = unquote(req.get('discussion_id'))
        defect_discussion = DefectDiscussion.objects.get(defect_discussion_id=discussion_id)
        employees = defect_discussion.attendees.all()
        attendees = []
        for employee in employees:
            attendees.append({'name':employee.first_name+" "+employee.last_name})

        return JsonResponse({'attendees' : attendees})

## DEFECT IDENTIFICATION PAGE 

class AdminDefectsView(View):
    template_name = 'fracas_defect.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        if req.get('defect_status'):
            defects = Defect.objects.filter(defect_status=req.get('defect_status'))
        elif req.get('defect_description'):
            defects = Defect.objects.filter(defect_description=req.get('defect_description'))
        elif req.get('investigation'):
            defects = Defect.objects.filter(investigation=req.get('investigation'))
        elif req.get('defect_status_remarks'):
            defects = Defect.objects.filter(defect_status_remarks=req.get('defect_status_remarks'))
        elif req.get('oem_defect_reference'):
            defects = Defect.objects.filter(oem_defect_reference=req.get('oem_defect_reference'))
        elif req.get('asset_type'):
            defects = Defect.objects.filter(asset_type=req.get('asset_type'))
        elif req.get('defect_open_date__gte') and req.get('defect_open_date__lt'):
            defects = Defect.objects.filter(defect_open_date__range=[req.get('defect_open_date__gte'),req.get('defect_open_date__lt')])
        elif req.get('defect_closed_date__gte') and req.get('defect_closed_date__lt'):
            defects = Defect.objects.filter(defect_closed_date__range=[req.get('defect_closed_date__gte'),req.get('defect_closed_date__lt')])
        else:
            defects = Defect.objects.all()
        asset_data = Asset.objects.all().distinct('asset_type')
        print(defects,'DDDDDD')
        current_date = date.today().strftime('%Y-%m-%d')
        tomorrow_date = date.today() + timedelta(days = 1)
        past_7_day_date = date.today() - timedelta(days = 8)
        first_day_of_month = date.today().strftime("%Y-%m-01")

        month = datetime.strptime(first_day_of_month, '%Y-%m-%d').month
        year = datetime.strptime(first_day_of_month, '%Y-%m-%d').year + month // 12
        month = month % 12 + 1
        day = min(datetime.strptime(first_day_of_month, '%Y-%m-%d').day, calendar.monthrange(year,month)[1])
        first_day_of_next_month = date(year, month, day).strftime('%Y-%m-%d')

        first_day_of_year = date.today() - offsets.YearBegin()
        first_day_of_next_year = (date.today() + offsets.YearEnd())+timedelta(days = 1)
        
        distinct_status_defects = Defect.objects.all().distinct('defect_status')
        distinct_oem_ref_defects = Defect.objects.all().distinct('oem_defect_reference')
        distinct_asset_type_defects = Defect.objects.all().distinct('asset_type')
        return render(request, self.template_name, {'defects' : defects[::-1], 
                                                    'asset_datas':asset_data,
                                                    'distinct_status_defects':distinct_status_defects,
                                                    'distinct_oem_ref_defects':distinct_oem_ref_defects,
                                                    'distinct_asset_type_defects':distinct_asset_type_defects,
                                                    'current_date':current_date,
                                                    'tomorrow_date':tomorrow_date.strftime('%Y-%m-%d'),
                                                    'past_7_day_date':past_7_day_date.strftime('%Y-%m-%d'),
                                                    'first_day_of_month':first_day_of_month,
                                                    'first_day_of_next_month':first_day_of_next_month,
                                                    'first_day_of_year':first_day_of_year.strftime('%Y-%m-%d'),
                                                    'first_day_of_next_year':first_day_of_next_year.strftime('%Y-%m-%d')

                                                    })
# 'asset_type':asset_type.replace(" ","_"), 'start_date':formated_start_date,'end_date':formated_end_date

class AdminDefectsAddView(View):
    template_name = 'fracas_defect_identification_details.html'

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        asset_type = req.get('asset_type')
        start_date = req.get('start_date')
        end_date = req.get('end_date')
        print(start_date,"sssssssssssssssss")
        url_header = request.build_absolute_uri()[:-len(request.get_full_path())]
        if start_date and end_date:
            formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
            formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
            print(start_date,formated_start_date,"===============")
            defect = Defect.objects.create(asset_type=asset_type,start_date=formated_start_date,end_date=formated_end_date)
            return JsonResponse({'asset_type':asset_type.replace(" ","_"), 'start_date':formated_start_date,'end_date':formated_end_date, 'defect_id':defect.defect_id, 'url_header':url_header})
        else:
            defect = Defect.objects.create(asset_type=asset_type)
        print(defect.defect_description, "fffffffffffffffff")
        return JsonResponse({'asset_type':asset_type.replace(" ","_"), 'start_date':'','end_date':'', 'defect_id':defect.defect_id, 'url_header':url_header})

class AdminFailuresView(View):
    template_name = 'fracas_defect_identification_details.html'

    def get(self, request, *args, **kwargs):
        print(request.META['HTTP_HOST'],"22222222")
        
        req = request.GET
        asset_type = req.get('asset_type')
        # start_date = req.get('start_date')
        # end_date = req.get('end_date')
        defect_id = req.get('defect_id')
        # formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        # formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        defect = Defect.objects.get(defect_id=defect_id)
        # failure_data = FailureData.objects.filter(asset_config_id__asset_type=asset_type, date__range=[start_date,end_date])
        failure_data = FailureData.objects.filter(asset_config_id__asset_type=asset_type)
        defect_failure_data = FailureData.objects.filter(defect=defect)
        return render(request, self.template_name, {'defect_id' : defect.defect_id, 'failure_datas':failure_data, 'defect':defect,'defect_failure_datas':defect_failure_data})

class AdminDefectsUpdateView(View):
    template_name = 'fracas_defect_identification_details.html'


    def get(self, request, *args, **kwargs):
        
        data=[]
        
        req = request.GET
        defect_id = req.get('defect_id')
        print(defect_id,"ZZZZZZZZZZ")      
        defect = Defect.objects.get(defect_id=defect_id)

        data.append({'defect_description':defect.defect_description,
                     'investigation':defect.investigation,
                     'defect_status_remarks':defect.defect_status_remarks,
                     'oem_defect_reference':defect.oem_defect_reference,
                     'defect_status':defect.defect_status,
                     'defect_open_date':(defect.defect_open_date).strftime('%d/%m/%Y'),
                     'defect_closed_date':(defect.defect_closed_date).strftime('%d/%m/%Y'),
                     'oem_target_date':(defect.oem_target_date).strftime('%d/%m/%Y'),
            })
        return JsonResponse({'success':'success', 'data':data})

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        # asset_type = unquote(req.get('asset_type'))
        defect_id = req.get('defect_id')
        defect_description = req.get('defect_description')
        investigation = req.get('defect_Investigation')
        defect_status_remarks = req.get('defect_status_remarks')
        oem_defect_reference = req.get('oem_defect_reference')
        defect_status = req.get('defect_status')
        progress_log = req.get('progress_log')
        delete_defect = req.get('delete_defect')
        if req.get('defect_open_date'):
            defect_open_date = datetime.strptime(req.get('defect_open_date'), "%d/%m/%Y").strftime("%Y-%m-%d")
        if req.get('defect_closed_date'):
            defect_closed_date = datetime.strptime(req.get('defect_closed_date'), "%d/%m/%Y").strftime("%Y-%m-%d")
        if req.get('oem_target_date'):
            oem_target_date = datetime.strptime(req.get('oem_target_date'), "%d/%m/%Y").strftime("%Y-%m-%d")
        print(defect_id,"mmmmmmmmmmm")
        failure_ids = req.getlist('idsArr[]')
        
        defect = Defect.objects.get(defect_id=defect_id)
        if not delete_defect:
            defect.defect_description=defect_description
            defect.investigation=investigation
            defect.defect_status_remarks=defect_status_remarks
            defect.oem_defect_reference=oem_defect_reference
            defect.defect_status=defect_status
            defect.progress_log=progress_log
            
            if req.get('defect_open_date'):
                defect.defect_open_date=defect_open_date
            if req.get('defect_closed_date'):
                defect.defect_closed_date=defect_closed_date
            if req.get('oem_target_date'):
                defect.oem_target_date=oem_target_date
            defect.save()
            
            defect_failure_datas = FailureData.objects.filter(defect=defect)
            for defect_failure_data in defect_failure_datas:
                defect_failure_data.defect = None
                defect_failure_data.save()
            failure_datas = FailureData.objects.filter(failure_id__in=failure_ids)
            for failure_data in failure_datas:
                failure_data.defect = defect
                failure_data.save()
        else:
            # corrective_action = CorrectiveAction.objects.get(defect=defect)
            # failure_data = FailureData.objects.get(defect=defect)
            # defect_discussion = DefectDiscussion.objects.get(defect=defect)
            defect.delete()

        return JsonResponse({'success':'success'})

class AdminDefectsFailureRemoveView(View):
    template_name = 'fracas_defect_identification_details.html'

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        defect_id = req.get('defect_id')
        failure_id = req.get('failure_id')
        # failure_ids = req.getlist('idsArr[]')
        defect = Defect.objects.get(defect_id=defect_id)
        
        failure_data = FailureData.objects.get(failure_id=failure_id, defect=defect)

        failure_data.defect = None
        failure_data.save()

        return JsonResponse({'success':'success'})


class AdminDefectsCorrectiveActionAddView(View):
    template_name = 'root_cause_change_form.html'


    def get(self, request, *args, **kwargs):
        
        data=[]
        
        req = request.GET
        defect_id = req.get('defect_id')
        print(defect_id,"XXXXXXXXXXX")      
        defect = Defect.objects.get(defect_id=defect_id)

        corrective_actions = CorrectiveAction.objects.filter(defect=defect)
        for action in corrective_actions:

            data.append({'corrective_action_owner':action.corrective_action_owner,
                     'corrective_action_status':action.corrective_action_status,
                     'corrective_action_description':action.corrective_action_description,
                     'corrective_action_update':action.corrective_action_update,
                     'defect_id':action.defect.defect_id,
                     'corrective_action_id':action.corrective_action_id
            })
        return JsonResponse({'success':'success', 'data':data})

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        # asset_type = unquote(req.get('asset_type'))
        defect_id = req.get('defect_id')
        corrective_action_owner = req.get('corrective_action_owner')
        corrective_action_status = req.get('corrective_action_status')
        corrective_action_description = req.get('corrective_action_description')
        corrective_action_update = req.get('corrective_action_update')
        defect = Defect.objects.get(defect_id=defect_id)
        corrective_action = CorrectiveAction.objects.create(
                            corrective_action_owner=corrective_action_owner,
                            corrective_action_status=corrective_action_status,
                            corrective_action_description=corrective_action_description,
                            corrective_action_update=corrective_action_update,
                            defect=defect
            )
        defect1=corrective_action.defect.defect_id
        return JsonResponse({'success':'success' ,'defect1':defect1})

class AdminDefectsCorrectiveActionUpdateView(View):
    template_name = 'fracas_review_board_details.html'


    def get(self, request, *args, **kwargs):
        req = request.GET

        corrective_action_id = req.get('corrective_action_id')
        print(corrective_action_id,"mlooooooooo")
        data=[]
        corrective_action = CorrectiveAction.objects.get(corrective_action_id=corrective_action_id)

        data.append({'corrective_action_owner':corrective_action.corrective_action_owner,
                 'corrective_action_status':corrective_action.corrective_action_status,
                 'corrective_action_description':corrective_action.corrective_action_description,
                 'corrective_action_update':corrective_action.corrective_action_update,
                 'defect_id':corrective_action.defect.defect_id,
                 'corrective_action_id':corrective_action.corrective_action_id
        })

        return JsonResponse({'success':'success', 'data':data})

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        # asset_type = unquote(req.get('asset_type'))

        corrective_action_id = req.get('corrective_action_id')
        delete_c_action = req.get('delete_c_action')
        corrective_action_owner = req.get('corrective_action_owner')
        corrective_action_description = req.get('corrective_action_description')
        corrective_action_update = req.get('corrective_action_update')
        corrective_action_status = req.get('corrective_action_status')
        print(corrective_action_owner,"ccccccccc")
        corrective_action = CorrectiveAction.objects.get(corrective_action_id=corrective_action_id)
        if delete_c_action:
            corrective_action.delete()
        else:
            corrective_action.corrective_action_owner=corrective_action_owner
            corrective_action.corrective_action_status=corrective_action_status
            corrective_action.corrective_action_description=corrective_action_description
            corrective_action.corrective_action_update=corrective_action_update

            corrective_action.save()

        return JsonResponse({'success':'success'})


class History(View):
    template_name = 'history.html'
    
    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        # if user_Role == 3 or user_Role == 4 or user_Role == 2:
        #     return redirect('/dashboard/')
        if user_Role == 1:
            subsystem = Product.objects.filter(is_active=0)
        else:
            subsystem = Product.objects.filter(product_id=P_id,is_active=0)
        return render(request, self.template_name,{'subsystem':subsystem})
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        data=[]
        req = request.POST
        productID = req.get('subsystem')
        # print(req)
        if user_Role == 1:
            if productID == "all":
                history_data =history.objects.filter()
            else:
                history_data =history.objects.filter(P_id=productID)
        else:
            history_data =history.objects.filter(P_id=P_id)
            
        if req.get('startDate') !="" and req.get('endDate') !="":
            start_date = datetime.strptime(req.get('startDate'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.strptime(req.get('endDate'), '%d/%m/%Y').strftime('%Y-%m-%d')
            history_data =history_data.filter(date__range=[start_date,end_date])
            
        if req.get('starttime') !="" and req.get('endtime') !="":
            start_time = req.get('starttime')
            end_time = req.get('endtime')
            history_data =history_data.filter(time__range=[start_time,end_time])
            
        for historys in history_data:
            userData =UserProfile.objects.filter(id=historys.user_id)
            email = User.objects.filter(id=userData[0].user_id)
            grp = Group.objects.filter(id=userData[0].user_role_id)
            if historys.P_id == 0:
                pd = "All"
            else:
                prod = Product.objects.filter(product_id=historys.P_id)
                pd= prod[0].product_name
            
            data.append({ 
                'id' :  historys.user_id,
                'email' : email[0].username,
                'name' : userData[0].first_name+' '+userData[0].last_name,
                'user_role' : grp[0].name,
                'product' : pd,
                'date' : historys.date,
                'time' : historys.time,
                'function_name' : historys.function_name,
                'message' : historys.message,
            })
        
        return JsonResponse({'data':data})
    
class HistoryP(View):
    template_name = 'historyp.html'
    
    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        # if user_Role == 3 or user_Role == 4 or user_Role == 2:
        #     return redirect('/dashboard/')
        id = kwargs.get("id")
        if id == None:
            return redirect('history')
        return render(request, self.template_name,{'userid':id})
    
class PersonalHistory(View):
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        data=[]
        req = request.POST
        userid = req.get('userid')
        # print(req)
        history_data =history.objects.filter(user_id=userid)
            
        if req.get('startDate') !="" and req.get('endDate') !="":
            start_date = datetime.strptime(req.get('startDate'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.strptime(req.get('endDate'), '%d/%m/%Y').strftime('%Y-%m-%d')
            history_data =history_data.filter(date__range=[start_date,end_date])
            
        if req.get('starttime') !="" and req.get('endtime') !="":
            start_time = req.get('starttime')
            end_time = req.get('endtime')
            history_data =history_data.filter(time__range=[start_time,end_time])
            
        for historys in history_data:
            userData =UserProfile.objects.filter(id=historys.user_id)
            email = User.objects.filter(id=userData[0].user_id)
            grp = Group.objects.filter(id=userData[0].user_role_id)
            if historys.P_id == 0:
                pd = "All"
            else:
                prod = Product.objects.filter(product_id=historys.P_id)
                pd= prod[0].product_name
            
            data.append({ 
                'id' :  historys.user_id,
                'email' : email[0].username,
                'name' : userData[0].first_name+' '+userData[0].last_name,
                'user_role' : grp[0].name,
                'product' : pd,
                'date' : historys.date,
                'time' : historys.time,
                'function_name' : historys.function_name,
                'message' : historys.message,
            })
        
        return JsonResponse({'data':data})
    
class ProjectManage(View):
    template_name = 'manage_project.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        # if user_Role == 3 or user_Role == 4 or user_Role == 2:
        #     return redirect('/dashboard/')
        units = PBSUnit.objects.all()
        MTBFMTBSAF = units[0].MTBFMTBSAF
        MTTR = units[0].MTTR
        return render(request, self.template_name,{'MTBFMTBSAF':MTBFMTBSAF,'MTTR':MTTR})

    def post(self, request, *args, **kwargs):
        data=[]
        req = request.POST
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 1:
            project = Product.objects.filter(is_active=0)
        else:
            project = Product.objects.filter(is_active=0,product_id=P_id)
        for i in project:
            data.append({ 
                'product_id' : i.product_id,
                'product_name' : i.product_name,
                'MTBF' : i.MTBF,
                'MTBSAF':i.MTBSAF,
                'MTTR':i.MTTR,
                'availability_target':i.availability_target,
                'user_role':user_Role,
                'num_of_trains':i.num_of_trains,
            })
        return JsonResponse({'data':data})  


class ManageEdit(View):
    template_name = 'edit_manageProduct.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4 or user_Role == 2:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]
        if id==None:
            data={ 
            'product_id' : '',
            'product_name' :'',
            'MTBF' : '',
            'MTBSAF':'',
            'MTTR':'',
            'availability_target':'',
            'num_of_trains':''
            }
        else:
            project_datas =Product.objects.filter(product_id=id)
            for i in project_datas:
                data={ 
                   'product_id' : i.product_id,
                    'product_name' :i.product_name,
                    'MTBF' : i.MTBF,
                    'MTBSAF':i.MTBSAF,
                    'MTTR':i.MTTR,
                    'availability_target':i.availability_target,
                    'num_of_trains':i.num_of_trains
                }
            #print(data)
        units = PBSUnit.objects.all()
        MTBFMTBSAF = units[0].MTBFMTBSAF
        MTTR = units[0].MTTR
        return render(request, self.template_name,{'data':data,'MTBFMTBSAF':MTBFMTBSAF,'MTTR':MTTR})

    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        product_id = req.get('product_id')
        product_name = req.get('product_name')
        MTBF = req.get('MTBF')
        MTBSAF = req.get('MTBSAF')
        MTTR = req.get('MTTR')
        availability_target = req.get('availability_target')
        num_of_trains = req.get('num_of_trains')
       
        if product_id =="":
            if Product.objects.filter(product_name=product_name,is_active=0).exists():
                return JsonResponse({'status':'0'})
            else:
                r=Product(product_name=product_name,MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,availability_target=availability_target,num_of_trains=num_of_trains)
                r.save()
                FindUser = UserProfile.objects.filter(user_id=user_ID)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                meg ="Add new project "
                meg ="PROJECT: "+product_name +"=> "+meg
                h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Add Project RAM Targets")
                h.save()
                return JsonResponse({'status':'1','id':r.product_id})
        else:
            AFTER = Product.objects.filter(product_id=product_id)
            meg =''
            if product_name != AFTER[0].product_name:
                meg = meg +'product_name: '+ AFTER[0].product_name +' to '+product_name+', '
            if MTBF != str(AFTER[0].MTBF):
                meg = meg +'MTBF: '+ str(AFTER[0].MTBF) +' to '+str(MTBF)+', '
            if MTBSAF != str(AFTER[0].MTBSAF):
                meg = meg +'MTBSAF: '+ str(AFTER[0].MTBSAF) +' to '+str(MTBSAF)+', '
            if MTTR != str(AFTER[0].MTTR):
                meg = meg +'MTTR: '+ str(AFTER[0].MTTR) +' to '+str(MTTR)+', '
            if availability_target != str(AFTER[0].availability_target):
                meg = meg +'availability_target: '+ str(AFTER[0].availability_target) +' to '+str(availability_target)+', '
            if num_of_trains != str(AFTER[0].num_of_trains):
                meg = meg +'num_of_trains: '+ str(AFTER[0].num_of_trains) +' to '+str(num_of_trains)+', '

            if Product.objects.filter(product_name=product_name,is_active=0).exists():
                if Product.objects.filter(product_name=product_name, product_id=product_id,is_active=0).exists():
                    Product.objects.filter(product_id=product_id).update(MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,availability_target=availability_target,num_of_trains=num_of_trains)
                    if meg !='':
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="PRODUCT ID: "+product_id +" => "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Add Project RAM Targets")
                        h.save()
                    return JsonResponse({'status':'1','id':product_id})
                else:
                    return JsonResponse({'status':'0'})
            else:
                Product.objects.filter(product_id=product_id).update(product_name=product_name,MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,availability_target=availability_target,num_of_trains=num_of_trains)
                if meg !='':
                    FindUser = UserProfile.objects.filter(user_id=user_ID)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    meg ="PRODUCT ID: "+product_id +" => "+meg
                    h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Add Project RAM Targets")
                    h.save()
                return JsonResponse({'status':'1','id':product_id})
               
class DeleteManageEdit(View):
    
    def post(self, request, *args, **kwargs):
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4 or user_Role == 2:
            return redirect('/dashboard/')
        req = self.request.POST
        id = req.get('id')
        Product.objects.filter(product_id=id).update(is_active=1)
        FindDelete = Product.objects.filter(product_id=id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete Project "
        meg ="PROJECT: "+FindDelete[0].product_name +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Add Project RAM Targets")
        h.save()
        return JsonResponse({'status':'1'})

    
class Config(View):
    template_name = 'config.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        # user_Role = request.session.get('user_Role')
        # if user_Role == 3 or user_Role == 4 or user_Role == 2:
        #     return redirect('/dashboard/')
        units = PBSUnit.objects.all()
        MTBFMTBSAF = units[0].MTBFMTBSAF
        MTTR = units[0].MTTR
        average_speed = units[0].average_speed
        chk_average_speed = units[0].chk_average_speed
        id = units[0].id
        return render(request, self.template_name,{'MTBFMTBSAF':MTBFMTBSAF,'MTTR':MTTR,'id':id,'average_speed':average_speed,'chk_average_speed':chk_average_speed})
    
    def post(self, request, *args, **kwargs):
        user_Role = request.session.get('user_Role')
        if user_Role != 1:
            return redirect('/dashboard/')
        req = self.request.POST
        id = req.get('id')
        MTBFMTBSAF = req.get('MTBFMTBSAF')
        MTTR = req.get('MTTR')
        AFTER = PBSUnit.objects.filter(id=id)
        meg = ''
        if MTBFMTBSAF != AFTER[0].MTBFMTBSAF:
            meg = meg +'MTBF/MTBSAF: '+ AFTER[0].MTBFMTBSAF +' to '+MTBFMTBSAF+', '
        if MTTR != AFTER[0].MTTR:
            meg = meg +'MTTR: '+ AFTER[0].MTTR +' to '+MTTR+', '

        average_speed  = req.get('average_speed')
        chk_average_speed  = req.get('chk_average_speed')

        PBSUnit.objects.filter(id=id).update(MTBFMTBSAF=MTBFMTBSAF,MTTR=MTTR,average_speed=average_speed,chk_average_speed=chk_average_speed)
        if meg != '':
            P_id = request.session['P_id']
            user_ID = request.session['user_ID']
            FindUser = UserProfile.objects.filter(user_id=user_ID)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            # meg ="Change Unit"
            h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Set PBS Master Unit")
            h.save()
        return JsonResponse({'status':'1'})

class SystemManage(View):
    template_name = 'manage_system.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        # if user_Role == 3 or user_Role == 4 or user_Role == 2:
        #     return redirect('/dashboard/')
        units = PBSUnit.objects.all()
        MTBFMTBSAF = units[0].MTBFMTBSAF
        MTTR = units[0].MTTR
        return render(request, self.template_name,{'MTBFMTBSAF':MTBFMTBSAF,'MTTR':MTTR})

    def post(self, request, *args, **kwargs):
        data=[]
        req = request.POST
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 1:
            System = Systems.objects.filter(is_active=0)
        else:
            System = Systems.objects.filter(is_active=0,project_id=P_id)
        for i in System:
            product = Product.objects.filter(product_id=i.project_id)
            data.append({ 
                'id':i.id,
                'project' : product[0].product_name,
                'System' : i.System,
                'MTBF' : i.MTBF,
                'MTBSAF':i.MTBSAF,
                'MTTR':i.MTTR,
                'availability_target':i.availability_target,
                'user_role':user_Role,
            })
        return JsonResponse({'data':data})  

class ManageSystemEdit(View):
    template_name = 'edit_manageSystem.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            project = Product.objects.filter(is_active=0)
        else:
            project = Product.objects.filter(product_id=P_id,is_active=0)
        if user_Role == 3 or user_Role == 4 or user_Role == 2:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]
        if id==None:
            data={ 
            'id':'',
            'project' : '',
            'System' :'',
            'MTBF' : '',
            'MTBSAF':'',
            'MTTR':'',
            'availability_target':''
            }
        else:
            System_datas =Systems.objects.filter(id=id)
            for i in System_datas:
                data={ 
                    'id':i.id,
                   'project' : i.project_id,
                    'System' :i.System,
                    'MTBF' : i.MTBF,
                    'MTBSAF':i.MTBSAF,
                    'MTTR':i.MTTR,
                    'availability_target':i.availability_target
                }
            #print(data)
        units = PBSUnit.objects.all()
        MTBFMTBSAF = units[0].MTBFMTBSAF
        MTTR = units[0].MTTR
        return render(request, self.template_name,{'project':project,'data':data,'MTBFMTBSAF':MTBFMTBSAF,'MTTR':MTTR})

    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        id = req.get('id')
        project = req.get('project')
        system = req.get('system')
        MTBF = req.get('MTBF')
        MTBSAF = req.get('MTBSAF')
        MTTR = req.get('MTTR')
        availability_target = req.get('availability_target')
       
        if id =="":
            if Systems.objects.filter(System=system,is_active=0).exists():
                return JsonResponse({'status':'0'})
            else:
                r=Systems(project_id=project,System=system,MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,availability_target=availability_target)
                r.save()
                FindUser = UserProfile.objects.filter(user_id=user_ID)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                meg ="Add System Level RAM Targets "
                meg ="System: "+system +"=> "+meg
                h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Add System Level RAM Targets")
                h.save()
                return JsonResponse({'status':'1','id':r.id})
        else:
            AFTER = Systems.objects.filter(id=id)
            meg =''
            if system != AFTER[0].System:
                meg = meg +'product_name: '+ AFTER[0].System +' to '+system+', '
            if MTBF != str(AFTER[0].MTBF):
                meg = meg +'MTBF: '+ str(AFTER[0].MTBF) +' to '+str(MTBF)+', '
            if MTBSAF != str(AFTER[0].MTBSAF):
                meg = meg +'MTBSAF: '+ str(AFTER[0].MTBSAF) +' to '+str(MTBSAF)+', '
            if MTTR != str(AFTER[0].MTTR):
                meg = meg +'MTTR: '+ str(AFTER[0].MTTR) +' to '+str(MTTR)+', '
            if availability_target != str(AFTER[0].availability_target):
                meg = meg +'availability_target: '+ str(AFTER[0].availability_target) +' to '+str(availability_target)+', '

            if Systems.objects.filter(System=system,is_active=0).exists():
                if Systems.objects.filter(System=system, id=id,is_active=0).exists():
                    Systems.objects.filter(id=id).update(project_id=project,MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,availability_target=availability_target)
                    if meg !='':
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="System ID: "+id +" => "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Add System Level RAM Targets")
                        h.save()
                    return JsonResponse({'status':'1','id':id})
                else:
                    return JsonResponse({'status':'0'})
            else:
                Systems.objects.filter(id=id).update(project_id=project,System=system,MTBF=MTBF,MTBSAF=MTBSAF,MTTR=MTTR,availability_target=availability_target)
                if meg !='':
                    FindUser = UserProfile.objects.filter(user_id=user_ID)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    meg ="System ID: "+id +" => "+meg
                    h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Add System Level RAM Targets")
                    h.save()
                return JsonResponse({'status':'1','id':id})
            
class DeleteManageSystemEdit(View):
    
    def post(self, request, *args, **kwargs):
        user_Role = request.session.get('user_Role')
        if user_Role == 3 or user_Role == 4 or user_Role == 2:
            return redirect('/dashboard/')
        req = self.request.POST
        id = req.get('id')
        Systems.objects.filter(id=id).update(is_active=1)
        FindDelete = Systems.objects.filter(id=id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete System Level RAM Targets "
        meg ="System: "+str(FindDelete[0].id )+"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=date.today(),time=current_time,message=meg,function_name="Add System Level RAM Targets")
        h.save()
        return JsonResponse({'status':'1'})
