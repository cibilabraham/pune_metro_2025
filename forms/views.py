from django.shortcuts import render, redirect

from fracas.models import *
from django.views import View
import calendar
from pandas.tseries import offsets
from django.http import HttpResponse,JsonResponse
from urllib.parse import unquote
from nested_inline.admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline
from django.db.models import Count
import json
from django.core.serializers.json import DjangoJSONEncoder
import datetime

import os
import xlrd
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import connection
import string

class assetRegister(View):
    template_name = 'asset_register.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            location_id = Asset.objects.filter(is_active=0).distinct('location_id')
            asset_serial_number = Asset.objects.filter(is_active=0).distinct('asset_serial_number')
            asset_type = PBSMaster.objects.filter(is_active=0).order_by('asset_type') 
            asset_description = Asset.objects.filter(is_active=0).distinct('asset_description')
            software_version = Asset.objects.filter(is_active=0).distinct('software_version')
            software_description = Asset.objects.filter(is_active=0).distinct('software_description')
            asset_status = Asset.objects.filter(is_active=0).distinct('asset_status')
        else:
            location_id = Asset.objects.filter(is_active=0,P_id=P_id).distinct('location_id')
            asset_serial_number = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_serial_number')
            asset_description = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_description')
            software_version = Asset.objects.filter(is_active=0,P_id=P_id).distinct('software_version')
            software_description = Asset.objects.filter(is_active=0,P_id=P_id).distinct('software_description')
            asset_status = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_status')
            asset_type = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type') 
        return render(request, self.template_name, {'asset_status':asset_status,'software_description':software_description, 'software_version':software_version, 'asset_description':asset_description, 'location_id' : location_id, 'asset_serial_number':asset_serial_number,'asset_type':asset_type})

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        location_id = req.get('location_id')
        asset_serial_number = req.get('asset_serial_number')
        asset_type = req.get('asset_type')
        asset_description = req.get('asset_description')
        software_version = req.get('software_version')
        software_description = req.get('software_description')
        asset_status = req.get('asset_status')
        
        Asset_data =Asset.objects.filter(is_active=0)
        print(Asset_data)

        if location_id != "all":
            Asset_data=Asset_data.filter(location_id=location_id)
        if asset_serial_number != "all":
            Asset_data=Asset_data.filter(asset_serial_number=asset_serial_number)
        if asset_type != "all":
            Asset_data=Asset_data.filter(asset_type=asset_type)
        if asset_description != "all":
            Asset_data=Asset_data.filter(asset_description=asset_description)
        if software_version != "all":
            Asset_data=Asset_data.filter(software_version=software_version)
        if software_description != "all":
            Asset_data=Asset_data.filter(software_description=software_description)
        if asset_status != "all":
            Asset_data=Asset_data.filter(asset_status=asset_status)
    
        # Asset_data = Asset.objects.all()
        for Assets in Asset_data:
            print(Assets.asset_type)
            if PBSMaster.objects.filter(id=Assets.asset_type,is_active=0).exists():
                print('uuuuuuuu')
                if user_Role == 1:
                    PBSMaster_datas=PBSMaster.objects.filter(id=Assets.asset_type,is_active=0)
                    for PBSMaster_data in PBSMaster_datas:
                        data.append({ 
                            'asset_config_id' :  Assets.asset_config_id,
                            'location_id' : Assets.location_id,
                            'location_description' : Assets.location_description,
                            'asset_serial_number' : Assets.asset_serial_number,
                            'asset_type' : PBSMaster_data.asset_type,
                            'asset_description' : Assets.asset_description,
                            'software_version' : Assets.software_version,
                            'software_description' : Assets.software_description,
                            'asset_status':Assets.asset_status,
                            'id':Assets.id,
                            'user_Role':user_Role,
                        }) 
                else:
                    if PBSMaster.objects.filter(id=Assets.asset_type,project_id=P_id,is_active=0).exists():
                        PBSMaster_datas=PBSMaster.objects.filter(id=Assets.asset_type,is_active=0)
                        for PBSMaster_data in PBSMaster_datas:
                            data.append({ 
                                'asset_config_id' :  Assets.asset_config_id,
                                'location_id' : Assets.location_id,
                                'location_description' : Assets.location_description,
                                'asset_serial_number' : Assets.asset_serial_number,
                                'asset_type' : PBSMaster_data.asset_type,
                                'asset_description' : Assets.asset_description,
                                'software_version' : Assets.software_version,
                                'software_description' : Assets.software_description,
                                'asset_status':Assets.asset_status,
                                'id':Assets.id,
                                'user_Role':user_Role
                            }) 
        print(data)
        return JsonResponse({'data':data})

    

class AddAsset(View):
    template_name = 'add_asset.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]
        if id==None:
            data={ 
            'asset_config_id' : '',
            'location_id' : '',
            'location_description' : '',
            'asset_serial_number' : '',
            'asset_type' : '',
            'asset_description' : '',
            'software_version' : '',
            'software_description' : '',
            'asset_status':'',
            'id':'',
            }
        else:
            Asset_datas =Asset.objects.filter(id=id)
            for Asset_data in Asset_datas:
                data={ 
                    'asset_config_id' : Asset_data.asset_config_id,
                    'location_id' : Asset_data.location_id,
                    'location_description' : Asset_data.location_description,
                    'asset_serial_number' : Asset_data.asset_serial_number,
                    'asset_type' : Asset_data.asset_type,
                    'asset_description' : Asset_data.asset_description,
                    'software_version' : Asset_data.software_version,
                    'software_description' : Asset_data.software_description,
                    'asset_status':Asset_data.asset_status,
                    'id':id,
                }
            #print(data)
        if user_Role == 1:
            asset_types = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
        else:
            asset_types = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type')
        return render(request, self.template_name,{'data':data,'asset_types':asset_types})

    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        location_id = req.get('location_id')
        asset_serial_number = req.get('asset_serial_number')
        asset_type = req.get('asset_type')
        asset_description = req.get('asset_description')
        software_version = req.get('software_version')
        software_description = req.get('software_description')
        asset_status = req.get('asset_status')
        asset_config_id = req.get('asset_config_id')
        location_description = req.get('location_description')
        Action = req.get('Action')
        ids = req.get('id')
        DATA = []
        HEAD = ["asset_config_id",'asset_serial_number','location_id','location_description','asset_type','software_version','asset_description','software_description','asset_status']
        asst =PBSMaster.objects.filter(asset_type=asset_type,is_active=0)
        for f in HEAD:
            if f == 'asset_type':
                DATA.append({
                    'field':f,
                    'value':asst[0].id
                })
            else:
                DATA.append({
                    'field':f,
                    'value':req.get(f)
                })
        # print(DATA)
        if ids =="":
            if Asset.objects.filter(asset_config_id=asset_config_id,is_active=0).exists():
                return JsonResponse({'status':'0'})
            else:
                Find_Pids =PBSMaster.objects.filter(asset_type=asset_type,is_active=0)
                for Find_Pid in Find_Pids:
                    r=Asset(P_id=Find_Pid.project_id,asset_config_id=asset_config_id,location_id=location_id,location_description=location_description,asset_serial_number=asset_serial_number,asset_type=Find_Pid.id,asset_description=asset_description,software_version=software_version,software_description=software_description,asset_status=asset_status)
                    r.save()
                    FindUser = UserProfile.objects.filter(user_id=user_ID)
                    now = datetime.datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    meg ="Add new Asset  "
                    meg ="ID: "+str(r.id) +"=> "+meg
                    h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Asset Register")
                    h.save()
                    return JsonResponse({'status':'1','id':r.id})
        else:
            meg =''
            for i in DATA:
                cursor.execute("SELECT * FROM fracas_asset WHERE id='{0}' and {1}='{2}'".format(ids,i['field'],i['value']))
                row = cursor.fetchone()
                if row == None:
                    cursor.execute("SELECT {0} FROM fracas_asset WHERE id='{1}'".format(i['field'],ids))
                    row1 = cursor.fetchone()
                    if i['field'] == 'asset_type':
                        asst1 =PBSMaster.objects.filter(id=row1[0])
                        meg = meg +i['field']+': '+ str(asst1[0].asset_type) +' to '+str(asset_type)+', '
                    else:
                        meg = meg +i['field']+': '+ str(row1[0]) +' to '+str(i['value'])+', '
                    
            if Asset.objects.filter(asset_config_id=asset_config_id,is_active=0).exists():
                if Asset.objects.filter(asset_config_id=asset_config_id, id=ids,is_active=0).exists():
                    Find_Pids =PBSMaster.objects.filter(asset_type=asset_type,is_active=0)
                    for Find_Pid in Find_Pids:
                        Asset.objects.filter(id=ids).update(P_id=Find_Pid.project_id,location_id=location_id,location_description=location_description,asset_serial_number=asset_serial_number,asset_type=Find_Pid.id,asset_description=asset_description,software_version=software_version,software_description=software_description,asset_status=asset_status)
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+ids +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Asset Register")
                            h.save()
                        return JsonResponse({'status':'1','id':ids})
                else:
                    return JsonResponse({'status':'0'})
            else:
                AFTER = Asset.objects.filter(id=ids)
                if FailureData.objects.filter(asset_config_id=AFTER[0].asset_config_id,is_active=0).exists():
                    return JsonResponse({'status':'2'})
                else:
                    Find_Pids =PBSMaster.objects.filter(asset_type=asset_type,is_active=0)
                    for Find_Pid in Find_Pids:
                        Asset.objects.filter(id=ids).update(P_id=Find_Pid.project_id,asset_config_id=asset_config_id,location_id=location_id,location_description=location_description,asset_serial_number=asset_serial_number,asset_type=Find_Pid.id,asset_description=asset_description,software_version=software_version,software_description=software_description,asset_status=asset_status)
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+ids +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Asset Register")
                            h.save()
                        return JsonResponse({'status':'1','id':ids})
                
class DeleteAsset(View):
    template_name = 'asset_register.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        # print(req)
        id = req.get('id')
        Asset.objects.filter(id=id).update(is_active=1)
        FindDelete = Asset.objects.filter(id=id)
        FailureData.objects.filter(asset_config_id=FindDelete[0].asset_config_id).update(is_active=1)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete asset "
        # FindDelete[0].asset_config_id
        meg ="ID: "+str(id) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Asset Register")
        h.save()
        return JsonResponse({'status':'1'})
            

