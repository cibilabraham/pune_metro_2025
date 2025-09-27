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
import sys
import random

from django.utils import timezone
from datetime import timedelta

import re

class assetRegister(View):
    template_name = 'asset_register.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            asset_type = PBSMaster.objects.filter(is_active=0).order_by('asset_type') 


            # location_id = Asset.objects.filter(is_active=0).distinct('location_id')
            # asset_serial_number = Asset.objects.filter(is_active=0).distinct('asset_serial_number')
            
            # asset_description = Asset.objects.filter(is_active=0).distinct('asset_description')
            # software_version = Asset.objects.filter(is_active=0).distinct('software_version')
            # software_description = Asset.objects.filter(is_active=0).distinct('software_description')
            # asset_status = Asset.objects.filter(is_active=0).distinct('asset_status')
        else:
            asset_type = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type') 

            # location_id = Asset.objects.filter(is_active=0,P_id=P_id).distinct('location_id')
            # asset_serial_number = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_serial_number')
            # asset_description = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_description')
            # software_version = Asset.objects.filter(is_active=0,P_id=P_id).distinct('software_version')
            # software_description = Asset.objects.filter(is_active=0,P_id=P_id).distinct('software_description')
            # asset_status = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_status')

        location_id = []
        asset_serial_number = []
        software_version = []
        software_description = []
        asset_status = []
        asset_description = []
            
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
        sel_car = req.get('sel_car')
        
        Asset_data =Asset.objects.filter(is_active=0)
        print(Asset_data)

        if location_id != "all":
            Asset_data=Asset_data.filter(location_id=location_id)
        if asset_serial_number != "all":
            Asset_data=Asset_data.filter(asset_config_id=asset_serial_number)
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
        if sel_car != "all":
            Asset_data=Asset_data.filter(sub_location=sel_car)
    
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
                            'sub_location':Assets.sub_location,
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
                                'sub_location':Assets.sub_location,
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
            'sub_location' : '',
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
                    'sub_location' : Asset_data.sub_location,
                    'asset_status':Asset_data.asset_status,
                    'id':id,
                }
            #print(data)
        if user_Role == 1:
            asset_types = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
        else:
            asset_types = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type')

        train_set_options = [f"TS#{i:02d}" for i in range(1, 35)]  # 01 to 34

        return render(request, self.template_name,{'data':data,'asset_types':asset_types,'train_set_options':train_set_options})

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
        sub_location = req.get('sub_location')
        Action = req.get('Action')
        ids = req.get('id')

        if ids =="":
            if Asset.objects.filter(asset_config_id=asset_config_id,is_active=1).exists():
                print('rec deleted')
                dltRec = Asset.objects.filter(asset_config_id=asset_config_id,is_active=1)
                ids = dltRec[0].id
                Asset.objects.filter(id=ids).update(is_active=0)



        DATA = []
        HEAD = ["asset_config_id",'asset_serial_number','location_id','location_description','asset_type','software_version','asset_description','software_description','asset_status','sub_location']
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
                    r=Asset(P_id=Find_Pid.project_id,asset_config_id=asset_config_id,location_id=location_id,location_description=location_description,asset_serial_number=asset_serial_number,asset_type=Find_Pid.id,asset_description=asset_description,software_version=software_version,software_description=software_description,asset_status=asset_status,sub_location=sub_location)
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

            if Asset.objects.filter(asset_config_id=asset_config_id, is_active=0).exclude(id=ids).exists():
                return JsonResponse({'status':'0'})


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
                        Asset.objects.filter(id=ids).update(P_id=Find_Pid.project_id,location_id=location_id,location_description=location_description,asset_serial_number=asset_serial_number,asset_type=Find_Pid.id,asset_description=asset_description,software_version=software_version,software_description=software_description,asset_status=asset_status,sub_location=sub_location)
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg = "ID: " + str(ids) + " => " + meg
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
                        Asset.objects.filter(id=ids).update(P_id=Find_Pid.project_id,asset_config_id=asset_config_id,location_id=location_id,location_description=location_description,asset_serial_number=asset_serial_number,asset_type=Find_Pid.id,asset_description=asset_description,software_version=software_version,software_description=software_description,asset_status=asset_status,sub_location=sub_location)
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
        incident = req.get('incident')
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
        if incident != "all":
            FailureData_data=FailureData_data.filter(incident=incident)
    
        # Asset_data = Asset.objects.all()
        for FailureDatas in FailureData_data:
            if PBSMaster.objects.filter(id=FailureDatas.asset_type,is_active=0).exists():
                PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas.asset_type)
                for PBSMaster_data in PBSMaster_datas:
                    if FailureMode.objects.filter(id=FailureDatas.mode_id_id,is_active=0).exists():
                        FailureModes = FailureMode.objects.filter(id=FailureDatas.mode_id_id)
                        for FailureMode_id in FailureModes:

                            ast_data = Asset.objects.filter(id=FailureDatas.location_id)


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

                                 'location_id' : ast_data[0].location_id,
                                    'kilometre_reading' : FailureDatas.kilometre_reading,
                                    'sel_car' : FailureDatas.sel_car,
                                    'equipment' : FailureDatas.equipment,
                                    'location' : FailureDatas.location,
                                    'direction':FailureDatas.direction,
                                    'incident' : FailureDatas.incident,
                                    'no_of_trip_cancel' : FailureDatas.no_of_trip_cancel,
                                    'department' : FailureDatas.department,
                                    'deboarding' : FailureDatas.deboarding,
                                    'reported_to_PPIO' : FailureDatas.reported_to_PPIO,
                                    'TO_name':FailureDatas.TO_name,


                                'revenue_service_delay':FailureDatas.revenue_service_delay,
                                'affecting_failures' : FailureDatas.affecting_failures,
                                'dept_location' : FailureDatas.dept_location,
                                'failure_category' : FailureDatas.failure_category,

                                'system' : PBSMaster_data.system,
                                'subsystem' : PBSMaster_data.subsystem,



                            })  
                    else:
                        ast_data = Asset.objects.filter(id=FailureDatas.location_id)
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

                            'location_id' : ast_data[0].location_id,
                                    'kilometre_reading' : FailureDatas.kilometre_reading,
                                    'sel_car' : FailureDatas.sel_car,
                                    'equipment' : FailureDatas.equipment,
                                    'location' : FailureDatas.location,
                                    'direction':FailureDatas.direction,
                                    'incident' : FailureDatas.incident,
                                    'no_of_trip_cancel' : FailureDatas.no_of_trip_cancel,
                                    'department' : FailureDatas.department,
                                    'deboarding' : FailureDatas.deboarding,
                                    'reported_to_PPIO' : FailureDatas.reported_to_PPIO,
                                    'TO_name':FailureDatas.TO_name,

                                'revenue_service_delay':FailureDatas.revenue_service_delay,
                                'affecting_failures' : FailureDatas.affecting_failures,
                                'dept_location' : FailureDatas.dept_location,
                                'failure_category' : FailureDatas.failure_category,
                                'system' : PBSMaster_data.system,
                                'subsystem' : PBSMaster_data.subsystem,


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


class SystemLocationId(View):
    template_name = 'add_failuredata.html'

    def get(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        req = request.GET
        data=[]
        asset_config_id = req.get('asset_config_id')
        if asset_config_id == "":
            return JsonResponse(data, safe=False)
        if user_Role == 1:
            # print(asset_config_id)
            location_id = Asset.objects.filter(is_active=0,id=asset_config_id).distinct('location_id')
        else:
            location_id = Asset.objects.filter(is_active=0,id=asset_config_id).distinct('location_id')
        for k in location_id:
            data.append({'location_id':k.location_id,
                         'id':k.id})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)
        # return render(request, self.template_name, {'sub_systems' : sub_systems, 'systems':systems})