class Failuredata(View):
    template_name = 'failuredata.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            asset_type = FailureData.objects.all().distinct('asset_type').order_by('asset_type')
            failure_type = FailureData.objects.all().distinct('failure_type')
            safety_failure = FailureData.objects.all().distinct('safety_failure')
            mode_id = FailureMode.objects.filter(is_active=0).distinct('mode_id')
            asset_type = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
        else:
            asset_type = FailureData.objects.all().distinct('asset_type').order_by('asset_type')
            failure_type = FailureData.objects.all().distinct('failure_type')
            safety_failure = FailureData.objects.all().distinct('safety_failure')
            mode_id = FailureMode.objects.filter(is_active=0,P_id=P_id).distinct('mode_id')
            asset_type = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type') 
        return render(request, self.template_name, {'asset_type':asset_type, 'failure_type':failure_type, 'safety_failure':safety_failure, 'mode_id' : mode_id})

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        asset_type = req.get('asset_type')
        failure_type = req.get('failure_type')
        safety_failure = req.get('safety_failure')
        mode_id = req.get('mode_id')
        if user_Role == 1:
            FailureData_data =FailureData.objects.filter(is_active=0)
        else:
            FailureData_data =FailureData.objects.filter(is_active=0,P_id=P_id)

        if asset_type != "all":
            FailureData_data=FailureData_data.filter(asset_type=asset_type)
        if req.get('date') !="":
            date = datetime.datetime.strptime(req.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            FailureData_data=FailureData_data.filter(date=date)
        if failure_type != "all":
            FailureData_data=FailureData_data.filter(failure_type=failure_type)
        if safety_failure != "all":
            FailureData_data=FailureData_data.filter(safety_failure=safety_failure)
        if mode_id != "all":
            FailureData_data=FailureData_data.filter(mode_id=mode_id)
    
        # Asset_data = Asset.objects.all()
        for FailureDatas in FailureData_data:
            if PBSMaster.objects.filter(id=FailureDatas.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    if FailureMode.objects.filter(id=FailureDatas.mode_id_id,is_active=0).exists():
                        FailureModes = FailureMode.objects.filter(id=FailureDatas.mode_id_id)
                        for FailureMode_id in FailureModes:
                            data.append({ 
                                'failure_id' :  FailureDatas.failure_id,
                                'asset_type' : PBSMaster_data.asset_type,
                                'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                                'event_description' : FailureDatas.event_description,
                                'mode_id' : FailureMode_id.mode_id,
                                'mode_description' : FailureDatas.mode_description,
                                'date' : FailureDatas.date,
                                'time' : FailureDatas.time,
                                'detection':FailureDatas.detection,
                                'service_delay' :  FailureDatas.service_delay,
                                'immediate_investigation' : FailureDatas.immediate_investigation,
                                'failure_type' : FailureDatas.failure_type,
                                'safety_failure' : FailureDatas.safety_failure,
                                'hazard_id' : FailureDatas.hazard_id,
                                'cm_description' : FailureDatas.cm_description,
                                'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                                'cm_start_date' : FailureDatas.cm_start_date,
                                'cm_start_time' : FailureDatas.cm_start_time,
                                'cm_end_date' : FailureDatas.cm_end_date,
                                'cm_end_time' : FailureDatas.cm_end_time,
                                'oem_failure_reference' : FailureDatas.oem_failure_reference,
                                'defect' : FailureDatas.defect_id,
                                'id':FailureDatas.id,
                                'user_Role':user_Role,
                            })  
                    else:
                        data.append({ 
                            'failure_id' :  FailureDatas.failure_id,
                            'asset_type' : PBSMaster_data.asset_type,
                            'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                            'event_description' : FailureDatas.event_description,
                            'mode_id' : '',
                            'mode_description' : FailureDatas.mode_description,
                            'date' : FailureDatas.date,
                            'time' : FailureDatas.time,
                            'detection':FailureDatas.detection,
                            'service_delay' :  FailureDatas.service_delay,
                            'immediate_investigation' : FailureDatas.immediate_investigation,
                            'failure_type' : FailureDatas.failure_type,
                            'safety_failure' : FailureDatas.safety_failure,
                            'hazard_id' : FailureDatas.hazard_id,
                            'cm_description' : FailureDatas.cm_description,
                            'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                            'cm_start_date' : FailureDatas.cm_start_date,
                            'cm_start_time' : FailureDatas.cm_start_time,
                            'cm_end_date' : FailureDatas.cm_end_date,
                            'cm_end_time' : FailureDatas.cm_end_time,
                            'oem_failure_reference' : FailureDatas.oem_failure_reference,
                            'defect' : FailureDatas.defect_id,
                            'id':FailureDatas.id,
                            'user_Role':user_Role,
                        })         
        return JsonResponse({'data':data})
    

class DeleteFailureData(View):
    template_name = 'failuredata.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        # print(req)
        id = req.get('id')
        FailureData.objects.filter(id=id).update(is_active=1)
        FindDelete = FailureData.objects.filter(id=id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete failuredata "
        # str(FindDelete[0].failure_id)
        meg ="ID: "+str(id) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Data Collection")
        h.save()
        return JsonResponse({'status':'1'})

class SystemAssetconfig(View):
    template_name = 'add_failuredata.html'

    def get(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        req = request.GET
        data=[]
        asset_type = req.get('asset_type')
        if asset_type == "":
            return JsonResponse(data, safe=False)
        if user_Role == 1:
            asset_config_id = Asset.objects.filter(is_active=0,asset_type=asset_type).distinct('asset_config_id')
        else:
            asset_config_id = Asset.objects.filter(is_active=0,asset_type=asset_type).distinct('asset_config_id')
        for k in asset_config_id:
            data.append({'asset_config_id':k.asset_config_id,
                         'id':k.id})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)
        # return render(request, self.template_name, {'sub_systems' : sub_systems, 'systems':systems})


class AddFailureData(View):
    template_name = 'add_failuredata.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]
        if id==None:
            data={ 
            'asset_type' : '',
            'failure_id' : '',
            'asset_config_id' : '',
            'event_description' : '',
            'mode_id' : '',
            'mode_description' : '',
            'date' : '',
            'time' : '',
            'detection':'',
            'service_delay' : '',
            'immediate_investigation' : '',
            'failure_type' : '',
            'safety_failure' : '',
            'hazard_id' : '',
            'cm_description' : '',
            'replaced_asset_config_id':'',
            'id':'',
            'cm_start_date' : '',
            'cm_start_time' : '',
            'cm_end_date' : '',
            'cm_end_time' : '',
            'oem_failure_reference' : '',
            'defect':'',
            }
        else:
            FailureDatas=FailureData.objects.filter(id=id)
            for datas in FailureDatas:
                data={ 
                'asset_type' : datas.asset_type,
                'failure_id' : datas.failure_id,
                'asset_config_id' : datas.asset_config_id,
                'event_description' : datas.event_description,
                'mode_id' :datas.mode_id,
                'mode_description' : datas.mode_description,
                'date' : datas.date,
                'time' : datas.time,
                'detection':datas.detection,
                'service_delay' : datas.service_delay,
                'immediate_investigation' : datas.immediate_investigation,
                'failure_type' : datas.failure_type,
                'safety_failure' : datas.safety_failure,
                'hazard_id' : datas.hazard_id,
                'cm_description' : datas.cm_description,
                'replaced_asset_config_id':datas.replaced_asset_config_id,
                'id':id,
                'cm_start_date' : datas.cm_start_date,
                'cm_start_time' : datas.cm_start_time,
                'cm_end_date' : datas.cm_end_date,
                'cm_end_time' : datas.cm_end_time,
                'oem_failure_reference' : datas.oem_failure_reference,
                'defect':datas.defect,
                }
            #print(data)
        if user_Role == 1:
            asset_types = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
            asset_config_id = Asset.objects.filter(is_active=0).distinct('asset_config_id')
            mode_id = FailureMode.objects.filter(is_active=0).distinct('mode_id')
            defect = Defect.objects.filter(is_active=0).distinct('defect_id')
        else:
            asset_types = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type')
            asset_config_id = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_config_id')
            mode_id = FailureMode.objects.filter(is_active=0,P_id=P_id).distinct('mode_id')
            defect = Defect.objects.filter(is_active=0,P_id=P_id).distinct('defect_id')
        return render(request, self.template_name,{'data':data,'defect':defect,'asset_type':asset_types
                                                   ,'asset_config_id':asset_config_id,'mode_id':mode_id})

    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        asset_type = req.get('asset_type')
        failure_id = req.get('failure_id')
        asset_config_ids = req.get('asset_config_id')
        event_description = req.get('event_description')
        mode_id = req.get('mode_id')
        date = datetime.datetime.strptime(req.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        time = req.get('time')
        detection = req.get('detection')
        service_delay = req.get('service_delay')
        immediate_investigation = req.get('immediate_investigation')
        failure_type = req.get('failure_type')
        safety_failure = req.get('safety_failure')
        hazard_id = req.get('hazard_id')
        cm_description = req.get('cm_description')
        replaced_asset_config_id = req.get('replaced_asset_config_id')
        cm_start_date = datetime.datetime.strptime(req.get('cm_start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        cm_start_time = req.get('cm_start_time')
        cm_end_date = req.get('cm_end_date')
        if cm_end_date != '':
            cm_end_date = datetime.datetime.strptime(req.get('cm_end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            cm_end_date = None
        print(cm_end_date,'cm_end_date')
        cm_end_time = req.get('cm_end_time')
        if cm_end_time == "":
            cm_end_time = None
        oem_failure_reference = req.get('oem_failure_reference')
        defect = req.get('defect')
        if defect == "":
            defect = None
        Action = req.get('Action')
        ids = req.get('id')
        ACID = Asset.objects.filter(id=asset_config_ids)
        asset_config_id = ACID[0].asset_config_id

        DATA = []
        HEAD = ["asset_type",'failure_id','asset_config_id_id','event_description','mode_id_id','date','time','detection','service_delay','immediate_investigation','failure_type','safety_failure','hazard_id','cm_description','replaced_asset_config_id','cm_start_date','cm_start_time','cm_end_date','cm_end_time','oem_failure_reference','defect_id']
        for f in HEAD:
            if f == 'asset_config_id_id':
                DATA.append({
                    'field':f,
                    'value':asset_config_id
                })
            elif f == 'mode_id_id':
                DATA.append({
                    'field':f,
                    'value':req.get('mode_id')
                })
            elif f == 'date':
                DATA.append({
                    'field':f,
                    'value':datetime.datetime.strptime(req.get(f), '%d/%m/%Y').strftime('%Y-%m-%d')
                })
            elif f == 'cm_start_date':
                DATA.append({
                    'field':f,
                    'value':datetime.datetime.strptime(req.get(f), '%d/%m/%Y').strftime('%Y-%m-%d')
                })
            elif f == 'cm_end_date':
                DATA.append({
                    'field':f,
                    'value':cm_end_date
                })
            elif f == 'cm_end_time':
                DATA.append({
                    'field':f,
                    'value':cm_end_time
                }) 
            elif f == 'defect_id':
                DATA.append({
                    'field':f,
                    'value':defect
                }) 
            else:
                DATA.append({
                    'field':f,
                    'value':req.get(f)
                })
        # print(DATA)

        if ids =="":
            if FailureData.objects.filter(failure_id=failure_id,is_active=0).exists():
                return JsonResponse({'status':'0'})
            else:
                Find_Pids =PBSMaster.objects.filter(id=asset_type)
                for Find_Pid in Find_Pids:
                    r=FailureData(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=mode_id,defect_id=defect,asset_type=asset_type,failure_id=failure_id,event_description=event_description,date=date,time=time,detection=detection,service_delay=service_delay,immediate_investigation=immediate_investigation,failure_type=failure_type,safety_failure=safety_failure,hazard_id=hazard_id,cm_description=cm_description,replaced_asset_config_id=replaced_asset_config_id,cm_start_date=cm_start_date,cm_start_time=cm_start_time,cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=oem_failure_reference)
                    r.save()
                    FindUser = UserProfile.objects.filter(user_id=user_ID)
                    now = datetime.datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    meg ="Add new failure data "
                    meg ="ID: "+str(r.id) +"=> "+meg
                    h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Data Collection")
                    h.save()
                    return JsonResponse({'status':'1','id':r.id})
        else:
            meg =''
            for i in DATA:
                print('---------------yyyyyyyyyyyyyyyyyyyy-----------')
                print(i['field'])
                if i['value'] != None and i['value'] != '' :
                    cursor.execute("SELECT * FROM fracas_failuredata WHERE id='{0}' and {1}='{2}'".format(ids,i['field'],i['value']))
                    row = cursor.fetchone()
                    print(row)

                    if row == None:
                        cursor.execute("SELECT {0} FROM fracas_failuredata WHERE id='{1}'".format(i['field'],ids))
                        row1 = cursor.fetchone()
                        if i['field'] == 'asset_type':
                            asst1 =PBSMaster.objects.filter(id=asset_type)
                            asst2 =PBSMaster.objects.filter(id=row1[0])
                            meg = meg +i['field']+': '+ asst2[0].asset_type +' to '+asst1[0].asset_type+', '
                        else:
                            meg = meg +i['field']+': '+ str(row1[0] )+' to '+str(i['value'])+', '
                else:
                    cursor.execute("SELECT {0} FROM fracas_failuredata WHERE id='{1}'".format(i['field'],ids))
                    row1 = cursor.fetchone()
                    if row1[0] != i['value']:
                        meg = meg +i['field']+': '+ str(row1[0]) +' to '+str(i['value'])+', '
                print('---------------fffffffffffffffff-----------')
            if FailureData.objects.filter(failure_id=failure_id,is_active=0).exists():
                print('---------------1111111111111111-----------')
                if FailureData.objects.filter(failure_id=failure_id,id=ids,is_active=0).exists():
                    Find_Pids =PBSMaster.objects.filter(id=asset_type)
                    for Find_Pid in Find_Pids:
                        FailureData.objects.filter(id=ids).update(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=mode_id,defect_id=defect,asset_type=asset_type,event_description=event_description,date=date,time=time,detection=detection,service_delay=service_delay,immediate_investigation=immediate_investigation,failure_type=failure_type,safety_failure=safety_failure,hazard_id=hazard_id,cm_description=cm_description,replaced_asset_config_id=replaced_asset_config_id,cm_start_date=cm_start_date,cm_start_time=cm_start_time,cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=oem_failure_reference)
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+ids +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Data Collection")
                            h.save()
                        return JsonResponse({'status':'1','id':ids})
                else:
                    return JsonResponse({'status':'0'})
            else:
                print('---------------2222222222222-----------')
                Find_Pids =PBSMaster.objects.filter(id=asset_type)
                for Find_Pid in Find_Pids:
                    FailureData.objects.filter(id=ids).update(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=mode_id,defect_id=defect,asset_type=asset_type,failure_id=failure_id,event_description=event_description,date=date,time=time,detection=detection,service_delay=service_delay,immediate_investigation=immediate_investigation,failure_type=failure_type,safety_failure=safety_failure,hazard_id=hazard_id,cm_description=cm_description,replaced_asset_config_id=replaced_asset_config_id,cm_start_date=cm_start_date,cm_start_time=cm_start_time,cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=oem_failure_reference)
                    if meg !='':
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="ID: "+ids +"=> "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Data Collection")
                        h.save()
                    return JsonResponse({'status':'1','id':ids})
                
class Failuremode(View):
    template_name = 'failuremode.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            asset_type = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
        else:
            asset_type = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type') 
        return render(request, self.template_name, {'asset_type':asset_type})

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        asset_type = req.get('asset_type')
        if user_Role == 1:
            FailureMode_data =FailureMode.objects.filter(is_active=0)
        else:
            FailureMode_data =FailureMode.objects.filter(is_active=0,P_id=P_id)
            
        for FailureModes in FailureMode_data:
            if asset_type != "all":
                if FailureModes.asset_type != []:
                    for i in FailureModes.asset_type:
                        if i ==  asset_type:
                            if PBSMaster.objects.filter(id=i,is_active=0).exists():
                                PBSMaster_datas=PBSMaster.objects.filter(id=i)
                                data.append({ 
                                    'mode_id' :  FailureModes.mode_id,
                                    'mode_description' : FailureModes.mode_description,
                                    'asset_type' : PBSMaster_datas[0].asset_type,
                                    'id' : FailureModes.id,
                                    'user_Role':user_Role,
                                })  
                    
            else: 
                if FailureModes.asset_type == []:
                    data.append({ 
                        'mode_id' :  FailureModes.mode_id,
                        'mode_description' : FailureModes.mode_description,
                        'asset_type' : '',
                        'id' : FailureModes.id,
                        'user_Role':user_Role,
                    })   
                else:
                    ASST = ''
                    for i in FailureModes.asset_type:
                        if PBSMaster.objects.filter(id=i,is_active=0).exists():
                            PBSMaster_datas=PBSMaster.objects.filter(id=i)
                            if ASST == '':
                                ASST = PBSMaster_datas[0].asset_type
                            else:
                                ASST = ASST +', '+ PBSMaster_datas[0].asset_type
                            
                    data.append({ 
                        'mode_id' :  FailureModes.mode_id,
                        'mode_description' : FailureModes.mode_description,
                        'asset_type' : ASST,
                        'id' : FailureModes.id,
                        'user_Role':user_Role,
                    })         
        return JsonResponse({'data':data})
        
class DeleteFailuremode(View):
    template_name = 'failuremode.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        # print(req)
        id = req.get('id')
        FailureMode.objects.filter(id=id).update(is_active=1)
        FailureData.objects.filter(mode_id_id=id).update(mode_id_id='')
        FindDelete = FailureMode.objects.filter(id=id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete failure mode "
        # FindDelete[0].mode_id
        meg ="ID: "+str(id) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
        h.save()
        return JsonResponse({'status':'1'})   
    
class AddFailuremode(View):
    template_name = 'add_failuremode.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]
        user_ID = request.session['user_ID']
        if id==None:
            data={ 
            'mode_id' :  '',
            'mode_description' : '',
            'asset_type' :'',
            'id' : '',
            'start_date':'',
            'end_date':'',
            'user_Role':user_Role,
            'mode_ID':'',
            }
        else:
            if FailureMode.objects.filter(id=id,is_active=1).exists():
                return redirect('/forms/failuremode/')
            FailureModes =FailureMode.objects.filter(id=id)
            for failureMode in FailureModes:
                data={ 
                    'mode_id' :  failureMode.mode_id,
                    'mode_description' : failureMode.mode_description,
                    'asset_type' :failureMode.asset_type[len(failureMode.asset_type) - 1],
                    'id' : failureMode.id,
                    'start_date':failureMode.start_date,
                    'end_date':failureMode.end_date,
                    'user_Role':user_Role,
                    'mode_ID':id,
                }
            #print(data)
        if user_Role == 1:
            asset_types = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
            asset_type = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
            defect = Defect.objects.filter(is_active=0).distinct('defect_id')
        else:
            asset_types = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type')
            asset_type = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type')
            defect = Defect.objects.filter(is_active=0,P_id=P_id).distinct('defect_id')
        return render(request, self.template_name,{'data':data,'asset_type':asset_type,'defect':defect,'asset_types':asset_type})
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)oldmode_id
        asset_type = req.get('asset_type')
        mode_id = req.get('mode_id')
        mode_description = req.get('mode_description')
        if req.get('start_date') !="" and req.get('end_date') !="":
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            start_date = None
            end_date = None
        ids= req.get('id')
        setModeId= req.get('setModeId')
        action= req.get('action')
        datas= req.get('datas')
        data=json.loads(datas)
        if ids == "":
            Asset_Types = []
            if asset_type !="":
                Asset_Types.append(asset_type)
        else:
            FINDASST_TYPE = FailureMode.objects.filter(id=ids)
            Asset_Types = FINDASST_TYPE[0].asset_type
            if asset_type != '':
                if not asset_type in Asset_Types:
                    Asset_Types.append(asset_type)
        if ids != "":
            FailureModes =FailureMode.objects.filter(id=ids)
            meg = ""
            if FailureModes[0].mode_id != mode_id: 
                meg = meg +'mode_id: '+ FailureModes[0].mode_id +' to '+mode_id+', '
            if FailureModes[0].mode_description != mode_description:
                meg = meg +'mode_description: '+ FailureModes[0].mode_description +' to '+mode_description+', '
     
        if asset_type != "":
            if action == '1':
                if ids =="":
                    if FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
                        return JsonResponse({'status':'0'})
                    else:
                        Find_Pids =PBSMaster.objects.filter(id=asset_type)
                        for Find_Pid in Find_Pids:
                            r=FailureMode(P_id=Find_Pid.project_id,mode_id=mode_id,mode_description=mode_description,asset_type=Asset_Types,start_date=start_date,end_date=end_date)
                            r.save()
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="Add new failure mode "
                            meg ="ID: "+str(r.id) +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                            h.save()
                            return JsonResponse({'status':'1','id':r.id})
                else:
                    if FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
                        if FailureMode.objects.filter(mode_id=mode_id, id=ids,is_active=0).exists():
                            Find_Pids =PBSMaster.objects.filter(id=asset_type)
                            for Find_Pid in Find_Pids:
                                FailureMode.objects.filter(id=ids).update(P_id=Find_Pid.project_id,mode_description=mode_description,asset_type=Asset_Types,start_date=start_date,end_date=end_date)
                                if meg !='':
                                    FindUser = UserProfile.objects.filter(user_id=user_ID)
                                    now = datetime.datetime.now()
                                    current_time = now.strftime("%H:%M:%S")
                                    meg ="ID: "+ids +"=> "+meg
                                    h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                                    h.save()
                                return JsonResponse({'status':'1','id':ids})
                        else:
                            return JsonResponse({'status':'0'})
                    else:
                        Find_Pids =PBSMaster.objects.filter(id=asset_type)
                        for Find_Pid in Find_Pids:
                            FailureMode.objects.filter(id=ids).update(P_id=Find_Pid.project_id,mode_id=mode_id,mode_description=mode_description,asset_type=Asset_Types,start_date=start_date,end_date=end_date)
                            if meg !='':
                                FindUser = UserProfile.objects.filter(user_id=user_ID)
                                now = datetime.datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                meg ="ID: "+ids +"=> "+meg
                                h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                                h.save()
                            return JsonResponse({'status':'1','id':ids})
            else:
                if data !="":
                    for items in data:
                        if items['id'] == 0:
                            failure_id=items['failure_id']
                            if FailureData.objects.filter(failure_id=failure_id,is_active=0).exists():
                                return JsonResponse({'status':'2','Fail_ID':items['failure_id']})   
                if ids =="":
                    if FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
                        return JsonResponse({'status':'0'})
                    else:
                        Find_Pids =PBSMaster.objects.filter(id=asset_type)
                        for Find_Pid in Find_Pids:
                            r=FailureMode(P_id=Find_Pid.project_id,mode_id=mode_id,mode_description=mode_description,asset_type=Asset_Types,start_date=start_date,end_date=end_date)
                            r.save()
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="Add new failure mode "
                            meg ="ID: "+str(r.id) +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                            h.save()
                            if data !="":
                                for item in data:
                                    if item['id'] == 0:
                                        Find_Pids =PBSMaster.objects.filter(id=item['asset_ty'])
                                        for Find_Pid in Find_Pids:
                                            date = datetime.datetime.strptime(item['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                            cm_start_date = datetime.datetime.strptime(item['cm_start_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                            cm_end_date = item['cm_end_date']
                                            if cm_end_date == '':
                                                cm_end_date = None
                                            else:
                                                cm_end_date = datetime.datetime.strptime(item['cm_end_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                            cm_end_time = item['cm_end_time']
                                            if cm_end_time == '':
                                                cm_end_time = None
                                            ACID = Asset.objects.filter(id=item['asset_config_ids'])
                                            asset_config_id = ACID[0].asset_config_id
                                            s=FailureData(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=r.id,defect_id=item['defect'],asset_type=item['asset_ty'],failure_id=item['failure_id'],event_description=item['event_description'],date=date,time=item['time'],detection=item['detection'],service_delay=item['service_delay'],immediate_investigation=item['immediate_investigation'],failure_type=item['failure_type'],safety_failure=item['safety_failure'],hazard_id=item['hazard_id'],cm_description=item['cm_description'],replaced_asset_config_id=item['replaced_asset_config_id'],cm_start_date=cm_start_date,cm_start_time=item['cm_start_time'],cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=item['oem_failure_reference'])
                                            s.save()
                                    else:
                                        FailureData.objects.filter(id=item['id']).update(mode_id_id=r.id)
                            return JsonResponse({'status':'1','id':r.id})
                else:
                    if user_Role == 1:
                        FailureData_data =FailureData.objects.filter(mode_id_id=ids).update(mode_id_id='')
                    else:
                        FailureData_data =FailureData.objects.filter(P_id=P_id,mode_id_id=ids).update(mode_id_id='')
                    if FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
                        if FailureMode.objects.filter(mode_id=mode_id, id=ids,is_active=0).exists():
                            Find_Pids =PBSMaster.objects.filter(id=asset_type)
                            for Find_Pid in Find_Pids:
                                FailureMode.objects.filter(id=ids).update(P_id=Find_Pid.project_id,mode_description=mode_description,asset_type=Asset_Types,start_date=start_date,end_date=end_date)
                                if meg !='':
                                    FindUser = UserProfile.objects.filter(user_id=user_ID)
                                    now = datetime.datetime.now()
                                    current_time = now.strftime("%H:%M:%S")
                                    meg ="ID: "+ids +"=> "+meg
                                    h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                                    h.save()
                                if data !="":
                                    for item in data:
                                        if item['id'] == 0:
                                            Find_Pids =PBSMaster.objects.filter(id=item['asset_ty'])
                                            for Find_Pid in Find_Pids:
                                                date = datetime.datetime.strptime(item['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                                cm_start_date = datetime.datetime.strptime(item['cm_start_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                                cm_end_date = item['cm_end_date']
                                                if cm_end_date == '':
                                                    cm_end_date = None
                                                else:
                                                    cm_end_date = datetime.datetime.strptime(item['cm_end_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                                cm_end_time = item['cm_end_time']
                                                if cm_end_time == '':
                                                    cm_end_time = None
                                                ACID = Asset.objects.filter(id=item['asset_config_ids'])
                                                asset_config_id = ACID[0].asset_config_id
                                                s=FailureData(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=ids,defect_id=item['defect'],asset_type=item['asset_ty'],failure_id=item['failure_id'],event_description=item['event_description'],date=date,time=item['time'],detection=item['detection'],service_delay=item['service_delay'],immediate_investigation=item['immediate_investigation'],failure_type=item['failure_type'],safety_failure=item['safety_failure'],hazard_id=item['hazard_id'],cm_description=item['cm_description'],replaced_asset_config_id=item['replaced_asset_config_id'],cm_start_date=cm_start_date,cm_start_time=item['cm_start_time'],cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=item['oem_failure_reference'])
                                                s.save()
                                        else:
                                            FailureData.objects.filter(id=item['id']).update(mode_id_id=ids)
                                return JsonResponse({'status':'1','id':ids})
                        else:
                            return JsonResponse({'status':'0'})
                    else:
                        Find_Pids =PBSMaster.objects.filter(id=asset_type)
                        for Find_Pid in Find_Pids:
                            FailureMode.objects.filter(id=ids).update(P_id=Find_Pid.project_id,mode_id=mode_id,mode_description=mode_description,asset_type=Asset_Types,start_date=start_date,end_date=end_date)
                            if meg !='':
                                FindUser = UserProfile.objects.filter(user_id=user_ID)
                                now = datetime.datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                meg ="ID: "+ids +"=> "+meg
                                h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                                h.save()
                            if data !="":
                                for item in data:
                                    if item['id'] == 0:
                                        Find_Pids =PBSMaster.objects.filter(id=item['asset_ty'])
                                        for Find_Pid in Find_Pids:
                                            date = datetime.datetime.strptime(item['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                            cm_start_date = datetime.datetime.strptime(item['cm_start_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                            cm_end_date = item['cm_end_date']
                                            if cm_end_date == '':
                                                cm_end_date = None
                                            else:
                                                cm_end_date = datetime.datetime.strptime(item['cm_end_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                            cm_end_time = item['cm_end_time']
                                            if cm_end_time == '':
                                                cm_end_time = None
                                            ACID = Asset.objects.filter(id=item['asset_config_ids'])
                                            asset_config_id = ACID[0].asset_config_id
                                            s=FailureData(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=ids,defect_id=item['defect'],asset_type=item['asset_ty'],failure_id=item['failure_id'],event_description=item['event_description'],date=date,time=item['time'],detection=item['detection'],service_delay=item['service_delay'],immediate_investigation=item['immediate_investigation'],failure_type=item['failure_type'],safety_failure=item['safety_failure'],hazard_id=item['hazard_id'],cm_description=item['cm_description'],replaced_asset_config_id=item['replaced_asset_config_id'],cm_start_date=cm_start_date,cm_start_time=item['cm_start_time'],cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=item['oem_failure_reference'])
                                            s.save()
                                    else:
                                        FailureData.objects.filter(id=item['id']).update(mode_id_id=ids)
                            return JsonResponse({'status':'1','id':ids})
        else:
            asset_type = Asset_Types
            if action == '1':
                if ids =="":
                    if FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
                        return JsonResponse({'status':'0'})
                    else:
                        r=FailureMode(P_id=P_id,mode_id=mode_id,mode_description=mode_description,asset_type=asset_type,start_date=start_date,end_date=end_date)
                        r.save()
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="Add new failure mode "
                        meg ="ID: "+str(r.id) +"=> "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                        h.save()
                        return JsonResponse({'status':'1','id':r.id})
                else:
                    if FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
                        if FailureMode.objects.filter(mode_id=mode_id, id=ids,is_active=0).exists():
                            FailureMode.objects.filter(id=ids).update(P_id=P_id,mode_description=mode_description,asset_type=asset_type,start_date=start_date,end_date=end_date)
                            if meg !='':
                                FindUser = UserProfile.objects.filter(user_id=user_ID)
                                now = datetime.datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                meg ="ID: "+ids +"=> "+meg
                                h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                                h.save()
                            return JsonResponse({'status':'1','id':ids})
                        else:
                            return JsonResponse({'status':'0'})
                    else:
                        FailureMode.objects.filter(id=ids).update(P_id=P_id,mode_id=mode_id,mode_description=mode_description,asset_type=asset_type,start_date=start_date,end_date=end_date)
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+ids +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                            h.save()
                        return JsonResponse({'status':'1','id':ids})
            else:
                if data !="":
                    for items in data:
                        if items['id'] == 0:
                            failure_id=items['failure_id']
                            if FailureData.objects.filter(failure_id=failure_id).exists():
                                return JsonResponse({'status':'2','Fail_ID':items['failure_id']})   
                if ids =="":
                    if FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
                        return JsonResponse({'status':'0'})
                    else:
                        r=FailureMode(P_id=P_id,mode_id=mode_id,mode_description=mode_description,asset_type=asset_type,start_date=start_date,end_date=end_date)
                        r.save()
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="Add new failure mode "
                        meg ="ID: "+str(r.id) +"=> "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                        h.save()
                        if data !="":
                            for item in data:
                                if item['id'] == 0:
                                    Find_Pids =PBSMaster.objects.filter(id=item['asset_ty'])
                                    for Find_Pid in Find_Pids:
                                        date = datetime.datetime.strptime(item['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                        cm_start_date = datetime.datetime.strptime(item['cm_start_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                        cm_end_date = item['cm_end_date']
                                        if cm_end_date == '':
                                            cm_end_date = None
                                        else:
                                            cm_end_date = datetime.datetime.strptime(item['cm_end_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                        cm_end_time = item['cm_end_time']
                                        if cm_end_time == '':
                                            cm_end_time = None
                                        ACID = Asset.objects.filter(id=item['asset_config_ids'])
                                        asset_config_id = ACID[0].asset_config_id
                                        s=FailureData(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=r.id,defect_id=item['defect'],asset_type=item['asset_ty'],failure_id=item['failure_id'],event_description=item['event_description'],date=date,time=item['time'],detection=item['detection'],service_delay=item['service_delay'],immediate_investigation=item['immediate_investigation'],failure_type=item['failure_type'],safety_failure=item['safety_failure'],hazard_id=item['hazard_id'],cm_description=item['cm_description'],replaced_asset_config_id=item['replaced_asset_config_id'],cm_start_date=cm_start_date,cm_start_time=item['cm_start_time'],cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=item['oem_failure_reference'])
                                        s.save()
                                else:
                                    FailureData.objects.filter(id=item['id']).update(mode_id_id=r.id)
                        return JsonResponse({'status':'1','id':r.id})
                else:
                    if user_Role == 1:
                        FailureData_data =FailureData.objects.filter(mode_id_id=ids).update(mode_id_id='')
                    else:
                        FailureData_data =FailureData.objects.filter(P_id=P_id,mode_id_id=ids).update(mode_id_id='')
                    if FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
                        if FailureMode.objects.filter(mode_id=mode_id, id=ids,is_active=0).exists():
                            FailureMode.objects.filter(id=ids).update(P_id=P_id,mode_description=mode_description,asset_type=asset_type,start_date=start_date,end_date=end_date)
                            if meg !='':
                                FindUser = UserProfile.objects.filter(user_id=user_ID)
                                now = datetime.datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                meg ="ID: "+ids +"=> "+meg
                                h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                                h.save()
                            if data !="":
                                for item in data:
                                    if item['id'] == 0:
                                        Find_Pids =PBSMaster.objects.filter(id=item['asset_ty'])
                                        for Find_Pid in Find_Pids:
                                            date = datetime.datetime.strptime(item['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                            cm_start_date = datetime.datetime.strptime(item['cm_start_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                            cm_end_date = item['cm_end_date']
                                            if cm_end_date == '':
                                                cm_end_date = None
                                            else:
                                                cm_end_date = datetime.datetime.strptime(item['cm_end_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                            cm_end_time = item['cm_end_time']
                                            if cm_end_time == '':
                                                cm_end_time = None
                                            ACID = Asset.objects.filter(id=item['asset_config_ids'])
                                            asset_config_id = ACID[0].asset_config_id
                                            s=FailureData(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=ids,defect_id=item['defect'],asset_type=item['asset_ty'],failure_id=item['failure_id'],event_description=item['event_description'],date=date,time=item['time'],detection=item['detection'],service_delay=item['service_delay'],immediate_investigation=item['immediate_investigation'],failure_type=item['failure_type'],safety_failure=item['safety_failure'],hazard_id=item['hazard_id'],cm_description=item['cm_description'],replaced_asset_config_id=item['replaced_asset_config_id'],cm_start_date=cm_start_date,cm_start_time=item['cm_start_time'],cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=item['oem_failure_reference'])
                                            s.save()
                                    else:
                                        FailureData.objects.filter(id=item['id']).update(mode_id_id=ids)
                            return JsonResponse({'status':'1','id':ids})
                        else:
                            return JsonResponse({'status':'0'})
                    else:
                        FailureMode.objects.filter(id=ids).update(P_id=P_id,mode_id=mode_id,mode_description=mode_description,asset_type=asset_type,start_date=start_date,end_date=end_date)
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+ids +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
                            h.save()
                        if data !="":
                            for item in data:
                                if item['id'] == 0:
                                    Find_Pids =PBSMaster.objects.filter(id=item['asset_ty'])
                                    for Find_Pid in Find_Pids:
                                        date = datetime.datetime.strptime(item['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                        cm_start_date = datetime.datetime.strptime(item['cm_start_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                        cm_end_date = item['cm_end_date']
                                        if cm_end_date == '':
                                            cm_end_date = None
                                        else:
                                            cm_end_date = datetime.datetime.strptime(item['cm_end_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                                        cm_end_time = item['cm_end_time']
                                        if cm_end_time == '':
                                            cm_end_time = None
                                        ACID = Asset.objects.filter(id=item['asset_config_ids'])
                                        asset_config_id = ACID[0].asset_config_id
                                        s=FailureData(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=ids,defect_id=item['defect'],asset_type=item['asset_ty'],failure_id=item['failure_id'],event_description=item['event_description'],date=date,time=item['time'],detection=item['detection'],service_delay=item['service_delay'],immediate_investigation=item['immediate_investigation'],failure_type=item['failure_type'],safety_failure=item['safety_failure'],hazard_id=item['hazard_id'],cm_description=item['cm_description'],replaced_asset_config_id=item['replaced_asset_config_id'],cm_start_date=cm_start_date,cm_start_time=item['cm_start_time'],cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=item['oem_failure_reference'])
                                        s.save()
                                else:
                                    FailureData.objects.filter(id=item['id']).update(mode_id_id=ids)
                        return JsonResponse({'status':'1','id':ids})
            
class Listfailuredata(View):
    template_name = 'add_failuremode.html'

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        asset_type = req.get('asset_type')
        if req.get('start_date') !="" and req.get('end_date') !="":
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            start_date = req.get('start_date')
            end_date = req.get('end_date')
            
        
        failuresAttributed = req.get('failuresAttributed')
        if user_Role == 1:
            FailureData_data =FailureData.objects.filter(is_active=0)
        else:
            FailureData_data =FailureData.objects.filter(is_active=0,P_id=P_id)

        if asset_type != "all":
            FailureData_data=FailureData_data.filter(asset_type=asset_type)
        if failuresAttributed !="":
            IDS = failuresAttributed.split(',')
            for i in IDS:
                if i != 0: 
                    FailureData_data=FailureData_data.filter().exclude(id=i)
        # Asset_data = Asset.objects.all()
        if start_date and end_date :
            FailureData_data=FailureData_data.filter(date__range=[start_date,end_date])
        
        for FailureDatas in FailureData_data:
            if PBSMaster.objects.filter(id=FailureDatas.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    if FailureMode.objects.filter(id=FailureDatas.mode_id_id,is_active=0).exists():
                        FailureModes = FailureMode.objects.filter(id=FailureDatas.mode_id_id)
                        for FailureMode_id in FailureModes:
                            data.append({ 
                                'failure_id' :  FailureDatas.failure_id,
                                'asset_type' : PBSMaster_data.asset_type,
                                'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                                'event_description' : FailureDatas.event_description,
                                'mode_id' : FailureMode_id.mode_id,
                                'mode_description' : FailureDatas.mode_description,
                                'date' : FailureDatas.date,
                                'time' : FailureDatas.time,
                                'detection':FailureDatas.detection,
                                'service_delay' :  FailureDatas.service_delay,
                                'immediate_investigation' : FailureDatas.immediate_investigation,
                                'failure_type' : FailureDatas.failure_type,
                                'safety_failure' : FailureDatas.safety_failure,
                                'hazard_id' : FailureDatas.hazard_id,
                                'cm_description' : FailureDatas.cm_description,
                                'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                                'cm_start_date' : FailureDatas.cm_start_date,
                                'cm_start_time' : FailureDatas.cm_start_time,
                                'cm_end_date' : FailureDatas.cm_end_date,
                                'cm_end_time' : FailureDatas.cm_end_time,
                                'oem_failure_reference' : FailureDatas.oem_failure_reference,
                                'id':FailureDatas.id,
                                'user_Role':user_Role,
                                'defect':FailureDatas.defect_id,
                            })  
                    else:
                        data.append({ 
                            'failure_id' :  FailureDatas.failure_id,
                            'asset_type' : PBSMaster_data.asset_type,
                            'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                            'event_description' : FailureDatas.event_description,
                            'mode_id' : '',
                            'mode_description' : FailureDatas.mode_description,
                            'date' : FailureDatas.date,
                            'time' : FailureDatas.time,
                            'detection':FailureDatas.detection,
                            'service_delay' :  FailureDatas.service_delay,
                            'immediate_investigation' : FailureDatas.immediate_investigation,
                            'failure_type' : FailureDatas.failure_type,
                            'safety_failure' : FailureDatas.safety_failure,
                            'hazard_id' : FailureDatas.hazard_id,
                            'cm_description' : FailureDatas.cm_description,
                            'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                            'cm_start_date' : FailureDatas.cm_start_date,
                            'cm_start_time' : FailureDatas.cm_start_time,
                            'cm_end_date' : FailureDatas.cm_end_date,
                            'cm_end_time' : FailureDatas.cm_end_time,
                            'oem_failure_reference' : FailureDatas.oem_failure_reference,
                            'id':FailureDatas.id,
                            'user_Role':user_Role,
                            'defect':FailureDatas.defect_id,
                        })         
        return JsonResponse({'data':data})
    
class Listfailuredata1(View):
    template_name = 'add_failuremode.html'

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        asset_type = req.get('asset_type')
      
        
        failuresAttributed = req.get('failuresAttributed')
        if user_Role == 1:
            FailureData_data =FailureData.objects.filter(is_active=0)
        else:
            FailureData_data =FailureData.objects.filter(is_active=0,P_id=P_id)

        if asset_type != "all":
            FailureData_data=FailureData_data.filter(asset_type=asset_type)
        if failuresAttributed !="":
            IDS = failuresAttributed.split(',')
            for i in IDS:
                if i != 0: 
                    FailureData_data=FailureData_data.filter().exclude(id=i)
        # Asset_data = Asset.objects.all()
      
        for FailureDatas in FailureData_data:
            if PBSMaster.objects.filter(id=FailureDatas.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    if FailureMode.objects.filter(id=FailureDatas.mode_id_id,is_active=0).exists():
                        FailureModes = FailureMode.objects.filter(id=FailureDatas.mode_id_id)
                        for FailureMode_id in FailureModes:
                            data.append({ 
                                'failure_id' :  FailureDatas.failure_id,
                                'asset_type' : PBSMaster_data.asset_type,
                                'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                                'event_description' : FailureDatas.event_description,
                                'mode_id' : FailureMode_id.mode_id,
                                'mode_description' : FailureDatas.mode_description,
                                'date' : FailureDatas.date,
                                'time' : FailureDatas.time,
                                'detection':FailureDatas.detection,
                                'service_delay' :  FailureDatas.service_delay,
                                'immediate_investigation' : FailureDatas.immediate_investigation,
                                'failure_type' : FailureDatas.failure_type,
                                'safety_failure' : FailureDatas.safety_failure,
                                'hazard_id' : FailureDatas.hazard_id,
                                'cm_description' : FailureDatas.cm_description,
                                'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                                'cm_start_date' : FailureDatas.cm_start_date,
                                'cm_start_time' : FailureDatas.cm_start_time,
                                'cm_end_date' : FailureDatas.cm_end_date,
                                'cm_end_time' : FailureDatas.cm_end_time,
                                'oem_failure_reference' : FailureDatas.oem_failure_reference,
                                'id':FailureDatas.id,
                                'user_Role':user_Role,
                                'defect':FailureDatas.defect_id,
                            })  
                    else:
                        data.append({ 
                            'failure_id' :  FailureDatas.failure_id,
                            'asset_type' : PBSMaster_data.asset_type,
                            'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                            'event_description' : FailureDatas.event_description,
                            'mode_id' : '',
                            'mode_description' : FailureDatas.mode_description,
                            'date' : FailureDatas.date,
                            'time' : FailureDatas.time,
                            'detection':FailureDatas.detection,
                            'service_delay' :  FailureDatas.service_delay,
                            'immediate_investigation' : FailureDatas.immediate_investigation,
                            'failure_type' : FailureDatas.failure_type,
                            'safety_failure' : FailureDatas.safety_failure,
                            'hazard_id' : FailureDatas.hazard_id,
                            'cm_description' : FailureDatas.cm_description,
                            'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                            'cm_start_date' : FailureDatas.cm_start_date,
                            'cm_start_time' : FailureDatas.cm_start_time,
                            'cm_end_date' : FailureDatas.cm_end_date,
                            'cm_end_time' : FailureDatas.cm_end_time,
                            'oem_failure_reference' : FailureDatas.oem_failure_reference,
                            'id':FailureDatas.id,
                            'user_Role':user_Role,
                            'defect':FailureDatas.defect_id,
                        })         
        return JsonResponse({'data':data})
    
class Listgetmodedata(View):
    template_name = 'add_failuremode.html'

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        mode_id = req.get('mode_id')
        if user_Role == 1:
            FailureData_data =FailureData.objects.filter(is_active=0,mode_id_id=mode_id)
        else:
            FailureData_data =FailureData.objects.filter(is_active=0,P_id=P_id,mode_id_id=mode_id)
        # Asset_data = Asset.objects.all()
        for FailureDatas in FailureData_data:
            if PBSMaster.objects.filter(id=FailureDatas.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    data.append({ 
                        'failure_id' :  FailureDatas.failure_id,
                        'asset_type' : PBSMaster_data.asset_type,
                        'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                        'event_description' : FailureDatas.event_description,
                        'mode_id' : mode_id,
                        'mode_description' : FailureDatas.mode_description,
                        'date' : FailureDatas.date,
                        'time' : FailureDatas.time,
                        'detection':FailureDatas.detection,
                        'service_delay' :  FailureDatas.service_delay,
                        'immediate_investigation' : FailureDatas.immediate_investigation,
                        'failure_type' : FailureDatas.failure_type,
                        'safety_failure' : FailureDatas.safety_failure,
                        'hazard_id' : FailureDatas.hazard_id,
                        'cm_description' : FailureDatas.cm_description,
                        'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                        'cm_start_date' : FailureDatas.cm_start_date,
                        'cm_start_time' : FailureDatas.cm_start_time,
                        'cm_end_date' : FailureDatas.cm_end_date,
                        'cm_end_time' : FailureDatas.cm_end_time,
                        'oem_failure_reference' : FailureDatas.oem_failure_reference,
                        'id':FailureDatas.id,
                        'user_Role':user_Role,
                        'defect':FailureDatas.defect_id,
                    })        
        return JsonResponse({'data':data})
    
    

    
class GetAssetType(View):
    template_name = 'failuremode.html'

    def post(self, request, *args, **kwargs):
        req = request.POST
        # print(req)
        asset_type = req.get('asset_type')
        if asset_type == "":
            PBSMaster_datas=''
        else:
            PBSMaster_datas=PBSMaster.objects.filter(id=asset_type)
        ASSET=''
        for a in PBSMaster_datas:
            ASSET=a.asset_type
        return JsonResponse({'asset_type':ASSET})  
    
    
class AddTempFailureData(View):
    template_name = 'add_failuremode.html'

    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        failure_id = req.get('failure_id')

        if FailureData.objects.filter(failure_id=failure_id,is_active=0).exists():
            return JsonResponse({'status':'0'})
        else:              
            return JsonResponse({'status':'1'})
        
                
class FindModeId(View):
    template_name = 'failuremode.html'

    def post(self, request, *args, **kwargs):
        req = request.POST
        # print(req)
        mode_id = req.get('mode_id')
        if FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
            return JsonResponse({'status':'0'})  
        else:
            return JsonResponse({'status':'1'})
        


class DefectsView(View):
    template_name = 'defect.html'

    def get(self, request, *args, **kwargs):
        add = kwargs.get("add")
        if add == None:
            add=0
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            defect_description = Defect.objects.filter(is_active=0).distinct('defect_description')
            investigation = Defect.objects.filter(is_active=0).distinct('investigation')
            asset_type = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
            defect_status = Defect.objects.filter(is_active=0).distinct('defect_status')
            defect_status_remarks = Defect.objects.filter(is_active=0).distinct('defect_status_remarks')
            oem_defect_reference = Defect.objects.filter(is_active=0).distinct('oem_defect_reference')
        else:
            defect_description = Defect.objects.filter(is_active=0,P_id=P_id).distinct('defect_description')
            investigation = Defect.objects.filter(is_active=0,P_id=P_id).distinct('investigation')
            defect_status = Defect.objects.filter(is_active=0,P_id=P_id).distinct('defect_status')
            defect_status_remarks = Defect.objects.filter(is_active=0,P_id=P_id).distinct('defect_status_remarks')
            oem_defect_reference = Defect.objects.filter(is_active=0,P_id=P_id).distinct('oem_defect_reference')
            asset_type = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type') 
        return render(request, self.template_name, {'add':add,'defect_description':defect_description,'investigation':investigation, 'defect_status':defect_status, 'defect_status_remarks':defect_status_remarks, 'oem_defect_reference' : oem_defect_reference,'asset_type':asset_type,'asset_types':asset_type})

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        defect_description = req.get('defect_description')
        investigation = req.get('investigation')
        asset_type = req.get('asset_type')
        defect_status = req.get('defect_status')
        defect_status_remarks = req.get('defect_status_remarks')
        oem_defect_reference = req.get('oem_defect_reference')
        if user_Role == 1:
            Defect_data =Defect.objects.filter(is_active=0)
        else:
            Defect_data =Defect.objects.filter(is_active=0,P_id=P_id)
            
        if req.get('defect_open_date') !="":
            defect_open_date = datetime.datetime.strptime(req.get('defect_open_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            Defect_data=Defect_data.filter(defect_open_date=defect_open_date)
        if req.get('defect_closed_date') !="":
            defect_closed_date = datetime.datetime.strptime(req.get('defect_closed_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            Defect_data=Defect_data.filter(defect_closed_date=defect_closed_date)

        if defect_description != "all":
            Defect_data=Defect_data.filter(defect_description=defect_description)
        if investigation != "all":
            Defect_data=Defect_data.filter(investigation=investigation)
        if asset_type != "all":
            Defect_data=Defect_data.filter(asset_type=asset_type)
        if defect_status != "all":
            Defect_data=Defect_data.filter(defect_status=defect_status)
        if defect_status_remarks != "all":
            Defect_data=Defect_data.filter(defect_status_remarks=defect_status_remarks)
        if oem_defect_reference != "all":
            Defect_data=Defect_data.filter(oem_defect_reference=oem_defect_reference)
    
        for Defects in Defect_data:
            if PBSMaster.objects.filter(id=Defects.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=Defects.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    data.append({ 
                        'defect_id' :  Defects.defect_id,
                        'defect_description' : Defects.defect_description,
                        'defect_open_date' : Defects.defect_open_date,
                        'defect_closed_date' : Defects.defect_closed_date,
                        'asset_type' : PBSMaster_data.asset_type,
                        'investigation' : Defects.investigation,
                        'defect_status' : Defects.defect_status,
                        'defect_status_remarks' : Defects.defect_status_remarks,
                        'oem_defect_reference':Defects.oem_defect_reference,
                        'id':Defects.defect_id,
                        'user_Role':user_Role,
                    }) 
        return JsonResponse({'data':data})
    
class DeleteDefectsView(View):
    template_name = 'defect.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        # print(req)
        id = req.get('id')
        Defect.objects.filter(defect_id=id).update(is_active=1)
        FailureData.objects.filter(defect_id=id).update(defect_id='')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete defect "
        meg ="DEFECT ID: "+str(id) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="FRACAS Defect Identification")
        h.save()
        return JsonResponse({'status':'1'}) 
    
class AddDefectsView(View):
    template_name = 'defect.html'

    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 4:
            return redirect('/dashboard/')
        req = request.POST
        # print(req)
        asset_type = req.get('asset_type')
        start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        if PBSMaster.objects.filter(id=asset_type,is_active=0).exists():
            PBSMaster_datas=PBSMaster.objects.filter(id=asset_type)
            for PBSMaster_data in PBSMaster_datas:
                s=Defect(asset_type=asset_type,start_date=start_date,end_date=end_date,P_id=PBSMaster_data.project_id)
                s.save()
                FindUser = UserProfile.objects.filter(user_id=user_ID)
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                meg ="Add new defect "
                meg ="DEFECT ID: "+str(s.defect_id) +"=> "+meg
                h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="FRACAS Defect Identification")
                h.save()
                return JsonResponse({'status':'1','id':s.defect_id})
        return JsonResponse({'status':'0'})
    
class UpdateDefect(View):
    template_name = 'update_defect.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]
        if id==None:
            return redirect('/forms/defect/')
        else:
            if Defect.objects.filter(defect_id=id,is_active=1).exists():
                return redirect('/forms/defect/')
            DefectDatas = Defect.objects.filter(defect_id=id)
            for datas in DefectDatas:
                data={ 
                'defect_description' : datas.defect_description,
                'investigation' : datas.investigation,
                'defect_status_remarks' : datas.defect_status_remarks,
                'oem_defect_reference' : datas.oem_defect_reference,
                'defect_status' :datas.defect_status,
                'defect_open_date' : datas.defect_open_date,
                'defect_closed_date' : datas.defect_closed_date,
                'oem_target_date' : datas.oem_target_date,
                'asset_type':datas.asset_type,
                'defect_id':datas.defect_id
                }
        return render(request, self.template_name,{'data':data})

    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        cursor = connection.cursor()
        # print(req)oldmode_id
        defect_status = req.get('defect_status')
        defect_description = req.get('defect_description')
        investigation = req.get('investigation')
        defect_status_remarks = req.get('defect_status_remarks')
        defect_open_date = datetime.datetime.strptime(req.get('defect_open_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        defect_closed_date = req.get('defect_closed_date')
        if defect_closed_date == '':
            defect_closed_date = None
        else:
            defect_closed_date = datetime.datetime.strptime(req.get('defect_closed_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        oem_target_date = datetime.datetime.strptime(req.get('oem_target_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        oem_defect_reference= req.get('oem_defect_reference')
        defect_id= req.get('defect_id')
        datas= req.get('datas')
        data=json.loads(datas)

        DATA = []
        HEAD = ["defect_description",'investigation','defect_status_remarks','oem_defect_reference','defect_status','oem_target_date','defect_open_date','defect_closed_date']
        for f in HEAD:
            if f == 'oem_target_date':
                DATA.append({
                    'field':f,
                    'value':oem_target_date
                })
            elif f == 'defect_open_date':
                DATA.append({
                    'field':f,
                    'value':defect_open_date
                })
            elif f == 'defect_closed_date':
                DATA.append({
                    'field':f,
                    'value':defect_closed_date
                })
            else:
                DATA.append({
                    'field':f,
                    'value':req.get(f)
                })
        # print(DATA)
        if defect_id != "":
            meg =''
            for i in DATA:
                print('----------')
                print(i['field'])
                if i['field'] == 'defect_closed_date':
                    cursor.execute("SELECT {0} FROM fracas_defect WHERE defect_id='{1}'".format(i['field'],defect_id))
                    row1 = cursor.fetchone()
                    if str(row1[0]) != i['value']:
                        meg = meg +i['field']+': '+ str(row1[0]) +' to '+str(i['value'])+', '
                else:
                    cursor.execute("SELECT * FROM fracas_defect WHERE defect_id='{0}' and {1}='{2}'".format(defect_id,i['field'],i['value']))
                    row = cursor.fetchone()
                    print(row)
                    if row == None:
                        cursor.execute("SELECT {0} FROM fracas_defect WHERE defect_id='{1}'".format(i['field'],defect_id))
                        row1 = cursor.fetchone()
                        meg = meg +i['field']+': '+ str(row1[0]) +' to '+str(i['value'])+', '


            if user_Role == 1:
                FailureData_data =FailureData.objects.filter(defect_id=defect_id).update(defect_id='')
            else:
                FailureData_data =FailureData.objects.filter(P_id=P_id,defect_id=defect_id).update(defect_id='')
            
            Defect.objects.filter(defect_id=defect_id).update(oem_defect_reference=oem_defect_reference,defect_status=defect_status,defect_description=defect_description,investigation=investigation,defect_status_remarks=defect_status_remarks,defect_open_date=defect_open_date,defect_closed_date=defect_closed_date,oem_target_date=oem_target_date)
            if meg !='':
                FindUser = UserProfile.objects.filter(user_id=user_ID)
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                meg ="DEFECT ID: "+defect_id +"=> "+meg
                h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="FRACAS Defect Identification")
                h.save()
            if data !="":
                for item in data:
                    FailureData.objects.filter(id=item['id']).update(defect_id=defect_id)
            return JsonResponse({'status':'1'})
        return JsonResponse({'status':'0'})
                
        
class Listgetdefectdata(View):
    template_name = 'update_defect.html'

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        defect_id = req.get('defect_id')
        if user_Role == 1:
            FailureData_data =FailureData.objects.filter(is_active=0,defect_id=defect_id)
        else:
            FailureData_data =FailureData.objects.filter(is_active=0,P_id=P_id,defect_id=defect_id)
        # Asset_data = Asset.objects.all()
        for FailureDatas in FailureData_data:
            if PBSMaster.objects.filter(id=FailureDatas.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    if FailureMode.objects.filter(id=FailureDatas.mode_id_id,is_active=0).exists():
                        FailureModes = FailureMode.objects.filter(id=FailureDatas.mode_id_id)
                        for FailureMode_id in FailureModes:
                            data.append({ 
                                'failure_id' :  FailureDatas.failure_id,
                                'asset_type' : PBSMaster_data.asset_type,
                                'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                                'event_description' : FailureDatas.event_description,
                                'mode_id' : FailureMode_id.mode_id,
                                'mode_description' : FailureDatas.mode_description,
                                'date' : FailureDatas.date,
                                'time' : FailureDatas.time,
                                'detection':FailureDatas.detection,
                                'service_delay' :  FailureDatas.service_delay,
                                'immediate_investigation' : FailureDatas.immediate_investigation,
                                'failure_type' : FailureDatas.failure_type,
                                'safety_failure' : FailureDatas.safety_failure,
                                'hazard_id' : FailureDatas.hazard_id,
                                'cm_description' : FailureDatas.cm_description,
                                'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                                'cm_start_date' : FailureDatas.cm_start_date,
                                'cm_start_time' : FailureDatas.cm_start_time,
                                'cm_end_date' : FailureDatas.cm_end_date,
                                'cm_end_time' : FailureDatas.cm_end_time,
                                'oem_failure_reference' : FailureDatas.oem_failure_reference,
                                'id':FailureDatas.id,
                                'user_Role':user_Role,
                                'defect':FailureDatas.defect_id,
                            })  
                    else:
                        data.append({ 
                            'failure_id' :  FailureDatas.failure_id,
                            'asset_type' : PBSMaster_data.asset_type,
                            'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                            'event_description' : FailureDatas.event_description,
                            'mode_id' : '',
                            'mode_description' : FailureDatas.mode_description,
                            'date' : FailureDatas.date,
                            'time' : FailureDatas.time,
                            'detection':FailureDatas.detection,
                            'service_delay' :  FailureDatas.service_delay,
                            'immediate_investigation' : FailureDatas.immediate_investigation,
                            'failure_type' : FailureDatas.failure_type,
                            'safety_failure' : FailureDatas.safety_failure,
                            'hazard_id' : FailureDatas.hazard_id,
                            'cm_description' : FailureDatas.cm_description,
                            'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                            'cm_start_date' : FailureDatas.cm_start_date,
                            'cm_start_time' : FailureDatas.cm_start_time,
                            'cm_end_date' : FailureDatas.cm_end_date,
                            'cm_end_time' : FailureDatas.cm_end_time,
                            'oem_failure_reference' : FailureDatas.oem_failure_reference,
                            'id':FailureDatas.id,
                            'user_Role':user_Role,
                            'defect':FailureDatas.defect_id,
                        })         
        return JsonResponse({'data':data})
    
class RootcauseView(View):
    template_name = 'rootcause.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        if user_Role == 1:
            RootCause_data =RootCause.objects.filter(is_active=0)
        else:
            RootCause_data =RootCause.objects.filter(is_active=0,P_id=P_id)
            
        for RootCauses in RootCause_data:
            if PBSMaster.objects.filter(id=RootCauses.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=RootCauses.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    data.append({ 
                        'rca_workshop_date' :  RootCauses.rca_workshop_date,
                        'root_cause_status' : RootCauses.root_cause_status,
                        'defect' : RootCauses.defect_id,
                        'immediate_cause' : RootCauses.immediate_cause,
                        'asset_type' : PBSMaster_data.asset_type,
                        'leading_reasons' : RootCauses.leading_reasons,
                        'root_cause_description' : RootCauses.root_cause_description,
                        'root_cause_id' : RootCauses.root_cause_id,
                        'id':RootCauses.root_cause_id,
                        'user_Role':user_Role,
                    }) 
        return JsonResponse({'data':data})

class DeleteRootcauseView(View):
    template_name = 'defect.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        # print(req)
        id = req.get('id')
        RootCause.objects.filter(root_cause_id=id).update(is_active=1)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete rootcause "
        meg ="ID: "+str(id) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
        h.save()
        return JsonResponse({'status':'1'})  
    
class ListfailuredataRootcauseView(View):
    template_name = 'add_rootcause.html'

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        asset_type = req.get('asset_type')
        defect = req.get('defect')
        if asset_type == "" or defect == "all":
            return JsonResponse({'data':data})
        if user_Role == 1:
            FailureData_data =FailureData.objects.filter(is_active=0)
        else:
            FailureData_data =FailureData.objects.filter(is_active=0,P_id=P_id)

        if asset_type != "":
            FailureData_data=FailureData_data.filter(asset_type=asset_type)
        if defect != "":
            FailureData_data=FailureData_data.filter(defect_id=defect)
        for FailureDatas in FailureData_data:
            if PBSMaster.objects.filter(id=FailureDatas.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    if FailureMode.objects.filter(id=FailureDatas.mode_id_id,is_active=0).exists():
                        FailureModes = FailureMode.objects.filter(id=FailureDatas.mode_id_id)
                        for FailureMode_id in FailureModes:
                            data.append({ 
                                'failure_id' :  FailureDatas.failure_id,
                                'asset_type' : PBSMaster_data.asset_type,
                                'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                                'event_description' : FailureDatas.event_description,
                                'mode_id' : FailureMode_id.mode_id,
                                'mode_description' : FailureDatas.mode_description,
                                'date' : FailureDatas.date,
                                'time' : FailureDatas.time,
                                'detection':FailureDatas.detection,
                                'service_delay' :  FailureDatas.service_delay,
                                'immediate_investigation' : FailureDatas.immediate_investigation,
                                'failure_type' : FailureDatas.failure_type,
                                'safety_failure' : FailureDatas.safety_failure,
                                'hazard_id' : FailureDatas.hazard_id,
                                'cm_description' : FailureDatas.cm_description,
                                'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                                'cm_start_date' : FailureDatas.cm_start_date,
                                'cm_start_time' : FailureDatas.cm_start_time,
                                'cm_end_date' : FailureDatas.cm_end_date,
                                'cm_end_time' : FailureDatas.cm_end_time,
                                'oem_failure_reference' : FailureDatas.oem_failure_reference,
                                'id':FailureDatas.id,
                                'user_Role':user_Role,
                                'defect':FailureDatas.defect_id,
                            })  
                    else:
                        data.append({ 
                            'failure_id' :  FailureDatas.failure_id,
                            'asset_type' : PBSMaster_data.asset_type,
                            'asset_config_id' : FailureDatas.asset_config_id.asset_config_id,
                            'event_description' : FailureDatas.event_description,
                            'mode_id' : '',
                            'mode_description' : FailureDatas.mode_description,
                            'date' : FailureDatas.date,
                            'time' : FailureDatas.time,
                            'detection':FailureDatas.detection,
                            'service_delay' :  FailureDatas.service_delay,
                            'immediate_investigation' : FailureDatas.immediate_investigation,
                            'failure_type' : FailureDatas.failure_type,
                            'safety_failure' : FailureDatas.safety_failure,
                            'hazard_id' : FailureDatas.hazard_id,
                            'cm_description' : FailureDatas.cm_description,
                            'replaced_asset_config_id' : FailureDatas.replaced_asset_config_id,
                            'cm_start_date' : FailureDatas.cm_start_date,
                            'cm_start_time' : FailureDatas.cm_start_time,
                            'cm_end_date' : FailureDatas.cm_end_date,
                            'cm_end_time' : FailureDatas.cm_end_time,
                            'oem_failure_reference' : FailureDatas.oem_failure_reference,
                            'id':FailureDatas.id,
                            'user_Role':user_Role,
                            'defect':FailureDatas.defect_id,
                        })         
        return JsonResponse({'data':data})


class AddRootcauseView(View):
    template_name = 'add_rootcause.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        user_ID = request.session['user_ID']
        if id==None:
            data={ 
            'root_cause_id' :  '',
            'asset_type' : '',
            'rca_workshop_date' :'',
            'id' : '',
            'root_cause_status':'',
            'defect':'',
            'user_Role':user_Role,
            'immediate_cause':'',
            'leading_reasons':'',
            'root_cause_description':'',
            }
        else:
            if RootCause.objects.filter(root_cause_id=id,is_active=1).exists():
                return redirect('/forms/rootcause/')
            RootCauses =RootCause.objects.filter(root_cause_id=id)
            for a in RootCauses:
                data={ 
                    'root_cause_id' :  a.root_cause_id,
                    'asset_type' : a.asset_type,
                    'rca_workshop_date' :a.rca_workshop_date,
                    'id' : a.root_cause_id,
                    'root_cause_status':a.root_cause_status,
                    'defect':a.defect_id,
                    'user_Role':user_Role,
                    'immediate_cause':a.immediate_cause,
                    'leading_reasons':a.leading_reasons,
                    'root_cause_description':a.root_cause_description,
                }
        if user_Role == 1:
            asset_type = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
            defect = Defect.objects.filter(is_active=0).distinct('defect_id')
        else:
            asset_type = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type')
            defect = Defect.objects.filter(is_active=0,P_id=P_id).distinct('defect_id')
        return render(request, self.template_name,{'data':data,'asset_types':asset_type,'defect':defect})
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        cursor = connection.cursor()
        # print(req)oldmode_id
        asset_type = req.get('asset_type')
        defect = req.get('defect')
        immediate_cause = req.get('immediate_cause')
        rca_workshop_date = datetime.datetime.strptime(req.get('rca_workshop_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        ids= req.get('id')
        root_cause_status= req.get('root_cause_status')
        action= req.get('action')
        datas= req.get('datas')
        data=json.loads(datas)
        leading_reasons = req.get('leading_reasons')
        root_cause_description = req.get('root_cause_description')

        DATA = []
        HEAD = ["asset_type",'defect_id','rca_workshop_date','root_cause_status','immediate_cause','leading_reasons','root_cause_description']
        for f in HEAD:
            if f == 'rca_workshop_date':
                DATA.append({
                    'field':f,
                    'value':rca_workshop_date
                })
            elif f == 'defect_id':
                DATA.append({
                    'field':f,
                    'value':defect
                })
            else:
                DATA.append({
                    'field':f,
                    'value':req.get(f)
                })
        # print(DATA)
        if ids !="":
            meg =''
            for i in DATA:
                cursor.execute("SELECT * FROM fracas_rootcause WHERE root_cause_id='{0}' and {1}='{2}'".format(ids,i['field'],i['value']))
                row = cursor.fetchone()
                if row == None:
                    cursor.execute("SELECT {0} FROM fracas_rootcause WHERE root_cause_id='{1}'".format(i['field'],ids))
                    row1 = cursor.fetchone()
                    if i['field'] == 'asset_type':
                        asst1 =PBSMaster.objects.filter(id=row1[0])
                        asst2 =PBSMaster.objects.filter(id=asset_type)
                        meg = meg +i['field']+': '+ str(asst1[0].asset_type) +' to '+str(asst2[0].asset_type)+', '
                    else:
                        meg = meg +i['field']+': '+ str(row1[0]) +' to '+str(i['value'])+', '


        if action == '1':
            if ids =="":
                if RootCause.objects.filter(defect_id=defect,is_active=0).exists():
                    return JsonResponse({'status':'0'})
                else:
                    Find_Pids =PBSMaster.objects.filter(id=asset_type)
                    for Find_Pid in Find_Pids:
                        r=RootCause(P_id=Find_Pid.project_id,asset_type=asset_type,defect_id=defect,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status)
                        r.save()
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="Add new rootcause "
                        meg ="ID: "+str(r.root_cause_id) +"=> "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
                        h.save()
                        return JsonResponse({'status':'1','id':r.root_cause_id})
            else:
                if RootCause.objects.filter(defect_id=defect,is_active=0).exists():
                    if RootCause.objects.filter(defect_id=defect,root_cause_id=ids,is_active=0).exists():
                        Find_Pids =PBSMaster.objects.filter(id=asset_type)
                        for Find_Pid in Find_Pids:
                            RootCause.objects.filter(root_cause_id=ids).update(P_id=Find_Pid.project_id,asset_type=asset_type,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status)
                            if meg !='':
                                FindUser = UserProfile.objects.filter(user_id=user_ID)
                                now = datetime.datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                meg ="ID: "+ids +"=> "+meg
                                h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
                                h.save()
                        return JsonResponse({'status':'1','id':ids})
                    else:
                        return JsonResponse({'status':'0'})
                else:
                    Find_Pids =PBSMaster.objects.filter(id=asset_type)
                    for Find_Pid in Find_Pids:
                        RootCause.objects.filter(root_cause_id=ids).update(P_id=Find_Pid.project_id,asset_type=asset_type,defect_id=defect,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status)
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+ids +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
                            h.save()
                        return JsonResponse({'status':'1','id':ids})
        else:
            CorrectiveAction.objects.filter(defect_id=defect).update(is_active=1)
            if ids =="":
                if RootCause.objects.filter(defect_id=defect,is_active=0).exists():
                    return JsonResponse({'status':'0'})
                else:
                    Find_Pids =PBSMaster.objects.filter(id=asset_type)
                    for Find_Pid in Find_Pids:
                        r=RootCause(P_id=Find_Pid.project_id,asset_type=asset_type,defect_id=defect,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status)
                        r.save()
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="Add new rootcause "
                        meg ="ID: "+str(r.root_cause_id) +"=> "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
                        h.save()
                        if data !="":
                            for items in data:
                                x= items['corrective_action_id'];
                                if x !="":
                                    CorrectiveAction.objects.filter(corrective_action_id=x).update(is_active=0)
                                else:
                                    a=CorrectiveAction(P_id=Find_Pid.project_id,defect_id=defect,corrective_action_owner=items['corrective_action_owner'],corrective_action_description=items['corrective_action_description'],corrective_action_update=items['corrective_action_update'],corrective_action_status=items['corrective_action_status'])
                                    a.save()
                        return JsonResponse({'status':'1','id':r.root_cause_id})
            else:
                if RootCause.objects.filter(defect_id=defect,is_active=0).exists():
                    if RootCause.objects.filter(defect_id=defect,root_cause_id=ids,is_active=0).exists():
                        Find_Pids =PBSMaster.objects.filter(id=asset_type)
                        for Find_Pid in Find_Pids:
                            RootCause.objects.filter(root_cause_id=ids).update(P_id=Find_Pid.project_id,asset_type=asset_type,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status)
                            if meg !='':
                                FindUser = UserProfile.objects.filter(user_id=user_ID)
                                now = datetime.datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                meg ="ID: "+ids +"=> "+meg
                                h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
                                h.save()
                            if data !="":
                                for items in data:
                                    x= items['corrective_action_id'];
                                    if x !="":
                                        CorrectiveAction.objects.filter(corrective_action_id=x).update(is_active=0)
                                    else:
                                        a=CorrectiveAction(P_id=Find_Pid.project_id,defect_id=defect,corrective_action_owner=items['corrective_action_owner'],corrective_action_description=items['corrective_action_description'],corrective_action_update=items['corrective_action_update'],corrective_action_status=items['corrective_action_status'])
                                        a.save()
                            return JsonResponse({'status':'1','id':ids})
                    else:
                        return JsonResponse({'status':'0'})
                else:
                    Find_Pids =PBSMaster.objects.filter(id=asset_type)
                    for Find_Pid in Find_Pids:
                        RootCause.objects.filter(root_cause_id=ids).update(P_id=Find_Pid.project_id,asset_type=asset_type,defect_id=defect,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status)
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+ids +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
                            h.save()
                        if data !="":
                            for items in data:
                                x= items['corrective_action_id'];
                                if x !="":
                                    CorrectiveAction.objects.filter(corrective_action_id=x).update(is_active=0)
                                else:
                                    a=CorrectiveAction(P_id=Find_Pid.project_id,defect_id=defect,corrective_action_owner=items['corrective_action_owner'],corrective_action_description=items['corrective_action_description'],corrective_action_update=items['corrective_action_update'],corrective_action_status=items['corrective_action_status'])
                                    a.save()
                        return JsonResponse({'status':'1','id':ids})
    
class ListgetCorrectivedatas(View):
    template_name = 'add_rootcause.html'

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        defect = req.get('defect')
        if defect == "":
            return JsonResponse({'data':data})
        if user_Role == 1:
            CorrectiveAction_data =CorrectiveAction.objects.filter(is_active=0,defect_id=defect)
        else:
            CorrectiveAction_data =CorrectiveAction.objects.filter(is_active=0,P_id=P_id,defect_id=defect)
        # Asset_data = Asset.objects.all()
        for CorrectiveActions in CorrectiveAction_data:
            data.append({ 
                'defect' :  defect,
                'corrective_action_id' : CorrectiveActions.corrective_action_id,
                'corrective_action_owner' : CorrectiveActions.corrective_action_owner,
                'corrective_action_description' : CorrectiveActions.corrective_action_description,
                'corrective_action_update' : CorrectiveActions.corrective_action_update,
                'corrective_action_status' : CorrectiveActions.corrective_action_status,
                'user_Role':user_Role,
                'id':CorrectiveActions.corrective_action_id,
            })        
        return JsonResponse({'data':data})
    
class Checkdefect(View):
    template_name = 'add_rootcause.html'

    def post(self, request, *args, **kwargs):
        req = request.POST
        # print(req)
        defect = req.get('defect')
        id = req.get('id')
        if id == '':
            R = RootCause.objects.filter(defect_id=defect,is_active=0)
        else:
            R = RootCause.objects.filter(defect_id=defect,is_active=0).exclude(root_cause_id=id)
        if R.exists():
            return JsonResponse({'status':'0'})  
        else:
            return JsonResponse({'status':'1'})
        
class ReviewBoardView(View):
    template_name = 'reviewboard.html'

    def get(self, request, *args, **kwargs):
        add = kwargs.get("add")
        if add == None:
            add=0
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            asset_type = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
        else:
            asset_type = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type') 
        return render(request, self.template_name, {'add':add,'asset_type':asset_type,'asset_types':asset_type})

    def post(self, request, *args, **kwargs):
        
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        asset_type = req.get('asset_type')
        
        if user_Role == 1:
            ReviewBoard_data =ReviewBoard.objects.filter(is_active=0)
        else:
            ReviewBoard_data =ReviewBoard.objects.filter(is_active=0,P_id=P_id)
        
        if asset_type != "all":
            ReviewBoard_data=ReviewBoard_data.filter(asset_type=asset_type)
        for ReviewBoards in ReviewBoard_data:
            if PBSMaster.objects.filter(id=ReviewBoards.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=ReviewBoards.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    data.append({ 
                        'asset_type' : PBSMaster_data.asset_type,
                        'asset_type_id' : ReviewBoards.asset_type,
                        'meeting_date' : ReviewBoards.meeting_date,
                        'meeting_id' : ReviewBoards.meeting_id,
                        'meeting_status' : ReviewBoards.meeting_status,
                        'id':ReviewBoards.id,
                        'user_Role':user_Role,
                    }) 
        return JsonResponse({'data':data})
    
class AddReviewBoardView(View):
    template_name = 'reviewboard.html'

    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 4:
            return redirect('/dashboard/')
        req = request.POST
        # print(req)
        asset_type = req.get('asset_type')
        from_date = datetime.datetime.strptime(req.get('from_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        to_date = datetime.datetime.strptime(req.get('to_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        if PBSMaster.objects.filter(id=asset_type,is_active=0).exists():
            PBSMaster_datas=PBSMaster.objects.filter(id=asset_type)
            for PBSMaster_data in PBSMaster_datas:
                s=ReviewBoard(asset_type=asset_type,from_date=from_date,to_date=to_date,P_id=PBSMaster_data.project_id)
                s.save()
                FindUser = UserProfile.objects.filter(user_id=user_ID)
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                meg ="Add new review board"
                meg ="ID: "+str(s.id) +"=> "+meg
                h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="FRACAS Review Board")
                h.save()
                return JsonResponse({'status':'1','id':s.id,'asset_type':asset_type,'from_date':from_date,'to_date':to_date})
        return JsonResponse({'status':'0'})
    


class ImportAssetForm(View):
    template_name = 'import_asset_register.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        if user_Role == 4:
            return redirect('/dashboard/')
        user_ID = request.session['user_ID']
        temp_table_asset_register.objects.filter(updated_by=user_ID).delete()
        return render(request, self.template_name,)
    
    
    def post(self, request, *args, **kwargs):
        user_ID = request.session['user_ID']
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        ExcelFile = request.FILES['import_assetRegister'] 
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
            if(cols_count is not 9):
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
           
            # return render(request, self.template_name, {"message": B1})

            asset_type_array=[]

            if(A1=='Asset config id' and B1=='Location id' and C1=='Location description'  and D1=='Asset serial number' and E1=='Asset type' and F1=='Asset description' and G1=='Software version' and H1=='Software description' and I1=='Asset status'):
                # return render(request, self.template_name, {"message": 'required format'})
                for row in range(1, row_count):
                    Asset_config_id= sheet.cell_value(row,0)
                    Location_id= sheet.cell_value(row,1)
                    Location_description= sheet.cell_value(row,2)
                    Asset_serial_number= sheet.cell_value(row,3)
                    Asset_type= sheet.cell_value(row,4)
                    Asset_description= sheet.cell_value(row,5)
                    Software_version= sheet.cell_value(row,6)
                    Software_description= sheet.cell_value(row,7)
                    Asset_status= sheet.cell_value(row,8)

                    Asset_config_id_err = '1'
                    Location_id_err = '1'
                    Location_description_err = '1'
                    Asset_serial_number_err = '1'
                    Asset_type_err = '1'
                    Asset_description_err = '1'
                    Software_version_err = '1'
                    Software_description_err = '1'
                    Asset_status_err = '1'
                    err_status = '1'
                   
                    if user_Role == 1:
                        if not PBSMaster.objects.filter(asset_type=Asset_type,is_active=0).exists():
                            Asset_type_err = 'Invalid asset type'
                    else:
                        if not PBSMaster.objects.filter(asset_type=Asset_type,is_active=0,project_id=P_id).exists():
                            Asset_type_err = 'Invalid asset type'
                    if Asset_config_id == "":
                        Asset_config_id_err = 'Empty'
                    if Location_id == "":
                        Location_id_err = 'Empty'
                    if Location_description == "":
                        Location_description_err = 'Empty'
                    if Asset_serial_number == "":
                        Asset_serial_number_err = 'Empty'
                    if Asset_type == "":
                        Asset_type_err = 'Empty'
                    if Asset_description == "":
                        Asset_description_err = 'Empty'
                    # if Software_version == "":
                    #     Software_version_err = 'Empty'
                    # if Software_description == "":
                    #     Software_description_err = 'Empty'
                    if Asset_status == "":
                        Asset_status_err = 'Empty'
                    else:
                        Asset_status1 = Asset_status.translate({ord(c): None for c in string.whitespace})

                        if Asset_status1.lower() =="online":
                            Asset_status = "Online"
                        elif Asset_status1.lower() =="under repair":
                            Asset_status = "Under Repair"
                        elif Asset_status1.lower() =="spare":
                            Asset_status = "Spare"
                        else:
                            Asset_status_err = 'Invalid asset status'

                    if Asset_config_id_err != '1' or Location_id_err != '1' or Location_description_err != '1' or Asset_serial_number_err != '1' or Asset_type_err != '1' or Asset_description_err != '1' or Software_version_err != '1' or Software_description_err != '1' or Asset_status_err != '1':
                        err_status = '0'
                    
                    data.append({
                        'id':row,
                        'asset_config_id' :  Asset_config_id,
                        'location_id' : Location_id,
                        'location_description' : Location_description,
                        'asset_serial_number' : Asset_serial_number,
                        'asset_type' : Asset_type,
                        'asset_description' : Asset_description,
                        'software_version' : Software_version,
                        'software_description' : Software_description,
                        'asset_status':Asset_status,
                        'err_status':err_status,
                        'asset_config_id_err' :  Asset_config_id_err,
                        'location_id_err' : Location_id_err,
                        'location_description_err' : Location_description_err,
                        'asset_serial_number_err' : Asset_serial_number_err,
                        'asset_type_err' : Asset_type_err,
                        'asset_description_err' : Asset_description_err,
                        'software_version_err' : Software_version_err,
                        'software_description_err' : Software_description_err,
                        'asset_status_err':Asset_status_err,
                    })
            else:
                message='The excel file is not in the required format'
                return render(request, self.template_name, {"message": message})
        else:
            message='The file selected is not excel document'
            return render(request, self.template_name, {"message": message})
        return render(request, self.template_name, {"data": data,"status":"1"})
    
    # def post(self, request, *args, **kwargs):
    #     temp_table_asset_register1 =''
    #     if temp_table_asset_register1:
    #         return render(request, self.template_name, {"message": 'please Wait an excel sheet is in progress'})
    #     else:
    #         user_ID = request.session['user_ID']
    #         ExcelFile = request.FILES['import_assetRegister']   
            
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
    #             if(cols_count is not 9):
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

    #             Asset_config_id_array=[]
                
    #             # return render(request, self.template_name, {"message": B1})

    #             if(A1=='Asset config id' and B1=='Location id' and C1=='Location description'  and D1=='Asset serial number' and E1=='Asset type' and F1=='Asset description' and G1=='Software version' and H1=='Software description' and I1=='Asset status' ):
    #                 # return render(request, self.template_name, {"message": 'required format'})
    #                 for row in range(1, row_count):
    #                     Asset_config_id= sheet.cell_value(row,0)
    #                     Location_id= sheet.cell_value(row,1)
    #                     Location_description= sheet.cell_value(row,2)
    #                     Asset_serial_number= sheet.cell_value(row,3)
    #                     Asset_type= sheet.cell_value(row,4)
    #                     Asset_description= sheet.cell_value(row,5)
    #                     Software_version= sheet.cell_value(row,6)
    #                     Software_description= sheet.cell_value(row,7)
    #                     Asset_status= sheet.cell_value(row,8)

                            
    #                     if Asset_config_id in Asset_config_id_array:
    #                         Asset_config_id=''
    #                     else:  
    #                         Asset_config_id_array.append(Asset_config_id)

    #                     updated_by = user_ID
    #                     if PBSMaster.objects.filter(asset_type=Asset_type).exists():
    #                         subsystem_data =PBSMaster.objects.filter(asset_type=Asset_type)
    #                         asset_type_id= subsystem_data[0].id
    #                         P_id=subsystem_data[0].project_id
    #                     else:
    #                         Asset_type=''
    #                         asset_type_id=''
    #                         P_id=''

    #                     # print('system' +system)
    #                     if Asset_config_id=="" or  Location_id=="" or Location_description=="" or Asset_serial_number==0 or Asset_type=="" or Asset_description=="" or Software_version=="" or Software_description=="" or Asset_status==""  : 
    #                         error_list ='1'
    #                     else:
    #                         error_list ='0'

    #                     u = temp_table_asset_register(asset_config_id=Asset_config_id, location_id=Location_id,location_description=Location_description,asset_serial_number=Asset_serial_number,asset_type=Asset_type,asset_description=Asset_description,software_version=Software_version,software_description=Software_description,asset_status=Asset_status,asset_type_id=asset_type_id,P_id=P_id,error_list=error_list,updated_by = user_ID)
    #                     u.save()
    #                     # return render(request, self.template_name, {"message": 'format'})


                    
    #             else:
    #                 message='The excel file is not in the required format'
    #                 return render(request, self.template_name, {"message": message})
    #         else:
    #             message='The file selected is not excel document'
    #             return render(request, self.template_name, {"message": message})

    #         importfile2 =temp_table_asset_register.objects.filter(updated_by=user_ID)
    #         if importfile2:
    #             data='1'
    #             dataUpdate=[]
    #             dataAdd=[]
    #         else:
    #             data=''
            
    #         asset_data = Asset.objects.filter()
    #         asset_type_array=[]
    #         for a1 in asset_data:
    #             asset_type_array.append(a1.asset_config_id)
                
    #         # return render(request, self.template_name, { "message":asset_type_array[0]})

    #         for imp in importfile2:
    #             if imp.asset_config_id in asset_type_array:
    #                 dataUpdate.append({         
    #                     'id' :imp.id,
    #                     'asset_config_id' :imp.asset_config_id,
    #                     'location_id' :imp.location_id,
    #                     'location_description' :imp.location_description,
    #                     'asset_serial_number' :imp.asset_serial_number,
    #                     'asset_type' :imp.asset_type ,
    #                     'asset_description' :imp.asset_description ,
    #                     'software_version' :imp.software_version ,
    #                     'software_description' :imp.software_description ,
    #                     'asset_status':imp.asset_status,
    #                     'error_list':imp.error_list,
    #                 })
    #             else:

    #                 dataAdd.append({ 
    #                     'id' :imp.id,
    #                     'asset_config_id' :imp.asset_config_id,
    #                     'location_id' :imp.location_id,
    #                     'location_description' :imp.location_description,
    #                     'asset_serial_number' :imp.asset_serial_number,
    #                     'asset_type' :imp.asset_type ,
    #                     'asset_description' :imp.asset_description ,
    #                     'software_version' :imp.software_version ,
    #                     'software_description' :imp.software_description ,
    #                     'asset_status':imp.asset_status,
    #                     'error_list':imp.error_list,
    #                 })
    #         return render(request, self.template_name, {"data":data ,"dataUpdate":dataUpdate,"dataAdd":dataAdd})



class AddImportAssetReg(View):
    template_name = 'import_asset_register.html'
    
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
                    itemasset_config_id = items['asset_config_id']
                    Project = PBSMaster.objects.filter(asset_type=itemAssetType,is_active=0)
                    if Asset.objects.filter(asset_config_id=itemasset_config_id).exists():
                        Asset.objects.filter(asset_config_id=itemasset_config_id).update(is_active=0,P_id=Project[0].project_id,location_id=items['location_id'],location_description=items['location_description'],asset_serial_number=items['asset_serial_number'],asset_type=Project[0].id,asset_description=items['asset_description'],software_version=items['software_version'],software_description=items['software_description'],asset_status=items['asset_status'])
                        updated+=1
                    else:
                        u = Asset(P_id=Project[0].project_id,asset_config_id=itemasset_config_id,location_id=items['location_id'],location_description=items['location_description'],asset_serial_number=items['asset_serial_number'],asset_type=Project[0].id,asset_description=items['asset_description'],software_version=items['software_version'],software_description=items['software_description'],asset_status=items['asset_status'])
                        u.save()
                        inserted+=1
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Insert "+str(inserted)+" record and Update "+str(updated)+" record to Asset"
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Import Asset Register")
        h.save()
        return JsonResponse({'status':'1','inserted': inserted,'updated': updated})
   
    # def post(self, request, *args, **kwargs):
    #     req = self.request.POST
    #     # ids = req.get('ids')
    #     user_ID = request.session['user_ID']

    #     ids=[int(x) for x in req.get('ids', '').split(',')]
    #     if ids=='':
    #         temp_table_asset_register.objects.filter(updated_by=user_ID).delete()
    #         return JsonResponse({'status':'1','inserted': 0,'updated': 0})

    #     else:

    #         imported_data = temp_table_asset_register.objects.filter(id__in=ids)
    #         # message=imported_data[0].asset_type
            
    #         asset_data = Asset.objects.filter()
    #         asset_config_id_array=[]
    #         for a1 in asset_data:
    #             asset_config_id_array.append(a1.asset_config_id)
            
    #         updated=0
    #         inserted=0
    #         for imp in imported_data:
    #             if imp.asset_config_id in asset_config_id_array:
    #                 updated+=1
    #                 Asset_1=Asset.objects.filter(asset_config_id=imp.asset_config_id)
    #                 id=Asset_1[0].id
    #                 Asset.objects.filter(id=id).update(asset_config_id=imp.asset_config_id, location_id=imp.location_id,location_description=imp.location_description,asset_serial_number=imp.asset_serial_number,asset_type=imp.asset_type_id,asset_description=imp.asset_description,software_version=imp.software_version,software_description=imp.software_description,asset_status=imp.asset_status,P_id=imp.P_id)
                
    #             else:
    #                 inserted+=1
    #                 u = Asset(asset_config_id=imp.asset_config_id, location_id=imp.location_id,location_description=imp.location_description,asset_serial_number=imp.asset_serial_number,asset_type=imp.asset_type_id,asset_description=imp.asset_description,software_version=imp.software_version,software_description=imp.software_description,asset_status=imp.asset_status,P_id=imp.P_id)
    #                 u.save()
    #         temp_table_asset_register.objects.filter(updated_by=user_ID).delete()
    #         # return render(request, self.template_name, {"message":message,'status':1 })
    #         P_id = request.session['P_id']
    #         user_ID = request.session['user_ID']
    #         FindUser = UserProfile.objects.filter(user_id=user_ID)
    #         now = datetime.datetime.now()
    #         current_time = now.strftime("%H:%M:%S")
    #         meg ="Insert "+str(inserted)+" record and Update "+str(updated)+" record to Asset"
    #         h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg)
    #         h.save()
    #         return JsonResponse({'status':'1','inserted': inserted,'updated': updated})







class ImportFailureData(View):
    template_name = 'import_failuredata.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        if user_Role == 4:
            return redirect('/dashboard/')

        user_ID = request.session['user_ID']
        temp_table_failure_data.objects.filter(updated_by=user_ID).delete()
        return render(request, self.template_name,)
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        user_ID = request.session['user_ID']
        ExcelFile = request.FILES['import_failureData'] 
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
            if(cols_count is not 21):
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
            O1= sheet.cell_value(0,14)
            P1= sheet.cell_value(0,15)
            Q1= sheet.cell_value(0,16)
            R1= sheet.cell_value(0,17)
            S1= sheet.cell_value(0,18)
            T1= sheet.cell_value(0,19)
            U1= sheet.cell_value(0,20)
            # return render(request, self.template_name, {"message": B1})
            asset_type_array=[]

            if(A1=='Failure id' and B1=='Asset type' and C1=='Asset config id' and D1=='Event description' and E1=='Mode id' and F1=='Date' and G1=='Time' and H1=='Detection' and I1=='Service delay' and J1=='Immediate investigation' and K1=='Failure type' and L1=='Safety failure' and M1=='Hazard id' and N1=='Cm description' and O1=='Replaced asset config id' and P1=='Cm start date' and Q1=='Cm start time' and R1=='Cm end date' and S1=='Cm end time' and T1=='Oem failure reference' and U1=='defect' ):
                # return render(request, self.template_name, {"message": 'required format'})
                print('------COMPLETE VALIDATION ______') 
                rowCountVar = 0
                for row in range(1, row_count):
                    rowCountVar = rowCountVar + 1
                    print('--------------------------------  '+ str(rowCountVar)) 
                    if isinstance(sheet.cell_value(row,0), str):
                        failure_id = sheet.cell_value(row,0)
                    else:
                        failure_id = int(sheet.cell_value(row,0))
                    asset_type=sheet.cell_value(row,1)
                    asset_config_id= sheet.cell_value(row,2)
                    event_description= sheet.cell_value(row,3)
                    if isinstance(sheet.cell_value(row,4), str):
                        mode_id = sheet.cell_value(row,4)
                    else:
                        mode_id = int(sheet.cell_value(row,4))
                    date= sheet.cell_value(row,5)
                    time = sheet.cell_value(row,6)
                    # time1 = xlrd.xldate_as_tuple(time1, wb.datemode)
                    # time = datetime.time(*time1[3:])
                    # time = time.strftime("%H:%M")
                    detection= sheet.cell_value(row,7)
                    if isinstance(sheet.cell_value(row,8), str):
                        service_delay = sheet.cell_value(row,8)
                    else:
                        service_delay = int(sheet.cell_value(row,8))
                    immediate_investigation = sheet.cell_value(row,9)
                    failure_type = sheet.cell_value(row,10)
                    safety_failure = sheet.cell_value(row,11)
                    hazard_id= sheet.cell_value(row,12)
                    cm_description = sheet.cell_value(row,13)
                    replaced_asset_config_id = sheet.cell_value(row,14)
                    cm_start_date =sheet.cell_value(row,15) 
                    cm_start_time = sheet.cell_value(row,16)
                    
                    # cm_start_time1 = xlrd.xldate_as_tuple(cm_start_time1, wb.datemode)
                    # cm_start_time1 = datetime.time(*cm_start_time1[3:])
                    # cm_start_time = cm_start_time1.strftime("%H:%M")
                    cm_end_date=sheet.cell_value(row,17) 
                    cm_end_time = sheet.cell_value(row,18)
                   
                    # cm_end_time1 = xlrd.xldate_as_tuple(cm_end_time1, wb.datemode)
                    # cm_end_time1 = datetime.time(*cm_end_time1[3:])
                    # cm_end_time = cm_end_time1.strftime("%H:%M")
                    oem_failure_reference = sheet.cell_value(row,19)
                    if isinstance(sheet.cell_value(row,20), str):
                        defect = sheet.cell_value(row,20)
                    else:
                        defect = int(sheet.cell_value(row,20))
                    failure_id_err = '1'
                    asset_type_err = '1'
                    asset_config_id_err = '1'
                    event_description_err = '1'
                    mode_id_err = '1'
                    date_err = '1'
                    time_err = '1'
                    detection_err = '1'
                    service_delay_err = '1'
                    immediate_investigation_err = '1'
                    failure_type_err = '1'
                    safety_failure_err = '1'
                    hazard_id_err = '1'
                    cm_description_err = '1'
                    replaced_asset_config_id_err = '1'
                    cm_start_date_err = '1'
                    cm_start_time_err = '1'
                    cm_end_date_err = '1'
                    cm_end_time_err = '1'
                    oem_failure_reference_err = '1'
                    defect_err = '1'
                    err_status = '1'


                    # if not isinstance(failure_id, int) :
                    #     failure_id_err='Value error'
                    if not isinstance(service_delay, int) :
                        service_delay_err='Value error'
                    if not isinstance(defect, int) :
                        defect=''
                    if mode_id != "":                        
                        if not FailureMode.objects.filter(mode_id=mode_id,is_active=0).exists():
                            mode_id_err = 'Invalid match'
                    else:
                        mode_id_err = 'Empty'

                    if defect != "": 
                        if not Defect.objects.filter(defect_id=defect,is_active=0).exists():
                            defect_err = 'Invalid match'
                    else:
                        defect_err = 'Empty'
                        
                    if failure_id == "":
                        failure_id_err = 'Empty'
                    if asset_type == "":
                        asset_type_err = 'Empty'
                    else:
                        if user_Role == 1:
                            if not PBSMaster.objects.filter(asset_type=asset_type,is_active=0).exists():
                                asset_type_err = 'Invalid asset type' 
                                asset_config_id_err = 'Invalid match'
                            else: 
                                Project = PBSMaster.objects.filter(asset_type=asset_type,is_active=0)
                                if asset_config_id == "":
                                    asset_config_id_err = 'Empty'
                                else:
                                    if not Asset.objects.filter(asset_config_id=asset_config_id,asset_type=Project[0].id,is_active=0).exists():
                                        asset_config_id_err = 'Invalid match'
                        else:
                            if not PBSMaster.objects.filter(asset_type=asset_type,is_active=0,project_id=P_id).exists():
                                asset_type_err = 'Invalid asset type' 
                                asset_config_id_err = 'Invalid match'
                            else: 
                                Project = PBSMaster.objects.filter(asset_type=asset_type,is_active=0,project_id=P_id)
                                if asset_config_id == "":
                                    asset_config_id_err = 'Empty'
                                else:
                                    if not Asset.objects.filter(asset_config_id=asset_config_id,asset_type=Project[0].id,is_active=0,P_id=P_id).exists():
                                        asset_config_id_err = 'Invalid match'
                    if event_description == "":
                        event_description_err = 'Empty'
                    if date == "":
                        now = datetime.datetime.now()
                        date = datetime.datetime.strftime(now, '%d-%m-%Y')
                    else:
                        if type(date) == str:
                            try:
                                date1 = datetime.datetime.strptime(str(date), '%d-%m-%Y').date()
                                date=datetime.datetime.strftime(date1, '%d-%m-%Y')
                            except ValueError:
                                message='Invalid Date format, should be (DD-MM-YYYY in string OR change cell format to date)  in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})
                        else:
                            try:
                                date1 = xlrd.xldate.xldate_as_datetime(date, wb.datemode)
                                try:
                                    date=datetime.datetime.strftime(date1, '%d-%m-%Y')
                                except ValueError:
                                    message='Invalid Date format in row '+str(rowCountVar)
                                    return render(request, self.template_name, {"message": message})
                                
                            except ValueError:
                                message='Invalid Date format in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})
                        
                    # print(date)
                        # date1 = datetime.datetime.strptime(str(date), '%d-%m-%Y').date()
                        # date=datetime.datetime.strftime(date1, '%d-%m-%Y')
                    # print(date)
                    if time == "":
                        time_err = 'Empty'
                    else:
                        print(type(time))
                        if type(time) == float:
                            print(time)
                            try:
                                time1 = xlrd.xldate.xldate_as_datetime(time, wb.datemode)
                                try:
                                    time=datetime.datetime.strftime(time1, '%H:%M:%S')
                                except ValueError:
                                    message='Invalid Time format in row '+str(rowCountVar)
                                    return render(request, self.template_name, {"message": message})
                                
                            except ValueError:
                                message='Invalid Time format in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})
                        else:
                            print(time)
                            try:
                                datetime.datetime.strptime(str(time), '%H:%M:%S').date()
                            except ValueError:
                                message='Invalid Time format, should be (HH:mm:ss in string OR change cell format to time) in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})
                    print(time)
                    if detection == "":
                        detection_err = 'Empty'
                    if service_delay == "":
                        service_delay_err = 'Empty'
                    if immediate_investigation == "":
                        immediate_investigation_err = 'Empty'
                        
                    failure_types = ['Software','Hardware','Random','Other']
                    if failure_type == "":
                        failure_type_err = 'Empty'
                    else:
                        if not failure_type in failure_types :
                            failure_type_err = 'Invalid failure type'
                        
                    if safety_failure == "":
                        safety_failure_err = 'Empty'
                    if cm_description == "":
                        cm_description_err = 'Empty'
                    
                    print('------ CHK VARIABLES STN 4 ______')  
                    if cm_start_date == "":
                        cm_start_date_err = 'Empty'
                    else:
                        if type(cm_start_date) == str:
                            try:
                                cm_start_date1 = datetime.datetime.strptime(str(cm_start_date), '%d-%m-%Y').date()
                                cm_start_date=datetime.datetime.strftime(cm_start_date1, '%d-%m-%Y')
                            except ValueError:
                                message='Invalid Cm start date format, should be (DD-MM-YYYY in string OR change cell format to date)  in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})
                        else:
                            try:
                                cm_start_date1 = xlrd.xldate.xldate_as_datetime(cm_start_date, wb.datemode)
                                try:
                                    cm_start_date=datetime.datetime.strftime(cm_start_date1, '%d-%m-%Y')
                                except ValueError:
                                    message='Invalid Cm start date format in row '+str(rowCountVar)
                                    return render(request, self.template_name, {"message": message})
                                
                            except ValueError:
                                message='Invalid Cm start date format in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})

                    # print(cm_start_date)
                      
                    if cm_start_time == "":
                        cm_start_time_err = 'Empty'
                    else:
                        if type(cm_start_time) == float:
                            # print(cm_start_time)
                            try:
                                cm_start_time1 = xlrd.xldate.xldate_as_datetime(cm_start_time, wb.datemode)
                                try:
                                    cm_start_time=datetime.datetime.strftime(cm_start_time1, '%H:%M:%S')
                                except ValueError:
                                    message='Invalid Cm start time format in row '+str(rowCountVar)
                                    return render(request, self.template_name, {"message": message})
                                
                            except ValueError:
                                message='Invalid Cm start time format in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})
                        else:
                            try:
                                datetime.datetime.strptime(str(cm_start_time), '%H:%M:%S').date()
                            except ValueError:
                                message='Invalid Cm start time format, should be (HH:mm:ss in string OR change cell format to time) in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})


                    # print(cm_start_time)
                    if cm_end_date == "":
                        cm_end_date = ''
                    else:
                        if type(cm_end_date) == str:
                            try:
                                cm_end_date1 = datetime.datetime.strptime(str(cm_end_date), '%d-%m-%Y').date()
                                cm_end_date=datetime.datetime.strftime(cm_end_date1, '%d-%m-%Y')
                            except ValueError:
                                message='Invalid Cm end date format, should be (DD-MM-YYYY in string OR change cell format to date)  in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})
                        else:
                            try:
                                cm_end_date1 = xlrd.xldate.xldate_as_datetime(cm_end_date, wb.datemode)
                                try:
                                    cm_end_date=datetime.datetime.strftime(cm_end_date1, '%d-%m-%Y')
                                except ValueError:
                                    message='Invalid Cm end date format in row '+str(rowCountVar)
                                    return render(request, self.template_name, {"message": message})
                                
                            except ValueError:
                                message='Invalid Cm end date format in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})

                    # print(cm_end_date)


                    if cm_end_time != "":
                        if type(cm_end_time) == float:
                            print(cm_end_time)
                            try:
                                cm_end_time1 = xlrd.xldate.xldate_as_datetime(cm_end_time, wb.datemode)
                                try:
                                    cm_end_time=datetime.datetime.strftime(cm_end_time1, '%H:%M:%S')
                                except ValueError:
                                    message='Invalid Cm end time format in row '+str(rowCountVar)
                                    return render(request, self.template_name, {"message": message})
                                
                            except ValueError:
                                message='Invalid Cm end time format in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})
                        else:
                            try:
                                datetime.datetime.strptime(str(cm_end_time), '%H:%M:%S').date()
                            except ValueError:
                                message='Invalid Cm end time format, should be (HH:mm:ss in string OR change cell format to time) in row '+str(rowCountVar)
                                return render(request, self.template_name, {"message": message})

                    # print(cm_end_time)
                        
                    if failure_id_err != '1' or asset_type_err != '1' or asset_config_id_err != '1' or event_description_err != '1' or date_err != '1' or time_err != '1' or detection_err != '1' or service_delay_err != '1' or immediate_investigation_err != '1' or failure_type_err != '1' or safety_failure_err != '1' or hazard_id_err != '1' or cm_description_err != '1' or replaced_asset_config_id_err != '1' or cm_start_date_err != '1' or cm_start_time_err != '1' or cm_end_date_err != '1' or cm_end_time_err != '1' or oem_failure_reference_err != '1' or mode_id_err != '1' or defect_err != '1':
                        err_status = '0'
                    data.append({
                        'id':row,
                        'failure_id' :  failure_id,
                        'asset_type' : asset_type,
                        'asset_config_id' : asset_config_id,
                        'event_description' : event_description,
                        'mode_id' : mode_id,
                        'date' : date,
                        'time' : time,
                        'detection':detection,
                        'service_delay' :  service_delay,
                        'immediate_investigation' : immediate_investigation,
                        'failure_type' : failure_type,
                        'safety_failure' : safety_failure,
                        'hazard_id' : hazard_id,
                        'cm_description' : cm_description,
                        'replaced_asset_config_id' : replaced_asset_config_id,
                        'cm_start_date' : cm_start_date,
                        'cm_start_time' : cm_start_time,
                        'cm_end_date' : cm_end_date,
                        'cm_end_time' : cm_end_time,
                        'oem_failure_reference' : oem_failure_reference,
                        'defect' : defect,
                        'err_status':err_status,
                        'failure_id_err' :  failure_id_err,
                        'asset_type_err' : asset_type_err,
                        'asset_config_id_err' : asset_config_id_err,
                        'event_description_err' : event_description_err,
                        'mode_id_err' : mode_id_err,
                        'date_err' : date_err,
                        'time_err' : time_err,
                        'detection_err':detection_err,
                        'service_delay_err' :  service_delay_err,
                        'immediate_investigation_err' : immediate_investigation_err,
                        'failure_type_err' : failure_type_err,
                        'safety_failure_err' : safety_failure_err,
                        'hazard_id_err' : hazard_id_err,
                        'cm_description_err' : cm_description_err,
                        'replaced_asset_config_id_err' : replaced_asset_config_id_err,
                        'cm_start_date_err' : cm_start_date_err,
                        'cm_start_time_err' : cm_start_time_err,
                        'cm_end_date_err' : cm_end_date_err,
                        'cm_end_time_err' : cm_end_time_err,
                        'oem_failure_reference_err' : oem_failure_reference_err,
                        'defect_err' : defect_err,
                    })
            else:
                message='The excel file is not in the required format'
                return render(request, self.template_name, {"message": message})
        else:
            message='The file selected is not excel document'
            return render(request, self.template_name, {"message": message})
        return render(request, self.template_name, {"data": data,"status":"1"})
    
    # def post(self, request, *args, **kwargs):
    #     user_ID = request.session['user_ID']
    #     # temp_table_FailureData1 =temp_table_FailureData.objects.filter(updated_by=user_ID)
    #     temp_table_FailureData1 =''
    #     if temp_table_FailureData1:
    #         return render(request, self.template_name, {"message": 'please Wait an excel sheet is in progress'})
    #     else:
    #         ExcelFile = request.FILES['import_failureData']   
            
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
    #             if(cols_count is not 21):
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
    #             M1= sheet.cell_value(0,12)
    #             N1= sheet.cell_value(0,13)
    #             O1= sheet.cell_value(0,14)
    #             P1= sheet.cell_value(0,15)
    #             Q1= sheet.cell_value(0,16)
    #             R1= sheet.cell_value(0,17)
    #             S1= sheet.cell_value(0,18)
    #             T1= sheet.cell_value(0,19)
    #             U1= sheet.cell_value(0,20)

    #             # return render(request, self.template_name, {"message": B1})
    #             failure_id_array=[]
    #             # c_failure_id_array=[]

    #             if(A1=='Failure id' and B1=='Asset type' and C1=='Asset config id' and D1=='Event description' and E1=='Mode id' and F1=='Date' and G1=='Time' and H1=='Detection' and I1=='Service delay' and J1=='Immediate investigation' and K1=='Failure type' and L1=='Safety failure' and M1=='Hazard id' and N1=='Cm description' and O1=='Replaced asset config id' and P1=='Cm start date' and Q1=='Cm start time' and R1=='Cm end date' and S1=='Cm end time' and T1=='Oem failure reference' and U1=='defect' ):
    #                 # return render(request, self.template_name, {"message": 'required format'})
    #                 for row in range(1, row_count):
    #                     if isinstance(sheet.cell_value(row,0), float):

    #                         c_failure_id=int(sheet.cell_value(row,0))
    #                         if isinstance(sheet.cell_value(row,0), float) and sheet.cell_value(row,0)==c_failure_id :
    #                             failure_id=c_failure_id
    #                             if failure_id in failure_id_array :
    #                                 failure_id=0
    #                             else:
    #                                 failure_id_array.append(failure_id)

    #                         else:
    #                             failure_id=0
    #                     else:
    #                         failure_id=0

    #                     asset_type= sheet.cell_value(row,1)
    #                     asset_config_id= sheet.cell_value(row,2)
                        
    #                     if Asset.objects.filter(asset_config_id=asset_config_id).exists():
    #                         Result =Asset.objects.filter(asset_config_id=asset_config_id)
    #                         asset_type_id2= Result[0].asset_type
                         
    #                     if PBSMaster.objects.filter(asset_type=asset_type).exists():
    #                         subsystem_data =PBSMaster.objects.filter(asset_type=asset_type)
    #                         asset_type_id= subsystem_data[0].id

    #                         P_id=subsystem_data[0].project_id

    #                         if (asset_type_id == asset_type_id2) :
    #                             pass
    #                         else :
    #                             asset_type=''
    #                             asset_type_id=''
    #                     else:
    #                         asset_type=''
    #                         asset_type_id=''
    #                         P_id=''
                        
                                               
    #                     event_description= sheet.cell_value(row,3)
    #                     mode_id= sheet.cell_value(row,4)
    #                     date= datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(row,5), wb.datemode))
    #                     time= sheet.cell_value(row,6)
    #                     detection= sheet.cell_value(row,7)
    #                     service_delay= sheet.cell_value(row,8)
    #                     immediate_investigation= sheet.cell_value(row,9)
    #                     failure_type= sheet.cell_value(row,10)
    #                     safety_failure= sheet.cell_value(row,11)
    #                     hazard_id= sheet.cell_value(row,12)
    #                     cm_description= sheet.cell_value(row,13)
    #                     replaced_asset_config_id= sheet.cell_value(row,14)
    #                     cm_start_date= datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(row,15), wb.datemode))
    #                     cm_start_time= sheet.cell_value(row,16)
    #                     cm_end_date= datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(row,17), wb.datemode))
    #                     cm_end_time= sheet.cell_value(row,18)
    #                     oem_failure_reference= sheet.cell_value(row,19)
    #                     defect= sheet.cell_value(row,20)

                       
    #                     if failure_id==0 or asset_type=='' or asset_config_id=='' or asset_type_id=='' or event_description=='' or date=='' or time=='' or detection=='' or service_delay=='' or immediate_investigation=='' or failure_type=='' or safety_failure=='' or hazard_id=='' or cm_description=='' or replaced_asset_config_id=='' or cm_start_date=='' or cm_start_time=='' or cm_end_date=='' or cm_end_time=='' or oem_failure_reference=='' : 
    #                         error_list ='1'
    #                     else:
    #                         error_list ='0'

    #                     u = temp_table_failure_data(failure_id=failure_id,asset_type=asset_type, asset_config_id=asset_config_id, asset_type_id=asset_type_id, event_description=event_description, mode_id=mode_id, date=date, time=time, detection=detection, service_delay=service_delay, immediate_investigation=immediate_investigation, failure_type=failure_type, safety_failure=safety_failure, hazard_id=hazard_id, cm_description=cm_description, replaced_asset_config_id=replaced_asset_config_id, cm_start_date=cm_start_date, cm_start_time=cm_start_time, cm_end_date=cm_end_date, cm_end_time=cm_end_time, oem_failure_reference=oem_failure_reference, defect=defect,P_id=P_id,error_list=error_list,updated_by=user_ID)
    #                     u.save()
    #                     # return render(request, self.template_name, {"message": 'format'})


                    
    #             else:
    #                 message='The excel file is not in the required format'
    #                 return render(request, self.template_name, {"message": message})
    #         else:
    #             message='The file selected is not excel document'
    #             return render(request, self.template_name, {"message": message})


    #         importfile2 =temp_table_failure_data.objects.filter(updated_by=user_ID)
    #         if importfile2:
    #             data='1'
    #             dataUpdate=[]
    #             dataAdd=[]
    #         else:
    #             data=''
            
    #         failure_data = FailureData.objects.filter()
    #         failure_id_array=[]
    #         for a1 in failure_data:
    #             failure_id_array.append(a1.failure_id)
           
    #         for imp in importfile2:
    #             if imp.failure_id in failure_id_array or imp.failure_id==0:
    #                 dataUpdate.append({    
    #                     'id' :imp.id,     
    #                     'failure_id' :imp.failure_id,
    #                     'asset_type' :imp.asset_type,
    #                     'asset_config_id' :imp.asset_config_id,
    #                     'event_description' :imp.event_description,
    #                     'mode_id' :imp.mode_id,
    #                     'date' :imp.date,
    #                     'time' :imp.time,
    #                     'detection' :imp.detection,
    #                     'service_delay' :imp.service_delay,
    #                     'immediate_investigation' :imp.immediate_investigation,
    #                     'failure_type' :imp.failure_type,
    #                     'safety_failure' :imp.safety_failure,
    #                     'hazard_id' :imp.hazard_id,
    #                     'cm_description' :imp.cm_description,
    #                     'replaced_asset_config_id' :imp.replaced_asset_config_id,
    #                     'cm_start_date' :imp.cm_start_date,
    #                     'cm_start_time' :imp.cm_start_time,
    #                     'cm_end_date' :imp.cm_end_date,
    #                     'cm_end_time' :imp.cm_end_time,
    #                     'oem_failure_reference' :imp.oem_failure_reference,
    #                     'defect' :imp.defect,
    #                     'error_list':imp.error_list,

    #                 })
    #             else:
    #                 dataAdd.append({ 
    #                     'id' :imp.id,
    #                     'failure_id' :imp.failure_id,
    #                     'asset_type' :imp.asset_type,
    #                     'asset_config_id' :imp.asset_config_id,
    #                     'event_description' :imp.event_description,
    #                     'mode_id' :imp.mode_id,
    #                     'date' :imp.date,
    #                     'time' :imp.time,
    #                     'detection' :imp.detection,
    #                     'service_delay' :imp.service_delay,
    #                     'immediate_investigation' :imp.immediate_investigation,
    #                     'failure_type' :imp.failure_type,
    #                     'safety_failure' :imp.safety_failure,
    #                     'hazard_id' :imp.hazard_id,
    #                     'cm_description' :imp.cm_description,
    #                     'replaced_asset_config_id' :imp.replaced_asset_config_id,
    #                     'cm_start_date' :imp.cm_start_date,
    #                     'cm_start_time' :imp.cm_start_time,
    #                     'cm_end_date' :imp.cm_end_date,
    #                     'cm_end_time' :imp.cm_end_time,
    #                     'oem_failure_reference' :imp.oem_failure_reference,
    #                     'defect' :imp.defect,
    #                     'error_list':imp.error_list,
    #                 })
    #         return render(request, self.template_name, {"data":data ,"dataUpdate":dataUpdate,"dataAdd":dataAdd})



class AddImportFailureData(View):
    template_name = 'import_failuredata.html'
    
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
                # itemdate = items['date']
                itemdate1=datetime.datetime.strptime(items['date'], '%d-%m-%Y').date()
                itemdate=datetime.datetime.strftime(itemdate1, '%Y-%m-%d')
                # print(itemdate)
                # itemcm_start_date = items['cm_start_date']
                itemcm_start_date1=datetime.datetime.strptime(items['cm_start_date'], '%d-%m-%Y').date()
                itemcm_start_date=datetime.datetime.strftime(itemcm_start_date1, '%Y-%m-%d')
                # print(itemcm_start_date)
                # itemcm_end_date = items['cm_end_date']
                print(items['cm_end_date'])

                if items['cm_end_date'] != "":
                    itemcm_end_date1=datetime.datetime.strptime(items['cm_end_date'], '%d-%m-%Y').date()
                    itemcm_end_date=datetime.datetime.strftime(itemcm_end_date1, '%Y-%m-%d')
                else:
                    itemcm_end_date = None
                print(itemcm_end_date)
              
                itemfailure_id = items['failure_id']
                itemasset_type = items['asset_type']
                itemasset_config_id = items['asset_config_id']
                itemmode_id = items['mode_id']
                itemdefect = items['defect']
                itemscm_end_time = items['cm_end_time']
                if itemscm_end_time == '':
                    itemscm_end_time = None
               
                if itemId in ids:
                    Project = PBSMaster.objects.filter(asset_type=itemasset_type,is_active=0)
                    if not FailureMode.objects.filter(mode_id=itemmode_id,P_id=Project[0].project_id).exists():
                        itemmode_id = None
                    else:
                        MODE = FailureMode.objects.filter(mode_id=itemmode_id,P_id=Project[0].project_id)
                        itemmode_id = MODE[0].id
                    if itemdefect == '':
                        itemdefect = None
                    else:
                        if not Defect.objects.filter(defect_id=itemdefect,P_id=Project[0].project_id).exists():
                            itemdefect = None
                    if FailureData.objects.filter(failure_id=itemfailure_id).exists():
                        FailureData.objects.filter(failure_id=itemfailure_id).update(is_active=0,P_id=Project[0].project_id,asset_type=Project[0].id,asset_config_id_id=itemasset_config_id,
                                        event_description=items['event_description'],mode_id_id=itemmode_id,date=itemdate,time=items['time'],detection=items['detection'],
                                        service_delay=items['service_delay'],immediate_investigation=items['immediate_investigation'],failure_type=items['failure_type'],
                                        safety_failure=items['safety_failure'],hazard_id=items['hazard_id'],cm_description=items['cm_description'],
                                        replaced_asset_config_id=items['replaced_asset_config_id'],cm_start_date=itemcm_start_date,
                                        cm_start_time=items['cm_start_time'],cm_end_date=itemcm_end_date,cm_end_time=itemscm_end_time,
                                        oem_failure_reference=items['oem_failure_reference'],defect_id=itemdefect)
                        updated+=1
                    else:
                        u = FailureData(P_id=Project[0].project_id,failure_id=itemfailure_id,asset_type=Project[0].id,asset_config_id_id=itemasset_config_id,
                                        event_description=items['event_description'],mode_id_id=itemmode_id,date=itemdate,time=items['time'],detection=items['detection'],
                                        service_delay=items['service_delay'],immediate_investigation=items['immediate_investigation'],failure_type=items['failure_type'],
                                        safety_failure=items['safety_failure'],hazard_id=items['hazard_id'],cm_description=items['cm_description'],
                                        replaced_asset_config_id=items['replaced_asset_config_id'],cm_start_date=itemcm_start_date,
                                        cm_start_time=items['cm_start_time'],cm_end_date=itemcm_end_date,cm_end_time=itemscm_end_time,
                                        oem_failure_reference=items['oem_failure_reference'],defect_id=itemdefect)
                        u.save()
                        inserted+=1
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Insert "+str(inserted)+" record and Update "+str(updated)+" record to Failuredata"
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Import Failure Data Collection")
        h.save()
        return JsonResponse({'status':'1','inserted': inserted,'updated': updated})
   
    # def post(self, request, *args, **kwargs):
    #     user_ID = request.session['user_ID']
    #     req = self.request.POST
    #     # ids = req.get('ids')
    #     ids=[int(x) for x in req.get('ids', '').split(',')]
    #     if ids=='':
    #         temp_table_failure_data.objects.filter(updated_by=user_ID).delete()  
    #         return JsonResponse({'status':'1','inserted': 0,'updated': 0})

    #     else:

    #         imported_data = temp_table_failure_data.objects.filter(id__in=ids)
    #         # message=imported_data[0].asset_type
            
    #         failure_data = FailureData.objects.filter()
    #         failure_id_array=[]
    #         for a1 in failure_data:
    #             failure_id_array.append(a1.failure_id)
            
    #         updated=0
    #         inserted=0
    #         for imp in imported_data:
    #             date = datetime.datetime.strptime(imp.date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    #             cm_start_date = datetime.datetime.strptime(imp.cm_start_date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    #             cm_end_date = datetime.datetime.strptime(imp.cm_end_date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    #             float_str = float(imp.service_delay)
    #             int_str = int(float_str)
    #             print(int_str)
    #             if imp.failure_id in failure_id_array :
    #                 updated+=1
    #                 Row_1=FailureData.objects.filter(failure_id=imp.failure_id)
    #                 id=Row_1[0].id
    #                 FailureData.objects.filter(id=id).update(failure_id=imp.failure_id,asset_type=imp.asset_type_id,asset_config_id_id=imp.asset_config_id,event_description=imp.event_description,mode_id=None,date=date,time=imp.time,detection=imp.detection,service_delay=int_str,immediate_investigation=imp.immediate_investigation,failure_type=imp.failure_type,safety_failure=imp.safety_failure,hazard_id=imp.hazard_id,cm_description=imp.cm_description,replaced_asset_config_id=imp.replaced_asset_config_id,cm_start_date=cm_start_date,cm_start_time=imp.cm_start_time,cm_end_date=cm_end_date,cm_end_time=imp.cm_end_time,oem_failure_reference=imp.oem_failure_reference,defect=None)
                
    #             else:
    #                 inserted+=1
    #                 u = FailureData(failure_id=imp.failure_id,asset_type=imp.asset_type_id,asset_config_id_id=imp.asset_config_id,event_description=imp.event_description,mode_id=None,date=date,time=imp.time,detection=imp.detection,service_delay=int_str,immediate_investigation=imp.immediate_investigation,failure_type=imp.failure_type,safety_failure=imp.safety_failure,hazard_id=imp.hazard_id,cm_description=imp.cm_description,replaced_asset_config_id=imp.replaced_asset_config_id,cm_start_date=cm_start_date,cm_start_time=imp.cm_start_time,cm_end_date=cm_end_date,cm_end_time=imp.cm_end_time,oem_failure_reference=imp.oem_failure_reference,defect=None)
    #                 u.save()
    #         temp_table_failure_data.objects.filter(updated_by=user_ID).delete()
    #         P_id = request.session['P_id']
    #         user_ID = request.session['user_ID']
    #         FindUser = UserProfile.objects.filter(user_id=user_ID)
    #         now = datetime.datetime.now()
    #         current_time = now.strftime("%H:%M:%S")
    #         meg ="Insert "+str(inserted)+" record and Update "+str(updated)+" record to failure data"
    #         h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg)
    #         h.save()
    #         return JsonResponse({'status':'1','inserted': inserted,'updated': updated})






class ImportFailuremode(View):
    template_name = 'import_failuremode.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        if user_Role == 4:
            return redirect('/dashboard/')
        user_ID = request.session['user_ID']
        temp_table_failure_mode.objects.filter(updated_by=user_ID).delete()
        return render(request, self.template_name,)
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        user_ID = request.session['user_ID']
        ExcelFile = request.FILES['import_failureMode'] 
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
            if(cols_count is not 3):
                message='The excel file is not in the required format'
                return render(request, self.template_name, {"message": message})


            A1= sheet.cell_value(0,0) 
            B1= sheet.cell_value(0,1)
            C1= sheet.cell_value(0,2)
            # return render(request, self.template_name, {"message": B1})

            asset_type_array=[]

            if(A1=='Mode id' and B1=='Mode description' and C1=='Asset type' ):
                # return render(request, self.template_name, {"message": 'required format'})
                for row in range(1, row_count):
                    mode_id= sheet.cell_value(row,0)
                    mode_description= sheet.cell_value(row,1)
                    asset_type= sheet.cell_value(row,2)
                    
                    mode_id_err = '1'
                    mode_description_err = '1'
                    asset_type_err = '1'
                    err_status = '1'
                    
                    if asset_type != "":
                        if user_Role == 1:
                            if not PBSMaster.objects.filter(asset_type=asset_type,is_active=0).exists():
                                asset_type_err = 'Invalid asset type'
                        else:
                            if not PBSMaster.objects.filter(asset_type=asset_type,is_active=0,project_id=P_id).exists():
                                asset_type_err = 'Invalid asset type'
                        
                    if mode_id == "":
                        mode_id_err = 'Empty'
                    if mode_description == "":
                        mode_description_err = 'Empty'
                        
                    if user_Role == 1:
                        if asset_type == "":
                            asset_type_err = 'Empty'
                  
                    if mode_id_err != '1' or mode_description_err != '1' or asset_type_err != '1' :
                        err_status = '0'
                    
                    data.append({
                        'id':row,
                        'mode_id':mode_id,
                        'mode_id_err':mode_id_err,
                        'mode_description':mode_description,
                        'mode_description_err':mode_description_err,
                        'asset_type':asset_type,
                        'asset_type_err':asset_type_err,
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
    #     temp_table_FailureMode1 =''
    #     if temp_table_FailureMode1:
    #         return render(request, self.template_name, {"message": 'please Wait an excel sheet is in progress'})
    #     else:
    #         user_ID = request.session['user_ID']
    #         ExcelFile = request.FILES['import_failureMode']   
            
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
    #             if(cols_count is not 3):
    #                 message='The excel file is not in the required format'
    #                 return render(request, self.template_name, {"message": message})

    #             A1= sheet.cell_value(0,0) 
    #             B1= sheet.cell_value(0,1)
    #             C1= sheet.cell_value(0,2)
               
                
    #             mode_id_array=[]
    #             if(A1=='Mode id' and B1=='Mode description' and C1=='Asset type'):
    #                 # return render(request, self.template_name, {"message": 'required format'})
    #                 for row in range(1, row_count):
    #                     mode_id= sheet.cell_value(row,0)
    #                     mode_description= sheet.cell_value(row,1)
    #                     asset_type= sheet.cell_value(row,2)
                        
                       
    #                     if PBSMaster.objects.filter(asset_type=asset_type).exists():
    #                         subsystem_data =PBSMaster.objects.filter(asset_type=asset_type)
    #                         asset_type_id= subsystem_data[0].id
    #                         P_id=subsystem_data[0].project_id
    #                     else:
    #                         asset_type=''
    #                         asset_type_id=''
    #                         P_id=''

                        
    #                     if mode_id in mode_id_array:
    #                         mode_id=''
    #                     else:  
    #                         mode_id_array.append(mode_id)

    #                     # print('system' +system)
    #                     if mode_id=="" or  asset_type=="" or asset_type_id=="" or mode_description=="": 
    #                         error_list ='1'
    #                     else:
    #                         error_list ='0'

    #                     u = temp_table_failure_mode(mode_id=mode_id, mode_description=mode_description,asset_type=asset_type,asset_type_id=asset_type_id,error_list=error_list,P_id=P_id, updated_by = user_ID)
    #                     u.save()
    #                     # return render(request, self.template_name, {"message": 'format'})


                    
    #             else:
    #                 message='The excel file is not in the required format'
    #                 return render(request, self.template_name, {"message": message})
    #         else:
    #             message='The file selected is not excel document'
    #             return render(request, self.template_name, {"message": message})

    #         importfile2 =temp_table_failure_mode.objects.filter(updated_by=user_ID)
    #         if importfile2:
    #             data='1'
    #             dataUpdate=[]
    #             dataAdd=[]
    #         else:
    #             data=''
            
    #         failure_mode = FailureMode.objects.filter()
    #         failure_mode_array=[]
    #         for fm in failure_mode:
    #             failure_mode_array.append(fm.mode_id)
                
    #         # return render(request, self.template_name, { "message":asset_type_array[0]})

    #         for imp in importfile2:
    #             if imp.mode_id in failure_mode_array:
    #                 dataUpdate.append({ 
    #                     'id':imp.id, 
    #                     'mode_id':imp.mode_id, 
    #                     'mode_description':imp.mode_description,
    #                     'asset_type':imp.asset_type,
    #                     'asset_type_id':imp.asset_type_id,
    #                     'error_list':imp.error_list,
    #                 })
    #             else:
    #                 dataAdd.append({ 
    #                     'id':imp.id, 
    #                     'mode_id':imp.mode_id, 
    #                     'mode_description':imp.mode_description,
    #                     'asset_type':imp.asset_type,
    #                     'asset_type_id':imp.asset_type_id,
    #                     'error_list':imp.error_list,
    #                 })
    #         return render(request, self.template_name, {"data":data ,"dataUpdate":dataUpdate,"dataAdd":dataAdd})




class AddImportFailuremode(View):
    template_name = 'import_failuremode.html'
    
    def post(self, request, *args, **kwargs):
        req = self.request.POST
        # ids = req.get('ids')
        user_ID = request.session['user_ID']
        P_id = request.session['P_id']
        updated=0
        inserted=0
        ids=[int(x) for x in req.get('ids', '').split(',')]
        datas= req.get('datas')
        data=json.loads(datas)
        if data !="":
            for items in data:
                Asst = []
                itemId=items['id']
                if itemId in ids:
                    itemAssetType = items['asset_type']
                    itemmode_id = items['mode_id']
                    if PBSMaster.objects.filter(asset_type=itemAssetType,is_active=0).exists():
                        Project = PBSMaster.objects.filter(asset_type=itemAssetType,is_active=0)
                        pj_id = Project[0].project_id
                        Asst.append(Project[0].id)
                    else:
                        pj_id = P_id
                        Asst = Asst
                        
                    if FailureMode.objects.filter(mode_id=itemmode_id).exists():
                        FailureMode.objects.filter(mode_id=itemmode_id).update(is_active=0,P_id=pj_id,asset_type=Asst,mode_description=items['mode_description'])
                        updated+=1
                    else:
                        u = FailureMode(mode_id=itemmode_id,P_id=pj_id,asset_type=Asst,mode_description=items['mode_description'])
                        u.save()
                        inserted+=1
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Insert "+str(inserted)+" record and Update "+str(updated)+" record to failure mode"
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Import Failure Mode Identification")
        h.save()
        return JsonResponse({'status':'1','inserted': inserted,'updated': updated})
    
    
    
    
    
   
    # def post(self, request, *args, **kwargs):
    #     req = self.request.POST
    #     user_ID = request.session['user_ID']

    #     # ids = req.get('ids')
    #     ids=[int(x) for x in req.get('ids', '').split(',')]
    #     if ids=='':
    #         temp_table_failure_mode.objects.filter(updated_by=user_ID).delete()
    #         return JsonResponse({'status':'1','inserted': 0,'updated': 0})

    #     else:

    #         imported_data = temp_table_failure_mode.objects.filter(id__in=ids)
    #         failure_mode = FailureMode.objects.filter()

    #         failure_mode_array=[]
    #         for fm in failure_mode:
    #             failure_mode_array.append(fm.mode_id)
            
    #         updated=0
    #         inserted=0
    #         for imp in imported_data:
    #             if imp.mode_id in failure_mode_array:
    #                 updated+=1
    #                 GetId=FailureMode.objects.filter(mode_id=imp.mode_id)
    #                 id=GetId[0].id
    #                 FailureMode.objects.filter(id=id).update(mode_id=imp.mode_id, mode_description=imp.mode_description,asset_type=imp.asset_type_id,P_id=imp.P_id)
                
    #             else:
    #                 inserted+=1
    #                 u = FailureMode(mode_id=imp.mode_id, mode_description=imp.mode_description,asset_type=imp.asset_type_id,P_id=imp.P_id)
    #                 u.save()
    #         temp_table_failure_mode.objects.filter(updated_by=user_ID).delete()
    #         P_id = request.session['P_id']
    #         user_ID = request.session['user_ID']
    #         FindUser = UserProfile.objects.filter(user_id=user_ID)
    #         now = datetime.datetime.now()
    #         current_time = now.strftime("%H:%M:%S")
    #         meg ="Insert "+str(inserted)+" record and Update "+str(updated)+" record to failure mode"
    #         h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg)
    #         h.save()
    #         return JsonResponse({'status':'1','inserted': inserted,'updated': updated})
    
    
class DeleteAllAsset(View):
    template_name = 'asset_register.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        ASST_CONF_IDS = ''
        # print(req)
        ids=[int(x) for x in req.get('ids', '').split(',')]
        for id in ids:
            Asset.objects.filter(id=id).update(is_active=1)
            FindDelete = Asset.objects.filter(id=id)
            FailureData.objects.filter(asset_config_id=FindDelete[0].asset_config_id).update(is_active=1)
            if ASST_CONF_IDS == '':
                ASST_CONF_IDS = FindDelete[0].asset_config_id
            else:
                ASST_CONF_IDS = ASST_CONF_IDS +', '+ FindDelete[0].asset_config_id
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete assets "
        # ASST_CONF_IDS
        meg ="ID: "+str(ids) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Asset Register")
        h.save()
        return JsonResponse({'status':'1'})
    
class DeleteAllFailureData(View):
    template_name = 'failuredata.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        FAILURE_ID = ''
        # print(req)
        ids=[int(x) for x in req.get('ids', '').split(',')]
        for id in ids:
            FailureData.objects.filter(id=id).update(is_active=1)
            FindDelete = FailureData.objects.filter(id=id)
            if FAILURE_ID == '':
                FAILURE_ID = FindDelete[0].failure_id
            else:
                FAILURE_ID = FAILURE_ID +', '+ FindDelete[0].failure_id
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete failuredatas "
        # FAILURE_ID
        meg ="ID: "+str(ids) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Data Collection")
        h.save()
        return JsonResponse({'status':'1'})
    
class DeleteAllFailuremode(View):
    template_name = 'failuremode.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        FAILURE_MODE = ''
        # print(req)
        ids=[int(x) for x in req.get('ids', '').split(',')]
        for id in ids:
            FailureMode.objects.filter(id=id).update(is_active=1)
            FailureData.objects.filter(mode_id_id=id).update(mode_id_id='')
            FindDelete = FailureMode.objects.filter(id=id)
            if FAILURE_MODE == '':
                FAILURE_MODE = FindDelete[0].mode_id
            else:
                FAILURE_MODE = FAILURE_MODE +', '+ FindDelete[0].mode_id
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete failure modes "
        # FAILURE_MODE
        meg ="ID: "+str(ids) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Failure Mode Identification")
        h.save()
        return JsonResponse({'status':'1'})   
    
class DeleteAllDefectsView(View):
    template_name = 'defect.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        # print(req)
        DEFECT_ID = ''
        ids=[int(x) for x in req.get('ids', '').split(',')]
        for id in ids:
            Defect.objects.filter(defect_id=id).update(is_active=1)
            FailureData.objects.filter(defect_id=id).update(defect_id='')
            if DEFECT_ID == '':
                DEFECT_ID = str(id)
            else:
                DEFECT_ID = DEFECT_ID +', '+ str(id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete defects "
        # DEFECT_ID
        meg ="DEFECT ID: "+str(ids) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="FRACAS Defect Identification")
        h.save()
        return JsonResponse({'status':'1'}) 
    
class DeleteAllRootcauseView(View):
    template_name = 'defect.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        # print(req)
        ROOTCAUSEID = ''
        ids=[int(x) for x in req.get('ids', '').split(',')]
        for id in ids:
            RootCause.objects.filter(root_cause_id=id).update(is_active=1)
            if ROOTCAUSEID == '':
                ROOTCAUSEID = str(id)
            else:
                ROOTCAUSEID = ROOTCAUSEID +', '+ str(id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete rootcause "
        # ROOTCAUSEID
        meg ="ID: "+str(ids) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
        h.save()
        return JsonResponse({'status':'1'})  
    
class DeleteAllReviewBoardView(View):
    template_name = 'reviewboard.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        MEET =''
        # print(req)
        ids=[int(x) for x in req.get('ids', '').split(',')]
        for id in ids:
            ReviewBoard.objects.filter(id=id).update(is_active=1)
            FindDelete = ReviewBoard.objects.filter(id=id)
            if MEET == '':
                MEET = FindDelete[0].meeting_id
            else:
                MEET = MEET +', '+ FindDelete[0].meeting_id
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete review board"
        # MEET
        meg ="ID: "+str(ids) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="FRACAS Review Board")
        h.save()
        return JsonResponse({'status':'1'}) 
    
class DeleteReviewBoardView(View):
    template_name = 'reviewboard.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        # print(req)
        id = req.get('id')
        ReviewBoard.objects.filter(id=id).update(is_active=1)
        FindDelete = ReviewBoard.objects.filter(id=id)
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Delete review board"
        # FindDelete[0].meeting_id
        meg ="ID: "+str(id) +"=> "+meg
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="FRACAS Review Board")
        h.save()
        return JsonResponse({'status':'1'}) 


class GETdefect(View):
    
    def get(self, request, *args, **kwargs):
        data = []
        req = request.GET
        asset_type = req.get('asset_type')
        defect = Defect.objects.filter(asset_type=asset_type,is_active=0)
        for k in defect:
            data.append(
                {'defect_id':k.defect_id,
                 'defect_description':k.defect_description,
                 },
              
                        )
        # response = {'data' : data}
        return JsonResponse(data, safe=False)
    
class CheckCorrectivedata(View):
    
    def post(self, request, *args, **kwargs):
        req = request.POST
        defect = req.get('defect')
        CAid = req.get('CAid')
        corrective_action_description = req.get('corrective_action_description')
        defect = Defect.objects.filter(defect_id=defect,is_active=0)
        if CAid != '':
            if CorrectiveAction.objects.filter(P_id=defect[0].P_id,corrective_action_description=corrective_action_description).exclude(corrective_action_id=CAid).exists():   
                return JsonResponse({'status':'1'})
            else:
                return JsonResponse({'status':'0'})
        else:
            if CorrectiveAction.objects.filter(P_id=defect[0].P_id,corrective_action_description=corrective_action_description).exists():   
                return JsonResponse({'status':'1'})
            else:
                return JsonResponse({'status':'0'})
            
 