class KmSystemLocationId(View):
    template_name = 'add_failuredata.html'

    def get(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        req = request.GET
        data=[]

        location_id = req.get('location_id')
        
        if location_id == "":
            return JsonResponse(data, safe=False)
        else:
            date = datetime.datetime.strptime(req.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            assetDt = Asset.objects.filter(id=location_id)
            print(assetDt[0].location_id)
            TrainSetNo = assetDt[0].location_id
            cleaned = TrainSetNo.replace('#', '').lower()
            header_name = f"{cleaned}_tkm"

            print(header_name)

            kilometre_reading = KilometreReading.objects.filter(date=date)
            if kilometre_reading:
                value = getattr(kilometre_reading[0], header_name, None)
                print(f"{header_name}: {value}")
                data.append({'value':value})

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


        jobcard_latest_id = 0
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month

        if FailureDataIDs.objects.filter(year=current_year,month=current_month).exists():
            JOBID = FailureDataIDs.objects.filter(year=current_year,month=current_month)
            jobcard_latest_id = JOBID[0].last_id

        new_job_id = int(jobcard_latest_id) + 1

        failure_unique_id = f"RST/{current_month:02}-{current_year}/FID_{new_job_id:04}"

        current_time = datetime.datetime.now().strftime("%H:%M")
        today_date = date.today()
       

        if id==None:
            data={ 
            'asset_type' : '',
            'failure_id' : failure_unique_id,
            'asset_config_id' : '',
            'event_description' : '',
            'mode_id' : '',
            'mode_description' : '',
            'date' : date.today(),
            'time' : current_time,
            'detection':'',
            'service_delay' : 0,
            'immediate_investigation' : '',
            'failure_type' : '',
            'safety_failure' : '',
            'hazard_id' : '',
            'cm_description' : '',
            'replaced_asset_config_id':'',
            'id':'',
            'cm_start_date' : datetime.datetime.now().strftime('%Y-%m-%d'),
            'cm_start_time' : datetime.datetime.now().strftime("%H:%M"),
            'cm_end_date' : datetime.datetime.now().strftime('%Y-%m-%d'),
            'cm_end_time' : datetime.datetime.now().strftime("%H:%M"),
            'oem_failure_reference' : '',
            'defect':'',

            'location_id' : '',
            'kilometre_reading' : '',
            'sel_car' : '',
            'equipment' : '',
            'location' : '',
            'direction':'',
            'incident' : '',
            'no_of_trip_cancel' : '',
            'department' : '',
            'deboarding' : '',
            'reported_to_PPIO' : '',
            'TO_name':'',

            'revenue_service_delay':'',
            'affecting_failures' : '',
            'dept_location' : '',
            'failure_category' : '',


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


                'location_id' : datas.location_id,
                'kilometre_reading' : datas.kilometre_reading,
                'sel_car' : datas.sel_car,
                'equipment' : datas.equipment,
                'location' : datas.location,
                'direction': datas.direction,
                'incident' : datas.incident,
                'no_of_trip_cancel' : datas.no_of_trip_cancel,
                'department' : datas.department,
                'deboarding' : datas.deboarding,
                'reported_to_PPIO' : datas.reported_to_PPIO,
                'TO_name': datas.TO_name,

                'revenue_service_delay':datas.revenue_service_delay,
                'affecting_failures' : datas.affecting_failures,
                'dept_location' : datas.dept_location,
                'failure_category' : datas.failure_category,



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

        units = PBSUnit.objects.all()
        criteria_delay_for_saf = units[0].criteria_delay_for_saf

        return render(request, self.template_name,{'data':data,'defect':defect,'asset_type':asset_types
                                                   ,'asset_config_id':asset_config_id,'mode_id':mode_id,'criteria_delay_for_saf':criteria_delay_for_saf})

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

        ids = req.get('id')

        if ids =="":
            cm_start_date = datetime.datetime.now().strftime('%Y-%m-%d')
            cm_start_time = datetime.datetime.now().strftime("%H:%M")
            cm_end_date = datetime.datetime.now().strftime('%Y-%m-%d')
            cm_end_time = datetime.datetime.now().strftime("%H:%M")
            service_delay = 0
            cm_description = ''

        else:

            fdt = FailureData.objects.filter(id=ids)
            cm_start_date = fdt[0].cm_start_date
            cm_start_time = fdt[0].cm_start_time
            cm_end_date = fdt[0].cm_end_date
            cm_end_time = fdt[0].cm_end_time
            service_delay = fdt[0].service_delay
            cm_description = fdt[0].cm_description


        oem_failure_reference = req.get('oem_failure_reference')
        defect = req.get('defect')
        if defect == "":
            defect = None
        Action = req.get('Action')
        
        ACID = Asset.objects.filter(id=asset_config_ids)
        asset_config_id = ACID[0].asset_config_id


        location_id = req.get('location_id')
        kilometre_reading = req.get('kilometre_reading')
        sel_car = req.get('sel_car')
        equipment = req.get('equipment')
        location = req.get('location')
        direction = req.get('direction')
        incident = req.get('incident')
        no_of_trip_cancel = req.get('no_of_trip_cancel')
        department = req.get('department')
        deboarding = req.get('deboarding')
        reported_to_PPIO = req.get('reported_to_PPIO')
        TO_name = req.get('TO_name')

        revenue_service_delay = req.get('revenue_service_delay')
        affecting_failures = req.get('affecting_failures')

        dept_location = req.get('dept_location')
        failure_category = req.get('failure_category')

        if revenue_service_delay == 0 or revenue_service_delay == "" or revenue_service_delay == None:
            revenue_service_delay = 0
            service_delay = 0
        else:
            service_delay = revenue_service_delay


        DATA = []
        HEAD = ["asset_type",'failure_id','asset_config_id_id','event_description','mode_id_id','date','time','detection','immediate_investigation','failure_type','safety_failure','hazard_id','cm_description','replaced_asset_config_id','cm_start_date','cm_start_time','cm_end_date','cm_end_time','oem_failure_reference','defect_id','location_id','kilometre_reading','equipment','location','direction','incident','no_of_trip_cancel','department','deboarding']
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
                    'value':cm_start_date
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
                    
                    r=FailureData(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=mode_id,defect_id=defect,asset_type=asset_type,failure_id=failure_id,event_description=event_description,date=date,time=time,detection=detection,immediate_investigation=immediate_investigation,failure_type=failure_type,safety_failure=safety_failure,hazard_id=hazard_id,cm_description=cm_description,replaced_asset_config_id=replaced_asset_config_id,cm_start_date=cm_start_date,cm_start_time=cm_start_time,cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=oem_failure_reference,location_id=location_id,kilometre_reading=kilometre_reading,sel_car=sel_car,equipment=equipment,location=location,direction=direction,incident=incident,no_of_trip_cancel=no_of_trip_cancel,department=department,deboarding=deboarding,reported_to_PPIO=reported_to_PPIO,TO_name=TO_name,affecting_failures=affecting_failures,revenue_service_delay=revenue_service_delay,dept_location=dept_location,failure_category=failure_category,service_delay=service_delay)
                    r.save()

                    jobcard_latest_id = 0
                    current_year = datetime.datetime.now().year
                    current_month = datetime.datetime.now().month

                    if JobCardIDs.objects.filter(year=current_year,month=current_month).exists():
                        JOBID = JobCardIDs.objects.filter(year=current_year,month=current_month)
                        jobcard_latest_id = JOBID[0].last_id

                    new_job_id = int(jobcard_latest_id) + 1

                    job_card_no = f"RST/{current_month:02}-{current_year}/{new_job_id:04}"

                    j = JobCard(job_card_no=job_card_no,failure_id=r,train_set_no=location_id,date=date,time=time,department=department,equipment=equipment)
                    j.save()

                    print('----here------')

                    if JobCardIDs.objects.filter(year=current_year,month=current_month).exists():
                        print('----update------')
                        JobCardIDs.objects.filter(year=current_year,month=current_month).update(last_id=new_job_id)
                    else:
                        print('----add------')
                        ju = JobCardIDs(year=current_year,month=current_month,last_id=new_job_id)
                        ju.save()


                    f_latest_id = 0
                 
                    if FailureDataIDs.objects.filter(year=current_year,month=current_month).exists():
                        JOBID = FailureDataIDs.objects.filter(year=current_year,month=current_month)
                        f_latest_id = JOBID[0].last_id

                    new_f_id = int(f_latest_id) + 1

                    if FailureDataIDs.objects.filter(year=current_year,month=current_month).exists():
                        FailureDataIDs.objects.filter(year=current_year,month=current_month).update(last_id=new_f_id)
                    else:
                        ju = FailureDataIDs(year=current_year,month=current_month,last_id=new_f_id)
                        ju.save()

                    if incident == 'Yes':

                        eir_latest_id = 0
                 
                        if EIRIDs.objects.filter(year=current_year).exists():
                            JOBID = EIRIDs.objects.filter(year=current_year)
                            eir_latest_id = JOBID[0].last_id

                        new_eir_id = int(eir_latest_id) + 1

                        eir_card_no = f"Maha Metro/RS/{current_year}/{new_eir_id:04}"

                        e = EIRGeneration(eir_gen_id=eir_card_no,failure_id=r)
                        e.save()

                        if EIRIDs.objects.filter(year=current_year).exists():
                            print('----update------')
                            EIRIDs.objects.filter(year=current_year).update(last_id=new_eir_id)
                        else:
                            print('----add------')
                            ju = EIRIDs(year=current_year,last_id=new_eir_id)
                            ju.save()


                        print('crate EIR')


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
                        FailureData.objects.filter(id=ids).update(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=mode_id,defect_id=defect,asset_type=asset_type,event_description=event_description,date=date,time=time,detection=detection,immediate_investigation=immediate_investigation,failure_type=failure_type,safety_failure=safety_failure,hazard_id=hazard_id,cm_description=cm_description,replaced_asset_config_id=replaced_asset_config_id,cm_start_date=cm_start_date,cm_start_time=cm_start_time,cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=oem_failure_reference,location_id=location_id,kilometre_reading=kilometre_reading,sel_car=sel_car,equipment=equipment,location=location,direction=direction,incident=incident,no_of_trip_cancel=no_of_trip_cancel,department=department,deboarding=deboarding,reported_to_PPIO=reported_to_PPIO,TO_name=TO_name,affecting_failures=affecting_failures,revenue_service_delay=revenue_service_delay,dept_location=dept_location,failure_category=failure_category,service_delay=service_delay)
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
                    FailureData.objects.filter(id=ids).update(P_id=Find_Pid.project_id,asset_config_id_id=asset_config_id,mode_id_id=mode_id,defect_id=defect,asset_type=asset_type,failure_id=failure_id,event_description=event_description,date=date,time=time,detection=detection,immediate_investigation=immediate_investigation,failure_type=failure_type,safety_failure=safety_failure,hazard_id=hazard_id,cm_description=cm_description,replaced_asset_config_id=replaced_asset_config_id,cm_start_date=cm_start_date,cm_start_time=cm_start_time,cm_end_date=cm_end_date,cm_end_time=cm_end_time,oem_failure_reference=oem_failure_reference,location_id=location_id,kilometre_reading=kilometre_reading,sel_car=sel_car,equipment=equipment,location=location,direction=direction,incident=incident,no_of_trip_cancel=no_of_trip_cancel,department=department,deboarding=deboarding,reported_to_PPIO=reported_to_PPIO,TO_name=TO_name,affecting_failures=affecting_failures,revenue_service_delay=revenue_service_delay,dept_location=dept_location,failure_category=failure_category,service_delay=service_delay)
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
                        'systemic_cause' : RootCauses.systemic_cause,
                        'organistaional_management_cause' : RootCauses.organistaional_management_cause,
                        'material_is_damaged' : RootCauses.material_is_damaged,
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
        if defect != "" and defect != "all":
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
            'systemic_cause':'',
            'organistaional_management_cause':'',
            'material_is_damaged':'',
            'assembly_no':'',
            'failure_detection':'',
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
                    'systemic_cause':a.systemic_cause,
                    'organistaional_management_cause':a.organistaional_management_cause,
                    'material_is_damaged':a.material_is_damaged,
                    'assembly_no':a.assembly_no,
                    'failure_detection':a.failure_detection,
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
        print(user_ID)
        user_data = UserProfile.objects.filter(user_id=user_ID)
        usr = f"{user_data[0].first_name} {user_data[0].last_name}"
        print(usr)

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

        systemic_cause = req.get('systemic_cause')
        organistaional_management_cause = req.get('organistaional_management_cause')
        material_is_damaged = req.get('material_is_damaged')
        assembly_no = req.get('assembly_no')
        failure_detection = req.get('failure_detection')

        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month

        Faolure_count = 0
        if asset_type == "" or defect == "all":
            Faolure_count = 0
        else:

            if user_Role == 1:
                FailureData_data =FailureData.objects.filter(is_active=0)
            else:
                FailureData_data =FailureData.objects.filter(is_active=0,P_id=P_id)

            if asset_type != "":
                FailureData_data=FailureData_data.filter(asset_type=asset_type)
            if defect != "" and defect != "all":
                FailureData_data=FailureData_data.filter(defect_id=defect)
            for FailureDatas in FailureData_data:
                if PBSMaster.objects.filter(id=FailureDatas.asset_type,is_active=0).exists():
                    Faolure_count = Faolure_count + 1


        DATA = []
        HEAD = ["asset_type",'defect_id','rca_workshop_date','root_cause_status','immediate_cause','leading_reasons','root_cause_description','systemic_cause','organistaional_management_cause','material_is_damaged','assembly_no','failure_detection']
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
                        r=RootCause(P_id=Find_Pid.project_id,asset_type=asset_type,defect_id=defect,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status,systemic_cause=systemic_cause,organistaional_management_cause=organistaional_management_cause,material_is_damaged=material_is_damaged,assembly_no=assembly_no,failure_detection=failure_detection)
                        r.save()
                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="Add new rootcause "
                        meg ="ID: "+str(r.root_cause_id) +"=> "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
                        h.save()

                        if Faolure_count > 1 and material_is_damaged == 'Yes':
                            print('create')

                            ncr_latest_id = 0
                 
                            if NCRIDs.objects.filter(year=current_year).exists():
                                NCRID = NCRIDs.objects.filter(year=current_year)
                                ncr_latest_id = NCRID[0].last_id

                            new_ncr_id = int(ncr_latest_id) + 1

                            ncr_rec_no = f"TWLPune-RS-{failure_detection}-NCR-{current_year}/{new_ncr_id:03}"

                            today_date = datetime.datetime.today().strftime('%Y-%m-%d')
                            current_time = datetime.datetime.now().strftime('%H:%M:%S')

                            e = NCRGeneration(ncr_gen_id=ncr_rec_no,rootcause_id=r,date=today_date,time=current_time,assembly_no=assembly_no,inspector_name=usr)
                            e.save()

                            if NCRIDs.objects.filter(year=current_year).exists():
                                print('----update------')
                                NCRIDs.objects.filter(year=current_year).update(last_id=new_ncr_id)
                            else:
                                print('----add------')
                                ju = NCRIDs(year=current_year,last_id=new_ncr_id)
                                ju.save()

                        return JsonResponse({'status':'1','id':r.root_cause_id})
            else:
                if RootCause.objects.filter(defect_id=defect,is_active=0).exists():
                    if RootCause.objects.filter(defect_id=defect,root_cause_id=ids,is_active=0).exists():
                        Find_Pids =PBSMaster.objects.filter(id=asset_type)
                        for Find_Pid in Find_Pids:
                            RootCause.objects.filter(root_cause_id=ids).update(P_id=Find_Pid.project_id,asset_type=asset_type,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status,systemic_cause=systemic_cause,organistaional_management_cause=organistaional_management_cause,material_is_damaged=material_is_damaged,assembly_no=assembly_no,failure_detection=failure_detection)
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
                        RootCause.objects.filter(root_cause_id=ids).update(P_id=Find_Pid.project_id,asset_type=asset_type,defect_id=defect,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status,systemic_cause=systemic_cause,organistaional_management_cause=organistaional_management_cause,material_is_damaged=material_is_damaged,assembly_no=assembly_no,failure_detection=failure_detection)
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
                        r=RootCause(P_id=Find_Pid.project_id,asset_type=asset_type,defect_id=defect,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status,systemic_cause=systemic_cause,organistaional_management_cause=organistaional_management_cause,material_is_damaged=material_is_damaged,assembly_no=assembly_no,failure_detection=failure_detection)
                        r.save()


                        if Faolure_count > 1 and material_is_damaged == 'Yes':
                            print('create')

                            ncr_latest_id = 0
                 
                            if NCRIDs.objects.filter(year=current_year).exists():
                                NCRID = NCRIDs.objects.filter(year=current_year)
                                ncr_latest_id = NCRID[0].last_id

                            new_ncr_id = int(ncr_latest_id) + 1

                            ncr_rec_no = f"TWLPune-RS-{failure_detection}-NCR-{current_year}/{new_ncr_id:03}"

                            today_date = datetime.datetime.today().strftime('%Y-%m-%d')
                            current_time = datetime.datetime.now().strftime('%H:%M:%S')

                            e = NCRGeneration(ncr_gen_id=ncr_rec_no,rootcause_id=r,date=today_date,time=current_time,assembly_no=assembly_no,inspector_name=usr)
                            e.save()

                            if NCRIDs.objects.filter(year=current_year).exists():
                                print('----update------')
                                NCRIDs.objects.filter(year=current_year).update(last_id=new_ncr_id)
                            else:
                                print('----add------')
                                ju = NCRIDs(year=current_year,last_id=new_ncr_id)
                                ju.save()



                        FindUser = UserProfile.objects.filter(user_id=user_ID)
                        now = datetime.datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        meg ="Add new rootcause "
                        meg ="ID: "+str(r.root_cause_id) +"=> "+meg
                        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
                        h.save()
                        if data !="":
                            for items in data:
                                x= items['corrective_action_id']
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
                            RootCause.objects.filter(root_cause_id=ids).update(P_id=Find_Pid.project_id,asset_type=asset_type,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status,systemic_cause=systemic_cause,organistaional_management_cause=organistaional_management_cause,material_is_damaged=material_is_damaged,assembly_no=assembly_no,failure_detection=failure_detection)
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
                        RootCause.objects.filter(root_cause_id=ids).update(P_id=Find_Pid.project_id,asset_type=asset_type,defect_id=defect,root_cause_description=root_cause_description,leading_reasons=leading_reasons,immediate_cause=immediate_cause,rca_workshop_date=rca_workshop_date,root_cause_status=root_cause_status,systemic_cause=systemic_cause,organistaional_management_cause=organistaional_management_cause,material_is_damaged=material_is_damaged,assembly_no=assembly_no,failure_detection=failure_detection)
                        if meg !='':
                            FindUser = UserProfile.objects.filter(user_id=user_ID)
                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            meg ="ID: "+ids +"=> "+meg
                            h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Root Cause Analysis")
                            h.save()
                        if data !="":
                            for items in data:
                                x= items['corrective_action_id']
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
        if defect == "" or defect == "all":
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

                        if Asset_status1.lower() =="active":
                            Asset_status = "ACTIVE"
                        elif Asset_status1.lower() =="under maintenance":
                            Asset_status = "UNDER MAINTENANCE"
                        elif Asset_status1.lower() =="idel/standby":
                            Asset_status = "IDEL/STANDBY"
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

    def is_valid_code(self, value: str) -> bool:
        pattern = r'^[A-Z]+/(0[1-9]|1[0-2])-\d{4}/\d+$'
        return bool(re.match(pattern, value))

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

            if(A1=='Failure ID' and B1=='Depot Location' and C1=='Failure Reported Date (DD-MM-YYYY)' and D1=='Failure Reported Time (HH:MM:SS)' and E1=='Train Set No' and F1=='CAR No' and G1=='System' and H1=='Subsytem' and I1=='Equipment' and J1=='Failure Location' and K1=='Failure description' and L1=='Immediate investigation' and M1=='Failure Category' and N1=='Category of Failure' and O1=='No. of Trips Cancelled' and P1=='Deboarding' and Q1=='Revenue Service Delay (mins)' and R1=='Failure type' and S1=='Asset Name' and T1=='Asset config id' and U1=='Incident' ):
                # return render(request, self.template_name, {"message": 'required format'})
                print('------COMPLETE VALIDATION ______') 
                rowCountVar = 0
                for row in range(1, row_count):

                    rowCountVar = rowCountVar + 1
                    print('--------------------------------  '+ str(rowCountVar)) 

                    failure_id = sheet.cell_value(row,0)
                    dept_location = sheet.cell_value(row,1)
                    date= sheet.cell_value(row,2)
                    time = sheet.cell_value(row,3)

                    cell_val = sheet.cell_value(row, 4)
                    if isinstance(cell_val, str):
                        location_id = cell_val.strip()
                    else:
                        location_id = str(cell_val).strip()


                    # location_id = sheet.cell_value(row,4).strip()
                    sel_car = sheet.cell_value(row,5)
                    system = sheet.cell_value(row,6)
                    subsytem = sheet.cell_value(row,7)
                    equipment = sheet.cell_value(row,8)
                    location = sheet.cell_value(row,9)
                    event_description = sheet.cell_value(row,10)
                    immediate_investigation = sheet.cell_value(row,11)
                    category_of_failure = sheet.cell_value(row,13)

                    cell_val = sheet.cell_value(row, 12)
                    if isinstance(cell_val, str):
                        failure_category = cell_val.strip()
                    else:
                        failure_category = str(cell_val).strip()
                    # failure_category = sheet.cell_value(row,13).strip()
                    no_of_trip_cancel = sheet.cell_value(row,14)
                    deboarding = sheet.cell_value(row,15)
                    revenue_service_delay = sheet.cell_value(row,16)

                    cell_val = sheet.cell_value(row, 17)
                    if isinstance(cell_val, str):
                        failure_type = cell_val.strip()
                    else:
                        failure_type = str(cell_val).strip()

                    asset_type = sheet.cell_value(row,18)
                    asset_config_id=sheet.cell_value(row,19)
                    incident=sheet.cell_value(row,20)


                    failure_id_err = '1'
                    dept_location_err = '1'
                    date_err = '1'
                    time_err = '1'
                    location_id_err = '1'
                    sel_car_err = '1'
                    system_err = '1'
                    subsytem_err = '1'
                    equipment_err = '1'
                    location_err = '1'
                    event_description_err = '1'
                    immediate_investigation_err = '1'
                    category_of_failure_err = '1'
                    failure_category_err = '1'
                    no_of_trip_cancel_err = '1'
                    deboarding_err = '1'
                    revenue_service_delay_err = '1'
                    failure_type_err = '1'
                    asset_type_err = '1'
                    asset_config_id_err = '1'
                    incident_err = '1'

                    err_status = '1'


                    if failure_id == "":
                        failure_id_err = 'Empty'
                    elif not self.is_valid_code(failure_id):
                        failure_id_err = 'Invalid Failure ID'

                    if dept_location == "":
                        dept_location_err = 'Empty'
                    elif dept_location != "RHD" and dept_location != "HVPCD":
                        dept_location_err = 'Invalid match – only RHD and HVPCD are accepted.'

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
                                        if location_id == "": 
                                            location_id_err = 'Empty'
                                        else:
                                            if not Asset.objects.filter(asset_config_id=asset_config_id,asset_type=Project[0].id,is_active=0,location_id=location_id).exists():
                                                location_id_err = 'Invalid match'

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
                                    else:
                                        if location_id == "": 
                                            location_id_err = 'Empty'
                                        else:
                                            if not Asset.objects.filter(asset_config_id=asset_config_id,asset_type=Project[0].id,is_active=0,P_id=P_id,location_id=location_id).exists():
                                                location_id_err = 'Invalid match'

                    if sel_car.strip() == "":
                        sel_car_err = 'Empty'
                    else:
                        allowed = {"DMA", "TC", "DMB"}  # valid options
                        # split by comma, strip spaces
                        selected = [s.strip() for s in sel_car.split(",") if s.strip()]

                        # check if every selected value is valid
                        if not all(val in allowed for val in selected):
                            sel_car_err = "Invalid match – only DMA, TC, and DMB are accepted"

                    if equipment == "":
                        equipment_err = 'Empty'

                    if location == "":
                        location_err = 'Empty'

                    if event_description == "":
                        event_description_err = 'Empty'

                    if immediate_investigation == "":
                        immediate_investigation_err = 'Empty'

                    if failure_category == "":
                        failure_category_err = 'Empty'
                    elif failure_category != "SAF" and failure_category != "Non-SAF" and failure_category != "Depot Failure":
                        failure_category_err = 'Invalid match – only SAF, Non-SAF and Depot Failure are accepted.'

                    if str(no_of_trip_cancel).strip() == "":
                        no_of_trip_cancel_err = "Empty"
                    elif not isinstance(no_of_trip_cancel, int):
                        try:
                            no_of_trip_cancel = int(no_of_trip_cancel)  # try convert
                        except ValueError:
                            no_of_trip_cancel_err = "Value error"

                    if deboarding == "":
                        deboarding_err = 'Empty'
                    elif deboarding != "Yes" and deboarding != "No" :
                        deboarding_err = 'Invalid match – only Yes or No are accepted.'

                    if str(revenue_service_delay).strip() == "":
                        revenue_service_delay_err = "Empty"
                    elif not isinstance(revenue_service_delay, int):
                        try:
                            revenue_service_delay = int(revenue_service_delay)  # try convert
                        except ValueError:
                            revenue_service_delay_err = "Value error"

                    failure_types = ['Software','Hardware','Random','Other']
                    if failure_type == "":
                        failure_type_err = 'Empty'
                    else:
                        if not failure_type in failure_types :
                            failure_type_err = 'Invalid failure type'

                    if incident == "":
                        incident_err = 'Empty'
                    elif incident != "Yes" and incident != "No" :
                        incident_err = 'Invalid match – only Yes or No are accepted.'

                    if failure_id_err != '1' or dept_location_err != '1' or date_err != '1' or time_err != '1' or location_id_err != '1' or sel_car_err != '1' or system_err != '1' or subsytem_err != '1' or equipment_err != '1' or location_err != '1' or event_description_err != '1' or immediate_investigation_err != '1' or category_of_failure_err != '1' or failure_category_err != '1' or no_of_trip_cancel_err != '1' or deboarding_err != '1' or revenue_service_delay_err != '1' or failure_type_err != '1' or asset_type_err != '1' or asset_config_id_err != '1' or incident_err != '1':
                        err_status = '0'


                    data.append({
                        'id':row,
                        'err_status':err_status,
                        'failure_id': failure_id,
                        'dept_location': dept_location,
                        'date':date,
                        'time' : time,
                        'location_id' : location_id,
                        'sel_car' : sel_car,
                        'system' : system,
                        'subsytem' : subsytem,
                        'equipment' : equipment,
                        'location': location,
                        'event_description' : event_description,
                        'immediate_investigation' : immediate_investigation,
                        'category_of_failure' : category_of_failure,
                        'failure_category' : failure_category,
                        'no_of_trip_cancel': no_of_trip_cancel,
                        'deboarding' : deboarding,
                        'revenue_service_delay' : revenue_service_delay,
                        'failure_type' :failure_type,
                        'asset_type': asset_type,
                        'asset_config_id':asset_config_id,
                        'failure_id_err' : failure_id_err,
                        'dept_location_err': dept_location_err,
                        'date_err' : date_err,
                        'time_err' : time_err,
                        'location_id_err' : location_id_err,
                        'sel_car_err' : sel_car_err,
                        'system_err' : system_err,
                        'subsytem_err' : subsytem_err,
                        'equipment_err' : equipment_err,
                        'location_err': location_err,
                        'event_description_err' : event_description_err,
                        'immediate_investigation_err' : immediate_investigation_err,
                        'category_of_failure_err' : category_of_failure_err,
                        'failure_category_err' : failure_category_err,
                        'no_of_trip_cancel_err' : no_of_trip_cancel_err,
                        'deboarding_err' : deboarding_err,
                        'revenue_service_delay_err' : revenue_service_delay_err,
                        'failure_type_err' : failure_type_err,
                        'asset_type_err' : asset_type_err,
                        'asset_config_id_err' : asset_config_id_err,
                        'incident' : incident,
                        'incident_err' : incident_err

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
                failure_id = items['failure_id']
                dept_location = items['dept_location']
                itemdate1=datetime.datetime.strptime(items['date'], '%d-%m-%Y').date()
                date=datetime.datetime.strftime(itemdate1, '%Y-%m-%d')
                time = items['time']
                location_id = items['location_id']
                sel_car = items['sel_car']
                equipment = items['equipment']
                location = items['location']
                event_description = items['event_description']
                immediate_investigation = items['immediate_investigation']
                failure_category = items['failure_category']
                no_of_trip_cancel = items['no_of_trip_cancel']
                deboarding = items['deboarding']
                revenue_service_delay = items['revenue_service_delay']
                failure_type = items['failure_type']
                asset_types = items['asset_type']
                asset_config_ids = items['asset_config_id']
                incident = items['incident']

                f_data = None

                if itemId in ids:
                    Project = PBSMaster.objects.filter(asset_type=asset_types,is_active=0)

                    failure_ext_id = ""
                    if FailureData.objects.filter(failure_id=failure_id,is_active=0).exists():
                        old_failure = FailureData.objects.filter(failure_id=failure_id,is_active=0)
                        failure_ext_id = old_failure[0].id
                        f_data = old_failure[0]
                        print(f"failure ID: {failure_id} alredy exist")

                    if failure_ext_id =="":
                        cm_start_date = datetime.datetime.now().strftime('%Y-%m-%d')
                        cm_start_time = datetime.datetime.now().strftime("%H:%M")
                        cm_end_date = datetime.datetime.now().strftime('%Y-%m-%d')
                        cm_end_time = datetime.datetime.now().strftime("%H:%M")
                        service_delay = 0
                        cm_description = ''

                    else:

                        fdt = FailureData.objects.filter(id=failure_ext_id)
                        cm_start_date = fdt[0].cm_start_date
                        cm_start_time = fdt[0].cm_start_time
                        cm_end_date = fdt[0].cm_end_date
                        cm_end_time = fdt[0].cm_end_time
                        service_delay = fdt[0].service_delay
                        cm_description = fdt[0].cm_description

                    if revenue_service_delay == 0 or revenue_service_delay == "" or revenue_service_delay == None:
                        revenue_service_delay = 0
                        service_delay = 0
                    else:
                        service_delay = revenue_service_delay


                    parts = failure_id.split("/")
                    date_str = parts[1]
                    num_str = parts[2]

                    current_month, current_year = date_str.split("-")
                    last_failure_id = num_str.lstrip("0")

                    if failure_ext_id =="":
                        f_latest_id = 0
                        if FailureDataIDs.objects.filter(year=current_year,month=current_month).exists():
                            JOBID = FailureDataIDs.objects.filter(year=current_year,month=current_month)
                            f_latest_id = JOBID[0].last_id
                        # print(f_latest_id)
                        if int(f_latest_id) < int(last_failure_id):
                            # print(f'update to {last_failure_id}')
                            if FailureDataIDs.objects.filter(year=current_year,month=current_month).exists():
                                FailureDataIDs.objects.filter(year=current_year,month=current_month).update(last_id=last_failure_id)
                            else:
                                ju = FailureDataIDs(year=current_year,month=current_month,last_id=last_failure_id)
                                ju.save()

                    ACID = Asset.objects.filter(asset_config_id=asset_config_ids)
                    asset_config_id = ACID[0].asset_config_id

                    location_id = ACID[0].id

                    mode_id = None
                    defect = None
                    asset_type = ACID[0].asset_type
                    detection = None
                   

                    if failure_ext_id =="":

                        r=FailureData(P_id=Project[0].project_id,asset_config_id_id=asset_config_id,mode_id_id=mode_id,defect_id=defect,asset_type=asset_type,failure_id=failure_id,event_description=event_description,date=date,time=time,immediate_investigation=immediate_investigation,failure_type=failure_type,cm_description=cm_description,cm_start_date=cm_start_date,cm_start_time=cm_start_time,cm_end_date=cm_end_date,cm_end_time=cm_end_time,location_id=location_id,sel_car=sel_car,equipment=equipment,location=location,no_of_trip_cancel=no_of_trip_cancel,deboarding=deboarding,revenue_service_delay=revenue_service_delay,dept_location=dept_location,failure_category=failure_category,service_delay=service_delay,detection='',replaced_asset_config_id='',oem_failure_reference='',incident=incident)
                        r.save()

                        f_data = r
                        
                        inserted+=1
                    else:

                        FailureData.objects.filter(id=failure_ext_id).update(is_active=0,P_id=Project[0].project_id,asset_config_id_id=asset_config_id,mode_id_id=mode_id,defect_id=defect,asset_type=asset_type,failure_id=failure_id,event_description=event_description,date=date,time=time,immediate_investigation=immediate_investigation,failure_type=failure_type,cm_description=cm_description,cm_start_date=cm_start_date,cm_start_time=cm_start_time,cm_end_date=cm_end_date,cm_end_time=cm_end_time,location_id=location_id,sel_car=sel_car,equipment=equipment,location=location,no_of_trip_cancel=no_of_trip_cancel,deboarding=deboarding,revenue_service_delay=revenue_service_delay,dept_location=dept_location,failure_category=failure_category,service_delay=service_delay,detection='',replaced_asset_config_id='',oem_failure_reference='',incident=incident)

                        updated+=1

                    if not JobCard.objects.filter(failure_id=f_data).exists():

                        # check jobcard here
                        jobcard_latest_id = 0
                        current_year = int(current_year)
                        current_month = int(current_month)
                        
                        if JobCardIDs.objects.filter(year=current_year,month=current_month).exists():
                            JOBID = JobCardIDs.objects.filter(year=current_year,month=current_month)
                            jobcard_latest_id = JOBID[0].last_id

                        new_job_id = int(jobcard_latest_id) + 1

                        job_card_no = f"RST/{current_month:02}-{current_year}/{new_job_id:04}"
                        print(f"job_card_no: {job_card_no}")

                        print('Job card not exists')
                        j = JobCard(job_card_no=job_card_no,failure_id=f_data,train_set_no=location_id,date=date,time=time,department='Operator',equipment=equipment)
                        j.save()

                        if JobCardIDs.objects.filter(year=current_year,month=current_month).exists():
                            JobCardIDs.objects.filter(year=current_year,month=current_month).update(last_id=new_job_id)
                        else:
                            ju = JobCardIDs(year=current_year,month=current_month,last_id=new_job_id)
                            ju.save()

                    if incident == 'Yes':
                        eir_latest_id = 0
                 
                        if EIRIDs.objects.filter(year=current_year).exists():
                            JOBID = EIRIDs.objects.filter(year=current_year)
                            eir_latest_id = JOBID[0].last_id

                        new_eir_id = int(eir_latest_id) + 1

                        eir_card_no = f"Maha Metro/RS/{current_year}/{new_eir_id:04}"

                        # print(eir_card_no)
                        if not EIRGeneration.objects.filter(failure_id=f_data).exists():
                          
                            e = EIRGeneration(eir_gen_id=eir_card_no,failure_id=f_data)
                            e.save()

                            if EIRIDs.objects.filter(year=current_year).exists():
                                print('----update------')
                                EIRIDs.objects.filter(year=current_year).update(last_id=new_eir_id)
                            else:
                                print('----add------')
                                ju = EIRIDs(year=current_year,last_id=new_eir_id)
                                ju.save()


                            print('crate EIR')



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



class jobcardRegister(View):
    template_name = 'jobcard_register.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        # if user_Role == 1:
        #     location_id = Asset.objects.filter(is_active=0).distinct('location_id')
        #     asset_serial_number = Asset.objects.filter(is_active=0).distinct('asset_serial_number')
        #     asset_type = PBSMaster.objects.filter(is_active=0).order_by('asset_type') 
        #     asset_description = Asset.objects.filter(is_active=0).distinct('asset_description')
        #     software_version = Asset.objects.filter(is_active=0).distinct('software_version')
        #     software_description = Asset.objects.filter(is_active=0).distinct('software_description')
        #     asset_status = Asset.objects.filter(is_active=0).distinct('asset_status')
        # else:
        #     location_id = Asset.objects.filter(is_active=0,P_id=P_id).distinct('location_id')
        #     asset_serial_number = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_serial_number')
        #     asset_description = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_description')
        #     software_version = Asset.objects.filter(is_active=0,P_id=P_id).distinct('software_version')
        #     software_description = Asset.objects.filter(is_active=0,P_id=P_id).distinct('software_description')
        #     asset_status = Asset.objects.filter(is_active=0,P_id=P_id).distinct('asset_status')
        #     asset_type = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type') 

        train_set_options = [f"TS#{i:02d}" for i in range(1, 35)]  # 01 to 34

        return render(request, self.template_name, {'train_set_options':train_set_options})

    def post(self, request, *args, **kwargs):

        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)

        location_id_f = req.get('location_id')
        department = req.get('department')
        assigned_to = req.get('assigned_to')
        status = req.get('status')
       
        JobCardDatas = JobCard.objects.filter().order_by('-job_card_no')

        if status != "all":
            JobCardDatas=JobCardDatas.filter(status=status)

        if req.get('date') !="":
            date = datetime.datetime.strptime(req.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            JobCardDatas=JobCardDatas.filter(date=date)

        if assigned_to != "all":
            if assigned_to == 'Maintainer':
                JobCardDatas = JobCardDatas.filter(run_status__in=[3, 4, 5])
            else:
                JobCardDatas = JobCardDatas.filter(run_status__in=[0, 1, 2, 6, 7])

        if department != "all":
            JobCardDatas=JobCardDatas.filter(failure_id__department=department)




        

    
       
        for jb in JobCardDatas:
            asset_type_id = jb.failure_id.asset_type
            if PBSMaster.objects.filter(id=asset_type_id,is_active=0).exists():
                ast_data = Asset.objects.filter(id=jb.failure_id.location_id)
                if location_id_f != "all":
                    ast_data = ast_data.filter(location_id=location_id_f)

                if ast_data :

                    if user_Role == 1:
                        PBSMaster_datas=PBSMaster.objects.filter(id=asset_type_id,is_active=0)
                        for PBSMaster_data in PBSMaster_datas:

                            job_equipmentArr = JobReplacedEquipment.objects.filter(job_card_id=jb.job_id,is_active=0)
                            if job_equipmentArr:
                                for jdar in job_equipmentArr:
                                    data.append({ 
                                        'job_card_no' :  jb.job_card_no,
                                        'dept_location': jb.failure_id.dept_location,
                                        'ohe_required':jb.ohe_required,
                                        'sel_car': jb.failure_id.sel_car,
                                        'location': jb.failure_id.location,
                                        'date' : jb.failure_id.date,
                                        'time' : jb.failure_id.time,
                                        'date_issued' : jb.date,
                                        'time_issued' : jb.time,
                                        'no_of_trip_cancel' : jb.failure_id.no_of_trip_cancel,
                                        'revenue_service_delay' : jb.failure_id.revenue_service_delay,

                                        'system' : PBSMaster_data.system,
                                        'subsystem' : PBSMaster_data.subsystem,
                                        'equipment' : jb.failure_id.equipment,
                                        'event_description' : jb.failure_id.event_description,
                                        'immediate_investigation' : jb.failure_id.immediate_investigation,
                                        'kilometre_reading' : jb.failure_id.kilometre_reading,

                                        



                                        'train_set_no' : ast_data[0].location_id,
                                        
                                        'department' : jb.failure_id.department,
                                        'nature_of_job' : jb.nature_of_job,
                                        'sic_required' : jb.sic_required,
                                        'assigned_to':jb.assigned_to,
                                        'last_update' : jb.last_update,
                                        'status':jb.status,
                                        'id':jb.job_id,
                                        'user_Role':user_Role,
                                        'run_status' : jb.run_status,
                                        'cm_start_date':jb.l2_date,
                                        'cm_start_time':jb.l2_time,
                                        'cm_end_date':jb.completion_date,
                                        'cm_end_time':jb.completion_date_time,
                                        'service_delay':jb.down_time,
                                        'cm_description':jb.details_of_the_activitues,

                                        'jobequipment_name':jdar.jobequipment_name,
                                        'jobequipment_new_no':jdar.jobequipment_new_no,
                                        'jobequipment_old_no':jdar.jobequipment_old_no,

                                        'received_by' : jb.received_by,

                                    }) 

                            else:
                                data.append({ 
                                    'job_card_no' :  jb.job_card_no,
                                    'dept_location': jb.failure_id.dept_location,
                                    'ohe_required':jb.ohe_required,
                                    'sel_car': jb.failure_id.sel_car,
                                    'location': jb.failure_id.location,
                                    'date_issued' : jb.date,
                                    'time_issued' : jb.time,
                                    'no_of_trip_cancel' : jb.failure_id.no_of_trip_cancel,
                                    'revenue_service_delay' : jb.failure_id.revenue_service_delay,

                                    'system' : PBSMaster_data.system,
                                    'subsystem' : PBSMaster_data.subsystem,
                                    'equipment' : jb.failure_id.equipment,
                                    'event_description' : jb.failure_id.event_description,
                                    'immediate_investigation' : jb.failure_id.immediate_investigation,
                                    'kilometre_reading' : jb.failure_id.kilometre_reading,



                                    'train_set_no' : ast_data[0].location_id,
                                    'date' : jb.failure_id.date,
                                    'time' : jb.failure_id.time,
                                    'department' : jb.failure_id.department,
                                    'nature_of_job' : jb.nature_of_job,
                                    'sic_required' : jb.sic_required,
                                    'assigned_to':jb.assigned_to,
                                    'last_update' : jb.last_update,
                                    'status':jb.status,
                                    'id':jb.job_id,
                                    'user_Role':user_Role,
                                    'run_status' : jb.run_status,
                                    'cm_start_date':jb.l2_date,
                                    'cm_start_time':jb.l2_time,
                                    'cm_end_date':jb.completion_date,
                                    'cm_end_time':jb.completion_date_time,
                                    'service_delay':jb.down_time,
                                    'cm_description':jb.details_of_the_activitues,

                                    'jobequipment_name':'',
                                    'jobequipment_new_no':'',
                                    'jobequipment_old_no':'',

                                    'received_by' : jb.received_by,

                                }) 
                    else:
                        if PBSMaster.objects.filter(id=asset_type_id,project_id=P_id,is_active=0).exists():
                            PBSMaster_datas=PBSMaster.objects.filter(id=asset_type_id,is_active=0)
                            for PBSMaster_data in PBSMaster_datas:

                                job_equipmentArr = JobReplacedEquipment.objects.filter(job_card_id=jb.job_id,is_active=0)
                                if job_equipmentArr:
                                    for jdar in job_equipmentArr:
                                        data.append({ 
                                            'job_card_no' :  jb.job_card_no,
                                            'dept_location': jb.failure_id.dept_location,
                                            'ohe_required':jb.ohe_required,
                                            'sel_car': jb.failure_id.sel_car,
                                            'location': jb.failure_id.location,
                                            'date_issued' : jb.date,
                                            'time_issued' : jb.time,
                                            'no_of_trip_cancel' : jb.failure_id.no_of_trip_cancel,
                                            'revenue_service_delay' : jb.failure_id.revenue_service_delay,

                                            'system' : PBSMaster_data.system,
                                            'subsystem' : PBSMaster_data.subsystem,
                                            'equipment' : jb.failure_id.equipment,
                                            'event_description' : jb.failure_id.event_description,
                                            'immediate_investigation' : jb.failure_id.immediate_investigation,
                                            'kilometre_reading' : jb.failure_id.kilometre_reading,



                                            'train_set_no' : ast_data[0].location_id,
                                            'date' : jb.failure_id.date,
                                            'time' : jb.failure_id.time,
                                            'department' : jb.failure_id.department,
                                            'nature_of_job' : jb.nature_of_job,
                                            'sic_required' : jb.sic_required,
                                            'assigned_to':jb.assigned_to,
                                            'last_update' : jb.last_update,
                                            'status':jb.status,
                                            'id':jb.job_id,
                                            'user_Role':user_Role,
                                            'run_status' : jb.run_status,
                                            'cm_start_date':jb.l2_date,
                                            'cm_start_time':jb.l2_time,
                                            'cm_end_date':jb.completion_date,
                                            'cm_end_time':jb.completion_date_time,
                                            'service_delay':jb.down_time,
                                            'cm_description':jb.details_of_the_activitues,

                                            'jobequipment_name':jdar.jobequipment_name,
                                            'jobequipment_new_no':jdar.jobequipment_new_no,
                                            'jobequipment_old_no':jdar.jobequipment_old_no,

                                            'received_by' : jb.received_by,

                                        }) 

                                else:

                                    data.append({ 
                                        'job_card_no' :  jb.job_card_no,
                                        'dept_location': jb.failure_id.dept_location,
                                        'ohe_required':jb.ohe_required,
                                        'sel_car': jb.failure_id.sel_car,
                                        'location': jb.failure_id.location,
                                        'date_issued' : jb.date,
                                        'time_issued' : jb.time,
                                        'no_of_trip_cancel' : jb.failure_id.no_of_trip_cancel,
                                        'revenue_service_delay' : jb.failure_id.revenue_service_delay,

                                        'system' : PBSMaster_data.system,
                                        'subsystem' : PBSMaster_data.subsystem,
                                        'equipment' : jb.failure_id.equipment,
                                        'event_description' : jb.failure_id.event_description,
                                        'immediate_investigation' : jb.failure_id.immediate_investigation,
                                        'kilometre_reading' : jb.failure_id.kilometre_reading,


                                        'train_set_no' : ast_data[0].location_id,
                                        'date' : jb.failure_id.date,
                                        'time' : jb.failure_id.time,
                                        'department' : jb.failure_id.department,
                                        'nature_of_job' : jb.nature_of_job,
                                        'sic_required' : jb.sic_required,
                                        'assigned_to':jb.assigned_to,
                                        'last_update' : jb.last_update,
                                        'status':jb.status,
                                        'id':jb.job_id,
                                        'user_Role':user_Role,
                                        'run_status' : jb.run_status,
                                        'cm_start_date':jb.l2_date,
                                        'cm_start_time':jb.l2_time,
                                        'cm_end_date':jb.completion_date,
                                        'cm_end_time':jb.completion_date_time,
                                        'service_delay':jb.down_time,
                                        'cm_description':jb.details_of_the_activitues,

                                        'jobequipment_name':'',
                                        'jobequipment_new_no':'',
                                        'jobequipment_old_no':'',

                                        'received_by' : jb.received_by,

                                    }) 
        print(data)
        return JsonResponse({'data':data})

    

class AddJobcard(View):
    template_name = 'add_jobcard.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]
        JobCard_datas =JobCard.objects.filter(job_id=id)
        jb = JobCard_datas[0]
        ast_data = Asset.objects.filter(id=jb.failure_id.location_id)

        user_ID = request.session['user_ID']
        user_data = UserProfile.objects.filter(user_id=user_ID)
        logedUsrName = f"{user_data[0].first_name} {user_data[0].last_name}"
        logedUsrDesignationEMPID = f"{user_data[0].designation}/{user_data[0].emp_id}"
        print(logedUsrDesignationEMPID)

        FailureDatas=FailureData.objects.filter(id=jb.failure_id.id)
        datas = FailureDatas[0]

        PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas[0].asset_type)

        job_details = []
        job_detailsArr = JobDetails.objects.filter(job_card_id=jb.job_id,is_active=0)
        st = 0
        for jdar in job_detailsArr:
            st = st + 1
            job_details.append({ 
                'job_details_id' :  jdar.job_details_id,
                'job_description' : jdar.job_description,
                's_no' : st,
            })

        full_path = jb.signature_img
        if full_path == None:
            relative_path = None
        else:
            # Find the index of /static
            index = full_path.find("/static")
            if index != -1:
                relative_path = full_path[index + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path = relative_path.lstrip("/")
            else:
                relative_path = full_path  # fallback if /static not found

        full_path2 = jb.signature_img2
        if full_path2 == None:
            relative_path2 = None
        else:
            # Find the index of /static
            index2 = full_path2.find("/static")
            if index2 != -1:
                relative_path2 = full_path2[index2 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path2 = relative_path2.lstrip("/")
            else:
                relative_path2 = full_path2  # fallback if /static not found


        full_path3 = jb.signature_img3
        if full_path3 == None:
            relative_path3 = None
        else:
            # Find the index of /static
            index3 = full_path3.find("/static")
            if index3 != -1:
                relative_path3 = full_path3[index3 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path3 = relative_path3.lstrip("/")
            else:
                relative_path3 = full_path3  # fallback if /static not found

        full_path4 = jb.signature_img4
        if full_path4 == None:
            relative_path4 = None
        else:
            # Find the index of /static
            index4 = full_path4.find("/static")
            if index4 != -1:
                relative_path4 = full_path4[index4 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path4 = relative_path4.lstrip("/")
            else:
                relative_path4 = full_path4  # fallback if /static not found

        full_path5 = jb.signature_img5
        if full_path5 == None:
            relative_path5 = None
        else:
            # Find the index of /static
            index5 = full_path5.find("/static")
            if index5 != -1:
                relative_path5 = full_path5[index5 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path5 = relative_path5.lstrip("/")
            else:
                relative_path5 = full_path5  # fallback if /static not found

        full_path6 = jb.signature_img6
        if full_path6 == None:
            relative_path6 = None
        else:
            # Find the index of /static
            index6 = full_path6.find("/static")
            if index6 != -1:
                relative_path6 = full_path6[index6 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path6 = relative_path6.lstrip("/")
            else:
                relative_path6 = full_path6  # fallback if /static not found

        current_time = datetime.datetime.now().strftime("%H:%M")
        today_date = date.today()

        if jb.event_date == None or jb.event_date == "":
            event_date = today_date
        else:
            event_date = jb.event_date

        if jb.event_time == None or jb.event_time == "":
            event_time = current_time
        else:
            event_time = jb.event_time

        if jb.l2_date == None or jb.l2_date == "":
            l2_date = today_date
        else:
            l2_date = jb.l2_date

        if jb.l1_date == None or jb.l1_date == "":
            l1_date = today_date
        else:
            l1_date = jb.l1_date

        if jb.l2_time == None or jb.l2_time == "":
            l2_time = current_time
        else:
            l2_time = jb.l2_time

        if jb.l1_time == None or jb.l1_time == "":
            l1_time = current_time
        else:
            l1_time = jb.l1_time

        if jb.completion_date == None or jb.completion_date == "":
            completion_date = today_date
        else:
            completion_date = jb.completion_date

        if jb.sic_start_date == None or jb.sic_start_date == "":
            sic_start_date = today_date
        else:
            sic_start_date = jb.sic_start_date

        if jb.completion_date_time == None or jb.completion_date_time == "":
            completion_date_time = current_time
        else:
            completion_date_time = jb.completion_date_time

        if jb.completion_date2 == None or jb.completion_date2 == "":
            completion_date2 = today_date
        else:
            completion_date2 = jb.completion_date2

        if jb.completion_date_time2 == None or jb.completion_date_time2 == "":
            completion_date_time2 = current_time
        else:
            completion_date_time2 = jb.completion_date_time2

        if jb.close_date == None or jb.close_date == "":
            close_date = today_date
        else:
            close_date = jb.close_date

        if jb.close_time == None or jb.close_time == "":
            close_time = current_time
        else:
            close_time = jb.close_time

        if jb.issued_to == None or jb.issued_to == "":
            issued_to = ''
        else:
            issued_to = jb.issued_to

        if jb.assigned_to == None or jb.assigned_to == "":
            assigned_to = ''
        else:
            assigned_to = jb.assigned_to

        if jb.issued_by == None or jb.issued_by == "":
            issued_by = logedUsrName
        else:
            issued_by = jb.issued_by

        if jb.issued_signature == None or jb.issued_signature == "":
            issued_signature = logedUsrDesignationEMPID
        else:
            issued_signature = jb.issued_signature

        if jb.received_by == None or jb.received_by == "":
            received_by = logedUsrName
        else:
            received_by = jb.received_by


        if jb.received_by_signature == None or jb.received_by_signature == "":
            received_by_signature = logedUsrDesignationEMPID
        else:
            received_by_signature = jb.received_by_signature


        if jb.details_of_the_activitues == None or jb.details_of_the_activitues == "":
            details_of_the_activitues = ''
        else:
            details_of_the_activitues = jb.details_of_the_activitues

        if jb.follow_up_details == None or jb.follow_up_details == "":
            follow_up_details = ''
        else:
            follow_up_details = jb.follow_up_details


        if jb.new_supervisor == None or jb.new_supervisor == "":
            new_supervisor = logedUsrName
        else:
            new_supervisor = jb.new_supervisor


        if jb.new_supervisor_signature == None or jb.new_supervisor_signature == "":
            new_supervisor_signature = logedUsrDesignationEMPID
        else:
            new_supervisor_signature = jb.new_supervisor_signature


            
        if jb.completion_name == None or jb.completion_name == "":
            completion_name = logedUsrName
        else:
            completion_name = jb.completion_name


        if jb.completion_signature == None or jb.completion_signature == "":
            completion_signature = logedUsrDesignationEMPID
        else:
            completion_signature = jb.completion_signature

            
        if jb.corrective_action == None or jb.corrective_action == "":
            corrective_action = ''
        else:
            corrective_action = jb.corrective_action

            
        if jb.completion_name2 == None or jb.completion_name2 == "":
            completion_name2 = logedUsrName
        else:
            completion_name2 = jb.completion_name2


        if jb.completion_signature2 == None or jb.completion_signature2 == "":
            completion_signature2 = logedUsrDesignationEMPID
        else:
            completion_signature2 = jb.completion_signature2


        if jb.close_name == None or jb.close_name == "":
            close_name = logedUsrName
        else:
            close_name = jb.close_name


        if jb.close_name_signature == None or jb.close_name_signature == "":
            close_name_signature = logedUsrDesignationEMPID
        else:
            close_name_signature = jb.close_name_signature


        if jb.down_time2 == None or jb.down_time2 == "":
            down_time2 = jb.down_time
        else:
            down_time2 = jb.down_time2

        if jb.new_supervisor_id == None or jb.new_supervisor_id == "":
            new_supervisor_id = ""
        else:
            new_supervisor_id = int(jb.new_supervisor_id)


        data={ 
            'job_card_no' :  jb.job_card_no,
            'train_set_no' : ast_data[0].location_id,
            'date' : jb.failure_id.date,
            'time' : jb.failure_id.time,
            'department' : jb.failure_id.department,
            'nature_of_job' : jb.nature_of_job,
            'sic_required' : jb.sic_required,
            'assigned_to':assigned_to,
            'last_update' : jb.last_update,
            'status':jb.status,
            'id':jb.job_id,
            'user_Role':user_Role,
            'run_status' : jb.run_status,

        
            'asset_type' : PBSMaster_datas[0].asset_type,
            'subsystem' : PBSMaster_datas[0].subsystem,
            'failure_id' : datas.failure_id,
            'asset_config_id' : datas.asset_config_id,
            'event_description' : datas.event_description,
            'mode_id' :datas.mode_id,
            'mode_description' : datas.mode_description,
            'detection':datas.detection,
            'service_delay' : datas.service_delay,
            'immediate_investigation' : datas.immediate_investigation,
            'failure_type' : datas.failure_type,
            'safety_failure' : datas.safety_failure,
            'hazard_id' : datas.hazard_id,
            'cm_description' : datas.cm_description,
            'replaced_asset_config_id':datas.replaced_asset_config_id,
            'cm_start_date' : datas.cm_start_date,
            'cm_start_time' : datas.cm_start_time,
            'cm_end_date' : datas.cm_end_date,
            'cm_end_time' : datas.cm_end_time,
            'oem_failure_reference' : datas.oem_failure_reference,
            'defect':datas.defect,


            'location_id' : datas.location_id,
            'kilometre_reading' : datas.kilometre_reading,
            'sel_car' : datas.sel_car,
            # 'equipment' : datas.equipment,
            'location' : datas.location,
            'direction': datas.direction,
            'incident' : datas.incident,
            'no_of_trip_cancel' : datas.no_of_trip_cancel,
            'deboarding' : datas.deboarding,
            'reported_to_PPIO' : datas.reported_to_PPIO,
            'TO_name': datas.TO_name,

            'ohe_required' : jb.ohe_required,
            'issued_to' : issued_to,
            'completion_time' : jb.completion_time,
            'from_revenue_service' : jb.from_revenue_service,
            'delay_to_service' : jb.delay_to_service,
            'trip_no':jb.trip_no,
            'event_date' : event_date,
            'event_time':event_time,
            'sic_no':jb.sic_no,

            'signature_img':relative_path,
            'issued_by' : issued_by,
            'l1_time':l1_time,
            'l1_date':l1_date,

            'signature_img2':relative_path2,
            'received_by' : received_by,
            'l2_time':l2_time,
            'l2_date':l2_date,


            'signature_img3':relative_path3,
            'follow_up_details' : follow_up_details,
            'details_of_the_activitues' : details_of_the_activitues,
            'handed_over':jb.handed_over,
            'new_supervisor':new_supervisor,

            'signature_img4':relative_path4,
            'completion_date_time' : completion_date_time,
            'completion_date':completion_date,
            'train_can_be_moved':jb.train_can_be_moved,
            'down_time':jb.down_time,
            'completion_name':completion_name,
            'train_can_be_energized':jb.train_can_be_energized,

            'signature_img5':relative_path5,
            'completion_date_time2' : completion_date_time2,
            'completion_date2': completion_date2,
            'train_can_be_moved2':jb.train_can_be_moved2,
            'down_time2':down_time2,
            'completion_name2':completion_name2,
            'train_can_be_energized2':jb.train_can_be_energized2,
            'corrective_action':corrective_action,
            'sic_start_time':jb.sic_start_time,
            'sic_has_performed':jb.sic_has_performed,

            'signature_img6':relative_path6,
            'close_name' : close_name,
            'close_date':close_date,
            'close_time':close_time,

            'issued_signature':issued_signature,
            'received_by_signature':received_by_signature,
            'logedUsrName':logedUsrName,
            'new_supervisor_signature':new_supervisor_signature,
            'new_supervisor_id':new_supervisor_id,
            'completion_signature':completion_signature,
            'completion_signature2':completion_signature2,
            'close_name_signature':close_name_signature,

            'sic_start_date':sic_start_date,

            'dept_location': jb.failure_id.dept_location,
            'date_issued' : jb.date,
            'time_issued' : jb.time,


            'system' : PBSMaster_datas[0].system,
            'equipment' : jb.failure_id.equipment,
            'event_description' : jb.failure_id.event_description,
            'immediate_investigation' : jb.failure_id.immediate_investigation,

            'revenue_service_delay' : jb.failure_id.revenue_service_delay,
            'failure_location': jb.failure_id.location,
            



        }

        prv_data = []
        JobCard_prvdatas =JobCard.objects.filter(failure_id__asset_config_id__location_id=jb.failure_id.asset_config_id.location_id,failure_id__date=jb.failure_id.date).exclude(job_id=id)
        st_gen = 0
        for jbr in JobCard_prvdatas:
            st_gen = st_gen + 1
            FailureDatasprv=FailureData.objects.filter(id=jbr.failure_id.id)
            datasprv = FailureDatasprv[0]
            sts = 'Open'
            if jbr.status == 1 or jbr.status == '1':
                sts = 'Closed'

            wrk = ''
            job_detailsArrLoop = JobDetails.objects.filter(job_card_id=jbr.job_id,is_active=0)
            for jdar in job_detailsArrLoop:
                if wrk == '':
                    wrk = jdar.job_description
                else:
                    wrk = f"{wrk}, {jdar.job_description}"

            prv_data.append({ 
                'st_gen':st_gen,
                'job_card_no' :  jbr.job_card_no,
                'issued_to' : jbr.issued_to,
                'immediate_investigation' : wrk,
                'completion_time' : jbr.completion_time,
                'status':sts,
            })

        prv_data2 = []
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        print(thirty_days_ago)
        JobCard_prvdatas2 =JobCard.objects.filter(failure_id__asset_config_id__location_id=jb.failure_id.asset_config_id.location_id,failure_id__equipment=jb.failure_id.equipment,date__gte=thirty_days_ago).exclude(job_id=id)
        st_gen = 0
        for jbr in JobCard_prvdatas2:
            st_gen = st_gen + 1
            PBSMaster_datas2 =PBSMaster.objects.filter(id=jbr.failure_id.asset_type)
            if PBSMaster_datas[0].system == PBSMaster_datas2[0].system:
                prv_data2.append({ 
                    'st_gen':st_gen,
                    'job_card_no' :  jbr.job_card_no,
                    'date' :  jbr.failure_id.date,
                    'immediate_investigation' :  jbr.failure_id.immediate_investigation,
                })

        job_works = []
        job_worksArr = JobWorkToMaintainers.objects.filter(job_card_id=jb.job_id,is_active=0)
        st = 0
        for jdar in job_worksArr:
            st = st + 1
            job_works.append({ 
                'job_work_id' :  jdar.job_work_id,
                'jobwork_name' :  jdar.jobwork_name,
                'jobwork_work' :  jdar.jobwork_work,
                'jobwork_signature' : jdar.jobwork_signature,
                's_no' : st,
            })

        job_equipment = []
        job_equipmentArr = JobReplacedEquipment.objects.filter(job_card_id=jb.job_id,is_active=0)
        st = 0
        for jdar in job_equipmentArr:
            st = st + 1
            job_equipment.append({ 
                'job_equipment_id' :  jdar.job_equipment_id,
                'jobequipment_name' :  jdar.jobequipment_name,
                'jobequipment_new_no' :  jdar.jobequipment_new_no,
                'jobequipment_old_no' : jdar.jobequipment_old_no,
                's_no' : st,
            })

        supervisorList = []
        userLDt = UserProfile.objects.filter(is_active=0,is_disable=0,user_role=6)
        for sprl in userLDt:
            supervisorList.append({ 
                'id' :  int(sprl.user.id),
                'val' :  f"{sprl.first_name} {sprl.last_name} - {sprl.designation} / {sprl.emp_id}",
            })

        

        # print(prv_data)
        return render(request, self.template_name,{'data':data,'job_details':job_details,'prv_data':prv_data, 'job_works':job_works, 'job_equipment':job_equipment ,'prv_data2':prv_data2,'supervisorList':supervisorList })
      
 
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        ids = req.get('id')
        st = req.get('st')

        print(st)

        if st == 1 or st == '1':

            ohe_required = req.get('ohe_required')
            issued_to = req.get('issued_to')
            completion_time = req.get('completion_time')
            from_revenue_service = req.get('from_revenue_service')
            delay_to_service = req.get('delay_to_service')
            trip_no = req.get('trip_no')
            nature_of_job = req.get('nature_of_job')
            # event_date = datetime.datetime.strptime(req.get('event_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            # event_time = req.get('event_time')

            if from_revenue_service == 'Yes':
                JobCard.objects.filter(job_id=ids).update(ohe_required=ohe_required,issued_to=issued_to,completion_time=completion_time,from_revenue_service=from_revenue_service,delay_to_service=delay_to_service,trip_no=trip_no,nature_of_job=nature_of_job,run_status=st)
            else:
                JobCard.objects.filter(job_id=ids).update(ohe_required=ohe_required,issued_to=issued_to,completion_time=completion_time,from_revenue_service=from_revenue_service,nature_of_job=nature_of_job,run_status=st)

            return JsonResponse({'status':'1'})
        elif st == 0 or st == '0':
            JobCard.objects.filter(job_id=ids).update(run_status=st,status=0)
            return JsonResponse({'status':'1'})

        elif st == 17 or st == '17':
            JobCard.objects.filter(job_id=ids).update(run_status=1,status=0)
            return JsonResponse({'status':'1'})

        elif st == 20 or st == '20':
            JobCard.objects.filter(job_id=ids).update(run_status=4,status=0)
            return JsonResponse({'status':'1'})

        elif st == 2 or st == '2':
            sic_required = req.get('sic_required')
            assigned_to = req.get('assigned_to')
            sic_no = req.get('sic_no')
            JobCard.objects.filter(job_id=ids).update(run_status=st,sic_required=sic_required,assigned_to=assigned_to,sic_no=sic_no)
            return JsonResponse({'status':'1'})

        elif st == 3 or st == '3':
            issued_by = req.get('issued_by')
            l1_date = datetime.datetime.strptime(req.get('l1_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            l1_time = req.get('l1_time')
            issued_signature = req.get('issued_signature')

            # uploaded_file = request.FILES['signature_img']
            # static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')

            # # Create folder if it doesn't exist
            # os.makedirs(static_path, exist_ok=True)

            # # Save file
            # file_path = os.path.join(static_path, uploaded_file.name)
            # with open(file_path, 'wb+') as destination:
            #     for chunk in uploaded_file.chunks():
            #         destination.write(chunk)

            JobCard.objects.filter(job_id=ids).update(run_status=st,issued_by=issued_by,l1_date=l1_date,l1_time=l1_time,issued_signature=issued_signature)
            return JsonResponse({'status':'1'})

        elif st == 4 or st == '4':
            received_by = req.get('received_by')
            l2_date = datetime.datetime.strptime(req.get('l2_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            l2_time = req.get('l2_time')
            received_by_signature = req.get('received_by_signature')

            # uploaded_file = request.FILES['signature_img2']
            # static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')

            # # Create folder if it doesn't exist
            # os.makedirs(static_path, exist_ok=True)

            # # Save file
            # file_path = os.path.join(static_path, uploaded_file.name)
            # with open(file_path, 'wb+') as destination:
            #     for chunk in uploaded_file.chunks():
            #         destination.write(chunk)

            JobCard.objects.filter(job_id=ids).update(run_status=st,received_by=received_by,l2_date=l2_date,l2_time=l2_time,received_by_signature=received_by_signature)
            return JsonResponse({'status':'1'})

        elif st == 5 or st == '5':
            follow_up_details = req.get('follow_up_details')
            details_of_the_activitues = req.get('details_of_the_activitues')
            handed_over = req.get('handed_over')
            new_supervisor = req.get('new_supervisor')
            new_supervisor_signature = req.get('new_supervisor_signature')
            new_supervisor_id = req.get('new_supervisor_id')

            if handed_over == 'Yes':
                userLDt = UserProfile.objects.filter(user=new_supervisor_id)
                sprl = userLDt[0]
                print(sprl)
                new_supervisor = f"{sprl.first_name} {sprl.last_name}"
                new_supervisor_signature = f"{sprl.designation} / {sprl.emp_id}"
                new_supervisor_id = sprl.user.id

            print(new_supervisor)

            # if 'signature_img3' in request.FILES:
            #     uploaded_file = request.FILES['signature_img3']
            #     static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')

            #     # Create folder if it doesn't exist
            #     os.makedirs(static_path, exist_ok=True)

            #     # Save file
            #     file_path = os.path.join(static_path, uploaded_file.name)
            #     with open(file_path, 'wb+') as destination:
            #         for chunk in uploaded_file.chunks():
            #             destination.write(chunk)
            # else:
            #     file_path = ''

            JobCard.objects.filter(job_id=ids).update(run_status=st,follow_up_details=follow_up_details,handed_over=handed_over,new_supervisor=new_supervisor,new_supervisor_id=new_supervisor_id,details_of_the_activitues=details_of_the_activitues,new_supervisor_signature=new_supervisor_signature)
            return JsonResponse({'status':'1'})

        elif st == 6 or st == '6':
            train_can_be_energized = req.get('train_can_be_energized')
            completion_name = req.get('completion_name')
            down_time = req.get('down_time')
            train_can_be_moved = req.get('train_can_be_moved')
            completion_date_time = req.get('completion_date_time')
            completion_date = datetime.datetime.strptime(req.get('completion_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            completion_signature = req.get('completion_signature')

            # uploaded_file = request.FILES['signature_img4']
            # static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')

            # # Create folder if it doesn't exist
            # os.makedirs(static_path, exist_ok=True)

            # # Save file
            # file_path = os.path.join(static_path, uploaded_file.name)
            # with open(file_path, 'wb+') as destination:
            #     for chunk in uploaded_file.chunks():
            #         destination.write(chunk)
         
            JobCard.objects.filter(job_id=ids).update(run_status=st,train_can_be_energized=train_can_be_energized,completion_name=completion_name,down_time=down_time,train_can_be_moved=train_can_be_moved,completion_date_time=completion_date_time,completion_date=completion_date,completion_signature=completion_signature)

            return JsonResponse({'status':'1'})

        elif st == 7 or st == '7':
            corrective_action = req.get('corrective_action')
            sic_start_time = req.get('sic_start_time')
            sic_has_performed = 1 if request.POST.get('sic_has_performed') == 'on' else 0

            train_can_be_energized2 = req.get('train_can_be_energized2')
            completion_name2 = req.get('completion_name2')
            down_time2 = req.get('down_time2')
            train_can_be_moved2 = req.get('train_can_be_moved2')
            completion_date_time2 = req.get('completion_date_time2')
            completion_date2 = datetime.datetime.strptime(req.get('completion_date2'), '%d/%m/%Y').strftime('%Y-%m-%d')
            completion_signature2 = req.get('completion_signature2')

            sic_start_date = datetime.datetime.strptime(req.get('sic_start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')

            # uploaded_file = request.FILES['signature_img5']
            # static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')

            # # Create folder if it doesn't exist
            # os.makedirs(static_path, exist_ok=True)

            # # Save file
            # file_path = os.path.join(static_path, uploaded_file.name)
            # with open(file_path, 'wb+') as destination:
            #     for chunk in uploaded_file.chunks():
            #         destination.write(chunk)
         
            JobCard.objects.filter(job_id=ids).update(run_status=st,train_can_be_energized2=train_can_be_energized2,completion_name2=completion_name2,down_time2=down_time2,train_can_be_moved2=train_can_be_moved2,completion_date_time2=completion_date_time2,completion_date2=completion_date2,completion_signature2=completion_signature2,corrective_action=corrective_action,sic_start_time=sic_start_time,sic_has_performed=sic_has_performed,sic_start_date=sic_start_date)

            return JsonResponse({'status':'1'})

        elif st == 8 or st == '8':
            close_name = req.get('close_name')
            close_time = req.get('close_time')
            close_date = datetime.datetime.strptime(req.get('close_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            close_name_signature = req.get('close_name_signature')

            # uploaded_file = request.FILES['signature_img6']
            # static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')

            # # Create folder if it doesn't exist
            # os.makedirs(static_path, exist_ok=True)

            # # Save file
            # file_path = os.path.join(static_path, uploaded_file.name)
            # with open(file_path, 'wb+') as destination:
            #     for chunk in uploaded_file.chunks():
            #         destination.write(chunk)

            jobcardDt = JobCard.objects.filter(job_id=ids)
            jobRec = jobcardDt[0]
            failure_id = jobRec.failure_id.failure_id
            print(f"failure_id={failure_id}")
            FailureData.objects.filter(failure_id=failure_id).update(cm_start_date=jobRec.l2_date,cm_start_time=jobRec.l2_time,cm_end_date=jobRec.completion_date,cm_end_time=jobRec.completion_date_time,cm_description=jobRec.corrective_action)

            
          
         
            JobCard.objects.filter(job_id=ids).update(run_status=st,close_name_signature=close_name_signature,close_name=close_name,close_time=close_time,close_date=close_date,status=1)

            return JsonResponse({'status':'1'})

        elif st == 15 or st == '15':
            job_description = req.get('job_description')
            s_no = req.get('s_no')
            JobDetailsID = req.get('JobDetailsID')

            if JobDetailsID == "":
                job_dt = JobCard.objects.filter(job_id=ids)
                j = JobDetails(job_card_id=job_dt[0],s_no=s_no,job_description=job_description)
                j.save()
            else:
                JobDetails.objects.filter(job_details_id=JobDetailsID).update(s_no=s_no,job_description=job_description)

            return JsonResponse({'status':'1'})


        elif st == 16 or st == '16':
            JobDetails.objects.filter(job_details_id=ids).update(is_active=1)
            return JsonResponse({'status':'1'})

        elif st == 18 or st == '18':
            # print('here')
            jobwork_name = req.get('jobwork_name')
            jobwork_work = req.get('jobwork_work')
            JobWorkID = req.get('JobWorkID')

            # static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')
            # # Create folder if it doesn't exist
            # os.makedirs(static_path, exist_ok=True)

            # if 'jobwork_signature' in request.FILES:
            #     uploaded_file = request.FILES['jobwork_signature']
            #     file_path = os.path.join(static_path, uploaded_file.name)
            #     jobwork_signature = uploaded_file.name
            #     with open(file_path, 'wb+') as destination:
            #         for chunk in uploaded_file.chunks():
            #             destination.write(chunk)
                        
            # print('here')

            if JobWorkID == "":
                job_dt = JobCard.objects.filter(job_id=ids)
                j = JobWorkToMaintainers(job_card_id=job_dt[0],jobwork_name=jobwork_name,jobwork_work=jobwork_work)
                j.save()
            else:
                JobWorkToMaintainers.objects.filter(job_work_id=JobWorkID).update(jobwork_name=jobwork_name,jobwork_work=jobwork_work)

            return JsonResponse({'status':'1'})

        
        elif st == 19 or st == '19':
            JobWorkToMaintainers.objects.filter(job_work_id=ids).update(is_active=1)
            return JsonResponse({'status':'1'})

        elif st == 21 or st == '21':
            # print('here')
            jobequipment_name = req.get('jobequipment_name')
            jobequipment_new_no = req.get('jobequipment_new_no')
            jobequipment_old_no = req.get('jobequipment_old_no')
            JobEquipmentID = req.get('JobEquipmentID')

            # print('here')

            if JobEquipmentID == "":
                job_dt = JobCard.objects.filter(job_id=ids)
                j = JobReplacedEquipment(job_card_id=job_dt[0],jobequipment_name=jobequipment_name,jobequipment_new_no=jobequipment_new_no,jobequipment_old_no=jobequipment_old_no)
                j.save()
            else:
                JobReplacedEquipment.objects.filter(job_equipment_id=JobEquipmentID).update(jobequipment_name=jobequipment_name,jobequipment_new_no=jobequipment_new_no,jobequipment_old_no=jobequipment_old_no)

            return JsonResponse({'status':'1'})

        elif st == 22 or st == '22':
            JobReplacedEquipment.objects.filter(job_equipment_id=ids).update(is_active=1)
            return JsonResponse({'status':'1'})

        elif st == 23 or st == '23':
            JobCard.objects.filter(job_id=ids).update(run_status=5,status=0)
            return JsonResponse({'status':'1'})

        elif st == 24 or st == '24':
            JobCard.objects.filter(job_id=ids).update(run_status=7,status=0)
            return JsonResponse({'status':'1'})

        elif st == 25 or st == '25':
            JobCard.objects.filter(job_id=ids).update(run_status=6,status=0)
            return JsonResponse({'status':'1'})
        
        elif st == 26 or st == '26':
            JobCard.objects.filter(job_id=ids).update(run_status=5,status=0)
            return JsonResponse({'status':'1'})

        elif st == 27 or st == '27':
            JobCard.objects.filter(job_id=ids).update(run_status=3,status=0)
            return JsonResponse({'status':'1'})

        elif st == 28 or st == '28':
            JobCard.objects.filter(job_id=ids).update(run_status=2,status=0)
            return JsonResponse({'status':'1'})

        elif st == 30 or st == '30':
            JobCard.objects.filter(job_id=ids).delete()
            return JsonResponse({'status':'1'})

        
        
        else:
            return JsonResponse({'status':'0'})


class ViewJobcard(View):
    template_name = 'view_jobcard.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]
        JobCard_datas =JobCard.objects.filter(job_id=id)
        jb = JobCard_datas[0]
        ast_data = Asset.objects.filter(id=jb.failure_id.location_id)

        FailureDatas=FailureData.objects.filter(id=jb.failure_id.id)
        datas = FailureDatas[0]

        PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas[0].asset_type)

        job_details = []
        job_detailsArr = JobDetails.objects.filter(job_card_id=jb.job_id,is_active=0)
        st = 0
        for jdar in job_detailsArr:
            st = st + 1
            job_details.append({ 
                'job_details_id' :  jdar.job_details_id,
                'job_description' : jdar.job_description,
                's_no' : st,
            })


        full_path = jb.signature_img
        if full_path == None:
            relative_path = None
        else:
            # Find the index of /static
            index = full_path.find("/static")
            if index != -1:
                relative_path = full_path[index + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path = relative_path.lstrip("/")
            else:
                relative_path = full_path  # fallback if /static not found

        full_path2 = jb.signature_img2
        if full_path2 == None:
            relative_path2 = None
        else:
            # Find the index of /static
            index2 = full_path2.find("/static")
            if index2 != -1:
                relative_path2 = full_path2[index2 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path2 = relative_path2.lstrip("/")
            else:
                relative_path2 = full_path2  # fallback if /static not found


        full_path3 = jb.signature_img3
        if full_path3 == None:
            relative_path3 = None
        else:
            # Find the index of /static
            index3 = full_path3.find("/static")
            if index3 != -1:
                relative_path3 = full_path3[index3 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path3 = relative_path3.lstrip("/")
            else:
                relative_path3 = full_path3  # fallback if /static not found


        full_path4 = jb.signature_img4
        if full_path4 == None:
            relative_path4 = None
        else:
            # Find the index of /static
            index4 = full_path4.find("/static")
            if index4 != -1:
                relative_path4 = full_path4[index4 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path4 = relative_path4.lstrip("/")
            else:
                relative_path4 = full_path4  # fallback if /static not found

        full_path5 = jb.signature_img5
        if full_path5 == None:
            relative_path5 = None
        else:
            # Find the index of /static
            index5 = full_path5.find("/static")
            if index5 != -1:
                relative_path5 = full_path5[index5 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path5 = relative_path5.lstrip("/")
            else:
                relative_path5 = full_path5  # fallback if /static not found

        full_path6 = jb.signature_img6
        if full_path6 == None:
            relative_path6 = None
        else:
            # Find the index of /static
            index6 = full_path6.find("/static")
            if index6 != -1:
                relative_path6 = full_path6[index6 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path6 = relative_path6.lstrip("/")
            else:
                relative_path6 = full_path6  # fallback if /static not found



        data={ 
            'job_card_no' :  jb.job_card_no,
            'train_set_no' : ast_data[0].location_id,
            'date' : jb.failure_id.date,
            'time' : jb.failure_id.time,
            'department' : jb.failure_id.department,
            'nature_of_job' : jb.nature_of_job,
            'sic_required' : jb.sic_required,
            'assigned_to':jb.assigned_to,
            'last_update' : jb.last_update,
            'status':jb.status,
            'id':jb.job_id,
            'user_Role':user_Role,
            'run_status' : jb.run_status,


            'asset_type' : PBSMaster_datas[0].asset_type,
            'subsystem' : PBSMaster_datas[0].subsystem,
            'failure_id' : datas.failure_id,
            'asset_config_id' : datas.asset_config_id,
            'event_description' : datas.event_description,
            'mode_id' :datas.mode_id,
            'mode_description' : datas.mode_description,
            'detection':datas.detection,
            'service_delay' : datas.service_delay,
            'immediate_investigation' : datas.immediate_investigation,
            'failure_type' : datas.failure_type,
            'safety_failure' : datas.safety_failure,
            'hazard_id' : datas.hazard_id,
            'cm_description' : datas.cm_description,
            'replaced_asset_config_id':datas.replaced_asset_config_id,
            'cm_start_date' : datas.cm_start_date,
            'cm_start_time' : datas.cm_start_time,
            'cm_end_date' : datas.cm_end_date,
            'cm_end_time' : datas.cm_end_time,
            'oem_failure_reference' : datas.oem_failure_reference,
            'defect':datas.defect,


            'location_id' : datas.location_id,
            'kilometre_reading' : datas.kilometre_reading,
            'sel_car' : datas.sel_car,
            'equipment' : datas.equipment,
            'location' : datas.location,
            'direction': datas.direction,
            'incident' : datas.incident,
            'no_of_trip_cancel' : datas.no_of_trip_cancel,
            'deboarding' : datas.deboarding,
            'reported_to_PPIO' : datas.reported_to_PPIO,
            'TO_name': datas.TO_name,

            'ohe_required' : jb.ohe_required,
            'issued_to' : jb.issued_to,
            'completion_time' : jb.completion_time,
            'from_revenue_service' : jb.from_revenue_service,
            'delay_to_service' : jb.delay_to_service,
            'trip_no':jb.trip_no,
            'event_date' : jb.event_date,
            'event_time':jb.event_time,

            'sic_no':jb.sic_no,

            'signature_img':relative_path,
            'issued_by' : jb.issued_by,
            'l1_time':jb.l1_time,
            'l1_date':jb.l1_date,

            'signature_img2':relative_path2,
            'received_by' : jb.received_by,
            'l2_time':jb.l2_time,
            'l2_date':jb.l2_date,


            'signature_img3':relative_path3,
            'follow_up_details' : jb.follow_up_details,
            'details_of_the_activitues' : jb.details_of_the_activitues,
            'handed_over':jb.handed_over,
            'new_supervisor':jb.new_supervisor,


            'signature_img4':relative_path4,
            'completion_date_time' : jb.completion_date_time,
            'completion_date':jb.completion_date,
            'train_can_be_moved':jb.train_can_be_moved,
            'down_time':jb.down_time,
            'completion_name':jb.completion_name,
            'train_can_be_energized':jb.train_can_be_energized,


            'signature_img5':relative_path5,
            'completion_date_time2' : jb.completion_date_time2,
            'completion_date2':jb.completion_date2,
            'train_can_be_moved2':jb.train_can_be_moved2,
            'down_time2':jb.down_time2,
            'completion_name2':jb.completion_name2,
            'train_can_be_energized2':jb.train_can_be_energized2,
            'corrective_action':jb.corrective_action,
            'sic_start_time':jb.sic_start_time,
            'sic_has_performed':jb.sic_has_performed,

            'signature_img6':relative_path6,
            'close_name' : jb.close_name,
            'close_date':jb.close_date,
            'close_time':jb.close_time,

            'issued_signature':jb.issued_signature,
            'received_by_signature':jb.received_by_signature,
            'new_supervisor_signature':jb.new_supervisor_signature,
            'new_supervisor_id':jb.new_supervisor_id,
            'completion_signature':jb.completion_signature,
            'completion_signature2':jb.completion_signature2,
            'close_name_signature':jb.close_name_signature,

            'sic_start_date':jb.sic_start_date,

            'dept_location': jb.failure_id.dept_location,
            'date_issued' : jb.date,
            'time_issued' : jb.time,

            'system' : PBSMaster_datas[0].system,
            'equipment' : jb.failure_id.equipment,
            'event_description' : jb.failure_id.event_description,
            'immediate_investigation' : jb.failure_id.immediate_investigation,

            'revenue_service_delay' : jb.failure_id.revenue_service_delay,
            'failure_location': jb.failure_id.location,
            



        }

        prv_data = []
        JobCard_prvdatas =JobCard.objects.filter(failure_id__asset_config_id__location_id=jb.failure_id.asset_config_id.location_id,failure_id__date=jb.failure_id.date).exclude(job_id=id)
        st_gen = 0
        for jbr in JobCard_prvdatas:
            st_gen = st_gen + 1
            FailureDatasprv=FailureData.objects.filter(id=jbr.failure_id.id)
            datasprv = FailureDatasprv[0]
            sts = 'Open'
            if jbr.status == 1 or jbr.status == '1':
                sts = 'Closed'

            wrk = ''
            job_detailsArrLoop = JobDetails.objects.filter(job_card_id=jbr.job_id,is_active=0)
            for jdar in job_detailsArrLoop:
                if wrk == '':
                    wrk = jdar.job_description
                else:
                    wrk = f"{wrk}, {jdar.job_description}"

            prv_data.append({ 
                'st_gen':st_gen,
                'job_card_no' :  jbr.job_card_no,
                'issued_to' : jbr.issued_to,
                'immediate_investigation' : wrk,
                'completion_time' : jbr.completion_time,
                'status':sts,
            })


        prv_data2 = []
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        print(thirty_days_ago)
        JobCard_prvdatas2 =JobCard.objects.filter(failure_id__asset_config_id__location_id=jb.failure_id.asset_config_id.location_id,failure_id__equipment=jb.failure_id.equipment,date__gte=thirty_days_ago).exclude(job_id=id)
        st_gen = 0
        for jbr in JobCard_prvdatas2:
            st_gen = st_gen + 1
            PBSMaster_datas2 =PBSMaster.objects.filter(id=jbr.failure_id.asset_type)
            if PBSMaster_datas[0].system == PBSMaster_datas2[0].system:
                prv_data2.append({ 
                    'st_gen':st_gen,
                    'job_card_no' :  jbr.job_card_no,
                    'date' :  jbr.failure_id.date,
                    'immediate_investigation' :  jbr.failure_id.immediate_investigation,
                })


        job_works = []
        job_worksArr = JobWorkToMaintainers.objects.filter(job_card_id=jb.job_id,is_active=0)
        st = 0
        for jdar in job_worksArr:
            st = st + 1
            job_works.append({ 
                'job_work_id' :  jdar.job_work_id,
                'jobwork_name' :  jdar.jobwork_name,
                'jobwork_work' :  jdar.jobwork_work,
                'jobwork_signature' : jdar.jobwork_signature,
                's_no' : st,
            })

        job_equipment = []
        job_equipmentArr = JobReplacedEquipment.objects.filter(job_card_id=jb.job_id,is_active=0)
        st = 0
        for jdar in job_equipmentArr:
            st = st + 1
            job_equipment.append({ 
                'job_equipment_id' :  jdar.job_equipment_id,
                'jobequipment_name' :  jdar.jobequipment_name,
                'jobequipment_new_no' :  jdar.jobequipment_new_no,
                'jobequipment_old_no' : jdar.jobequipment_old_no,
                's_no' : st,
            })


        return render(request, self.template_name,{'data':data,'job_details':job_details, 'prv_data':prv_data, 'job_works':job_works, 'job_equipment':job_equipment ,"prv_data2":prv_data2 })
      




class DwdJobcard(View):
    template_name = 'dwd_jobcard.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]
        JobCard_datas =JobCard.objects.filter(job_id=id)
        jb = JobCard_datas[0]
        ast_data = Asset.objects.filter(id=jb.failure_id.location_id)

        FailureDatas=FailureData.objects.filter(id=jb.failure_id.id)
        datas = FailureDatas[0]

        PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas[0].asset_type)

        job_details = []
        job_detailsArr = JobDetails.objects.filter(job_card_id=jb.job_id,is_active=0)
        st = 0
        for jdar in job_detailsArr:
            st = st + 1
            job_details.append({ 
                'job_details_id' :  jdar.job_details_id,
                'job_description' : jdar.job_description,
                's_no' : st,
            })


        full_path = jb.signature_img
        if full_path == None:
            relative_path = None
        else:
            # Find the index of /static
            index = full_path.find("/static")
            if index != -1:
                relative_path = full_path[index + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path = relative_path.lstrip("/")
            else:
                relative_path = full_path  # fallback if /static not found

        full_path2 = jb.signature_img2
        if full_path2 == None:
            relative_path2 = None
        else:
            # Find the index of /static
            index2 = full_path2.find("/static")
            if index2 != -1:
                relative_path2 = full_path2[index2 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path2 = relative_path2.lstrip("/")
            else:
                relative_path2 = full_path2  # fallback if /static not found


        full_path3 = jb.signature_img3
        if full_path3 == None:
            relative_path3 = None
        else:
            # Find the index of /static
            index3 = full_path3.find("/static")
            if index3 != -1:
                relative_path3 = full_path3[index3 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path3 = relative_path3.lstrip("/")
            else:
                relative_path3 = full_path3  # fallback if /static not found


        full_path4 = jb.signature_img4
        if full_path4 == None:
            relative_path4 = None
        else:
            # Find the index of /static
            index4 = full_path4.find("/static")
            if index4 != -1:
                relative_path4 = full_path4[index4 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path4 = relative_path4.lstrip("/")
            else:
                relative_path4 = full_path4  # fallback if /static not found

        full_path5 = jb.signature_img5
        if full_path5 == None:
            relative_path5 = None
        else:
            # Find the index of /static
            index5 = full_path5.find("/static")
            if index5 != -1:
                relative_path5 = full_path5[index5 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path5 = relative_path5.lstrip("/")
            else:
                relative_path5 = full_path5  # fallback if /static not found

        full_path6 = jb.signature_img6
        if full_path6 == None:
            relative_path6 = None
        else:
            # Find the index of /static
            index6 = full_path6.find("/static")
            if index6 != -1:
                relative_path6 = full_path6[index6 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path6 = relative_path6.lstrip("/")
            else:
                relative_path6 = full_path6  # fallback if /static not found



        data={ 
            'job_card_no' :  jb.job_card_no,
            'train_set_no' : ast_data[0].location_id,
            'date' : jb.failure_id.date,
            'time' : jb.failure_id.time,
            'department' : jb.failure_id.department,
            'nature_of_job' : jb.nature_of_job,
            'sic_required' : jb.sic_required,
            'assigned_to':jb.assigned_to,
            'last_update' : jb.last_update,
            'status':jb.status,
            'id':jb.job_id,
            'user_Role':user_Role,
            'run_status' : jb.run_status,


            'asset_type' : PBSMaster_datas[0].asset_type,
            'subsystem' : PBSMaster_datas[0].subsystem,
            'failure_id' : datas.failure_id,
            'asset_config_id' : datas.asset_config_id,
            'event_description' : datas.event_description,
            'mode_id' :datas.mode_id,
            'mode_description' : datas.mode_description,
            'detection':datas.detection,
            'service_delay' : datas.service_delay,
            'immediate_investigation' : datas.immediate_investigation,
            'failure_type' : datas.failure_type,
            'safety_failure' : datas.safety_failure,
            'hazard_id' : datas.hazard_id,
            'cm_description' : datas.cm_description,
            'replaced_asset_config_id':datas.replaced_asset_config_id,
            'cm_start_date' : datas.cm_start_date,
            'cm_start_time' : datas.cm_start_time,
            'cm_end_date' : datas.cm_end_date,
            'cm_end_time' : datas.cm_end_time,
            'oem_failure_reference' : datas.oem_failure_reference,
            'defect':datas.defect,


            'location_id' : datas.location_id,
            'kilometre_reading' : datas.kilometre_reading,
            'sel_car' : datas.sel_car,
            'equipment' : datas.equipment,
            'location' : datas.location,
            'direction': datas.direction,
            'incident' : datas.incident,
            'no_of_trip_cancel' : datas.no_of_trip_cancel,
            'deboarding' : datas.deboarding,
            'reported_to_PPIO' : datas.reported_to_PPIO,
            'TO_name': datas.TO_name,

            'ohe_required' : jb.ohe_required,
            'issued_to' : jb.issued_to,
            'completion_time' : jb.completion_time,
            'from_revenue_service' : jb.from_revenue_service,
            'delay_to_service' : jb.delay_to_service,
            'trip_no':jb.trip_no,
            'event_date' : jb.event_date,
            'event_time':jb.event_time,

            'sic_no':jb.sic_no,

            'signature_img':relative_path,
            'issued_by' : jb.issued_by,
            'l1_time':jb.l1_time,
            'l1_date':jb.l1_date,

            'signature_img2':relative_path2,
            'received_by' : jb.received_by,
            'l2_time':jb.l2_time,
            'l2_date':jb.l2_date,


            'signature_img3':relative_path3,
            'follow_up_details' : jb.follow_up_details,
            'details_of_the_activitues' : jb.details_of_the_activitues,
            'handed_over':jb.handed_over,
            'new_supervisor':jb.new_supervisor,


            'signature_img4':relative_path4,
            'completion_date_time' : jb.completion_date_time,
            'completion_date':jb.completion_date,
            'train_can_be_moved':jb.train_can_be_moved,
            'down_time':jb.down_time,
            'completion_name':jb.completion_name,
            'train_can_be_energized':jb.train_can_be_energized,


            'signature_img5':relative_path5,
            'completion_date_time2' : jb.completion_date_time2,
            'completion_date2':jb.completion_date2,
            'train_can_be_moved2':jb.train_can_be_moved2,
            'down_time2':jb.down_time2,
            'completion_name2':jb.completion_name2,
            'train_can_be_energized2':jb.train_can_be_energized2,
            'corrective_action':jb.corrective_action,
            'sic_start_time':jb.sic_start_time,
            'sic_has_performed':jb.sic_has_performed,

            'signature_img6':relative_path6,
            'close_name' : jb.close_name,
            'close_date':jb.close_date,
            'close_time':jb.close_time,

            'issued_signature':jb.issued_signature,
            'received_by_signature':jb.received_by_signature,
            'new_supervisor_signature':jb.new_supervisor_signature,
            'new_supervisor_id':jb.new_supervisor_id,
            'completion_signature':jb.completion_signature,
            'completion_signature2':jb.completion_signature2,
            'close_name_signature':jb.close_name_signature,


            'dept_location': jb.failure_id.dept_location,
            'date_issued' : jb.date,
            'time_issued' : jb.time,

            'system' : PBSMaster_datas[0].system,
            'equipment' : jb.failure_id.equipment,
            'event_description' : jb.failure_id.event_description,
            'immediate_investigation' : jb.failure_id.immediate_investigation,

            'revenue_service_delay' : jb.failure_id.revenue_service_delay,
            'failure_location': jb.failure_id.location,
            



        }

        prv_data = []
        JobCard_prvdatas =JobCard.objects.filter(failure_id__asset_config_id__location_id=jb.failure_id.asset_config_id.location_id,failure_id__date=jb.failure_id.date).exclude(job_id=id)
        st_gen = 0
        for jbr in JobCard_prvdatas:
            st_gen = st_gen + 1
            FailureDatasprv=FailureData.objects.filter(id=jbr.failure_id.id)
            datasprv = FailureDatasprv[0]
            sts = 'Open'
            if jbr.status == 1 or jbr.status == '1':
                sts = 'Closed'

            wrk = ''
            job_detailsArrLoop = JobDetails.objects.filter(job_card_id=jbr.job_id,is_active=0)
            for jdar in job_detailsArrLoop:
                if wrk == '':
                    wrk = jdar.job_description
                else:
                    wrk = f"{wrk}, {jdar.job_description}"

            prv_data.append({ 
                'st_gen':st_gen,
                'job_card_no' :  jbr.job_card_no,
                'issued_to' : jbr.issued_to,
                'immediate_investigation' : wrk,
                'completion_time' : jbr.completion_time,
                'status':sts,
            })


        prv_data2 = []
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        print(thirty_days_ago)
        JobCard_prvdatas2 =JobCard.objects.filter(failure_id__asset_config_id__location_id=jb.failure_id.asset_config_id.location_id,failure_id__equipment=jb.failure_id.equipment,date__gte=thirty_days_ago).exclude(job_id=id)
        st_gen = 0
        for jbr in JobCard_prvdatas2:
            st_gen = st_gen + 1
            PBSMaster_datas2 =PBSMaster.objects.filter(id=jbr.failure_id.asset_type)
            if PBSMaster_datas[0].system == PBSMaster_datas2[0].system:
                prv_data2.append({ 
                    'st_gen':st_gen,
                    'job_card_no' :  jbr.job_card_no,
                    'date' :  jbr.failure_id.date,
                    'immediate_investigation' :  jbr.failure_id.immediate_investigation,
                })


        job_works = []
        job_worksArr = JobWorkToMaintainers.objects.filter(job_card_id=jb.job_id,is_active=0)
        st = 0
        for jdar in job_worksArr:
            st = st + 1
            job_works.append({ 
                'job_work_id' :  jdar.job_work_id,
                'jobwork_name' :  jdar.jobwork_name,
                'jobwork_work' :  jdar.jobwork_work,
                'jobwork_signature' : jdar.jobwork_signature,
                's_no' : st,
            })

        job_equipment = []
        job_equipmentArr = JobReplacedEquipment.objects.filter(job_card_id=jb.job_id,is_active=0)
        st = 0
        for jdar in job_equipmentArr:
            st = st + 1
            job_equipment.append({ 
                'job_equipment_id' :  jdar.job_equipment_id,
                'jobequipment_name' :  jdar.jobequipment_name,
                'jobequipment_new_no' :  jdar.jobequipment_new_no,
                'jobequipment_old_no' : jdar.jobequipment_old_no,
                's_no' : st,
            })


        return render(request, self.template_name,{'data':data,'job_details':job_details, 'prv_data':prv_data, 'job_works':job_works, 'job_equipment':job_equipment ,"prv_data2":prv_data2 })
      




class EIRRegister(View):
    template_name = 'eir_register.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')

        train_set_options = [f"TS#{i:02d}" for i in range(1, 35)]  # 01 to 34
     
        return render(request, self.template_name, {'train_set_options':train_set_options})

    def post(self, request, *args, **kwargs):

        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST

        location_id_f = req.get('location_id')
        depot = req.get('depot')
      
        EIRGenerationDatas = EIRGeneration.objects.filter().order_by('-eir_gen_id')

        if depot != "all":
            EIRGenerationDatas=EIRGenerationDatas.filter(depot=depot)

        if req.get('date') !="":
            date = datetime.datetime.strptime(req.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            EIRGenerationDatas=EIRGenerationDatas.filter(failure_id__date=date)




        # # print(req)
        # print('==========HERE=========')
       
        
        # print(EIRGenerationDatas)
       
        for jb in EIRGenerationDatas:
            asset_type_id = jb.failure_id.asset_type
            if PBSMaster.objects.filter(id=asset_type_id,is_active=0).exists():
                ast_data = Asset.objects.filter(id=jb.failure_id.location_id)
                if location_id_f != "all":
                    ast_data=ast_data.filter(location_id=location_id_f)
                if ast_data:

                    if user_Role == 1:
                        PBSMaster_datas=PBSMaster.objects.filter(id=asset_type_id,is_active=0)
                        for PBSMaster_data in PBSMaster_datas:
                            data.append({ 
                                'eir_id' :  jb.eir_id,
                                'train_set_no' : ast_data[0].location_id,
                                'date' : jb.failure_id.date,
                                'time' : jb.failure_id.time,
                                'department' : jb.failure_id.department,
                                'eir_gen_id' : jb.eir_gen_id,
                                'depot' : jb.depot,
                                'addressed_by':jb.addressed_by,
                                'incident_details' : jb.incident_details,
                                'repercussion':jb.repercussion,
                                'id':jb.eir_id,
                                'user_Role':user_Role,
                                'incident_location' : jb.incident_location,
                                'incident_time' : jb.incident_time,
                                'sel_car' : jb.failure_id.sel_car,
                                'equipment' : jb.failure_id.equipment,
                                'component' : jb.component,
                                'location': jb.failure_id.location,
                                
                            }) 
                    else:
                        if PBSMaster.objects.filter(id=asset_type_id,project_id=P_id,is_active=0).exists():
                            PBSMaster_datas=PBSMaster.objects.filter(id=asset_type_id,is_active=0)
                            for PBSMaster_data in PBSMaster_datas:
                                data.append({ 
                                    'eir_id' :  jb.eir_id,
                                    'train_set_no' : ast_data[0].location_id,
                                    'date' : jb.failure_id.date,
                                    'time' : jb.failure_id.time,
                                    'department' : jb.failure_id.department,
                                    'eir_gen_id' : jb.eir_gen_id,
                                    'depot' : jb.depot,
                                    'addressed_by':jb.addressed_by,
                                    'incident_details' : jb.incident_details,
                                    'repercussion':jb.repercussion,
                                    'id':jb.eir_id,
                                    'user_Role':user_Role,
                                    'incident_location' : jb.incident_location,
                                    'incident_time' : jb.incident_time,
                                    'sel_car' : jb.failure_id.sel_car,
                                    'equipment' : jb.failure_id.equipment,
                                    'component' : jb.component,
                                    'location': jb.failure_id.location,
                                }) 
        # print(data)
        return JsonResponse({'data':data})

    

class AddEIR(View):
    template_name = 'add_eir.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]

        EIRGeneration_datas =EIRGeneration.objects.filter(eir_id=id)
        jb = EIRGeneration_datas[0]
        ast_data = Asset.objects.filter(id=jb.failure_id.location_id)

        FailureDatas=FailureData.objects.filter(id=jb.failure_id.id)
        datas = FailureDatas[0]

        PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas[0].asset_type)


        full_path2 = jb.signature_img2
        if full_path2 == None:
            relative_path2 = None
        else:
            # Find the index of /static
            index2 = full_path2.find("/static")
            if index2 != -1:
                relative_path2 = full_path2[index2 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path2 = relative_path2.lstrip("/")
            else:
                relative_path2 = full_path2  # fallback if /static not found


        full_path3 = jb.signature_img3
        if full_path3 == None:
            relative_path3 = None
        else:
            # Find the index of /static
            index3 = full_path3.find("/static")
            if index3 != -1:
                relative_path3 = full_path3[index3 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path3 = relative_path3.lstrip("/")
            else:
                relative_path3 = full_path3  # fallback if /static not found

       
        data={ 
            'eir_id' :  jb.eir_id,
            'train_set_no' : ast_data[0].location_id,
            'date' : jb.failure_id.date,
            'time' : jb.failure_id.time,
            'department' : jb.failure_id.department,
            'eir_gen_id' : jb.eir_gen_id,
            'depot' : jb.depot,
            'addressed_by':jb.addressed_by,
            'incident_details' : jb.incident_details,
            'repercussion':jb.repercussion,
            'id':jb.eir_id,
            'user_Role':user_Role,
            'incident_location' : jb.incident_location,
            'incident_time' : jb.incident_time,
            'sel_car' : jb.failure_id.sel_car,
            'equipment' : jb.failure_id.equipment,
            'component' : jb.component,
            'location': jb.failure_id.location,
            'immediate_investigation':jb.failure_id.immediate_investigation,

            'action_taken_in_depot': jb.action_taken_in_depot,
            'concern': jb.concern,
            'further_action': jb.further_action,
            'TRSL':jb.TRSL,
            'signature_img2':relative_path2,
            'signature_img3':relative_path3,


        }


        prv_data = []
        EIRGeneration_datas_prvdatas = EIRGeneration.objects.filter(failure_id__equipment=jb.failure_id.equipment,component=jb.component).exclude(eir_id=id)
        st_gen = 0
        for jbr in EIRGeneration_datas_prvdatas:
            st_gen = st_gen + 1
            ast_data = Asset.objects.filter(id=jbr.failure_id.location_id)

            prv_data.append({ 
                'st_gen':st_gen,
                'eir_gen_id' :  jbr.eir_gen_id,
                'date' : jbr.failure_id.date,
                'depot' : jbr.depot,
                'train_set_no' : ast_data[0].location_id,
                'sel_car' : jbr.failure_id.sel_car,
                'incident_location' : jbr.incident_location,
                'incident_time' : jbr.incident_time,
                'id':jbr.eir_id,
            })

        job_details = []
        job_detailsArr = InvestigationDetails.objects.filter(eir_dt_id=jb.eir_id,is_active=0)
        st = 0
        for jdar in job_detailsArr:
            st = st + 1
            job_details.append({ 
                'details_id' :  jdar.details_id,
                'non_compliance_details' : jdar.non_compliance_details,
                'onvestigation_details' : jdar.onvestigation_details,
                'relevant_ERTS_clause' : jdar.relevant_ERTS_clause,
                's_no' : st,
            })

        images = []
        imgArr = EIRImages.objects.filter(eir_dt_id=jb.eir_id,is_active=0)
        for jdar in imgArr:

            full_path6 = jdar.file_path
            if full_path6 == None:
                relative_path6 = None
            else:
                # Find the index of /static
                index6 = full_path6.find("/static")
                if index6 != -1:
                    relative_path6 = full_path6[index6 + len("/static"):]  # remove /static as well
                    # optionally remove leading slash
                    relative_path6 = relative_path6.lstrip("/")
                else:
                    relative_path6 = full_path6  # fallback if /static not found

            images.append({ 
                'img_id' :  jdar.img_id,
                'file_path' : relative_path6,
            })


        # print(prv_data)
        return render(request, self.template_name,{'data':data ,'prv_data':prv_data , 'job_details':job_details, 'images':images })
      
 
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        ids = req.get('id')
        st = req.get('st')

        print(st)

        if st == 1 or st == '1':

            depot = req.get('depot')
            component = req.get('component')
            addressed_by = req.get('addressed_by')
            incident_details = req.get('incident_details')
            repercussion = req.get('repercussion')
            incident_location = req.get('incident_location')
            incident_time = req.get('incident_time')

            EIRGeneration.objects.filter(eir_id=ids).update(depot=depot,component=component,addressed_by=addressed_by,incident_details=incident_details,repercussion=repercussion,incident_location=incident_location,incident_time=incident_time)

            return JsonResponse({'status':'1'})

        elif st == 2 or st == '2':
            non_compliance_details = req.get('non_compliance_details')
            onvestigation_details = req.get('onvestigation_details')
            relevant_ERTS_clause = req.get('relevant_ERTS_clause')
            JobDetailsID = req.get('JobDetailsID')

            if JobDetailsID == "":
                eir_dt = EIRGeneration.objects.filter(eir_id=ids)
                j = InvestigationDetails(eir_dt_id=eir_dt[0],non_compliance_details=non_compliance_details,onvestigation_details=onvestigation_details,relevant_ERTS_clause=relevant_ERTS_clause)
                j.save()
            else:
                InvestigationDetails.objects.filter(details_id=JobDetailsID).update(non_compliance_details=non_compliance_details,onvestigation_details=onvestigation_details,relevant_ERTS_clause=relevant_ERTS_clause)

            return JsonResponse({'status':'1'})

        elif st == 3 or st == '3':
            InvestigationDetails.objects.filter(details_id=ids).update(is_active=1)
            return JsonResponse({'status':'1'})

        elif st == 4 or st == '4':
            action_taken_in_depot = req.get('action_taken_in_depot')
            concern = req.get('concern')
            further_action = req.get('further_action')
            TRSL = req.get('TRSL')
           
            if 'signature_img' in request.FILES:

                static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')
                os.makedirs(static_path, exist_ok=True)

                # Get all uploaded files under 'signature_img'
                uploaded_files = request.FILES.getlist('signature_img')

                eir_dt = EIRGeneration.objects.filter(eir_id=ids)

                for uploaded_file in uploaded_files:
                    file_path = os.path.join(static_path, uploaded_file.name)

                    with open(file_path, 'wb+') as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)

                    j = EIRImages(eir_dt_id=eir_dt[0],file_path=file_path)
                    j.save()

            if 'signature_img2' in request.FILES:
                uploaded_file = request.FILES['signature_img2']
                static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')

                # Create folder if it doesn't exist
                os.makedirs(static_path, exist_ok=True)

                # Save file
                file_path = os.path.join(static_path, uploaded_file.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

                EIRGeneration.objects.filter(eir_id=ids).update(signature_img2=file_path)

            if 'signature_img3' in request.FILES:
                uploaded_file = request.FILES['signature_img3']
                static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')

                # Create folder if it doesn't exist
                os.makedirs(static_path, exist_ok=True)

                # Save file
                file_path = os.path.join(static_path, uploaded_file.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

                EIRGeneration.objects.filter(eir_id=ids).update(signature_img3=file_path)


           
            EIRGeneration.objects.filter(eir_id=ids).update(action_taken_in_depot=action_taken_in_depot,concern=concern,further_action=further_action,TRSL=TRSL)
            return JsonResponse({'status':'1'})

        elif st == 5 or st == '5':
            EIRImages.objects.filter(img_id=ids).update(is_active=1)
            return JsonResponse({'status':'1'})

        
        else:
            return JsonResponse({'status':'0'})


class ViewEIR(View):
    template_name = 'view_eir.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]

        EIRGeneration_datas =EIRGeneration.objects.filter(eir_id=id)
        jb = EIRGeneration_datas[0]
        ast_data = Asset.objects.filter(id=jb.failure_id.location_id)

        FailureDatas=FailureData.objects.filter(id=jb.failure_id.id)
        datas = FailureDatas[0]

        PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas[0].asset_type)


        full_path2 = jb.signature_img2
        if full_path2 == None:
            relative_path2 = None
        else:
            # Find the index of /static
            index2 = full_path2.find("/static")
            if index2 != -1:
                relative_path2 = full_path2[index2 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path2 = relative_path2.lstrip("/")
            else:
                relative_path2 = full_path2  # fallback if /static not found


        full_path3 = jb.signature_img3
        if full_path3 == None:
            relative_path3 = None
        else:
            # Find the index of /static
            index3 = full_path3.find("/static")
            if index3 != -1:
                relative_path3 = full_path3[index3 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path3 = relative_path3.lstrip("/")
            else:
                relative_path3 = full_path3  # fallback if /static not found

       
        data={ 
            'eir_id' :  jb.eir_id,
            'train_set_no' : ast_data[0].location_id,
            'date' : jb.failure_id.date,
            'time' : jb.failure_id.time,
            'department' : jb.failure_id.department,
            'eir_gen_id' : jb.eir_gen_id,
            'depot' : jb.depot,
            'addressed_by':jb.addressed_by,
            'incident_details' : jb.incident_details,
            'repercussion':jb.repercussion,
            'id':jb.eir_id,
            'user_Role':user_Role,
            'incident_location' : jb.incident_location,
            'incident_time' : jb.incident_time,
            'sel_car' : jb.failure_id.sel_car,
            'equipment' : jb.failure_id.equipment,
            'component' : jb.component,
            'location': jb.failure_id.location,
            'immediate_investigation':jb.failure_id.immediate_investigation,

            'action_taken_in_depot': jb.action_taken_in_depot,
            'concern': jb.concern,
            'further_action': jb.further_action,
            'TRSL':jb.TRSL,
            'signature_img2':relative_path2,
            'signature_img3':relative_path3,


        }


        prv_data = []
        EIRGeneration_datas_prvdatas = EIRGeneration.objects.filter(failure_id__equipment=jb.failure_id.equipment,component=jb.component).exclude(eir_id=id)
        st_gen = 0
        for jbr in EIRGeneration_datas_prvdatas:
            st_gen = st_gen + 1
            ast_data = Asset.objects.filter(id=jbr.failure_id.location_id)

            prv_data.append({ 
                'st_gen':st_gen,
                'eir_gen_id' :  jbr.eir_gen_id,
                'date' : jbr.failure_id.date,
                'depot' : jbr.depot,
                'train_set_no' : ast_data[0].location_id,
                'sel_car' : jbr.failure_id.sel_car,
                'incident_location' : jbr.incident_location,
                'incident_time' : jbr.incident_time,
                'id':jbr.eir_id,
            })

        job_details = []
        job_detailsArr = InvestigationDetails.objects.filter(eir_dt_id=jb.eir_id,is_active=0)
        st = 0
        for jdar in job_detailsArr:
            st = st + 1
            job_details.append({ 
                'details_id' :  jdar.details_id,
                'non_compliance_details' : jdar.non_compliance_details,
                'onvestigation_details' : jdar.onvestigation_details,
                'relevant_ERTS_clause' : jdar.relevant_ERTS_clause,
                's_no' : st,
            })

        images = []
        imgArr = EIRImages.objects.filter(eir_dt_id=jb.eir_id,is_active=0)
        for jdar in imgArr:

            full_path6 = jdar.file_path
            if full_path6 == None:
                relative_path6 = None
            else:
                # Find the index of /static
                index6 = full_path6.find("/static")
                if index6 != -1:
                    relative_path6 = full_path6[index6 + len("/static"):]  # remove /static as well
                    # optionally remove leading slash
                    relative_path6 = relative_path6.lstrip("/")
                else:
                    relative_path6 = full_path6  # fallback if /static not found

            images.append({ 
                'img_id' :  jdar.img_id,
                'file_path' : relative_path6,
            })


        # print(prv_data)
        return render(request, self.template_name,{'data':data ,'prv_data':prv_data , 'job_details':job_details, 'images':images })
       




class KilometreReadingReg(View):
    template_name = 'kilometre_reading.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
     
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):

        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        # req = request.POST
        # print(req)
        print('==========HERE=========')
       
        KilometreReadingDatas = KilometreReading.objects.filter().order_by('-date')
        print(KilometreReadingDatas)
       
        for jb in KilometreReadingDatas:
            run_date = jb.date
            previous_record = KilometreReading.objects.filter(date__lt=run_date).order_by('-date').first()

            if previous_record:
                print('Previous record exists:', previous_record)
                record = KilometreReading.objects.filter(date__lt=run_date).order_by('-date').first()
                if record:
                    dail_jb = record
                else:
                    dail_jb = jb
            else:
                dail_jb = jb

            data.append({
                'id':jb.km_id,
                'date':jb.date,
                'ts01_tkm' : jb.ts01_tkm,
                'ts02_tkm' : jb.ts02_tkm,
                'ts03_tkm' : jb.ts03_tkm,
                'ts04_tkm' : jb.ts04_tkm,
                'ts05_tkm' : jb.ts05_tkm,
                'ts06_tkm' : jb.ts06_tkm,
                'ts07_tkm' : jb.ts07_tkm,
                'ts08_tkm' : jb.ts08_tkm,
                'ts09_tkm' : jb.ts09_tkm,
                'ts10_tkm' : jb.ts10_tkm,
                'ts11_tkm' : jb.ts11_tkm,
                'ts12_tkm' : jb.ts12_tkm,
                'ts13_tkm' : jb.ts13_tkm,
                'ts14_tkm' : jb.ts14_tkm,
                'ts15_tkm' : jb.ts15_tkm,
                'ts16_tkm' : jb.ts16_tkm,
                'ts17_tkm' : jb.ts17_tkm,
                'ts18_tkm' : jb.ts18_tkm,
                'ts19_tkm' : jb.ts19_tkm,
                'ts20_tkm' : jb.ts20_tkm,
                'ts21_tkm' : jb.ts21_tkm,
                'ts22_tkm' : jb.ts22_tkm,
                'ts23_tkm' : jb.ts23_tkm,
                'ts24_tkm' : jb.ts24_tkm,
                'ts25_tkm' : jb.ts25_tkm,
                'ts26_tkm' : jb.ts26_tkm,
                'ts27_tkm' : jb.ts27_tkm,
                'ts28_tkm' : jb.ts28_tkm,
                'ts29_tkm' : jb.ts29_tkm,
                'ts30_tkm' : jb.ts30_tkm,
                'ts31_tkm' : jb.ts31_tkm,
                'ts32_tkm' : jb.ts32_tkm,
                'ts33_tkm' : jb.ts33_tkm,
                'ts34_tkm' : jb.ts34_tkm,

                'tsd01_tkm' : dail_jb.ts01_tkm,
                'tsd02_tkm' : dail_jb.ts02_tkm,
                'tsd03_tkm' : dail_jb.ts03_tkm,
                'tsd04_tkm' : dail_jb.ts04_tkm,
                'tsd05_tkm' : dail_jb.ts05_tkm,
                'tsd06_tkm' : dail_jb.ts06_tkm,
                'tsd07_tkm' : dail_jb.ts07_tkm,
                'tsd08_tkm' : dail_jb.ts08_tkm,
                'tsd09_tkm' : dail_jb.ts09_tkm,
                'tsd10_tkm' : dail_jb.ts10_tkm,
                'tsd11_tkm' : dail_jb.ts11_tkm,
                'tsd12_tkm' : dail_jb.ts12_tkm,
                'tsd13_tkm' : dail_jb.ts13_tkm,
                'tsd14_tkm' : dail_jb.ts14_tkm,
                'tsd15_tkm' : dail_jb.ts15_tkm,
                'tsd16_tkm' : dail_jb.ts16_tkm,
                'tsd17_tkm' : dail_jb.ts17_tkm,
                'tsd18_tkm' : dail_jb.ts18_tkm,
                'tsd19_tkm' : dail_jb.ts19_tkm,
                'tsd20_tkm' : dail_jb.ts20_tkm,
                'tsd21_tkm' : dail_jb.ts21_tkm,
                'tsd22_tkm' : dail_jb.ts22_tkm,
                'tsd23_tkm' : dail_jb.ts23_tkm,
                'tsd24_tkm' : dail_jb.ts24_tkm,
                'tsd25_tkm' : dail_jb.ts25_tkm,
                'tsd26_tkm' : dail_jb.ts26_tkm,
                'tsd27_tkm' : dail_jb.ts27_tkm,
                'tsd28_tkm' : dail_jb.ts28_tkm,
                'tsd29_tkm' : dail_jb.ts29_tkm,
                'tsd30_tkm' : dail_jb.ts30_tkm,
                'tsd31_tkm' : dail_jb.ts31_tkm,
                'tsd32_tkm' : dail_jb.ts32_tkm,
                'tsd33_tkm' : dail_jb.ts33_tkm,
                'tsd34_tkm' : dail_jb.ts34_tkm,

                'user_Role':user_Role

            })
          
        print(data)
        return JsonResponse({'data':data, 'user_Role':user_Role })


class AddKilometreReading(View):
    template_name = 'add_kilometre_reading.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]

        today_date = date.today()
        print(id)

        if id == "" or id == None:
            data={ 
                'id' : '',
                'date' : today_date,
                'ts01_tkm' : 0,
                'ts02_tkm' : 0,
                'ts03_tkm' : 0,
                'ts04_tkm' : 0,
                'ts05_tkm' : 0,
                'ts06_tkm' : 0,
                'ts07_tkm' : 0,
                'ts08_tkm' : 0,
                'ts09_tkm' : 0,
                'ts10_tkm' : 0,
                'ts11_tkm' : 0,
                'ts12_tkm' : 0,
                'ts13_tkm' : 0,
                'ts14_tkm' : 0,
                'ts15_tkm' : 0,
                'ts16_tkm' : 0,
                'ts17_tkm' : 0,
                'ts18_tkm' : 0,
                'ts19_tkm' : 0,
                'ts20_tkm' : 0,
                'ts21_tkm' : 0,
                'ts22_tkm' : 0,
                'ts23_tkm' : 0,
                'ts24_tkm' : 0,
                'ts25_tkm' : 0,
                'ts26_tkm' : 0,
                'ts27_tkm' : 0,
                'ts28_tkm' : 0,
                'ts29_tkm' : 0,
                'ts30_tkm' : 0,
                'ts31_tkm' : 0,
                'ts32_tkm' : 0,
                'ts33_tkm' : 0,
                'ts34_tkm' : 0,

            }

       
        record = []
        if id != "" and id != None:
            record = KilometreReading.objects.filter(km_id=id).first()
        else:
            print(today_date)
            record = KilometreReading.objects.filter(date__lte=today_date).order_by('-date').first()
            id = ''

        if record:
            jb = record
            data={ 
                'id':id,
                'date':jb.date,
                'ts01_tkm' : jb.ts01_tkm,
                'ts02_tkm' : jb.ts02_tkm,
                'ts03_tkm' : jb.ts03_tkm,
                'ts04_tkm' : jb.ts04_tkm,
                'ts05_tkm' : jb.ts05_tkm,
                'ts06_tkm' : jb.ts06_tkm,
                'ts07_tkm' : jb.ts07_tkm,
                'ts08_tkm' : jb.ts08_tkm,
                'ts09_tkm' : jb.ts09_tkm,
                'ts10_tkm' : jb.ts10_tkm,
                'ts11_tkm' : jb.ts11_tkm,
                'ts12_tkm' : jb.ts12_tkm,
                'ts13_tkm' : jb.ts13_tkm,
                'ts14_tkm' : jb.ts14_tkm,
                'ts15_tkm' : jb.ts15_tkm,
                'ts16_tkm' : jb.ts16_tkm,
                'ts17_tkm' : jb.ts17_tkm,
                'ts18_tkm' : jb.ts18_tkm,
                'ts19_tkm' : jb.ts19_tkm,
                'ts20_tkm' : jb.ts20_tkm,
                'ts21_tkm' : jb.ts21_tkm,
                'ts22_tkm' : jb.ts22_tkm,
                'ts23_tkm' : jb.ts23_tkm,
                'ts24_tkm' : jb.ts24_tkm,
                'ts25_tkm' : jb.ts25_tkm,
                'ts26_tkm' : jb.ts26_tkm,
                'ts27_tkm' : jb.ts27_tkm,
                'ts28_tkm' : jb.ts28_tkm,
                'ts29_tkm' : jb.ts29_tkm,
                'ts30_tkm' : jb.ts30_tkm,
                'ts31_tkm' : jb.ts31_tkm,
                'ts32_tkm' : jb.ts32_tkm,
                'ts33_tkm' : jb.ts33_tkm,
                'ts34_tkm' : jb.ts34_tkm,
            }


        # print(prv_data)
        return render(request, self.template_name,{ 'data':data })
      
 
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        ids = req.get('id')

        date = datetime.datetime.strptime(req.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        if KilometreReading.objects.filter(date=date).exists(): 
            KilometreReading.objects.filter(date=date).update(ts01_tkm=req.get('ts01_tkm'),ts02_tkm=req.get('ts02_tkm'),ts03_tkm=req.get('ts03_tkm'),ts04_tkm=req.get('ts04_tkm'),ts05_tkm=req.get('ts05_tkm'),ts06_tkm=req.get('ts06_tkm'),ts07_tkm=req.get('ts07_tkm'),ts08_tkm=req.get('ts08_tkm'),ts09_tkm=req.get('ts09_tkm'),ts10_tkm=req.get('ts10_tkm'),ts11_tkm=req.get('ts11_tkm'),ts12_tkm=req.get('ts12_tkm'),ts13_tkm=req.get('ts13_tkm'),ts14_tkm=req.get('ts14_tkm'),ts15_tkm=req.get('ts15_tkm'),ts16_tkm=req.get('ts16_tkm'),ts17_tkm=req.get('ts17_tkm'),ts18_tkm=req.get('ts18_tkm'),ts19_tkm=req.get('ts19_tkm'),ts20_tkm=req.get('ts20_tkm'),ts21_tkm=req.get('ts21_tkm'),ts22_tkm=req.get('ts22_tkm'),ts23_tkm=req.get('ts23_tkm'),ts24_tkm=req.get('ts24_tkm'),ts25_tkm=req.get('ts25_tkm'),ts26_tkm=req.get('ts26_tkm'),ts27_tkm=req.get('ts27_tkm'),ts28_tkm=req.get('ts28_tkm'),ts29_tkm=req.get('ts29_tkm'),ts30_tkm=req.get('ts30_tkm'),ts31_tkm=req.get('ts31_tkm'),ts32_tkm=req.get('ts32_tkm'),ts33_tkm=req.get('ts33_tkm'),ts34_tkm=req.get('ts34_tkm'))
            return JsonResponse({'status':'1','message':'success'})

        else:
            j = KilometreReading(date=date,ts01_tkm=req.get('ts01_tkm'),ts02_tkm=req.get('ts02_tkm'),ts03_tkm=req.get('ts03_tkm'),ts04_tkm=req.get('ts04_tkm'),ts05_tkm=req.get('ts05_tkm'),ts06_tkm=req.get('ts06_tkm'),ts07_tkm=req.get('ts07_tkm'),ts08_tkm=req.get('ts08_tkm'),ts09_tkm=req.get('ts09_tkm'),ts10_tkm=req.get('ts10_tkm'),ts11_tkm=req.get('ts11_tkm'),ts12_tkm=req.get('ts12_tkm'),ts13_tkm=req.get('ts13_tkm'),ts14_tkm=req.get('ts14_tkm'),ts15_tkm=req.get('ts15_tkm'),ts16_tkm=req.get('ts16_tkm'),ts17_tkm=req.get('ts17_tkm'),ts18_tkm=req.get('ts18_tkm'),ts19_tkm=req.get('ts19_tkm'),ts20_tkm=req.get('ts20_tkm'),ts21_tkm=req.get('ts21_tkm'),ts22_tkm=req.get('ts22_tkm'),ts23_tkm=req.get('ts23_tkm'),ts24_tkm=req.get('ts24_tkm'),ts25_tkm=req.get('ts25_tkm'),ts26_tkm=req.get('ts26_tkm'),ts27_tkm=req.get('ts27_tkm'),ts28_tkm=req.get('ts28_tkm'),ts29_tkm=req.get('ts29_tkm'),ts30_tkm=req.get('ts30_tkm'),ts31_tkm=req.get('ts31_tkm'),ts32_tkm=req.get('ts32_tkm'),ts33_tkm=req.get('ts33_tkm'),ts34_tkm=req.get('ts34_tkm'))
            j.save()

            return JsonResponse({'status':'1','message':'success'})

        return JsonResponse({'status':'0','message':'Failed to save Kilometre Reading'})





class NCRRegister(View):
    template_name = 'ncr_register.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
     
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):

        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        req = request.POST
        # print(req)
        print('==========HERE=========')


        status = req.get('status')
       
        NCRGenerationDatas = NCRGeneration.objects.filter().order_by('-ncr_gen_id')

        if status != "all":
            if status == 0 or status == '0':
                NCRGenerationDatas=NCRGenerationDatas.filter(ncr_status=0,rejection_status=0)
            elif status == 1 or status == '1':
                NCRGenerationDatas=NCRGenerationDatas.filter(ncr_status=1)
            elif status == 2 or status == '2':
                NCRGenerationDatas=NCRGenerationDatas.filter(ncr_status=0,rejection_status=1)

        if req.get('date') !="":
            date = datetime.datetime.strptime(req.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            NCRGenerationDatas=NCRGenerationDatas.filter(date=date)

        if req.get('date2') !="":
            date2 = datetime.datetime.strptime(req.get('date2'), '%d/%m/%Y').strftime('%Y-%m-%d')
            NCRGenerationDatas=NCRGenerationDatas.filter(fnl_date=date2)

       
        
        print(NCRGenerationDatas)
       
        for jb in NCRGenerationDatas:
            asset_type_id = jb.rootcause_id.asset_type
            if PBSMaster.objects.filter(id=asset_type_id,is_active=0).exists():
                if user_Role == 1:
                    PBSMaster_datas=PBSMaster.objects.filter(id=asset_type_id,is_active=0)
                    for PBSMaster_data in PBSMaster_datas:
                        data.append({ 
                            'ncr_gen_id' :  jb.ncr_gen_id,
                            'date' : jb.date,
                            'time' : jb.time,
                            'id':jb.rec_id,
                            'user_Role':user_Role,
                            'fnl_date':jb.fnl_date,
                            'ncr_status':jb.ncr_status,
                            'remark':jb.remark,
                            'rejection_status':jb.rejection_status,
                            'accept_status':jb.accept_status,
                            'assembly_name':jb.assembly_name,
                            'assembly_no':jb.assembly_no,
                        }) 
                else:
                    if PBSMaster.objects.filter(id=asset_type_id,project_id=P_id,is_active=0).exists():
                        PBSMaster_datas=PBSMaster.objects.filter(id=asset_type_id,is_active=0)
                        for PBSMaster_data in PBSMaster_datas:
                            data.append({ 
                                'ncr_gen_id' :  jb.ncr_gen_id,
                                'date' : jb.date,
                                'time' : jb.time,
                                'id':jb.rec_id,
                                'user_Role':user_Role,
                                'fnl_date':jb.fnl_date,
                                'ncr_status':jb.ncr_status,
                                'remark':jb.remark,
                                'rejection_status':jb.rejection_status,
                                'accept_status':jb.accept_status,
                                'assembly_name':jb.assembly_name,
                                'assembly_no':jb.assembly_no,
                            }) 
        print(data)
        return JsonResponse({'data':data})

    


class AddNCR(View):
    template_name = 'add_ncr.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]

        if user_Role == 1:
            asset_types = PBSMaster.objects.filter(is_active=0).order_by('asset_type')
        else:
            asset_types = PBSMaster.objects.filter(is_active=0,project_id=P_id).order_by('asset_type')

        NCRGeneration_datas =NCRGeneration.objects.filter(rec_id=id)
        jb = NCRGeneration_datas[0]

        PBSMaster_datas=PBSMaster.objects.filter(id=jb.rootcause_id.asset_type)

        Defect_datas=Defect.objects.filter(defect_id=jb.rootcause_id.defect.defect_id)

        current_time = datetime.datetime.now().strftime("%H:%M")
        today_date = date.today()

        if jb.defect_time == None or jb.defect_time == "":
            defect_time = current_time
        else:
            defect_time = jb.defect_time


        if jb.defect_date == None or jb.defect_date == "":
            defect_date = Defect_datas[0].defect_open_date
        else:
            defect_date = datetime.datetime.strptime(jb.defect_date, "%Y-%m-%d").date() 

        if jb.corrective_action_date == None or jb.corrective_action_date == "":
            corrective_action_date = today_date
        else:
            corrective_action_date = datetime.datetime.strptime(jb.corrective_action_date, "%Y-%m-%d").date() 


        if jb.approved_date == None or jb.approved_date == "":
            approved_date = today_date
        else:
            approved_date = datetime.datetime.strptime(jb.approved_date, "%Y-%m-%d").date() 

        if jb.action_date == None or jb.action_date == "":
            action_date = today_date
        else:
            action_date = datetime.datetime.strptime(jb.action_date, "%Y-%m-%d").date() 

        if jb.verification_date == None or jb.verification_date == "":
            verification_date = today_date
        else:
            verification_date = datetime.datetime.strptime(jb.verification_date, "%Y-%m-%d").date() 

        if jb.fnl_date == None or jb.fnl_date == "":
            fnl_date = ''
        else:
            fnl_date = datetime.datetime.strptime(jb.fnl_date, "%Y-%m-%d").date() 

        if jb.defect_description == None or jb.defect_description == "":
            defect_description = Defect_datas[0].defect_description
        else:
            defect_description = jb.defect_description

        if jb.assembly_name == "" or jb.assembly_name == None:
            Find_asst =PBSMaster.objects.filter(id=jb.rootcause_id.asset_type)
            assembly_name = Find_asst[0].asset_type
        else:
            assembly_name = jb.assembly_name

        asset_type = jb.rootcause_id.asset_type

        data={ 
            'ncr_gen_id' :  jb.ncr_gen_id,
            'date' : datetime.datetime.strptime(jb.date, "%Y-%m-%d").date(),
            'time' : jb.time,
            'id':jb.rec_id,
            'user_Role':user_Role,
            'defect_time':defect_time,
            'defect_date':defect_date,
            'corrective_action_date':corrective_action_date,
            'approved_date':approved_date,
            'action_date':action_date,
            'verification_date':verification_date,
            'fnl_date':fnl_date,
            'project_name':PBSMaster_datas[0].project.product_name,
            'defect_description':defect_description,

            'inspector_name':jb.inspector_name,
            'assembly_name':assembly_name,
            'assembly_no':jb.assembly_no,
            'drawing_no':jb.drawing_no,
            'detection_workstation':jb.detection_workstation,
            'location_id':jb.location_id,
            'sel_car':jb.sel_car,
            'serial_no':jb.serial_no,
            'green_red_channel':jb.green_red_channel,

            'chkMinor':jb.chkMinor,
            'chkMajor':jb.chkMajor,
            'chkCritical':jb.chkCritical,

            'specification':jb.specification,
            'defect_source':jb.defect_source,
            'supplier_name':jb.supplier_name,
            'defect_location':jb.defect_location,
            'defect_detected_by':jb.defect_detected_by,
            'defect_detected_workstation':jb.defect_detected_workstation,
            'no_of_parts_deloverd':jb.no_of_parts_deloverd,
            'no_of_defective_parts':jb.no_of_defective_parts,

            'active_deviations':jb.active_deviations,
            'chk_Internal':jb.chk_Internal,
            'chk_Supplier':jb.chk_Supplier,
            'chk_TWL':jb.chk_TWL,
            'chk_Transportation':jb.chk_Transportation,

            'ok_img':jb.ok_img,
            'notok_img':jb.notok_img,
            'signature_img':jb.signature_img,
            'signature_img2':jb.signature_img2,
            'signature_img3':jb.signature_img3,
            'signature_img4':jb.signature_img4,
            'signature_img5':jb.signature_img5,


            'initial_analysis':jb.initial_analysis,
            'attachments_files':jb.attachments_files,
            'responsibility':jb.responsibility,
            'invoice_number':jb.invoice_number,
            'non_conforming_part_disposition':jb.non_conforming_part_disposition,
            'responsible_for_execution':jb.responsible_for_execution,
            'containment_action':jb.containment_action,
            'corrective_action_by':jb.corrective_action_by,
            'corrective_action_designation':jb.corrective_action_designation,
            'approved_by':jb.approved_by,
            'approved_designation':jb.approved_designation,
            'action_name':jb.action_name,
            'verification_name':jb.verification_name,
            'inp_root_cause':jb.inp_root_cause,
            'occurrence':jb.occurrence,
            'detection':jb.detection,
            'effectiveness':jb.effectiveness,

            'cost_1':jb.cost_1,
            'cost_2':jb.cost_2,
            'cost_3':jb.cost_3,
            'cost_4':jb.cost_4,
            'cost_5':jb.cost_5,
            'cost_6':jb.cost_6,
            'total_cost':jb.total_cost,


            'no_of_day_open':jb.no_of_day_open,
            'physical_closure':jb.physical_closure,
            'physical_closure_rca_capa':jb.physical_closure_rca_capa,
            'fnl_name':jb.fnl_name,
            'fnl_designation':jb.fnl_designation,

            'asset_type':asset_type,
            'root_cause_analysis':jb.root_cause_analysis,
            'ncr_status':jb.ncr_status,

            'rev_no' : jb.rev_no,

            'remark':jb.remark,
            'rejection_status':jb.rejection_status,
            'accept_status':jb.accept_status,


        }


        train_set_options = Asset.objects.filter(is_active=0,asset_type=asset_type).distinct('location_id')

        asset_serial_number = Asset.objects.filter(is_active=0,asset_type=asset_type).distinct('asset_serial_number')


        Corrective_data = []
        if user_Role == 1:
            CorrectiveAction_data =CorrectiveAction.objects.filter(is_active=0,defect_id=jb.rootcause_id.defect)
        else:
            CorrectiveAction_data =CorrectiveAction.objects.filter(is_active=0,P_id=P_id,defect_id=jb.rootcause_id.defect)

        for CorrectiveActions in CorrectiveAction_data:
            Corrective_data.append({ 
                'corrective_action_id' : CorrectiveActions.corrective_action_id,
                'corrective_action_owner' : CorrectiveActions.corrective_action_owner,
                'corrective_action_description' : CorrectiveActions.corrective_action_description,
                'corrective_action_update' : CorrectiveActions.corrective_action_update,
                'corrective_action_status' : CorrectiveActions.corrective_action_status,
            })    

        imageList = NCRImagesList.objects.filter(is_active=0,ncr_gen_id=jb.rec_id)

        return render(request, self.template_name,{'data':data ,'train_set_options':train_set_options,'Corrective_data':Corrective_data , 'asset_types': asset_types, 'asset_serial_number':asset_serial_number, 'imageList':imageList })
      
 
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        ids = req.get('id')
        st = req.get('st')

        inspector_name = req.get('inspector_name')
        # asset_type = req.get('asset_type')
        # Find_Pids =PBSMaster.objects.filter(asset_type=asset_type,is_active=0)
        # Find_Pid = Find_Pids[0]
        
        # asset_type = Find_Pid.id
        rev_no = req.get('rev_no')
        assembly_name = req.get('assembly_name')
        assembly_no = req.get('assembly_no')
        drawing_no = req.get('drawing_no')
        detection_workstation = req.get('detection_workstation')
        location_id = req.get('location_id_val')
        sel_car = req.get('sel_car_val')
        serial_no = req.get('serial_no')
        green_red_channel = req.get('green_red_channel')

        chkMinor = req.get('chkMinorV')
        chkMajor = req.get('chkMajorV')
        chkCritical = req.get('chkCriticalV')

        specification = req.get('specification')
        defect_source = req.get('defect_source')
        supplier_name = req.get('supplier_name')
        defect_location = req.get('defect_location')
        defect_detected_by = req.get('defect_detected_by')
        defect_detected_workstation = req.get('defect_detected_workstation')
        no_of_parts_deloverd = req.get('no_of_parts_deloverd')
        no_of_defective_parts = req.get('no_of_defective_parts')
        defect_description = req.get('defect_description')

        defect_time = req.get('defect_time')
        defect_date = req.get('defect_date')
        if defect_date != "":
            defect_date = datetime.datetime.strptime(req.get('defect_date'), '%d/%m/%Y').strftime('%Y-%m-%d')


        active_deviations = req.get('active_deviations')
        chk_Internal = req.get('chk_InternalV')
        chk_Supplier = req.get('chk_SupplierV')
        chk_TWL = req.get('chk_TWLV')
        chk_Transportation = req.get('chk_TransportationV')

        static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')
        # Create folder if it doesn't exist
        os.makedirs(static_path, exist_ok=True)


        if 'ok_img' in request.FILES:
            uploaded_files = request.FILES.getlist('ok_img')  # get list of uploaded files
            for uploaded_file in uploaded_files:
                file_path = os.path.join(static_path, uploaded_file.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

                im = NCRImagesList(ncr_gen_id=ids,file_path=uploaded_file.name)
                im.save()
            
        # if 'ok_img' in request.FILES:
        #     uploaded_file = request.FILES['ok_img']
        #     file_path = os.path.join(static_path, uploaded_file.name)
        #     ok_img = uploaded_file.name
        #     with open(file_path, 'wb+') as destination:
        #         for chunk in uploaded_file.chunks():
        #             destination.write(chunk)
        #     NCRGeneration.objects.filter(rec_id=ids).update(ok_img=ok_img)


        # if 'notok_img' in request.FILES:
        #     uploaded_file = request.FILES['notok_img']
        #     file_path = os.path.join(static_path, uploaded_file.name)
        #     notok_img = uploaded_file.name
        #     with open(file_path, 'wb+') as destination:
        #         for chunk in uploaded_file.chunks():
        #             destination.write(chunk)

        #     NCRGeneration.objects.filter(rec_id=ids).update(notok_img=notok_img)

        if 'signature_img' in request.FILES:
            uploaded_file = request.FILES['signature_img']
            file_path = os.path.join(static_path, uploaded_file.name)
            signature_img = uploaded_file.name
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            NCRGeneration.objects.filter(rec_id=ids).update(signature_img=signature_img)
     
        if 'signature_img2' in request.FILES:
            uploaded_file = request.FILES['signature_img2']
            file_path = os.path.join(static_path, uploaded_file.name)
            signature_img2 = uploaded_file.name
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            NCRGeneration.objects.filter(rec_id=ids).update(signature_img2=signature_img2)
     

        if 'signature_img3' in request.FILES:
            uploaded_file = request.FILES['signature_img3']
            file_path = os.path.join(static_path, uploaded_file.name)
            signature_img3 = uploaded_file.name
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            NCRGeneration.objects.filter(rec_id=ids).update(signature_img3=signature_img3)


        if 'signature_img4' in request.FILES:
            uploaded_file = request.FILES['signature_img4']
            file_path = os.path.join(static_path, uploaded_file.name)
            signature_img4 = uploaded_file.name
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            NCRGeneration.objects.filter(rec_id=ids).update(signature_img4=signature_img4)
  
        

        initial_analysis = req.get('initial_analysis')
        attachments_files = req.get('attachments_files')
        responsibility = req.get('responsibility')
        invoice_number = req.get('invoice_number')
        non_conforming_part_disposition = req.get('non_conforming_part_disposition')
        responsible_for_execution = req.get('responsible_for_execution')
        containment_action = req.get('containment_action')
        corrective_action_by = req.get('corrective_action_by')
        corrective_action_designation = req.get('corrective_action_designation')
        approved_by = req.get('approved_by')
        approved_designation = req.get('approved_designation')
        action_name = req.get('action_name')
        verification_name = req.get('verification_name')
        inp_root_cause = req.get('inp_root_cause')
        occurrence = req.get('occurrence')
        detection = req.get('detection')
        effectiveness = req.get('effectiveness')

        corrective_action_date = req.get('corrective_action_date')
        if corrective_action_date != "":
            corrective_action_date = datetime.datetime.strptime(req.get('corrective_action_date'), '%d/%m/%Y').strftime('%Y-%m-%d')

        approved_date = req.get('approved_date')
        if approved_date != "":
            approved_date = datetime.datetime.strptime(req.get('approved_date'), '%d/%m/%Y').strftime('%Y-%m-%d')

        action_date = req.get('action_date')
        if action_date != "":
            action_date = datetime.datetime.strptime(req.get('action_date'), '%d/%m/%Y').strftime('%Y-%m-%d')

        verification_date = req.get('verification_date')
        if verification_date != "":
            verification_date = datetime.datetime.strptime(req.get('verification_date'), '%d/%m/%Y').strftime('%Y-%m-%d')


        cost_1 = req.get('cost_1')
        cost_2 = req.get('cost_2')
        cost_3 = req.get('cost_3')
        cost_4 = req.get('cost_4')
        cost_5 = req.get('cost_5')
        cost_6 = req.get('cost_6')
        total_cost = req.get('total_cost')

        

        root_cause_analysis = req.get('root_cause_analysis')
        

        NCRGeneration.objects.filter(rec_id=ids).update(inspector_name=inspector_name,assembly_name=assembly_name,assembly_no=assembly_no,drawing_no=drawing_no,detection_workstation=detection_workstation,location_id=location_id,sel_car=sel_car,serial_no=serial_no,green_red_channel=green_red_channel,chkMinor=chkMinor,chkMajor=chkMajor,chkCritical=chkCritical,specification=specification,defect_source=defect_source,supplier_name=supplier_name,defect_location=defect_location,defect_detected_by=defect_detected_by,defect_detected_workstation=defect_detected_workstation,no_of_parts_deloverd=no_of_parts_deloverd,no_of_defective_parts=no_of_defective_parts,defect_description=defect_description,defect_time=defect_time,defect_date=defect_date,active_deviations=active_deviations,chk_Internal=chk_Internal,chk_Supplier=chk_Supplier,chk_TWL=chk_TWL,chk_Transportation=chk_Transportation,corrective_action_date=corrective_action_date,approved_date=approved_date,action_date=action_date,verification_date=verification_date,initial_analysis=initial_analysis,attachments_files=attachments_files,responsibility=responsibility,invoice_number=invoice_number,non_conforming_part_disposition=non_conforming_part_disposition,responsible_for_execution=responsible_for_execution,containment_action=containment_action,corrective_action_by=corrective_action_by,corrective_action_designation=corrective_action_designation,approved_by=approved_by,approved_designation=approved_designation,action_name=action_name,verification_name=verification_name,inp_root_cause=inp_root_cause,occurrence=occurrence,detection=detection,effectiveness=effectiveness,cost_1=cost_1,cost_2=cost_2,cost_3=cost_3,cost_4=cost_4,cost_5=cost_5,cost_6=cost_6,total_cost=total_cost,root_cause_analysis=root_cause_analysis,ncr_status=0,rev_no=rev_no)


        return JsonResponse({'status':'1'})




class ViewNCR(View):
    template_name = 'view_ncr.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]

        NCRGeneration_datas =NCRGeneration.objects.filter(rec_id=id)
        jb = NCRGeneration_datas[0]

        PBSMaster_datas=PBSMaster.objects.filter(id=jb.rootcause_id.asset_type)

        Defect_datas=Defect.objects.filter(defect_id=jb.rootcause_id.defect.defect_id)

        current_time = datetime.datetime.now().strftime("%H:%M")
        today_date = date.today()

        if jb.defect_time == None or jb.defect_time == "":
            defect_time = current_time
        else:
            time_obj1 = datetime.datetime.strptime(jb.defect_time, "%H:%M")
            defect_time = time_obj1.strftime("%I:%M %p")

        if jb.defect_date == None or jb.defect_date == "":
            defect_date = Defect_datas[0].defect_open_date
        else:
            defect_date = datetime.datetime.strptime(jb.defect_date, "%Y-%m-%d").date() 

        if jb.corrective_action_date == None or jb.corrective_action_date == "":
            corrective_action_date = today_date
        else:
            corrective_action_date = datetime.datetime.strptime(jb.corrective_action_date, "%Y-%m-%d").date() 


        if jb.approved_date == None or jb.approved_date == "":
            approved_date = today_date
        else:
            approved_date = datetime.datetime.strptime(jb.approved_date, "%Y-%m-%d").date() 

        if jb.action_date == None or jb.action_date == "":
            action_date = today_date
        else:
            action_date = datetime.datetime.strptime(jb.action_date, "%Y-%m-%d").date() 

        if jb.verification_date == None or jb.verification_date == "":
            verification_date = today_date
        else:
            verification_date = datetime.datetime.strptime(jb.verification_date, "%Y-%m-%d").date() 

        if jb.fnl_date == None or jb.fnl_date == "":
            fnl_date = today_date
        else:
            fnl_date = datetime.datetime.strptime(jb.fnl_date, "%Y-%m-%d").date() 

        if jb.defect_description == None or jb.defect_description == "":
            defect_description = Defect_datas[0].defect_description
        else:
            defect_description = jb.defect_description


        time_obj = datetime.datetime.strptime(jb.time, "%H:%M:%S")
        formatted_time = time_obj.strftime("%I:%M %p")

        data={ 
            'ncr_gen_id' :  jb.ncr_gen_id,
            'date' : datetime.datetime.strptime(jb.date, "%Y-%m-%d").date(),
            'time' : formatted_time,
            'id':jb.rec_id,
            'user_Role':user_Role,
            'defect_time':defect_time,
            'defect_date':defect_date,
            'corrective_action_date':corrective_action_date,
            'approved_date':approved_date,
            'action_date':action_date,
            'verification_date':verification_date,
            'fnl_date':fnl_date,
            'project_name':PBSMaster_datas[0].project.product_name,
            'defect_description':defect_description,

            'inspector_name':jb.inspector_name,
            'assembly_name':jb.assembly_name,
            'assembly_no':jb.assembly_no,
            'drawing_no':jb.drawing_no,
            'detection_workstation':jb.detection_workstation,
            'location_id':jb.location_id,
            'sel_car':jb.sel_car,
            'serial_no':jb.serial_no,
            'green_red_channel':jb.green_red_channel,

            'chkMinor':jb.chkMinor,
            'chkMajor':jb.chkMajor,
            'chkCritical':jb.chkCritical,

            'specification':jb.specification,
            'defect_source':jb.defect_source,
            'supplier_name':jb.supplier_name,
            'defect_location':jb.defect_location,
            'defect_detected_by':jb.defect_detected_by,
            'defect_detected_workstation':jb.defect_detected_workstation,
            'no_of_parts_deloverd':jb.no_of_parts_deloverd,
            'no_of_defective_parts':jb.no_of_defective_parts,

            'active_deviations':jb.active_deviations,
            'chk_Internal':jb.chk_Internal,
            'chk_Supplier':jb.chk_Supplier,
            'chk_TWL':jb.chk_TWL,
            'chk_Transportation':jb.chk_Transportation,

            'ok_img':jb.ok_img,
            'notok_img':jb.notok_img,
            'signature_img':jb.signature_img,
            'signature_img2':jb.signature_img2,
            'signature_img3':jb.signature_img3,
            'signature_img4':jb.signature_img4,
            'signature_img5':jb.signature_img5,


            'initial_analysis':jb.initial_analysis,
            'attachments_files':jb.attachments_files,
            'responsibility':jb.responsibility,
            'invoice_number':jb.invoice_number,
            'non_conforming_part_disposition':jb.non_conforming_part_disposition,
            'responsible_for_execution':jb.responsible_for_execution,
            'containment_action':jb.containment_action,
            'corrective_action_by':jb.corrective_action_by,
            'corrective_action_designation':jb.corrective_action_designation,
            'approved_by':jb.approved_by,
            'approved_designation':jb.approved_designation,
            'action_name':jb.action_name,
            'verification_name':jb.verification_name,
            'inp_root_cause':jb.inp_root_cause,
            'occurrence':jb.occurrence,
            'detection':jb.detection,
            'effectiveness':jb.effectiveness,

            'cost_1':jb.cost_1,
            'cost_2':jb.cost_2,
            'cost_3':jb.cost_3,
            'cost_4':jb.cost_4,
            'cost_5':jb.cost_5,
            'cost_6':jb.cost_6,
            'total_cost':jb.total_cost,


            'no_of_day_open':jb.no_of_day_open,
            'physical_closure':jb.physical_closure,
            'physical_closure_rca_capa':jb.physical_closure_rca_capa,
            'fnl_name':jb.fnl_name,
            'fnl_designation':jb.fnl_designation,

            'root_cause_analysis':jb.root_cause_analysis,
            'ncr_status':jb.ncr_status,

            'rev_no' : jb.rev_no,

            'remark':jb.remark,
            'rejection_status':jb.rejection_status,
            'accept_status':jb.accept_status,


        }


        if user_Role == 1:
            train_set_options = Asset.objects.filter(is_active=0).distinct('location_id')
        else:
            train_set_options = Asset.objects.filter(is_active=0,P_id=P_id).distinct('location_id')


        Corrective_data = []
        if user_Role == 1:
            CorrectiveAction_data =CorrectiveAction.objects.filter(is_active=0,defect_id=jb.rootcause_id.defect)
        else:
            CorrectiveAction_data =CorrectiveAction.objects.filter(is_active=0,P_id=P_id,defect_id=jb.rootcause_id.defect)

        for CorrectiveActions in CorrectiveAction_data:
            Corrective_data.append({ 
                'corrective_action_id' : CorrectiveActions.corrective_action_id,
                'corrective_action_owner' : CorrectiveActions.corrective_action_owner,
                'corrective_action_description' : CorrectiveActions.corrective_action_description,
                'corrective_action_update' : CorrectiveActions.corrective_action_update,
                'corrective_action_status' : CorrectiveActions.corrective_action_status,
            })     

        imageList = NCRImagesList.objects.filter(is_active=0,ncr_gen_id=jb.rec_id)

        return render(request, self.template_name,{'data':data ,'train_set_options':train_set_options,'Corrective_data':Corrective_data,'imageList':imageList })

    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        ids = req.get('id')
        st = req.get('st')
        if st == 1 or st == '1':
            NCRImagesList.objects.filter(img_id=ids).update(is_active=1)
            return JsonResponse({'status':'1'})

        if st == 2 or st == '2':
            physical_closure = req.get('physical_closure')
            physical_closure_rca_capa = req.get('physical_closure_rca_capa')

            no_of_day_open = req.get('no_of_day_open')
        
            fnl_name = req.get('fnl_name')
            fnl_designation = req.get('fnl_designation')

            fnl_date = req.get('fnl_date')
            if fnl_date != "":
                fnl_date = datetime.datetime.strptime(req.get('fnl_date'), '%d/%m/%Y').strftime('%Y-%m-%d')

            static_path = os.path.join(settings.BASE_DIR, 'static', 'uploads')
            # Create folder if it doesn't exist
            os.makedirs(static_path, exist_ok=True)

            if 'signature_img5' in request.FILES:
                uploaded_file = request.FILES['signature_img5']
                file_path = os.path.join(static_path, uploaded_file.name)
                signature_img5 = uploaded_file.name
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
                NCRGeneration.objects.filter(rec_id=ids).update(signature_img5=signature_img5)


            NCRGeneration.objects.filter(rec_id=ids).update(physical_closure=physical_closure,physical_closure_rca_capa=physical_closure_rca_capa,fnl_date=fnl_date,no_of_day_open=no_of_day_open,fnl_name=fnl_name,fnl_designation=fnl_designation,ncr_status=1)

            return JsonResponse({'status':'1'})

        if st == 3 or st == '3':
            assembly_no = req.get('assembly_no')
            drawing_no = req.get('drawing_no')
            detection_workstation = req.get('detection_workstation')
            remark = req.get('remark')
            accept_status = req.get('accept_status')
            rejection_status = req.get('rejection_status')

            NCRGeneration.objects.filter(rec_id=ids).update(assembly_no=assembly_no,drawing_no=drawing_no,detection_workstation=detection_workstation,remark=remark,accept_status=accept_status,rejection_status=rejection_status)

            return JsonResponse({'status':'1'})
        
        return JsonResponse({'status':'0'})

      
 

class GetSerialNumber(View):
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

        
        # print(prv_data)
        return render(request, self.template_name,{'data':data })
      
 
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        ids = req.get('id')
        asset_type = req.get('asset_type')
        location_id = req.get('location_id')
        sub_location = req.get('sub_location')

        new_id = False
        if ids =="":
            new_id = True
        else:
            Find_Pids =PBSMaster.objects.filter(asset_type=asset_type,is_active=0)
            Find_Pid = Find_Pids[0]
            if Asset.objects.filter(id=ids,asset_type=Find_Pid.id,location_id=location_id,sub_location=sub_location).exists():
                asstDt = Asset.objects.filter(id=ids,asset_type=Find_Pid.id,location_id=location_id,sub_location=sub_location)
                gen_serialnumber = asstDt[0].asset_serial_number
                return JsonResponse({'status':'1','data':gen_serialnumber})
            else:
                new_id = True

        if new_id:

            serial_latest_id = 0
                 
            if AssetSerialNumberIDs.objects.filter(asset_type=asset_type,location_id=location_id,sub_location=sub_location).exists():
                AssetSerialNumberID = AssetSerialNumberIDs.objects.filter(asset_type=asset_type,location_id=location_id,sub_location=sub_location)
                serial_latest_id = AssetSerialNumberID[0].last_id

            new_serial_id = int(serial_latest_id) + 1

            gen_serialnumber = f"{asset_type}/{location_id}/{sub_location}/{new_serial_id:03}"

            if Asset.objects.filter(asset_serial_number=gen_serialnumber).exists():
                if AssetSerialNumberIDs.objects.filter(asset_type=asset_type,location_id=location_id,sub_location=sub_location).exists():
                    print('----update------')
                    AssetSerialNumberIDs.objects.filter(asset_type=asset_type,location_id=location_id,sub_location=sub_location).update(last_id=new_serial_id)
                else:
                    print('----add------')
                    ju = AssetSerialNumberIDs(asset_type=asset_type,location_id=location_id,sub_location=sub_location,last_id=new_serial_id)
                    ju.save()

                new_serial_id = int(serial_latest_id) + 2
                gen_serialnumber = f"{asset_type}/{location_id}/{sub_location}/{new_serial_id:03}"


            return JsonResponse({'status':'1','data':gen_serialnumber})


        return JsonResponse({'status':'0'})

class LocatioIDFromAssetType(View):
    template_name = 'asset_register.html'

    def get(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        req = request.GET
        data=[]
        asset_type = req.get('asset_type')
        if asset_type == "":
            return JsonResponse(data, safe=False)
        if user_Role == 1:
            # print(asset_config_id)
            location_id = Asset.objects.filter(is_active=0,asset_type=asset_type).distinct('location_id')
        else:
            location_id = Asset.objects.filter(is_active=0,asset_type=asset_type).distinct('location_id')
        for k in location_id:
            data.append({'option':k.location_id,
                         'id':k.location_id})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)
        # return render(request, self.template_name, {'sub_systems' : sub_systems, 'systems':systems})

class LocatioIDFromAssetTypeNcr(View):
    template_name = 'asset_register.html'

    def get(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        req = request.GET
        data=[]
        asset_type = req.get('asset_type')
        if asset_type == "":
            return JsonResponse(data, safe=False)


        Find_Pids =PBSMaster.objects.filter(asset_type=asset_type,is_active=0)
        Find_Pid = Find_Pids[0]
        
        asset_type = Find_Pid.id

        
        if user_Role == 1:
            # print(asset_config_id)
            location_id = Asset.objects.filter(is_active=0,asset_type=asset_type).distinct('location_id')
        else:
            location_id = Asset.objects.filter(is_active=0,asset_type=asset_type).distinct('location_id')
        for k in location_id:
            data.append({'option':k.location_id,
                         'id':k.location_id})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)
        # return render(request, self.template_name, {'sub_systems' : sub_systems, 'systems':systems})


class GetAllSerialNumber(View):
    template_name = 'asset_register.html'

    def get(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        req = request.GET
        data=[]
        asset_type = req.get('asset_type')
        location_id = req.get('location_id')
        sel_car = req.get('sel_car')

     
        if user_Role == 1:
            # print(asset_config_id)
            asset_serial_number = Asset.objects.filter(is_active=0)
        else:
            asset_serial_number = Asset.objects.filter(is_active=0)

        if asset_type != "all":
            asset_serial_number=asset_serial_number.filter(asset_type=asset_type)

        if location_id != "all":
            asset_serial_number=asset_serial_number.filter(location_id=location_id)

        if sel_car != "all":
            asset_serial_number=asset_serial_number.filter(sub_location=sel_car)

        for k in asset_serial_number:
            data.append({'option':k.asset_serial_number,
                         'id':k.asset_config_id})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)
        # return render(request, self.template_name, {'sub_systems' : sub_systems, 'systems':systems})

class GetAllSerialNumberNcr(View):
    template_name = 'asset_register.html'

    def get(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_Role = request.session.get('user_Role')
        req = request.GET
        data=[]
        asset_type = req.get('asset_type')
        location_id = req.get('location_id')
        sel_car = req.get('sel_car')

     
        if user_Role == 1:
            # print(asset_config_id)
            asset_serial_number = Asset.objects.filter(is_active=0)
        else:
            asset_serial_number = Asset.objects.filter(is_active=0)

        if asset_type != "":

            Find_Pids =PBSMaster.objects.filter(asset_type=asset_type,is_active=0)
            Find_Pid = Find_Pids[0]
            
            asset_type = Find_Pid.id

            asset_serial_number=asset_serial_number.filter(asset_type=asset_type)

        for k in asset_serial_number:
            data.append({'option':k.asset_serial_number,
                         'id':k.asset_serial_number})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)
        # return render(request, self.template_name, {'sub_systems' : sub_systems, 'systems':systems})



class DwdEIR(View):
    template_name = 'dwd_eir.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]

        EIRGeneration_datas =EIRGeneration.objects.filter(eir_id=id)
        jb = EIRGeneration_datas[0]
        ast_data = Asset.objects.filter(id=jb.failure_id.location_id)

        FailureDatas=FailureData.objects.filter(id=jb.failure_id.id)
        datas = FailureDatas[0]

        PBSMaster_datas=PBSMaster.objects.filter(id=FailureDatas[0].asset_type)


        full_path2 = jb.signature_img2
        if full_path2 == None:
            relative_path2 = None
        else:
            # Find the index of /static
            index2 = full_path2.find("/static")
            if index2 != -1:
                relative_path2 = full_path2[index2 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path2 = relative_path2.lstrip("/")
            else:
                relative_path2 = full_path2  # fallback if /static not found


        full_path3 = jb.signature_img3
        if full_path3 == None:
            relative_path3 = None
        else:
            # Find the index of /static
            index3 = full_path3.find("/static")
            if index3 != -1:
                relative_path3 = full_path3[index3 + len("/static"):]  # remove /static as well
                # optionally remove leading slash
                relative_path3 = relative_path3.lstrip("/")
            else:
                relative_path3 = full_path3  # fallback if /static not found

       
        data={ 
            'eir_id' :  jb.eir_id,
            'train_set_no' : ast_data[0].location_id,
            'date' : jb.failure_id.date,
            'time' : jb.failure_id.time,
            'department' : jb.failure_id.department,
            'eir_gen_id' : jb.eir_gen_id,
            'depot' : jb.depot,
            'addressed_by':jb.addressed_by,
            'incident_details' : jb.incident_details,
            'repercussion':jb.repercussion,
            'id':jb.eir_id,
            'user_Role':user_Role,
            'incident_location' : jb.incident_location,
            'incident_time' : jb.incident_time,
            'sel_car' : jb.failure_id.sel_car,
            'equipment' : jb.failure_id.equipment,
            'component' : jb.component,
            'location': jb.failure_id.location,
            'immediate_investigation':jb.failure_id.immediate_investigation,

            'action_taken_in_depot': jb.action_taken_in_depot,
            'concern': jb.concern,
            'further_action': jb.further_action,
            'TRSL':jb.TRSL,
            'signature_img2':relative_path2,
            'signature_img3':relative_path3,


        }


        prv_data = []
        EIRGeneration_datas_prvdatas = EIRGeneration.objects.filter(failure_id__equipment=jb.failure_id.equipment,component=jb.component).exclude(eir_id=id)
        st_gen = 0
        for jbr in EIRGeneration_datas_prvdatas:
            st_gen = st_gen + 1
            ast_data = Asset.objects.filter(id=jbr.failure_id.location_id)

            prv_data.append({ 
                'st_gen':st_gen,
                'eir_gen_id' :  jbr.eir_gen_id,
                'date' : jbr.failure_id.date,
                'depot' : jbr.depot,
                'train_set_no' : ast_data[0].location_id,
                'sel_car' : jbr.failure_id.sel_car,
                'incident_location' : jbr.incident_location,
                'incident_time' : jbr.incident_time,
                'id':jbr.eir_id,
            })

        job_details = []
        job_detailsArr = InvestigationDetails.objects.filter(eir_dt_id=jb.eir_id,is_active=0)
        st = 0
        for jdar in job_detailsArr:
            st = st + 1
            job_details.append({ 
                'details_id' :  jdar.details_id,
                'non_compliance_details' : jdar.non_compliance_details,
                'onvestigation_details' : jdar.onvestigation_details,
                'relevant_ERTS_clause' : jdar.relevant_ERTS_clause,
                's_no' : st,
            })

        images = []
        imgArr = EIRImages.objects.filter(eir_dt_id=jb.eir_id,is_active=0)
        for jdar in imgArr:

            full_path6 = jdar.file_path
            if full_path6 == None:
                relative_path6 = None
            else:
                # Find the index of /static
                index6 = full_path6.find("/static")
                if index6 != -1:
                    relative_path6 = full_path6[index6 + len("/static"):]  # remove /static as well
                    # optionally remove leading slash
                    relative_path6 = relative_path6.lstrip("/")
                else:
                    relative_path6 = full_path6  # fallback if /static not found

            images.append({ 
                'img_id' :  jdar.img_id,
                'file_path' : relative_path6,
            })


        # print(prv_data)
        return render(request, self.template_name,{'data':data ,'prv_data':prv_data , 'job_details':job_details, 'images':images })




class DwdNCR(View):
    template_name = 'dwd_ncr.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]

        NCRGeneration_datas =NCRGeneration.objects.filter(rec_id=id)
        jb = NCRGeneration_datas[0]

        PBSMaster_datas=PBSMaster.objects.filter(id=jb.rootcause_id.asset_type)

        Defect_datas=Defect.objects.filter(defect_id=jb.rootcause_id.defect.defect_id)

        current_time = datetime.datetime.now().strftime("%H:%M")
        today_date = date.today()

        if jb.defect_time == None or jb.defect_time == "":
            defect_time = current_time
        else:
            time_obj1 = datetime.datetime.strptime(jb.defect_time, "%H:%M")
            defect_time = time_obj1.strftime("%I:%M %p")

        if jb.defect_date == None or jb.defect_date == "":
            defect_date = Defect_datas[0].defect_open_date
        else:
            defect_date = datetime.datetime.strptime(jb.defect_date, "%Y-%m-%d").date() 

        if jb.corrective_action_date == None or jb.corrective_action_date == "":
            corrective_action_date = today_date
        else:
            corrective_action_date = datetime.datetime.strptime(jb.corrective_action_date, "%Y-%m-%d").date() 


        if jb.approved_date == None or jb.approved_date == "":
            approved_date = today_date
        else:
            approved_date = datetime.datetime.strptime(jb.approved_date, "%Y-%m-%d").date() 

        if jb.action_date == None or jb.action_date == "":
            action_date = today_date
        else:
            action_date = datetime.datetime.strptime(jb.action_date, "%Y-%m-%d").date() 

        if jb.verification_date == None or jb.verification_date == "":
            verification_date = today_date
        else:
            verification_date = datetime.datetime.strptime(jb.verification_date, "%Y-%m-%d").date() 

        if jb.fnl_date == None or jb.fnl_date == "":
            fnl_date = today_date
        else:
            fnl_date = datetime.datetime.strptime(jb.fnl_date, "%Y-%m-%d").date() 

        if jb.defect_description == None or jb.defect_description == "":
            defect_description = Defect_datas[0].defect_description
        else:
            defect_description = jb.defect_description


        time_obj = datetime.datetime.strptime(jb.time, "%H:%M:%S")
        formatted_time = time_obj.strftime("%I:%M %p")

        data={ 
            'ncr_gen_id' :  jb.ncr_gen_id,
            'date' : datetime.datetime.strptime(jb.date, "%Y-%m-%d").date(),
            'time' : formatted_time,
            'id':jb.rec_id,
            'user_Role':user_Role,
            'defect_time':defect_time,
            'defect_date':defect_date,
            'corrective_action_date':corrective_action_date,
            'approved_date':approved_date,
            'action_date':action_date,
            'verification_date':verification_date,
            'fnl_date':fnl_date,
            'project_name':PBSMaster_datas[0].project.product_name,
            'defect_description':defect_description,

            'inspector_name':jb.inspector_name,
            'assembly_name':jb.assembly_name,
            'assembly_no':jb.assembly_no,
            'drawing_no':jb.drawing_no,
            'detection_workstation':jb.detection_workstation,
            'location_id':jb.location_id,
            'sel_car':jb.sel_car,
            'serial_no':jb.serial_no,
            'green_red_channel':jb.green_red_channel,

            'chkMinor':jb.chkMinor,
            'chkMajor':jb.chkMajor,
            'chkCritical':jb.chkCritical,

            'specification':jb.specification,
            'defect_source':jb.defect_source,
            'supplier_name':jb.supplier_name,
            'defect_location':jb.defect_location,
            'defect_detected_by':jb.defect_detected_by,
            'defect_detected_workstation':jb.defect_detected_workstation,
            'no_of_parts_deloverd':jb.no_of_parts_deloverd,
            'no_of_defective_parts':jb.no_of_defective_parts,

            'active_deviations':jb.active_deviations,
            'chk_Internal':jb.chk_Internal,
            'chk_Supplier':jb.chk_Supplier,
            'chk_TWL':jb.chk_TWL,
            'chk_Transportation':jb.chk_Transportation,

            'ok_img':jb.ok_img,
            'notok_img':jb.notok_img,
            'signature_img':jb.signature_img,
            'signature_img2':jb.signature_img2,
            'signature_img3':jb.signature_img3,
            'signature_img4':jb.signature_img4,
            'signature_img5':jb.signature_img5,


            'initial_analysis':jb.initial_analysis,
            'attachments_files':jb.attachments_files,
            'responsibility':jb.responsibility,
            'invoice_number':jb.invoice_number,
            'non_conforming_part_disposition':jb.non_conforming_part_disposition,
            'responsible_for_execution':jb.responsible_for_execution,
            'containment_action':jb.containment_action,
            'corrective_action_by':jb.corrective_action_by,
            'corrective_action_designation':jb.corrective_action_designation,
            'approved_by':jb.approved_by,
            'approved_designation':jb.approved_designation,
            'action_name':jb.action_name,
            'verification_name':jb.verification_name,
            'inp_root_cause':jb.inp_root_cause,
            'occurrence':jb.occurrence,
            'detection':jb.detection,
            'effectiveness':jb.effectiveness,

            'cost_1':jb.cost_1,
            'cost_2':jb.cost_2,
            'cost_3':jb.cost_3,
            'cost_4':jb.cost_4,
            'cost_5':jb.cost_5,
            'cost_6':jb.cost_6,
            'total_cost':jb.total_cost,


            'no_of_day_open':jb.no_of_day_open,
            'physical_closure':jb.physical_closure,
            'physical_closure_rca_capa':jb.physical_closure_rca_capa,
            'fnl_name':jb.fnl_name,
            'fnl_designation':jb.fnl_designation,

            'root_cause_analysis':jb.root_cause_analysis,
            'ncr_status':jb.ncr_status,

            'rev_no' : jb.rev_no,


        }


        if user_Role == 1:
            train_set_options = Asset.objects.filter(is_active=0).distinct('location_id')
        else:
            train_set_options = Asset.objects.filter(is_active=0,P_id=P_id).distinct('location_id')


        Corrective_data = []
        if user_Role == 1:
            CorrectiveAction_data =CorrectiveAction.objects.filter(is_active=0,defect_id=jb.rootcause_id.defect)
        else:
            CorrectiveAction_data =CorrectiveAction.objects.filter(is_active=0,P_id=P_id,defect_id=jb.rootcause_id.defect)

        for CorrectiveActions in CorrectiveAction_data:
            Corrective_data.append({ 
                'corrective_action_id' : CorrectiveActions.corrective_action_id,
                'corrective_action_owner' : CorrectiveActions.corrective_action_owner,
                'corrective_action_description' : CorrectiveActions.corrective_action_description,
                'corrective_action_update' : CorrectiveActions.corrective_action_update,
                'corrective_action_status' : CorrectiveActions.corrective_action_status,
            })     

        imageList = NCRImagesList.objects.filter(is_active=0,ncr_gen_id=jb.rec_id)

        return render(request, self.template_name,{'data':data ,'train_set_options':train_set_options,'Corrective_data':Corrective_data,'imageList':imageList })

       


class ImportKilometreReadingForm(View):
    template_name = 'importkilometre_reading.html'

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
            # print(cols_count)
            if(cols_count is not 35):
                message='The excel file is not in the required format'
                return render(request, self.template_name, {"message": message})


            valid = False

            if sheet.cell_value(0,0) != "Dates":
                message="Invalid header: A1 must be 'Dates'"
                return render(request, self.template_name, {"message": message})
            else:
                valid = True
                # Loop B1 to AI1 (columns 2 to 35 → TS#01 to TS#34)
                for col in range(1, 35):  # 2 = B, 35 = AI
                    expected = f"TS#{col:02d}"  # TS#01, TS#02, ..., TS#34
                    cell_value = sheet.cell_value(1,col)

                    if cell_value != expected:
                        message= f"Invalid header at column {col}: expected {expected}, got {cell_value}"
                        valid = False
                        return render(request, self.template_name, {"message": message})

           
            asset_type_array=[]

            if valid :
                # return render(request, self.template_name, {"message": 'required format'})

                for row in range(2, row_count):
                    date= sheet.cell_value(row,0)
                    err_status = '1'

                    date_err = '1'
                
                    if date == "":
                        date_err = 'Empty'
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

                    row_data = {
                        'id': row,
                        'date': date,
                        'date_err': date_err,
                        'err_status': '1'
                    }

                    # Loop through TS01 → TS34 (columns 2 → 35)
                    for col in range(1, 35):
                        ts_key = f"TS{col:02d}"       # TS01, TS02, ..., TS34
                        ts_err_key = f"{ts_key}_err"

                        ts_value = sheet.cell_value(row,col)
                        ts_err = '1' if ts_value not in (None, "") else 'Empty'

                        row_data[ts_key] = ts_value
                        row_data[ts_err_key] = ts_err

                        if ts_err != '1':
                            row_data['err_status'] = '0'  # mark error if any TS is empty

                    if date_err != '1':
                        row_data['err_status'] = '0'

                    data.append(row_data)

            else:
                message='The excel file is not in the required format'
                return render(request, self.template_name, {"message": message})
        else:
            message='The file selected is not excel document'
            return render(request, self.template_name, {"message": message})
        return render(request, self.template_name, {"data": data,"status":"1"})
    
   



class AddImportKilometreReading(View):
    template_name = 'importkilometre_reading.html'
    
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
                    date = datetime.datetime.strptime(items['date'], '%d-%m-%Y').strftime('%Y-%m-%d')
                    if KilometreReading.objects.filter(date=date).exists(): 
                        KilometreReading.objects.filter(date=date).update(ts01_tkm=items['TS01'],ts02_tkm=items['TS02'],ts03_tkm=items['TS03'],ts04_tkm=items['TS04'],ts05_tkm=items['TS05'],ts06_tkm=items['TS06'],ts07_tkm=items['TS07'],ts08_tkm=items['TS08'],ts09_tkm=items['TS09'],ts10_tkm=items['TS10'],ts11_tkm=items['TS11'],ts12_tkm=items['TS12'],ts13_tkm=items['TS13'],ts14_tkm=items['TS14'],ts15_tkm=items['TS15'],ts16_tkm=items['TS16'],ts17_tkm=items['TS17'],ts18_tkm=items['TS18'],ts19_tkm=items['TS19'],ts20_tkm=items['TS20'],ts21_tkm=items['TS21'],ts22_tkm=items['TS22'],ts23_tkm=items['TS23'],ts24_tkm=items['TS24'],ts25_tkm=items['TS25'],ts26_tkm=items['TS26'],ts27_tkm=items['TS27'],ts28_tkm=items['TS28'],ts29_tkm=items['TS29'],ts30_tkm=items['TS30'],ts31_tkm=items['TS31'],ts32_tkm=items['TS32'],ts33_tkm=items['TS33'],ts34_tkm=items['TS34'])

                        updated+=1

                    else:
                        j = KilometreReading(date=date,ts01_tkm=items['TS01'],ts02_tkm=items['TS02'],ts03_tkm=items['TS03'],ts04_tkm=items['TS04'],ts05_tkm=items['TS05'],ts06_tkm=items['TS06'],ts07_tkm=items['TS07'],ts08_tkm=items['TS08'],ts09_tkm=items['TS09'],ts10_tkm=items['TS10'],ts11_tkm=items['TS11'],ts12_tkm=items['TS12'],ts13_tkm=items['TS13'],ts14_tkm=items['TS14'],ts15_tkm=items['TS15'],ts16_tkm=items['TS16'],ts17_tkm=items['TS17'],ts18_tkm=items['TS18'],ts19_tkm=items['TS19'],ts20_tkm=items['TS20'],ts21_tkm=items['TS21'],ts22_tkm=items['TS22'],ts23_tkm=items['TS23'],ts24_tkm=items['TS24'],ts25_tkm=items['TS25'],ts26_tkm=items['TS26'],ts27_tkm=items['TS27'],ts28_tkm=items['TS28'],ts29_tkm=items['TS29'],ts30_tkm=items['TS30'],ts31_tkm=items['TS31'],ts32_tkm=items['TS32'],ts33_tkm=items['TS33'],ts34_tkm=items['TS34'])
                        j.save()

                        inserted+=1

        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        FindUser = UserProfile.objects.filter(user_id=user_ID)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        meg ="Insert "+str(inserted)+" record and Update "+str(updated)+" record to Daily Kilometre Reading"
        h = history(user_id=FindUser[0].id,P_id=P_id,date=datetime.date.today(),time=current_time,message=meg,function_name="Import Daily Kilometre Reading")
        h.save()
        return JsonResponse({'status':'1','inserted': inserted,'updated': updated})
   
   


class ViewDowntimeMaintenanceLog(View):
    template_name = 'downtime_maintenance_log.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
     
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):

        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        # req = request.POST
        # print(req)
        print('==========HERE=========')
       
        DowntimeMaintenanceLogDt = DowntimeMaintenanceLog.objects.filter().order_by('-date')
        print(DowntimeMaintenanceLogDt)
       
        for jb in DowntimeMaintenanceLogDt:

            data.append({
                'id':jb.log_id,
                'date':jb.date,
                'dt_sc' : jb.dt_sc,
                'dt_opm' : jb.dt_opm,
                'dt_cm' : jb.dt_cm,
                'user_Role':user_Role

            })
          
        print(data)
        return JsonResponse({'data':data, 'user_Role':user_Role })



class AddDowntimeMaintenanceLog(View):
    template_name = 'add_downtime_maintenance_log.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        user_Role = request.session.get('user_Role')
        P_id = request.session['P_id']
        if user_Role == 4:
            return redirect('/dashboard/')
        id = kwargs.get("id")
        data=[]

        today_date = date.today()

        if id == "" or id == None:
            cust_date = datetime.datetime.strptime(str(today_date), '%Y-%m-%d').strftime('%Y-%m')
            cust_date = f"{cust_date}-01"
            if DowntimeMaintenanceLog.objects.filter(date=cust_date).exists():
                setDt = DowntimeMaintenanceLog.objects.filter(date=cust_date)
                id = setDt[0].log_id
            print(cust_date)

        if id == "" or id == None:
            data={ 
                'id' : '',
                'date' : today_date,
                'dt_sc' : 0,
                'dt_opm' : 0,
                'dt_cm' : 0,
            }
        else:
            record = DowntimeMaintenanceLog.objects.filter(log_id=id).first()
            if record:
                data={ 
                    'id' : id,
                    'date':record.date,
                    'dt_sc' : record.dt_sc,
                    'dt_opm' : record.dt_opm,
                    'dt_cm' : record.dt_cm,
                }


        # print(prv_data)
        return render(request, self.template_name,{ 'data':data })
      
 
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        req = request.POST
        cursor = connection.cursor()
        # print(req)
        ids = req.get('id')

        date = datetime.datetime.strptime(req.get('date'), '%m/%Y').strftime('%Y-%m')
        print(date)
        date = f"{date}-01"

        if DowntimeMaintenanceLog.objects.filter(date=date).exists(): 
            DowntimeMaintenanceLog.objects.filter(date=date).update(dt_sc=req.get('dt_sc'),dt_opm=req.get('dt_opm'),dt_cm=req.get('dt_cm'))
            return JsonResponse({'status':'1','message':'success'})

        else:
            j = DowntimeMaintenanceLog(date=date,dt_sc=req.get('dt_sc'),dt_opm=req.get('dt_opm'),dt_cm=req.get('dt_cm'))
            j.save()

            return JsonResponse({'status':'1','message':'success'})

        return JsonResponse({'status':'0','message':'Failed to save Downtime Maintenance Log'})


class DeleteDowntimeMaintenanceLog(View):
    template_name = 'downtime_maintenance_log.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        # print(req)
        id = req.get('id')
        DowntimeMaintenanceLog.objects.filter(log_id=id).delete()
        return JsonResponse({'status':'1'})
            


