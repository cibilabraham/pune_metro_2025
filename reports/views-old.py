from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from fracas.models import Asset,Defect, CorrectiveAction, ReviewBoard, DefectDiscussion, FailureData, Action, RootCause, PBSMaster
from django.views import View

from datetime import datetime, date, timedelta
import isoweek
#import datetime
from pandas.tseries import offsets
import calendar
import numpy as np
import random
import math

import pdfkit
from fracas.models import *
from django.db.models import Sum

class ReviewBoardMinutesDownloadView(View):
    template_name = 'review_details.html'

    def get(self, request, *args, **kwargs):
        pdfkit.from_file('review_details.html', 'micro.pdf')
        return render(request, self.template_name, {})


# Create your views here.
class Project(View):

    def get(self, request, *args, **kwargs):
        data = []
        req = request.GET
        project = req.get('project')
        system = PBSMaster.objects.filter(project_id=project,is_active=0).distinct('system')
        for k in system:
            data.append({'system':k.system})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)

class SystemSubsystem(View):
    template_name = 'defect_status_report.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        data = []
        system = req.get('system')
        sub_systems = PBSMaster.objects.filter(system=system,is_active=0).distinct('subsystem')
        for k in sub_systems:
            data.append({'subsystem':k.subsystem})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)
        # return render(request, self.template_name, {'sub_systems' : sub_systems, 'systems':systems})
class Products(View):
    template_name = 'defect_status_report.html'

    def get(self, request, *args, **kwargs):
        data = []
        req = request.GET
        system = req.get('system')
        sub_system = req.get('sub_system')
        asset_type = req.get('asset_type')
        products = PBSMaster.objects.filter(system=system, subsystem=sub_system, asset_type=asset_type).distinct('product_id')
        print(products,"looooooooooooooooooooooo")
        for k in products:
            data.append({'product_id':k.product_id})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)

class AssetTypes(View):
    template_name = 'defect_status_report.html'

    def get(self, request, *args, **kwargs):
        data = []
        req = request.GET
        subsystem = req.get('subsystem')
        # product_id = req.get('product_id')
        asset_types = PBSMaster.objects.filter(subsystem=subsystem,is_active=0).distinct('asset_type')
        for k in asset_types:
            data.append({'asset_type':k.asset_type,'id':k.id})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)
    
class DefectTypes(View):
    template_name = 'defect_status_report.html'

    def get(self, request, *args, **kwargs):
        data = []
        req = request.GET
        LRUType = req.get('LRUType')
        # product_id = req.get('product_id')
        Defects = Defect.objects.filter(asset_type=LRUType,is_active=0).distinct('defect_id')
        for k in Defects:
            data.append({'defect_id':k.defect_id,'des':k.defect_description})
        # response = {'data' : data}
        return JsonResponse(data, safe=False)

class defectStatus(View):
    template_name = 'defect_status_report.html'

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
        return render(request, self.template_name, {'project' : project})

    def post(self, request, *args, **kwargs):
        data = []
        req = request.POST
        project = req.get('project')
        system = req.get('system')
        sub_system = req.get('sub_system')
        product_id = req.get('product_id')
        lru_type = req.get('lru_type')
        print(system,sub_system,product_id,lru_type)
        
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            defect_data=Defect.objects.filter(is_active=0)
        else:
            defect_data=Defect.objects.filter(is_active=0,P_id=P_id)
            
        if project != "all":
            SUBSYSTEM=PBSMaster.objects.filter(project_id=project)
            a=[]
            for SUB in SUBSYSTEM:
                a.append(SUB.id)
            defect_data=defect_data.filter(asset_type__in=a) 
            
            if system != "all":
                SUBSYSTEM=PBSMaster.objects.filter(system=system)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                defect_data=defect_data.filter(asset_type__in=a) 
            
                if sub_system != "all":
                    SUBSYSTEM=PBSMaster.objects.filter(subsystem=sub_system)
                    a=[]
                    for SUB in SUBSYSTEM:
                        a.append(SUB.id)
                    defect_data=defect_data.filter(asset_type__in=a) 
                    
                    if lru_type != "all":
                        defect_data=defect_data.filter(asset_type=lru_type)
                        
        if req.get('start_date') !="" and req.get('end_date') !="":
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            defect_data=defect_data.filter(defect_open_date__range=[start_date,end_date])
        
        for Defects in defect_data:
            if CorrectiveAction.objects.filter(defect_id = Defects.defect_id,is_active=0).exists():
                action = [];
                CorrectiveAction_data=CorrectiveAction.objects.filter(defect_id = Defects.defect_id,is_active=0)
                for CorrectiveActions in CorrectiveAction_data:
                    action.append({
                    "corrective_action_description" :CorrectiveActions.corrective_action_description,
                    "corrective_action_update"       : CorrectiveActions.corrective_action_update
                    }) 
            else:
                action = [];
            data.append({ 
                "defect_id" :  Defects.defect_id,
                "defect_description" : Defects.defect_description,
                "defect_status" : Defects.defect_status,
                "oem_defect_reference" : Defects.oem_defect_reference,
                "target_date" : Defects.oem_target_date,
                "action":action
                })   
        return JsonResponse({'data':data})
            
        
        # asset_types = []
        # pbs_asset_types = []
        # if system == "all":
        #     pbs_asset_types = PBSMaster.objects.all()
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.id)
        # if sub_system == "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.id)
        # if product_id == "all" and lru_type != "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem_id=sub_system, id=lru_type)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.id)
        # if lru_type == "--All--":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem_id=sub_system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.id)
        # if (sub_system == "all" or product_id == "all" or lru_type == "--All--") and not start_date and not end_date:
        #     print("11111111")
        #     defect_data = Defect.objects.filter(asset_type__in=asset_types).order_by('asset_type')
        # elif (sub_system and lru_type == "--All--" and not product_id) and not start_date and not end_date:
        #     print("22222222")
        #     defect_data = Defect.objects.filter(asset_type__in=asset_types).order_by('asset_type')
        # elif sub_system == "all" and start_date and end_date:
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     defect_data = Defect.objects.filter(defect_open_date__range=[formated_start_date,formated_end_date], asset_type__in=asset_types)
        # elif product_id == "all" and start_date and end_date:
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     defect_data = Defect.objects.filter(defect_open_date__range=[formated_start_date,formated_end_date], asset_type__in=asset_types)
        # elif lru_type == "--All--" and start_date and end_date:
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     defect_data = Defect.objects.filter(defect_open_date__range=[formated_start_date,formated_end_date], asset_type__in=asset_types)
        # elif lru_type and lru_type != "--All--" and start_date and end_date:
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     defect_data = Defect.objects.filter(defect_open_date__range=[formated_start_date,formated_end_date], asset_type=lru_type).order_by('asset_type')
        # elif lru_type and lru_type != "--All--":
        #     defect_data = Defect.objects.filter(asset_type=lru_type).order_by('asset_type')
        # elif system == "all" and start_date and end_date:
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     defect_data = Defect.objects.filter(defect_open_date__range=[formated_start_date,formated_end_date], asset_type__in=asset_types)
        #     print(defect_data)
        # else:
        #     defect_data = Defect.objects.all().order_by('asset_type')
        # data = []
        # for  defect in defect_data:
        #     correctiveaction =CorrectiveAction.objects.filter(defect = defect)
        #     action = [];
        #     actions ={}
        #     for correctiveactions in correctiveaction:
        #         action.append({
        #                    "corrective_action_description" :correctiveactions.corrective_action_description,
        #                    "corrective_action_update"       : correctiveactions.corrective_action_update
        #                     })        
        #     data.append({ 
        #         "defect_id" :  defect.defect_id,
        #         "defect_description" : defect.defect_description,
        #         "defect_status" : defect.defect_status,
        #         "oem_defect_reference" : defect.oem_defect_reference,
        #         "target_date" : defect.oem_target_date,
        #         "action":action

        #                })            
        # #data = [defect_data.to_dict_json() for defect in defect_data]
        # response = {'data' : data}
        # return JsonResponse(response)

class ReviewBoardView(View):
    template_name = 'review_board.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        data=[]
        if user_Role == 1:
            review_board = ReviewBoard.objects.filter(is_active=0)
        else:
            review_board = ReviewBoard.objects.filter(is_active=0,P_id=P_id)
        for a in review_board:
            if PBSMaster.objects.filter(id=a.asset_type,is_active=0).exists():
                PBSMaster_data=PBSMaster.objects.filter(id=a.asset_type,is_active=0)
                for i in PBSMaster_data:
                    data.append({ 
                        'asset_type' :  i.asset_type,
                        'from_date' : a.from_date,
                        'to_date' : a.to_date,
                        'meeting_date' : a.meeting_date,
                        'meeting_id':a.meeting_id,
                        'id':a.id,
                    })
        return JsonResponse({'data':data})


class ReviewBoardDetailsView(View):
    template_name = 'review_details.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        meeting_id = req.get('meeting_id')

        try:
            review_board = ReviewBoard.objects.get(id=meeting_id)
        except:
            pass
        meeting_date = review_board.meeting_date
        deffect_discussions = DefectDiscussion.objects.filter(review_board=review_board)
        attendees = []
        final_deffects = []
        final_actions = []
        user_roles_data = Group.objects.all()
        for deffect_discussion in deffect_discussions:
            deffect_obj = Defect.objects.get(defect_id=deffect_discussion.defect.defect_id)
            failure_count = FailureData.objects.filter(defect=deffect_discussion.defect).exclude(failure_type='Other').count()

            corrective_actions = deffect_obj.correctiveaction_set.all()
            root_causes = deffect_obj.rootcause_set.all()

            diffects = {'defect_id':deffect_obj.defect_id,
                        'failure_count':failure_count,
                        'corrective_actions':corrective_actions,
                        'defect_status':deffect_obj.defect_status,
                        'oem_number':deffect_obj.oem_defect_reference,
                        'asset_type':deffect_obj.asset_type,
                        'oem_target_date':deffect_obj.oem_target_date,
                        'root_causes':root_causes}

            final_deffects.append(diffects)
            actions = Action.objects.filter(defect_discussion_id=deffect_discussion.defect_discussion_id)
            for action in actions:
                if action not in final_actions:
                    target_date = action.defect_discussion_id.defect.oem_target_date
                    if action.action_status == 'open' and (target_date - meeting_date).days < -7:
                        color = "badge-danger" #Red color                    
                    elif action.action_status == 'open' and (target_date - meeting_date).days > 7:
                        color = "badge-warning" #Yellow color
                    else:
                        color = "badge-success" #Green color
                            
                    final_actions.append({'action':action, 'cls':color})
            for attende in deffect_discussion.attendees.all():
                if attende not in attendees:
                    attendees.append(attende)

        return render(request, self.template_name, {'attendees' : attendees, 
                                                    'review_date':review_board.meeting_date,
                                                    'final_deffects':final_deffects,
                                                    'final_actions':final_actions,
                                                    'user_roles':user_roles_data,
                                                    'meeting_id':meeting_id,
                                                    })



class RootCauseCorrectiveStatusView(View):
    template_name = 'rootcause_corrective_status.html'

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
        return render(request, self.template_name, {'project' : project})

    def post(self, request, *args, **kwargs):

        req = request.POST
        project = req.get('project')
        system = req.get('system')
        sub_system = req.get('sub_system')
        product_id = req.get('product_id')
        lru_type = req.get('lru_type')
        start_date = req.get('start_date')
        end_date = req.get('end_date')
        defect_id = req.get('defect_id')
        data=[]
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            RootCause_data=RootCause.objects.filter(is_active=0)
        else:
            RootCause_data=RootCause.objects.filter(is_active=0,P_id=P_id)
            
        if project != "all":
            SUBSYSTEM=PBSMaster.objects.filter(project_id=project)
            a=[]
            for SUB in SUBSYSTEM:
                a.append(SUB.id)
            RootCause_data=RootCause_data.filter(asset_type__in=a) 
            
            if system != "all":
                SUBSYSTEM=PBSMaster.objects.filter(system=system)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                RootCause_data=RootCause_data.filter(asset_type__in=a)
            
                if sub_system != "all":
                    SUBSYSTEM=PBSMaster.objects.filter(subsystem=sub_system)
                    a=[]
                    for SUB in SUBSYSTEM:
                        a.append(SUB.id)
                    RootCause_data=RootCause_data.filter(asset_type__in=a) 
                    
                    if lru_type != "all":
                        RootCause_data=RootCause_data.filter(asset_type=lru_type)
                        
                        if defect_id != "all":
                            RootCause_data=RootCause_data.filter(defect_id=defect_id)
                            
        if req.get('start_date') !="" and req.get('end_date'):
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            RootCause_data=RootCause_data.filter(rca_workshop_date__range=[start_date,end_date])
        
        for RootCauses in RootCause_data:
            if CorrectiveAction.objects.filter(defect_id = RootCauses.defect,is_active=0).exists():
                CorrectiveAction_data=CorrectiveAction.objects.filter(defect_id = RootCauses.defect,is_active=0)
                for CorrectiveActions in CorrectiveAction_data:
                    data.append({
                        'defect_id':RootCauses.defect_id,
                        'root_cause_id':RootCauses.root_cause_id,
                        'root_cause_description':RootCauses.root_cause_description,
                        'root_cause_status':RootCauses.root_cause_status,
                        'corrective_action_id':CorrectiveActions.corrective_action_id,
                        'corrective_action_owner':CorrectiveActions.corrective_action_owner,
                        'corrective_action_description':CorrectiveActions.corrective_action_description,
                        'corrective_action_status':CorrectiveActions.corrective_action_status,
                    })
            else:
                data.append({
                    'defect_id':RootCauses.defect_id,
                    'root_cause_id':RootCauses.root_cause_id,
                    'root_cause_description':RootCauses.root_cause_description,
                    'root_cause_status':RootCauses.root_cause_status,
                    'corrective_action_id':'',
                    'corrective_action_owner':'',
                    'corrective_action_description':'',
                    'corrective_action_status':'',
                })
        return JsonResponse({'data':data})
    
        # asset_types = []
        # pbs_asset_types = []
        # if system == "all":
        #     pbs_asset_types = PBSMaster.objects.all()
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if sub_system == "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if product_id == "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem=sub_system, asset_type=lru_type)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if lru_type == "--All--":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem=sub_system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        

        # if (sub_system == "all" or product_id == "all" or lru_type == "--All--") and not start_date and not end_date and not defect_id:
        #     rootcause_datas = RootCause.objects.filter(asset_type__in=asset_types)
        
        # elif system=="all" and start_date and end_date and defect_id:
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     rootcause_datas = RootCause.objects.filter(defect__defect_id=defect_id, asset_type__in=asset_types, rca_workshop_date__range=[formated_start_date,formated_end_date])

        # elif system=="all" and start_date and end_date and not defect_id:
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     rootcause_datas = RootCause.objects.filter(asset_type__in=asset_types, rca_workshop_date__range=[formated_start_date,formated_end_date])

        # elif system=="all" and defect_id and not start_date and not end_date :
        #     rootcause_datas = RootCause.objects.filter(defect__defect_id=defect_id, asset_type__in=asset_types)

        # elif (sub_system == "all" or product_id == "all" or lru_type == "--All--") and start_date and end_date and not defect_id:
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     rootcause_datas = RootCause.objects.filter(asset_type__in=asset_types, rca_workshop_date__range=[formated_start_date,formated_end_date])

        # elif (sub_system == "all" or product_id == "all" or lru_type == "--All--") and defect_id and not start_date and not end_date:
        #     rootcause_datas = RootCause.objects.filter(asset_type__in=asset_types, defect__defect_id=defect_id)


        # elif lru_type and lru_type != "--All--" and start_date and end_date and defect_id:
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     rootcause_datas = RootCause.objects.filter(defect__defect_id=defect_id, asset_type=lru_type, rca_workshop_date__range=[formated_start_date,formated_end_date])
        
        # elif lru_type and lru_type != "--All--" and defect_id=='' and start_date=='' and end_date=='':
        #     rootcause_datas = RootCause.objects.filter(asset_type=lru_type)
        
        # elif defect_id and lru_type=='' and start_date=='' and end_date=='':
        #     rootcause_datas = RootCause.objects.filter(defect__defect_id=defect_id)
        
        # elif lru_type and lru_type != "--All--" and defect_id and start_date=='' and end_date=='':
        #     rootcause_datas = RootCause.objects.filter(defect__defect_id=defect_id, asset_type=lru_type)
        
        # elif start_date and end_date and defect_id=='' and lru_type=='':
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     rootcause_datas = RootCause.objects.filter(rca_workshop_date__range=[formated_start_date,formated_end_date])
        
        # elif lru_type  and lru_type != "--All--" and start_date and end_date and defect_id=='':
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     rootcause_datas = RootCause.objects.filter(asset_type=lru_type, rca_workshop_date__range=[formated_start_date,formated_end_date])
        
        # elif defect_id and start_date and end_date and lru_type=='':
        #     formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        #     rootcause_datas = RootCause.objects.filter(defect__defect_id=defect_id, rca_workshop_date__range=[formated_start_date,formated_end_date])
        
        # else:
        #     rootcause_datas = RootCause.objects.all()
        # data = []
        # root_cause = []
        # for rootcause_data in rootcause_datas:
        #     corrective_actions = CorrectiveAction.objects.filter(defect__defect_id=rootcause_data.defect.defect_id)
        #     for corrective_action in corrective_actions:
        #         data.append({'defect_id':rootcause_data.defect.defect_id,
        #                      'root_cause_id':rootcause_data.root_cause_id,
        #                      'root_cause_description':rootcause_data.root_cause_description,
        #                      'root_cause_status':rootcause_data.root_cause_status,
        #                      'corrective_action_id':corrective_action.corrective_action_id,
        #                      'corrective_action_owner':corrective_action.corrective_action_owner,
        #                      'corrective_action_description':corrective_action.corrective_action_description,
        #                      'corrective_action_status':corrective_action.corrective_action_status,
        #             })

        # response = {'data' : data}
        # return JsonResponse(response)

class MTBFvsTimeReportView(View):
    template_name = 'mtbf_time_report.html'

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
        Asset_data = Asset.objects.all().distinct('asset_type')
        defect_datas = Defect.objects.all().distinct('defect_id')
        systems = PBSMaster.objects.all().distinct('system')
        return render(request, self.template_name, {'project':project,'asset_data' : Asset_data, 'defect_datas' : defect_datas, 'systems':systems})

    def post(self, request, *args, **kwargs):

        req = request.POST
        project = req.get('project')
        system = req.get('system')
        sub_system = req.get('sub_system')
        FN_NAME = req.get('FN_NAME')
        product_id = req.get('product_id')
        lru_type = req.get('lru_type')
        
        data=[]
        data1=[]
        scale=[]
        asset_types = []
        pbs_asset_types = []
        
        if req.get('start_date') !="" and req.get('end_date') !="":
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            start_date = req.get('start_date')
            end_date = req.get('end_date')
        pbs_mtbf_value = ''
        
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        
        if user_Role == 1:
            Asset_data=Asset.objects.filter(is_active=0)
        else:
            Asset_data=Asset.objects.filter(is_active=0,P_id=P_id)
        pbs_master_data = PBSMaster.objects.filter(is_active=0)
        if FN_NAME == 'two':
            if project != "all":
                if Asset_data.filter(asset_type=lru_type,is_active=0).exists():
                    Asset_data=Asset_data.filter(asset_type=lru_type) 
                    pbs_master_data = pbs_master_data.filter(id=lru_type)
                else:
                    response = {'status':'1','data' : data, 'data1' : data1, 'scale':scale}
                    return JsonResponse(response)
        elif FN_NAME == 'three':
            if project != "all":
                SUBSYSTEM=PBSMaster.objects.filter(project_id=project,is_active=0,system=system)
                if not SUBSYSTEM.exists():
                    response = {'status':'1','data' : data, 'data1' : data1, 'scale':scale}
                    return JsonResponse(response)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                Asset_data=Asset_data.filter(asset_type__in=a) 
                pbs_master_data = pbs_master_data.filter(id__in=a)   
        else:
            if project != "all":
                SUBSYSTEM=PBSMaster.objects.filter(project_id=project,is_active=0)
                if not SUBSYSTEM.exists():
                    response = {'status':'1','data' : data, 'data1' : data1, 'scale':scale}
                    return JsonResponse(response)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                Asset_data=Asset_data.filter(asset_type__in=a) 
                pbs_master_data = pbs_master_data.filter(id__in=a)
        if FN_NAME == 'two':
            pbs_mtbf_value = pbs_master_data[0].MTBF
        elif FN_NAME == 'three':
            if Systems.objects.filter(project_id=project,System=system,is_active=0).exists():
                D_MTBF = Systems.objects.filter(project_id=project,System=system,is_active=0) 
                pbs_mtbf_value = D_MTBF[0].MTBF
            else:
                response = {'status':'2','data' : data, 'data1' : data1, 'scale':scale}
                return JsonResponse(response)
        else:
            D_MTBF = Product.objects.filter(product_id=project) 
            pbs_mtbf_value = D_MTBF[0].MTBF
        # for pbs in pbs_master_data:
        #     pbs_mtbf_value = pbs.MTBF
        
        for ASSET in Asset_data:
            asset_types.append(ASSET.asset_type)
        
      
        if (lru_type or asset_types) and asset_types!=['']: 

            if lru_type and lru_type!="all":
                if not FailureData.objects.filter(asset_type=lru_type, date__range=[start_date,end_date],is_active=0).exclude(failure_type='Other').exists():
                    response = {'status':'1','data' : data, 'data1' : data1, 'scale':scale}
                    return JsonResponse(response)
            else:
                if not FailureData.objects.filter(asset_type__in=asset_types, date__range=[start_date,end_date],is_active=0).exclude(failure_type='Other').exists():
                    response = {'status':'1','data' : data, 'data1' : data1, 'scale':scale}
                    return JsonResponse(response)
            
            if lru_type and lru_type!="all":
                asset_data = Asset.objects.filter(asset_type=lru_type,is_active=0)
            else:
                asset_data = Asset.objects.filter(asset_type__in=asset_types,is_active=0)
            if start_date and end_date : # coming start date and end date are used further calculation
                formated_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                formated_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
                # formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').date()
                # formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').date()
            else: # Took current year start date and end date are used further calculation
                formated_start_date = (date.today() - offsets.YearBegin()).date()
                formated_end_date = (date.today() + offsets.YearEnd()).date()
            number_of_days = (formated_end_date-formated_start_date).days
           
            # To get scale dates. If number of days greater than 150days scales took as months and otherwise took as weeks
            first_week_day = formated_start_date.weekday()
            first_week_sunday = formated_start_date + timedelta(days=(5-first_week_day))
            second_week_start_date = first_week_sunday + timedelta(days=1)
            # number_of_days = (formated_end_date-second_week_start_date).days
            if number_of_days % 7 == 0:
                weeks = number_of_days//7
            else:
                weeks = number_of_days/7
            if type(weeks)==float:
                week_number = int(weeks) + 2
            else:
                week_number = weeks + 1
            
            # to get week end date
            week_end_date = second_week_start_date + timedelta(days=week_number*7)
            asset_count = asset_data.count()
            cum_actual_failure_count = 0

            if lru_type and lru_type!="all":
                Hightest_date_of_failure = FailureData.objects.filter(asset_config_id__asset_type=lru_type, is_active=0).exclude(failure_type='Other').order_by('-date')
            else:
                Hightest_date_of_failure = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types,is_active=0).exclude(failure_type='Other').order_by('-date')

            print(Hightest_date_of_failure[0].date,'Hightest_date_of_failure')
            Hightest_date_of_failure = str(Hightest_date_of_failure[0].date)
            Hightest_date_of_failure = datetime.datetime.strptime(Hightest_date_of_failure, '%Y-%m-%d').strftime('%Y-%m-%d')
           

            for i in range(1, week_number+1):
                if FN_NAME == 'two':
                    lru_population_hours = (asset_count*24*7)*i # to get LRU Weekely Hours
                else:
                    lru_population_hours = (24*7)*i # to get LRU Weekely Hours
                actual_mtbf_value = 'null'
                # to get start/end dates of current week
                if i == 1:
                    week_start_date = formated_start_date
                    
                elif i == 2:
                    week_start_date = second_week_start_date
                else:
                    week_start_date = week_end_date + timedelta(days=1)
                if i ==1:
                    week_end_date = first_week_sunday
                else:
                    week_end_date = week_start_date + timedelta(days=6) 

                failure_count = 0
                if lru_type and lru_type!="all":
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[week_start_date,week_end_date],is_active=0).exclude(failure_type='Other').count()
                else:
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types, date__range=[week_start_date,week_end_date],is_active=0).exclude(failure_type='Other').count()
                
                if failure_count != 0:
                    cum_actual_failure_count = cum_actual_failure_count+failure_count
                if cum_actual_failure_count != 0:
                    actual_mtbf_value = round(lru_population_hours/cum_actual_failure_count,2)

                print(week_end_date,'week_end_date')
                week_end_date1 = datetime.datetime.strptime(str(week_end_date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                print(Hightest_date_of_failure,'Hightest_date_of_failure')
                if week_end_date1 < Hightest_date_of_failure or failure_count != 0 :
                    findUnit = PBSUnit.objects.filter()
                    if findUnit[0].MTBFMTBSAF == 'days':
                        if actual_mtbf_value != 'null':
                            actual_mtbf_value = round(actual_mtbf_value/24,2)                        
                    elif findUnit[0].MTBFMTBSAF == 'mins':
                        if actual_mtbf_value != 'null':
                            actual_mtbf_value = actual_mtbf_value *60
                    else:
                        actual_mtbf_value = actual_mtbf_value
                else:
                    actual_mtbf_value = 'null'

                data.append({'x':week_start_date.strftime('%Y-%m-%d'), 'y':actual_mtbf_value})
                data1.append({'x':week_start_date.strftime('%Y-%m-%d'), 'y':pbs_mtbf_value})
           
        else:
            data=[]
        response = {'data' : data, 'data1' : data1, 'scale':scale}
        return JsonResponse(response)

class LogPlotMtbfReportView(View):
    template_name = 'log_plot_mtbf.html'

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
        Asset_data = Asset.objects.all().distinct('asset_type')
        defect_datas = Defect.objects.all().distinct('defect_id')
        systems = PBSMaster.objects.all().distinct('system')
        return render(request, self.template_name, {'project':project,'asset_data' : Asset_data, 'defect_datas' : defect_datas, 'systems':systems})


    def post(self, request, *args, **kwargs):
        req = request.POST
        project = req.get('project')
        system = req.get('system')
        sub_system = req.get('sub_system')
        FN_NAME = req.get('FN_NAME')
        product_id = req.get('product_id')
        lru_type = req.get('lru_type')
        
        data=[]
        data1=[]
        data2=[]
        data3=[]
        scale = []
        slop_value = 0
        asset_types = []
        pbs_asset_types = []
        
        if req.get('start_date') !="" and req.get('end_date') !="":
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            start_date = req.get('start_date')
            end_date = req.get('end_date')
            given_start_date=(date.today() - offsets.YearBegin()).date()
        pbs_mtbf_value = 0
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        
        if user_Role == 1:
            Asset_data=Asset.objects.filter(is_active=0)
        else:
            Asset_data=Asset.objects.filter(is_active=0,P_id=P_id)
        pbs_master_data = PBSMaster.objects.filter(is_active=0)
        if FN_NAME == 'two':
            if project != "all":
               if Asset_data.filter(asset_type=lru_type,is_active=0).exists():
                    Asset_data=Asset_data.filter(asset_type=lru_type)
                    pbs_master_data = pbs_master_data.filter(id=lru_type)
               else:
                    response = {'status':'1','data' : data, 'data1' : data1, 'data2' : data2, 'slop':slop_value}
                    return JsonResponse(response)    
        elif FN_NAME == 'three':
            if project != "all":
                SUBSYSTEM=PBSMaster.objects.filter(project_id=project,is_active=0,system=system)
                if not SUBSYSTEM.exists():
                    response = {'status':'1','data' : data, 'data1' : data1, 'data2' : data2, 'slop':slop_value}
                    return JsonResponse(response)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                Asset_data=Asset_data.filter(asset_type__in=a) 
                pbs_master_data = pbs_master_data.filter(id__in=a)
        else:
            if project != "all":
                SUBSYSTEM=PBSMaster.objects.filter(project_id=project,is_active=0)
                if not SUBSYSTEM.exists():
                    response = {'status':'1','data' : data, 'data1' : data1, 'data2' : data2, 'slop':slop_value}
                    return JsonResponse(response)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                Asset_data=Asset_data.filter(asset_type__in=a) 
                pbs_master_data = pbs_master_data.filter(id__in=a)
        if FN_NAME == 'two':
            pbs_mtbf_value = pbs_master_data[0].MTBF
        elif FN_NAME == 'three':
            if Systems.objects.filter(project_id=project,System=system,is_active=0).exists():
                D_MTBF = Systems.objects.filter(project_id=project,System=system,is_active=0) 
                pbs_mtbf_value = D_MTBF[0].MTBF
            else:
                response = {'status':'2','data' : data, 'data1' : data1, 'data2' : data2, 'slop':slop_value}
                return JsonResponse(response)
        else:
            D_MTBF = Product.objects.filter(product_id=project) 
            pbs_mtbf_value = D_MTBF[0].MTBF
        
        
        for ASSET in Asset_data:
            asset_types.append(ASSET.asset_type)

        
        if (lru_type or asset_types) and asset_types!=['']: 

            if lru_type and lru_type!="all":
                if not FailureData.objects.filter(asset_type=lru_type, date__range=[start_date,end_date],is_active=0).exclude(failure_type='Other').exists():
                    response = {'status':'1','data' : data, 'data1' : data1, 'data2' : data2, 'slop':slop_value}
                    return JsonResponse(response)
            else:
                if not FailureData.objects.filter(asset_type__in=asset_types, date__range=[start_date,end_date],is_active=0).exclude(failure_type='Other').exists():
                    response = {'status':'1','data' : data, 'data1' : data1, 'data2' : data2, 'slop':slop_value}
                    return JsonResponse(response)
            
            if lru_type and lru_type!="all":
                asset_data = Asset.objects.filter(asset_type=lru_type,is_active=0)
            else:
                asset_data = Asset.objects.filter(asset_type__in=asset_types,is_active=0)
            if start_date and end_date : # coming start date and end date are used further calculation
                formated_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                formated_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
                # formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').date()
                # formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').date()
            else: # Took current year start date and end date are used further calculation
                formated_start_date = (date.today() - offsets.YearBegin()).date()
                formated_end_date = (date.today() + offsets.YearEnd()).date()
            number_of_days = (formated_end_date-formated_start_date).days
           
            # To get scale dates. If number of days greater than 150days scales took as months and otherwise took as weeks
            first_week_day = formated_start_date.weekday()
            first_week_sunday = formated_start_date + timedelta(days=(5-first_week_day))
            second_week_start_date = first_week_sunday + timedelta(days=1)
            # number_of_days = (formated_end_date-second_week_start_date).days
            if number_of_days % 7 == 0:
                weeks = number_of_days//7
            else:
                weeks = number_of_days/7
            if type(weeks)==float:
                week_number = int(weeks) + 2
            else:
                week_number = weeks + 1
            
            # to get week end date
            week_end_date = second_week_start_date + timedelta(days=week_number*7)
            asset_count = asset_data.count()
            cum_actual_failure_count = 0

            if lru_type and lru_type!="all":
                Hightest_date_of_failure = FailureData.objects.filter(asset_config_id__asset_type=lru_type, is_active=0).exclude(failure_type='Other').order_by('-date')
            else:
                Hightest_date_of_failure = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types,is_active=0).exclude(failure_type='Other').order_by('-date')

            print(Hightest_date_of_failure[0].date,'Hightest_date_of_failure')
            Hightest_date_of_failure = str(Hightest_date_of_failure[0].date)
            Hightest_date_of_failure = datetime.datetime.strptime(Hightest_date_of_failure, '%Y-%m-%d').strftime('%Y-%m-%d')
           
            pbs_mtbf_value = round(np.log(pbs_mtbf_value),2)
            Ii = 1

            for i in range(1, week_number+1):
                if FN_NAME == 'two':
                    lru_population_hours = (asset_count*24*7)*i # to get LRU Weekely Hours
                else:
                    lru_population_hours = (24*7)*i # to get LRU Weekely Hours
                actual_mtbf_value = 'null'
                # to get start/end dates of current week
                if i == 1:
                    week_start_date = formated_start_date
                    
                elif i == 2:
                    week_start_date = second_week_start_date
                else:
                    week_start_date = week_end_date + timedelta(days=1)
                if i ==1:
                    week_end_date = first_week_sunday
                else:
                    week_end_date = week_start_date + timedelta(days=6) 

                failure_count = 0
                if lru_type and lru_type!="all":
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[week_start_date,week_end_date],is_active=0).exclude(failure_type='Other').count()
                else:
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types, date__range=[week_start_date,week_end_date],is_active=0).exclude(failure_type='Other').count()
                
                if failure_count != 0:
                    cum_actual_failure_count = cum_actual_failure_count+failure_count
                if cum_actual_failure_count != 0:
                    actual_mtbf_value = round(lru_population_hours/cum_actual_failure_count,2)

                findUnit = PBSUnit.objects.filter()
                if findUnit[0].MTBFMTBSAF == 'days':
                    lru_population_hours = lru_population_hours/24 
                elif findUnit[0].MTBFMTBSAF == 'mins':
                    lru_population_hours = lru_population_hours*60
                else:
                    lru_population_hours = lru_population_hours

                lru_population_hours = round(np.log(lru_population_hours),2)

                week_end_date1 = datetime.datetime.strptime(str(week_end_date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                
                if week_end_date1 < Hightest_date_of_failure or failure_count != 0:
                    findUnit = PBSUnit.objects.filter()
                    if findUnit[0].MTBFMTBSAF == 'days':
                        if actual_mtbf_value != 'null':
                            actual_mtbf_value = round(actual_mtbf_value/24,2)                        
                    elif findUnit[0].MTBFMTBSAF == 'mins':
                        if actual_mtbf_value != 'null':
                            actual_mtbf_value = actual_mtbf_value *60
                    else:
                        actual_mtbf_value = actual_mtbf_value
                    last_x_point = lru_population_hours
                    last_y_point = actual_mtbf_value
                else:
                    actual_mtbf_value = 'null'
                if Ii == 1:
                    if actual_mtbf_value != 'null':
                        first_x_point = lru_population_hours
                        first_y_point = actual_mtbf_value
                        Ii = 2

                if actual_mtbf_value != 'null':
                    actual_mtbf_value = round(np.log(actual_mtbf_value),2)

                data.append({'x': lru_population_hours, 'y': actual_mtbf_value})
                data1.append({'x': lru_population_hours, 'y': pbs_mtbf_value})
            

            print(first_x_point,'first_x_point')
            print(first_y_point,'first_y_point')
            print(last_x_point,'last_x_point')
            print(last_y_point,'last_y_point')
            if first_x_point == last_x_point and first_y_point == last_y_point:
                slope = 1
            else:
                slope = (last_y_point - first_y_point) / (last_x_point - first_x_point)
            print(slope,'slope')
            LinerPointFlow = 0
            for i in range(1, week_number+1):
                if FN_NAME == 'two':
                    lru_population_hours = (asset_count*24*7)*i # to get LRU Weekely Hours
                else:
                    lru_population_hours = (24*7)*i # to get LRU Weekely Hours
                actual_mtbf_value = 'null'
                # to get start/end dates of current week
                if i == 1:
                    week_start_date = formated_start_date
                    
                elif i == 2:
                    week_start_date = second_week_start_date
                else:
                    week_start_date = week_end_date + timedelta(days=1)
                if i ==1:
                    week_end_date = first_week_sunday
                else:
                    week_end_date = week_start_date + timedelta(days=6) 

                failure_count = 0
                if lru_type and lru_type!="all":
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[week_start_date,week_end_date],is_active=0).exclude(failure_type='Other').count()
                else:
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types, date__range=[week_start_date,week_end_date],is_active=0).exclude(failure_type='Other').count()
                
                if failure_count != 0:
                    cum_actual_failure_count = cum_actual_failure_count+failure_count
                if cum_actual_failure_count != 0:
                    actual_mtbf_value = round(lru_population_hours/cum_actual_failure_count,2)

                findUnit = PBSUnit.objects.filter()
                if findUnit[0].MTBFMTBSAF == 'days':
                    lru_population_hours = lru_population_hours/24 
                elif findUnit[0].MTBFMTBSAF == 'mins':
                    lru_population_hours = lru_population_hours*60
                else:
                    lru_population_hours = lru_population_hours

                lru_population_hours = round(np.log(lru_population_hours),2)

                week_end_date1 = datetime.datetime.strptime(str(week_end_date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

                

                if lru_population_hours == first_x_point:
                    LinerPoint = first_y_point
                    LinerPointFlow = 1
                    predicted_mtbf_value = 'null'
                else:
                    LinerPoint = 'null'
                    predicted_mtbf_value = 'null'

                if LinerPointFlow == 2:
                    if week_end_date1 < Hightest_date_of_failure or failure_count != 0:
                        predicted_mtbf_value = 'null'
                        DX = lru_population_hours - last_x_point
                        MS = DX * slope
                        LinerPoint = MS + last_y_point
                    else:
                        LinerPoint = 'null'
                        DX = lru_population_hours - last_x_point
                        MS = DX * slope
                        predicted_mtbf_value = MS + last_y_point

                if LinerPointFlow == 1:
                    LinerPointFlow = 2

                if LinerPoint != 'null':
                    LinerPoint = round(np.log(LinerPoint),2)
                print('predicted_mtbf_value',predicted_mtbf_value)
                
                if predicted_mtbf_value != 'null':
                    if predicted_mtbf_value >=0:
                        predicted_mtbf_value = round(np.log(predicted_mtbf_value),2)
                    else:
                        predicted_mtbf_value = 'null'
                
                data2.append({'x': lru_population_hours, 'y': LinerPoint})
                data3.append({'x': lru_population_hours, 'y': predicted_mtbf_value})
            

        else:
            data=[]
        response = {'data' : data, 'data1' : data1, 'data2' : data2, 'slop':data3}
        return JsonResponse(response)




class CumalativeMtbfReportView(View):
    template_name = 'cum_actual_mtbf.html'

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
        Asset_data = Asset.objects.all().distinct('asset_type')
        defect_datas = Defect.objects.all().distinct('defect_id')
        systems = PBSMaster.objects.all().distinct('system')
        return render(request, self.template_name, {'project':project,'asset_data' : Asset_data, 'systems':systems})

    def post(self, request, *args, **kwargs):

        req = request.POST
        system = req.get('system')
        sub_system = req.get('sub_system')
        product_id = req.get('product_id')
        lru_type = req.get('lru_type')
        if req.get('start_date') !="" and req.get('end_date') !="":
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            start_date = req.get('start_date')
            end_date = req.get('end_date')
        pbs_mtbf_value = 0
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        
        if user_Role == 1:
            Asset_data=Asset.objects.filter(is_active=0)
        else:
            Asset_data=Asset.objects.filter(is_active=0,P_id=P_id)
        pbs_master_data = PBSMaster.objects.filter(is_active=0)
        if sub_system != "all":
            SUBSYSTEM=PBSMaster.objects.filter(subsystem_id=sub_system,is_active=0)
            a=[]
            for SUB in SUBSYSTEM:
                a.append(SUB.id)
            Asset_data=Asset_data.filter(asset_type__in=a) 
            pbs_master_data = pbs_master_data.filter(id__in=a)
        if lru_type != "all":
            Asset_data=Asset_data.filter(asset_type=lru_type)
            pbs_master_data = pbs_master_data.filter(id=lru_type)
            
        for pbs in pbs_master_data:
            pbs_mtbf_value = pbs.MTBF
        actual_MTBF=[]
        prediced_MTBF=[]
        MTBF_target=[]
        software_mode=[]
        week_scale=[]
        scale = []
        asset_types = []
        pbs_asset_types = []
        
        for ASSET in Asset_data:
            asset_types.append(ASSET.asset_type)
        # if system and not (product_id or lru_type):
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem='', product_id='', asset_type='')[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF
        # if system and (sub_system=="all" or product_id=="all" or lru_type=="--All--"):
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem='', product_id='', asset_type='')[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF
        
        # if system and sub_system and not (sub_system=="all" or product_id or lru_type):
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system)[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF

        # if system and sub_system and not lru_type:
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system)[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF

        # if system and sub_system and lru_type and lru_type!="--All--":
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system, asset_type=lru_type)
        #     pbs_mtbf_value = pbs_master_data[0].MTBF

        # if system and sub_system and product_id and product_id!="all":
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system, product_id=product_id)
        #     pbs_mtbf_value = pbs_master_data[0].MTBF
        
        # actual_MTBF=[]
        # prediced_MTBF=[]
        # MTBF_target=[]
        # software_mode=[]
        # week_scale=[]
        # scale = []
        # asset_types = []
        # pbs_asset_types = []
        # if system and sub_system == "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if product_id == "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem=sub_system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if lru_type == "--All--":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem=sub_system, product_id=product_id)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if (lru_type or asset_types) and asset_types!=['']:
        #     if lru_type and lru_type!="--All--":
        #         all_defects = Defect.objects.filter(asset_type=lru_type)
        #         defects_count = Defect.objects.filter(asset_type=lru_type).count()
        #         asset_data = Asset.objects.filter(asset_type=lru_type)
        #     else:
        #         all_defects = Defect.objects.filter(asset_type__in=asset_types)
        #         defects_count = Defect.objects.filter(asset_type__in=asset_types).count()
        #         asset_data = Asset.objects.filter(asset_type__in=asset_types)
                
            # print(asset_data)
            cum_actual_failure_count = 0
            cum_actual_failure_count1 = 0
            predicted_avg_failures_per_week = 0
            actual_mtbf_value = 0
            defects_week = 0
            prediced_mtbf_value = 0
            i=0
            
            # default_date = (date.today() - offsets.YearBegin()).date()
            current_date = datetime(2019,4,23).date()#date.today()
            # start_date = ''
            # end_date = ''
            
            # defects_count = all_defects.count()
            if start_date and end_date : # coming start date and end date are used further calculation
                defect_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                defect_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            else:
                defect_start_date = (date.today() - offsets.YearBegin()).date()
                defect_end_date = (date.today() + offsets.YearEnd()).date()

            first_week_day = defect_start_date.weekday()
            first_week_sunday = defect_start_date + timedelta(days=(5-first_week_day))
            second_week_start_date = first_week_sunday + timedelta(days=1)
            number_of_days = (defect_end_date-second_week_start_date).days
            if number_of_days % 7 == 0:
                weeks = number_of_days//7
            else:
                weeks = number_of_days/7
            if type(weeks)==float:
                week_number = int(weeks) + 2
            else:
                week_number = weeks + 1
            # total_failures_count = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[defect_start_date,defect_end_date]).count()
            #no_defect_failures = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[defect_start_date,defect_end_date], defect=None)
            if lru_type and lru_type!="all":
                distinct_defect_failures = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[defect_start_date,defect_end_date]).exclude(defect=None,failure_type='Other').distinct('defect__defect_id')
            else:
                distinct_defect_failures = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types, date__range=[defect_start_date,defect_end_date]).exclude(defect=None,failure_type='Other').distinct('defect__defect_id')
            #defects_count = distinct_defect_failures.count()
            # if no_defect_failures:
            #     defects_count = defects_count + 1
            failure_defects = []
            total_failures_count = 0
            new_total_defect_count = 0
            for distinct_defect_failure in distinct_defect_failures:
                # print(distinct_defect_failure.defect)
                if distinct_defect_failure.defect.failuredata_set.all():
                    latest_failure_date = distinct_defect_failure.defect.failuredata_set.all().latest('date').date
                    failure_days = (latest_failure_date-second_week_start_date).days
                    if failure_days % 7 == 0:
                        failure_weeks = failure_days//7
                    else:
                        failure_weeks = failure_days/7
                    if type(failure_weeks)==float:
                        failure_week_number = int(failure_weeks) + 2
                    else:
                        failure_week_number = failure_weeks + 1
                    # print(len(distinct_defect_failure.defect.failuredata_set.all()),failure_week_number)
                    
                    failure_week_count = (len(distinct_defect_failure.defect.failuredata_set.all())/failure_week_number)*52              
                    total_failures_count += math.ceil(failure_week_count)
                    # print(total_failures_count, math.ceil(failure_week_count))
                    #print(defect_start_date,latest_failure_date,len(distinct_defect_failure.defect.failuredata_set.all()),failure_week_number,failure_week_count, "NEW Calc")
                    new_defect_count = round(len(distinct_defect_failure.defect.failuredata_set.all())/failure_week_number, 2)
                    new_total_defect_count = new_total_defect_count + new_defect_count
                    failure_defects.append({'defect_id':distinct_defect_failure.defect.defect_id, 'count':math.ceil(failure_week_count), 'new_count':new_defect_count})
                    
                    # print(new_defect_count, distinct_defect_failure.defect.defect_id, "Rate of defects")
            # print(new_total_defect_count, "New Total Defect Count")
            week_scale.append(str(0))
            actual_MTBF.append({'x':0, 'y':'null',})
            prediced_MTBF.append({'x':0, 'y':'null',})
            software_mode.append({'x':0, 'y': 'null','custome': []})
            asset_count = asset_data.count()
            # print(asset_count,"count")
            random_failure_count = round((24*365*asset_count)/pbs_mtbf_value,1)
            # print(random_failure_count,"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
            if random_failure_count != 0:
                total_failures_count += random_failure_count
                
            # print(total_failures_count, random_failure_count)
            # print(new_total_defect_count,"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
            avg_failures_per_week = round(total_failures_count/(week_number-1),2)
            duplicate_avg_failures_per_week = avg_failures_per_week
            # print(total_failures_count, avg_failures_per_week, random_failure_count, total_failures_count)
            flag = False
            last_actual_values = []
            last_actual_weeks = []
            for week in range(1, week_number+1):

                # to get start/end dates of current week
                # if week == 1:
                #     week_start_date = defect_start_date
                # elif week == 2:
                #     week_start_date = second_week_start_date
                # else:
                #     week_start_date = week_end_date + timedelta(days=1)

                # if week ==1:
                #     week_end_date = first_week_sunday
                # else:
                #     week_end_date = week_start_date + timedelta(days=6)

                if week == 1:
                    week_start_date = defect_start_date
                else:
                    week_start_date = week_end_date + timedelta(days=1)

                week_end_date = week_start_date + timedelta(days=6)
                
                if lru_type and lru_type!="all":
                    defects = Defect.objects.filter(asset_type=lru_type, oem_target_date__range=[week_start_date,week_end_date])
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[week_start_date,week_end_date]).exclude(failure_type='Other').count()
                else:
                    defects = Defect.objects.filter(asset_type__in=asset_types, oem_target_date__range=[week_start_date,week_end_date])
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types, date__range=[week_start_date,week_end_date]).exclude(failure_type='Other').count()
                oem_references = []
                # print(week_start_date, week_end_date, defects, len(defects))
                
                predicted_avg_failures_per_week = predicted_avg_failures_per_week+avg_failures_per_week
                i = i+1
                lru_population_hours = (asset_count*24*7)*i
                # print(week_start_date, defects, avg_failures_per_week, predicted_avg_failures_per_week)
                if week_end_date <= current_date:
                    if failure_count != 0:
                        cum_actual_failure_count = cum_actual_failure_count+failure_count
                        actual_mtbf_value = round(lru_population_hours/cum_actual_failure_count,2)
                        # print(lru_population_hours,cum_actual_failure_count,failure_count,actual_mtbf_value)
                    # print(failure_count, cum_actual_failure_count, "loooooooo")
                    if actual_mtbf_value == 0:
                        actual_mtbf_value = 'null'

                    actual_MTBF.append({'x':week, 'y':actual_mtbf_value,})
                    prediced_MTBF.append({'x':week, 'y':'null',})
                    last_actual_values.append(actual_mtbf_value)
                    last_actual_weeks.append(week)
                else:
                    if new_total_defect_count != 0:
                    # if avg_failures_per_week != 0:
                        actual_mtbf_value = 0

                        # new_total_defect_count = round((new_total_defect_count + (random_failure_count/52)),0)
                        # cum_actual_failure_count = cum_actual_failure_count+round((new_total_defect_count + (random_failure_count/52)),0)
                        if flag == False:
                            prediced_MTBF.pop()
                            prediced_MTBF.append({'x':last_actual_weeks[-1], 'y':last_actual_values[-1],})
                            flag = True
                        cum_actual_failure_count = cum_actual_failure_count+new_total_defect_count+(random_failure_count/52)
                        prediced_mtbf_value = round(lru_population_hours/cum_actual_failure_count, 2)
                        # prediced_mtbf_value = round(lru_population_hours/predicted_avg_failures_per_week, 2)
                        prediced_MTBF.append({'x':week, 'y':prediced_mtbf_value,})
                        
                no_of_defect_failures = 0
                # print(prediced_MTBF)
                # print()
                if defects:
                    defects_week = week
                    cum_cta1 = 0
                    for defect in defects: 
                        print(defect,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                        if defect.defect_id in [d['defect_id'] for d in failure_defects]:
                            no_of_defect_failures = [d['count'] for d in failure_defects if d['defect_id']==defect.defect_id][0]
                            new_no_of_defect_failures = [d['new_count'] for d in failure_defects if d['defect_id']==defect.defect_id][0]
                        # cum_cta = (((defect.oem_target_date).month)/12)*no_of_defect_failures
                        remaining_week = (53-week)/52
                        # total_failures_count = total_failures_count-math.ceil(cum_cta)
                        new_total_defect_count = round((new_total_defect_count - (new_no_of_defect_failures*remaining_week)),2)
                        print(week,(53-week),remaining_week)
                        total_failures_count = total_failures_count - (no_of_defect_failures*remaining_week)
                        oem_references.append(defect.oem_defect_reference)
                    avg_failures_per_week = round(total_failures_count/(week_number-1),2)
                # print(len(defects), lru_population_hours,avg_failures_per_week,round(predicted_avg_failures_per_week,2),prediced_mtbf_value)
                # print(avg_failures_per_week,predicted_avg_failures_per_week,cum_actual_failure_count,actual_mtbf_value,prediced_mtbf_value,'----',week,"looooooooo")
                MTBF_target.append({'x':week, 'y':pbs_mtbf_value,})
                soft_mode = 'null'
                if len(oem_references) > 0 :
                    soft_mode = '0'
                software_mode.append({'x':week, 'y': soft_mode,'custome': oem_references})
                week_scale.append(str(week))
            updated_predicted_failure_count_list=[]
            lru_population_hours1_list=[]
            lru_population_hours1=0
            updated_predicted_failure_count=0

        response = {'actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
        return JsonResponse(response)


class CumalativeMtbfReportF2View(View):
    template_name = 'cum_actual_mtbf.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('index')
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        if user_Role == 1:
            subsystem = Product.objects.all()
        else:
            subsystem = Product.objects.filter(product_id=P_id)
        Asset_data = Asset.objects.all().distinct('asset_type')
        defect_datas = Defect.objects.all().distinct('defect_id')
        systems = PBSMaster.objects.all().distinct('system')
        return render(request, self.template_name, {'subsystem':subsystem,'asset_data' : Asset_data, 'systems':systems})

    def post(self, request, *args, **kwargs):
        req = request.POST
        project = req.get('project')
        MTBFT = req.get('MTBFT')
        system = req.get('system')
        sub_system = req.get('sub_system')
        FN_NAME = req.get('FN_NAME')
        product_id = req.get('product_id')
        lru_type = req.get('lru_type')
        
        actual_MTBF=[]
        prediced_MTBF=[]
        MTBF_target=[]
        software_mode=[]
        week_scale=[]
        scale = []
        asset_types = []
        pbs_asset_types = []
        
        if req.get('start_date') !="" and req.get('end_date') !="":
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            start_date = req.get('start_date')
            end_date = req.get('end_date')
        pbs_mtbf_value = 0
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        
        if user_Role == 1:
            Asset_data=Asset.objects.filter(is_active=0)
        else:
            Asset_data=Asset.objects.filter(is_active=0,P_id=P_id)
        pbs_master_data = PBSMaster.objects.filter(is_active=0)
        if FN_NAME == 'two':
            if project != "all":
                if Asset_data.filter(asset_type=lru_type,is_active=0).exists():
                    Asset_data=Asset_data.filter(asset_type=lru_type) 
                    pbs_master_data = pbs_master_data.filter(id=lru_type)
                else:
                    response = {'actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
        else:
            if project != "all":
                SUBSYSTEM=PBSMaster.objects.filter(project_id=project,is_active=0)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                Asset_data=Asset_data.filter(asset_type__in=a) 
                pbs_master_data = pbs_master_data.filter(id__in=a)
        if FN_NAME == 'two':
            if MTBFT == 'MTBF':
                pbs_mtbf_value = pbs_master_data[0].MTBF
            else:
                pbs_mtbf_value = pbs_master_data[0].MTBSAF
        else:
            if MTBFT == 'MTBF':
                D_MTBF = Product.objects.filter(product_id=project) 
                pbs_mtbf_value = D_MTBF[0].MTBF
            else:
                D_MTBF = Product.objects.filter(product_id=project) 
                pbs_mtbf_value = D_MTBF[0].MTBSAF
                
        print(pbs_mtbf_value,'pbs_mtbf_value')
                
        if pbs_mtbf_value == 0:
            print('---work--')
            response = {'status':'1','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
            return JsonResponse(response)
        
        for ASSET in Asset_data:
            asset_types.append(ASSET.asset_type)

        # req = request.POST
        # system = req.get('system')
        # sub_system = req.get('sub_system')
        # product_id = req.get('product_id')
        # lru_type = req.get('lru_type')
        # start_date = req.get('start_date')
        # end_date = req.get('end_date')
        # pbs_mtbf_value = 0 
        # if system and not (product_id or lru_type):
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem='', product_id='', asset_type='')[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF
        # if system and (sub_system=="all" or product_id=="all" or lru_type=="--All--"):
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem='', product_id='', asset_type='')[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF
        
        # if system and sub_system and not (sub_system=="all" or product_id or lru_type):
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system)[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF

        # if system and sub_system and not lru_type:
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system)[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF

        # if system and sub_system and lru_type and lru_type!="--All--":
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system, asset_type=lru_type)
        #     pbs_mtbf_value = pbs_master_data[0].MTBF

        # if system and sub_system and product_id and product_id!="all":
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system, product_id=product_id)
        #     pbs_mtbf_value = pbs_master_data[0].MTBF
        
        # actual_MTBF=[]
        # prediced_MTBF=[]
        # MTBF_target=[]
        # software_mode=[]
        # week_scale=[]
        # scale = []
        # asset_types = []
        # pbs_asset_types = []
        # if system and sub_system == "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if product_id == "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem=sub_system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if lru_type == "--All--":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem=sub_system, product_id=product_id)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        if (lru_type or asset_types) and asset_types!=['']:
            if lru_type and lru_type!="all":
                all_defects = Defect.objects.filter(asset_type=lru_type,is_active=0)
                defects_count = Defect.objects.filter(asset_type=lru_type,is_active=0).count()
                if Asset.objects.filter(asset_type=lru_type,is_active=0).exists():
                    asset_data = Asset.objects.filter(asset_type=lru_type,is_active=0)
                else:
                    response = {'actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
            else:
                all_defects = Defect.objects.filter(asset_type__in=asset_types,is_active=0)
                defects_count = Defect.objects.filter(asset_type__in=asset_types,is_active=0).count()
                if Asset.objects.filter(asset_type__in=asset_types,is_active=0):
                    asset_data = Asset.objects.filter(asset_type__in=asset_types,is_active=0)
                else:
                    response = {'actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
            cum_actual_failure_count = 0
            cum_actual_failure_count1 = 0
            predicted_avg_failures_per_week = 0
            actual_mtbf_value = 0
            defects_week = 0
            prediced_mtbf_value = 0
            i=0
            # default_date = (date.today() - offsets.YearBegin()).date()
            current_date = date.today()#date.today()
            # start_date = ''
            # end_date = ''
            # defects_count = all_defects.count()
            print('---AAAAAAAA---')
            if start_date and end_date : # coming start date and end date are used further calculation
                defect_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                defect_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            else:
                defect_start_date = (date.today() - offsets.YearBegin()).date()
                defect_end_date = (date.today() + offsets.YearEnd()).date()
            print('Start:-',defect_start_date, 'End:-', defect_end_date)
            first_week_day = defect_start_date.weekday()
            first_week_sunday = defect_start_date + timedelta(days=(5-first_week_day))
            second_week_start_date = first_week_sunday + timedelta(days=1)
            number_of_days = (defect_end_date-second_week_start_date).days
            if number_of_days % 7 == 0:
                weeks = number_of_days//7
            else:
                weeks = number_of_days/7
            if type(weeks)==float:
                week_number = int(weeks) + 2
            else:
                week_number = weeks + 1
            print('---BBBBBBBB---')
            # total_failures_count = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[defect_start_date,defect_end_date]).count()
            #no_defect_failures = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[defect_start_date,defect_end_date], defect=None)
            if lru_type and lru_type!="all":
                distinct_defect_failures = FailureData.objects.filter(asset_type=lru_type, date__range=[defect_start_date,defect_end_date],is_active=0).exclude(defect=None,failure_type='Other').distinct('defect__defect_id')
                # distinct_defect_failures = FailureData.objects.filter(asset_config_id__asset_type=lru_type, start_date >= defect_start_date,end_date <= defect_end_date).exclude(defect=None).distinct('defect__defect_id')
            else:
                distinct_defect_failures = FailureData.objects.filter(asset_type__in=asset_types, date__range=[defect_start_date,defect_end_date],is_active=0).exclude(defect=None,failure_type='Other').distinct('defect__defect_id')
            #defects_count = distinct_defect_failures.count()
            # if no_defect_failures:
            #     defects_count = defects_count + 1
            failure_defects = []
            total_failures_count = 0
            new_total_defect_count = 0
            print('---CCCCCC---')
            for distinct_defect_failure in distinct_defect_failures:
                # print(distinct_defect_failure.defect)
               
                if distinct_defect_failure.defect != None:
                    if distinct_defect_failure.defect.failuredata_set.all():
                        latest_failure_date = distinct_defect_failure.defect.failuredata_set.all().latest('date').date
                        failure_days = (latest_failure_date-second_week_start_date).days
                        if failure_days % 7 == 0:
                            failure_weeks = failure_days//7
                        else:
                            failure_weeks = failure_days/7
                        if type(failure_weeks)==float:
                            failure_week_number = int(failure_weeks) + 2
                        else:
                            failure_week_number = failure_weeks + 1
                        # print(len(distinct_defect_failure.defect.failuredata_set.all()),failure_week_number)
                        # failure_week_count = (len(distinct_defect_failure.defect.failuredata_set.all())/failure_week_number)*52              
                        failure_week_count = len(distinct_defect_failure.defect.failuredata_set.filter(date__range=[defect_start_date,defect_end_date]).exclude(defect=None))

                        # total_failures_count += math.ceil(failure_week_count)
                        total_failures_count += failure_week_count
                        # print(total_failures_count, math.ceil(failure_week_count))
                        #print(defect_start_date,latest_failure_date,len(distinct_defect_failure.defect.failuredata_set.all()),failure_week_number,failure_week_count, "NEW Calc")
                        print('defect_defect_id:====',distinct_defect_failure.defect_id,"failure_week_count=========",failure_week_count )
                        new_defect_count = round(len(distinct_defect_failure.defect.failuredata_set.all())/failure_week_number, 2)
                        new_total_defect_count = new_total_defect_count + new_defect_count
                        failure_defects.append({'defect_id':distinct_defect_failure.defect.defect_id, 'count':failure_week_count, 'new_count':new_defect_count})
                        
                        # print(new_defect_count, distinct_defect_failure.defect.defect_id, "Rate of defects")
            # print(new_total_defect_count, "New Total Defect Count")
            week_scale.append(str(0))
            actual_MTBF.append({'x':0, 'y':'null',})
            prediced_MTBF.append({'x':0, 'y':'null',})
            software_mode.append({'x':0, 'y': 'null','custome': []})
            asset_count = asset_data.count()
            random_failure_count = round((24*365*asset_count)/pbs_mtbf_value)
            # print(random_failure_count,"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
            if random_failure_count != 0:
                total_failures_count += random_failure_count
                
            # print(total_failures_count, random_failure_count)
            print('---FFFFFF---')
            avg_failures_per_week = round(total_failures_count/(week_number-1),9)
            duplicate_avg_failures_per_week = avg_failures_per_week
            # print(avg_failures_per_week,"==========avg_failures_per_week")
            # print(total_failures_count, avg_failures_per_week, random_failure_count, total_failures_count)
            flag = False
            last_actual_values = []
            last_actual_weeks = []
            print(pbs_mtbf_value)
            for week in range(1, week_number+1):

                # to get start/end dates of current week
                # if week == 1:
                #     week_start_date = defect_start_date
                # elif week == 2:
                #     week_start_date = second_week_start_date
                # else:
                #     week_start_date = week_end_date + timedelta(days=1)

                # if week ==1:
                #     week_end_date = first_week_sunday
                # else:
                #     week_end_date = week_start_date + timedelta(days=6)

                if week == 1:
                    week_start_date = defect_start_date
                else:
                    week_start_date = week_end_date + timedelta(days=1)

                week_end_date = week_start_date + timedelta(days=6)
                
                if lru_type and lru_type!="all":
                    defects = Defect.objects.filter(asset_type=lru_type, oem_target_date__range=[week_start_date,week_end_date],is_active=0)
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[week_start_date,week_end_date],is_active=0).exclude(failure_type='Other').count()
                else:
                    defects = Defect.objects.filter(asset_type__in=asset_types, oem_target_date__range=[week_start_date,week_end_date],is_active=0)
                    failure_count = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types, date__range=[week_start_date,week_end_date],is_active=0).exclude(failure_type='Other').count()
                oem_references = []
                # print(week_start_date, week_end_date, defects, len(defects))
                predicted_avg_failures_per_week = predicted_avg_failures_per_week+avg_failures_per_week
                i = i+1
                lru_population_hours = (asset_count*24*7)*i
                # print(week_start_date, defects, avg_failures_per_week, predicted_avg_failures_per_week)
                print('---------------------------------------------')
                print('---------------------------------------------')
                print(current_date,'current_date')
                print(week_end_date,'week_end_date')
                if week_end_date <= current_date:
                    print('NO MFDGH')
                    if failure_count != 0:
                        cum_actual_failure_count = cum_actual_failure_count+failure_count
                        actual_mtbf_value = round(lru_population_hours/cum_actual_failure_count,2)
                        # print(lru_population_hours,cum_actual_failure_count,failure_count,actual_mtbf_value)
                    # print(failure_count, cum_actual_failure_count, "loooooooo")
                    if actual_mtbf_value == 0:
                        actual_mtbf_value = 'null'
                        
                    findUnit = PBSUnit.objects.filter()
                    if findUnit[0].MTBFMTBSAF == 'days':
                        if actual_mtbf_value != 'null':
                            actual_mtbf_value = round(actual_mtbf_value/24,2)                        
                    elif findUnit[0].MTBFMTBSAF == 'mins':
                        if actual_mtbf_value != 'null':
                            actual_mtbf_value = actual_mtbf_value *60
                    else:
                        actual_mtbf_value = actual_mtbf_value

                    actual_MTBF.append({'x':week, 'y':actual_mtbf_value,})
                    prediced_MTBF.append({'x':week, 'y':'null',})
                    last_actual_values.append(actual_mtbf_value)
                    last_actual_weeks.append(week)
                else:
                    print('/////----PReaffgsgs MTBF ghdgdhd-----///')
                    # if new_total_defect_count != 0:
                    if avg_failures_per_week != 0:
                        actual_mtbf_value = 0

                        # new_total_defect_count = round((new_total_defect_count + (random_failure_count/52)),0)
                        # cum_actual_failure_count = cum_actual_failure_count+round((new_total_defect_count + (random_failure_count/52)),0)
                        
                        
                        if flag == False:
                            if failure_count != 0:
                                cum_actual_failure_count = cum_actual_failure_count+failure_count
                                actual_mtbf_value = round(lru_population_hours/cum_actual_failure_count,2)
                                # print(lru_population_hours,cum_actual_failure_count,failure_count,actual_mtbf_value)
                                # print(failure_count, cum_actual_failure_count, "loooooooo")
                            if actual_mtbf_value == 0:
                                actual_mtbf_value = 'null'
                            # prediced_MTBF.pop()
                            # prediced_MTBF.append({'x':last_actual_weeks[-1], 'y':last_actual_values[-1],})
                            findUnit = PBSUnit.objects.filter()
                            if findUnit[0].MTBFMTBSAF == 'days':
                                if actual_mtbf_value != 'null':
                                    actual_mtbf_value = round(actual_mtbf_value/24,2)                        
                            elif findUnit[0].MTBFMTBSAF == 'mins':
                                if actual_mtbf_value != 'null':
                                    actual_mtbf_value = actual_mtbf_value *60
                            else:
                                actual_mtbf_value = actual_mtbf_value
                            
                            actual_MTBF.append({'x':week, 'y':actual_mtbf_value,})
                            flag = True

                        #cum_actual_failure_count = cum_actual_failure_count+new_total_defect_count+(random_failure_count/52)
                        # prediced_mtbf_value = round(lru_population_hours/cum_actual_failure_count, 2)
                        # print(cum_actual_failure_count,"!!!!!!!!!!!!!!!!!!!!")
                        
                        prediced_mtbf_value = round(lru_population_hours/predicted_avg_failures_per_week, 2)
                        
                        findUnit = PBSUnit.objects.filter()
                        if findUnit[0].MTBFMTBSAF == 'days':
                            if prediced_mtbf_value != 'null':
                                prediced_mtbf_value = round(prediced_mtbf_value/24,2)                        
                        elif findUnit[0].MTBFMTBSAF == 'mins':
                            if prediced_mtbf_value != 'null':
                                prediced_mtbf_value = prediced_mtbf_value *60
                        else:
                            prediced_mtbf_value = prediced_mtbf_value
                        
                        
                        prediced_MTBF.append({'x':week, 'y':prediced_mtbf_value,})
                print('---------------------------------------------')
                print('---------------------------------------------')
                print('---66666---')       
                no_of_defect_failures = 0
                fail_mitg_post_cr = 0
                # print(prediced_MTBF)
                # print()                
                if defects:
                    defects_week = week
                    cum_cta1 = 0
                    for defect in defects: 
                        print("dfdfd")
                        if defect.defect_id in [d['defect_id'] for d in failure_defects]:
                            no_of_defect_failures = [d['count'] for d in failure_defects if d['defect_id']==defect.defect_id][0]
                            new_no_of_defect_failures = [d['new_count'] for d in failure_defects if d['defect_id']==defect.defect_id][0]
                        else:
                            new_no_of_defect_failures=0
                        # cum_cta = (((defect.oem_target_date).month)/12)*no_of_defect_failures
                        remaining_week = (week_number-1)-week
                        # total_failures_count = total_failures_count-math.ceil(cum_cta)
                        new_total_defect_count = round((new_total_defect_count - new_no_of_defect_failures),2)
                        fail_mitg_post_cr = round((no_of_defect_failures*remaining_week)/(week_number-1))
                        # total_failures_count = total_failures_count - (no_of_defect_failures*remaining_week)
                        total_failures_count = round(total_failures_count - fail_mitg_post_cr)
                        oem_references.append(defect.oem_defect_reference)
                        print(no_of_defect_failures,'==========',total_failures_count)
                        print('fail_mitg_post_cr ====',fail_mitg_post_cr)
                    avg_failures_per_week = round(total_failures_count/(week_number-1),2)
                # print(len(defects), lru_population_hours,avg_failures_per_week,round(predicted_avg_failures_per_week,2),prediced_mtbf_value)
                # print(no_of_defect_failures,'----',total_failures_count,avg_failures_per_week,predicted_avg_failures_per_week,cum_actual_failure_count,actual_mtbf_value,prediced_mtbf_value,"looooooooo")
                MTBF_target.append({'x':week, 'y':pbs_mtbf_value,})
                soft_mode = 'null'
                if len(oem_references) > 0 :
                    soft_mode = '0'
                software_mode.append({'x':week, 'y': soft_mode,'custome': oem_references})
                week_scale.append(str(week))
                print('Week:', week,'LRU POP:',lru_population_hours,'AVG failures:',avg_failures_per_week, 'Actual failures:',failure_count, 'cum_actual_failure_count:',cum_actual_failure_count, 'Actula MTBF:',actual_mtbf_value,'Predict Fail:',predicted_avg_failures_per_week, 'Pred MTBF:',prediced_mtbf_value)
                print('Total fail count:', total_failures_count, 'fail_mitg_post_cr:',fail_mitg_post_cr)
            updated_predicted_failure_count_list=[]
            lru_population_hours1_list=[]
            lru_population_hours1=0
            updated_predicted_failure_count=0

        response = {'actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
        return JsonResponse(response)
    
class AvailabilityView(View):
    template_name = 'availability.html'

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
        return render(request, self.template_name, {'project' : project})
    
    def post(self, request, *args, **kwargs):
        req = request.POST
        project = req.get('project')
        system = req.get('system')
        sub_system = req.get('sub_system')
        FN_NAME = req.get('FN_NAME')
        product_id = req.get('product_id')
        lru_type = req.get('lru_type')
        
        Avalability_data=[]
        availability_target_data=[]
        week_scale=[]
        scale = []
        asset_types = []
        pbs_asset_types = []
        
        if req.get('start_date') !="" and req.get('end_date') !="":
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            start_date = req.get('start_date')
            end_date = req.get('end_date')
        pbs_mtbf_value = 0
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        
        if user_Role == 1:
            Asset_data=Asset.objects.filter(is_active=0)
        else:
            Asset_data=Asset.objects.filter(is_active=0,P_id=P_id)
        pbs_master_data = PBSMaster.objects.filter(is_active=0)
        
        if FN_NAME == 'two':
            if project != "all":
                if Asset_data.filter(asset_type=lru_type,is_active=0).exists():
                    Asset_data=Asset_data.filter(asset_type=lru_type)
                    pbs_master_data = pbs_master_data.filter(id=lru_type)
                else:
                    response = {'status':'1','Avaiability' : Avalability_data, 'availability_targets' : availability_target_data, 'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)    
        elif FN_NAME == 'three':
            if project != "all":
                SUBSYSTEM=PBSMaster.objects.filter(project_id=project,is_active=0,system=system)
                if not SUBSYSTEM.exists():
                    response = {'status':'1','Avaiability' : Avalability_data, 'availability_targets' : availability_target_data, 'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                Asset_data=Asset_data.filter(asset_type__in=a) 
                pbs_master_data = pbs_master_data.filter(id__in=a)
        else:
            if project != "all":
                SUBSYSTEM=PBSMaster.objects.filter(project_id=project,is_active=0)
                if not SUBSYSTEM.exists():
                    response = {'status':'1','Avaiability' : Avalability_data, 'availability_targets' : availability_target_data, 'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                Asset_data=Asset_data.filter(asset_type__in=a) 
                pbs_master_data = pbs_master_data.filter(id__in=a)
                
        if FN_NAME == 'two':
            availability_target = pbs_master_data[0].availability_target
        elif FN_NAME == 'three':
            if Systems.objects.filter(project_id=project,System=system,is_active=0).exists():
                D_availability_target = Systems.objects.filter(project_id=project,System=system,is_active=0) 
                availability_target = D_availability_target[0].availability_target
            else:
                response = {'status':'2','Avaiability' : Avalability_data, 'availability_targets' : availability_target_data, 'rangeScale' : week_scale, 'scale':scale}
                return JsonResponse(response)
        else:
            D_availability_target = Product.objects.filter(product_id=project) 
            availability_target = D_availability_target[0].availability_target
            
        for ASSET in Asset_data:
            asset_types.append(ASSET.asset_type)
            
        if (lru_type or asset_types) and asset_types!=['']:
            if lru_type and lru_type!="all":
                if not FailureData.objects.filter(asset_type=lru_type, date__range=[start_date,end_date],is_active=0).exclude(failure_type='Other').exists():
                    response = {'status':'1','Avaiability' : Avalability_data, 'availability_targets' : availability_target_data, 'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
            else:
                if not FailureData.objects.filter(asset_type__in=asset_types, date__range=[start_date,end_date],is_active=0).exclude(failure_type='Other').exists():
                    response = {'status':'1','Avaiability' : Avalability_data, 'availability_targets' : availability_target_data, 'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
                
            if lru_type and lru_type!="all":
                if FailureData.objects.filter(asset_type=lru_type,is_active=0).exclude(failure_type='Other').exists():
                    all_failure = FailureData.objects.filter(asset_type=lru_type,is_active=0).exclude(failure_type='Other')
                    asset_count = Asset.objects.filter(asset_type=lru_type,is_active=0).count()
                else:
                    response = {'Avaiability' : Avalability_data, 'availability_targets' : availability_target_data, 'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
            else:
                if FailureData.objects.filter(asset_type__in=asset_types,is_active=0).exclude(failure_type='Other').exists():
                    all_failure = FailureData.objects.filter(asset_type__in=asset_types,is_active=0).exclude(failure_type='Other')
                    asset_count = Asset.objects.filter(asset_type__in=asset_types,is_active=0).count()
                else:
                    response = {'Avaiability' : Avalability_data, 'availability_targets' : availability_target_data, 'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
            if FN_NAME == 'two':
                fist_hrs = 7*24*asset_count
            else:
                fist_hrs = 7*24
            
            if start_date and end_date : # coming start date and end date are used further calculation
                start_dates = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                end_dates = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            else:
                start_dates = (date.today() - offsets.YearBegin()).date()
                end_dates = (date.today() + offsets.YearEnd()).date()
        
            # print('Start:-',start_dates, 'End:-', end_dates)
            first_week_day = start_dates.weekday()
            first_week_sunday = start_dates + timedelta(days=(5-first_week_day))
            second_week_start_date = first_week_sunday + timedelta(days=1)
            number_of_days = (end_dates-second_week_start_date).days
            if number_of_days % 7 == 0:
                weeks = number_of_days//7
            else:
                weeks = number_of_days/7
            if type(weeks)==float:
                week_number = int(weeks) + 2
            else:
                week_number = weeks + 1 

            if lru_type and lru_type!="all":
                Hightest_date_of_failure = FailureData.objects.filter(asset_config_id__asset_type=lru_type, is_active=0).exclude(failure_type='Other').order_by('-date')
            else:
                Hightest_date_of_failure = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types,is_active=0).exclude(failure_type='Other').order_by('-date')

            print(Hightest_date_of_failure[0].date,'Hightest_date_of_failure')
            Hightest_date_of_failure = str(Hightest_date_of_failure[0].date)
            Hightest_date_of_failure = datetime.datetime.strptime(Hightest_date_of_failure, '%Y-%m-%d').strftime('%Y-%m-%d')
           
            for week in range(1, week_number+1):
                if week == 1:
                    week_start_date = start_dates
                    
                elif week == 2:
                    week_start_date = second_week_start_date
                else:
                    week_start_date = week_end_date + timedelta(days=1)
                if week ==1:
                    week_end_date = first_week_sunday
                else:
                    week_end_date = week_start_date + timedelta(days=6) 
                print("----------------------")
                print(week_start_date,'week_start_date')
                print(week_end_date,'week_end_date')
                
                time_period = week
                if week == 1:
                    cumulative_operating_hours = fist_hrs
                else:
                    cumulative_operating_hours = fist_hrs*week
                if lru_type and lru_type!="all":
                    if FailureData.objects.filter(asset_type=lru_type,is_active=0,date__range=[week_start_date,week_end_date]).exclude(failure_type='Other').exists():
                        Find_Week_wise_Service_Delay1 = FailureData.objects.filter(asset_type=lru_type,is_active=0,date__range=[week_start_date,week_end_date]).exclude(failure_type='Other')
                        Find_Week_wise_Service_Delay = sum([int(item.service_delay) for item in Find_Week_wise_Service_Delay1])
                    else:
                        Find_Week_wise_Service_Delay = None
                else:
                    if FailureData.objects.filter(asset_type__in=asset_types,is_active=0,date__range=[week_start_date,week_end_date]).exclude(failure_type='Other').exists():
                        Find_Week_wise_Service_Delay1 = FailureData.objects.filter(asset_type__in=asset_types,is_active=0,date__range=[week_start_date,week_end_date]).exclude(failure_type='Other')
                        Find_Week_wise_Service_Delay = sum([int(item.service_delay) for item in Find_Week_wise_Service_Delay1])

                    else:
                        Find_Week_wise_Service_Delay = None
                if Find_Week_wise_Service_Delay == None:
                    Week_wise_Service_Delay = 0
                else:
                    Week_wise_Service_Delay = Find_Week_wise_Service_Delay
                    
                # print(Week_wise_Service_Delay)
                
                Week_wise_Service_Delay_Hrs = Week_wise_Service_Delay/60
                
                # print(Week_wise_Service_Delay_Hrs)
                
                if week == 1:
                    Cumulative_service_delay_Hrs = Week_wise_Service_Delay_Hrs
                    Temp_Week_wise_Service_Delay_Hrs = Cumulative_service_delay_Hrs
                else:
                    Cumulative_service_delay_Hrs = Week_wise_Service_Delay_Hrs + Temp_Week_wise_Service_Delay_Hrs
                    Temp_Week_wise_Service_Delay_Hrs = Cumulative_service_delay_Hrs
                Up_Time_Hrs = cumulative_operating_hours - Cumulative_service_delay_Hrs
                Avaiability = Up_Time_Hrs*100 / cumulative_operating_hours

                print(week_end_date,'week_end_date')
                week_end_date1 = datetime.datetime.strptime(str(week_end_date), '%Y-%m-%d').strftime('%Y-%m-%d')
                print(Hightest_date_of_failure,'Hightest_date_of_failure')
                if week_end_date1 < Hightest_date_of_failure or Find_Week_wise_Service_Delay != None:
                    Avaiability = Avaiability
                else:
                    Avaiability = 'null'



                # Avaiability = ((100 - Cumulative_service_delay_Hrs) / cumulative_operating_hours)
                #Avaiability = random.randint(1,100)    
                Avalability_data.append({'x':week, 'y':Avaiability,})
                availability_target_data.append({'x':week, 'y':availability_target,})
                week_scale.append(str(week))
                print(time_period,cumulative_operating_hours,Week_wise_Service_Delay,Week_wise_Service_Delay_Hrs,Cumulative_service_delay_Hrs,Cumulative_service_delay_Hrs,Up_Time_Hrs,Avaiability,availability_target)
                
        response = {'Avaiability' : Avalability_data, 'availability_targets' : availability_target_data, 'rangeScale' : week_scale, 'scale':scale}
        return JsonResponse(response)
    
class ReviewBoardDetailsToPDFView(View):
    template_name = 'PDFreview_details.html'

    def get(self, request, *args, **kwargs):
        req = request.GET
        meeting_id = req.get('meeting_id')

        try:
            review_board = ReviewBoard.objects.get(id=meeting_id)
        except:
            pass
        meeting_date = review_board.meeting_date
        deffect_discussions = DefectDiscussion.objects.filter(review_board=review_board)
        attendees = []
        final_deffects = []
        final_actions = []
        user_roles_data = Group.objects.all()
        for deffect_discussion in deffect_discussions:
            deffect_obj = Defect.objects.get(defect_id=deffect_discussion.defect.defect_id)
            failure_count = FailureData.objects.filter(defect=deffect_discussion.defect).exclude(failure_type='Other').count()

            corrective_actions = deffect_obj.correctiveaction_set.all()
            root_causes = deffect_obj.rootcause_set.all()

            diffects = {'defect_id':deffect_obj.defect_id,
                        'failure_count':failure_count,
                        'corrective_actions':corrective_actions,
                        'defect_status':deffect_obj.defect_status,
                        'oem_number':deffect_obj.oem_defect_reference,
                        'asset_type':deffect_obj.asset_type,
                        'oem_target_date':deffect_obj.oem_target_date,
                        'root_causes':root_causes}

            final_deffects.append(diffects)
            actions = Action.objects.filter(defect_discussion_id=deffect_discussion.defect_discussion_id)
            for action in actions:
                if action not in final_actions:
                    target_date = action.defect_discussion_id.defect.oem_target_date
                    if action.action_status == 'open' and (target_date - meeting_date).days < -7:
                        color = "badge-danger" #Red color                    
                    elif action.action_status == 'open' and (target_date - meeting_date).days > 7:
                        color = "badge-warning" #Yellow color
                    else:
                        color = "badge-success" #Green color
                            
                    final_actions.append({'action':action, 'cls':color})
            for attende in deffect_discussion.attendees.all():
                if attende not in attendees:
                    attendees.append(attende)

        return render(request, self.template_name, {'attendees' : attendees, 
                                                    'review_date':review_board.meeting_date,
                                                    'final_deffects':final_deffects,
                                                    'final_actions':final_actions,
                                                    'user_roles':user_roles_data,
                                                    'meeting_id':meeting_id,
                                                    })

class CumalativeMtbfReportF3View(View):
    template_name = 'cum_actual_mtbf2.html'

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
        Asset_data = Asset.objects.all().distinct('asset_type')
        defect_datas = Defect.objects.all().distinct('defect_id')
        systems = PBSMaster.objects.all().distinct('system')
        return render(request, self.template_name, {'project':project,'asset_data' : Asset_data, 'systems':systems})

    def post(self, request, *args, **kwargs):
        req = request.POST
        project = req.get('project')
        MTBFT = req.get('MTBFT')
        system = req.get('system')
        sub_system = req.get('sub_system')
        FN_NAME = req.get('FN_NAME')
        product_id = req.get('product_id')
        lru_type = req.get('lru_type')
        
        actual_MTBF=[]
        prediced_MTBF=[]
        MTBF_target=[]
        software_mode=[]
        week_scale=[]
        scale = []
        asset_types = []
        pbs_asset_types = []
        
        if req.get('start_date') !="" and req.get('end_date') !="":
            start_date = datetime.datetime.strptime(req.get('start_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            end_date = datetime.datetime.strptime(req.get('end_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            start_date = req.get('start_date')
            end_date = req.get('end_date')
        pbs_mtbf_value = 0
        P_id = request.session['P_id']
        user_ID = request.session['user_ID']
        user_Role = request.session.get('user_Role')
        
        if user_Role == 1:
            Asset_data=Asset.objects.filter(is_active=0)
        else:
            Asset_data=Asset.objects.filter(is_active=0,P_id=P_id)
        pbs_master_data = PBSMaster.objects.filter(is_active=0)
        if FN_NAME == 'two':
            if project != "all":
                if Asset_data.filter(asset_type=lru_type,is_active=0).exists():
                    Asset_data=Asset_data.filter(asset_type=lru_type) 
                    pbs_master_data = pbs_master_data.filter(id=lru_type)
                else:
                    response = {'status':'3','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
        elif FN_NAME == 'three':
            if project != "all":
                SUBSYSTEM=PBSMaster.objects.filter(project_id=project,is_active=0,system=system)
                if not SUBSYSTEM.exists():
                    response = {'status':'3','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                Asset_data=Asset_data.filter(asset_type__in=a) 
                pbs_master_data = pbs_master_data.filter(id__in=a)
        else:
            if project != "all":
                SUBSYSTEM=PBSMaster.objects.filter(project_id=project,is_active=0)
                if not SUBSYSTEM.exists():
                    response = {'status':'3','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
                a=[]
                for SUB in SUBSYSTEM:
                    a.append(SUB.id)
                Asset_data=Asset_data.filter(asset_type__in=a) 
                pbs_master_data = pbs_master_data.filter(id__in=a)
        if FN_NAME == 'two':
            if MTBFT == 'MTBF':
                pbs_mtbf_value = pbs_master_data[0].MTBF
            else:
                pbs_mtbf_value = pbs_master_data[0].MTBSAF
        elif FN_NAME == 'three':
            if Systems.objects.filter(project_id=project,System=system,is_active=0).exists():
                if MTBFT == 'MTBF':
                    D_MTBF = Systems.objects.filter(project_id=project,System=system,is_active=0) 
                    pbs_mtbf_value = D_MTBF[0].MTBF
                else:
                    D_MTBF = Systems.objects.filter(project_id=project,System=system,is_active=0)  
                    pbs_mtbf_value = D_MTBF[0].MTBSAF
            else:
                response = {'status':'4','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                return JsonResponse(response)
        else:
            if MTBFT == 'MTBF':
                D_MTBF = Product.objects.filter(product_id=project) 
                pbs_mtbf_value = D_MTBF[0].MTBF
            else:
                D_MTBF = Product.objects.filter(product_id=project) 
                pbs_mtbf_value = D_MTBF[0].MTBSAF
                
                
        if pbs_mtbf_value == 0:
            response = {'status':'1','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
            return JsonResponse(response)
        
        for ASSET in Asset_data:
            asset_types.append(ASSET.asset_type)

        # req = request.POST
        # system = req.get('system')
        # sub_system = req.get('sub_system')
        # product_id = req.get('product_id')
        # lru_type = req.get('lru_type')
        # start_date = req.get('start_date')
        # end_date = req.get('end_date')
        # pbs_mtbf_value = 0 
        # if system and not (product_id or lru_type):
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem='', product_id='', asset_type='')[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF
        # if system and (sub_system=="all" or product_id=="all" or lru_type=="--All--"):
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem='', product_id='', asset_type='')[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF
        
        # if system and sub_system and not (sub_system=="all" or product_id or lru_type):
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system)[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF

        # if system and sub_system and not lru_type:
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system)[0]
        #     pbs_mtbf_value = pbs_master_data.MTBF

        # if system and sub_system and lru_type and lru_type!="--All--":
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system, asset_type=lru_type)
        #     pbs_mtbf_value = pbs_master_data[0].MTBF

        # if system and sub_system and product_id and product_id!="all":
        #     pbs_master_data = PBSMaster.objects.filter(system=system, subsystem=sub_system, product_id=product_id)
        #     pbs_mtbf_value = pbs_master_data[0].MTBF
        
        # actual_MTBF=[]
        # prediced_MTBF=[]
        # MTBF_target=[]
        # software_mode=[]
        # week_scale=[]
        # scale = []
        # asset_types = []
        # pbs_asset_types = []
        # if system and sub_system == "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if product_id == "all":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem=sub_system)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        # if lru_type == "--All--":
        #     pbs_asset_types = PBSMaster.objects.filter(system=system, subsystem=sub_system, product_id=product_id)
        #     for asset in pbs_asset_types:
        #         asset_types.append(asset.asset_type)
        if (lru_type or asset_types) and asset_types!=['']:
            
            if lru_type and lru_type!="all":
                if not FailureData.objects.filter(asset_type=lru_type, date__range=[start_date,end_date],is_active=0).exclude(failure_type='Other').exists():
                    response = {'status':'3','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
                else:
                    if not Defect.objects.filter(asset_type=lru_type, oem_target_date__range=[start_date,end_date],is_active=0).exists():
                        response = {'status':'2','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                        return JsonResponse(response)
            else:
                if not FailureData.objects.filter(asset_type__in=asset_types, date__range=[start_date,end_date],is_active=0).exclude(failure_type='Other').exists():
                    response = {'status':'3','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
                else:
                    if not Defect.objects.filter(asset_type__in=asset_types, oem_target_date__range=[start_date,end_date],is_active=0).exists():
                        response = {'status':'2','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                        return JsonResponse(response)

            if lru_type and lru_type!="all":
                all_defects = Defect.objects.filter(asset_type=lru_type,is_active=0)
                defects_count = Defect.objects.filter(asset_type=lru_type,is_active=0).count()
                if Asset.objects.filter(asset_type=lru_type,is_active=0).exists():
                    asset_data = Asset.objects.filter(asset_type=lru_type,is_active=0)
                else:
                    response = {'status':'2','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)
            else:
                all_defects = Defect.objects.filter(asset_type__in=asset_types,is_active=0)
                defects_count = Defect.objects.filter(asset_type__in=asset_types,is_active=0).count()
                if Asset.objects.filter(asset_type__in=asset_types,is_active=0):
                    asset_data = Asset.objects.filter(asset_type__in=asset_types,is_active=0)
                else:
                    response = {'status':'2','actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
                    return JsonResponse(response)


            cum_actual_failure_count = 0
            cum_actual_failure_count1 = 0
            predicted_avg_failures_per_week = 0
            actual_mtbf_value = 0
            defects_week = 0
            prediced_mtbf_value = 0
            i=0
            
            # default_date = (date.today() - offsets.YearBegin()).date()
            current_date = datetime.datetime.strptime(str(date.today()), '%Y-%m-%d')
            # print(current_date,'current_date')
            # start_date = ''
            # end_date = ''
            
            # defects_count = all_defects.count()
            if start_date and end_date : # coming start date and end date are used further calculation
                defect_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                defect_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            else:
                defect_start_date = (date.today() - offsets.YearBegin()).date()
                defect_end_date = (date.today() + offsets.YearEnd()).date()

            # print(defect_start_date,'defect_start_date')
            # print(defect_end_date,'defect_end_date')

            first_week_day = defect_start_date.weekday()
            first_week_sunday = defect_start_date + timedelta(days=(5-first_week_day))
            second_week_start_date = first_week_sunday + timedelta(days=1)
            number_of_days = (defect_end_date-second_week_start_date).days
            if number_of_days % 7 == 0:
                weeks = number_of_days//7
            else:
                weeks = number_of_days/7
            if type(weeks)==float:
                week_number = int(weeks) + 2
            else:
                week_number = weeks + 1
            # total_failures_count = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[defect_start_date,defect_end_date]).count()
            #no_defect_failures = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[defect_start_date,defect_end_date], defect=None)
            if lru_type and lru_type!="all":
                distinct_defect_failures = FailureData.objects.filter(asset_config_id__asset_type=lru_type, date__range=[defect_start_date,defect_end_date],is_active=0).exclude(defect=None,failure_type='Other').distinct('defect__defect_id')
            else:
                distinct_defect_failures = FailureData.objects.filter(asset_config_id__asset_type__in=asset_types, date__range=[defect_start_date,defect_end_date],is_active=0).exclude(defect=None,failure_type='Other').distinct('defect__defect_id')
            #defects_count = distinct_defect_failures.count()
            # if no_defect_failures:
            #     defects_count = defects_count + 1
            failure_defects = []
            total_failures_count = 0
            new_total_defect_count = 0
            for distinct_defect_failure in distinct_defect_failures:
                # print(distinct_defect_failure.defect)
                if distinct_defect_failure.defect != None:
                    if distinct_defect_failure.defect.failuredata_set.all():
                        # print('--------work---------')
                        latest_failure_date = distinct_defect_failure.defect.failuredata_set.all().latest('date').date
                        # print(latest_failure_date,'latest_failure_date')
                        # print(second_week_start_date,'second_week_start_date')
                        latest_failure_date = datetime.datetime.strptime(str(latest_failure_date), '%Y-%m-%d')
                        failure_days = (latest_failure_date-second_week_start_date).days
                        # print(failure_days)
                        if failure_days % 7 == 0:
                            failure_weeks = failure_days//7
                        else:
                            failure_weeks = failure_days/7
                        if type(failure_weeks)==float:
                            failure_week_number = int(failure_weeks) + 2
                        else:
                            failure_week_number = failure_weeks + 1
                        # print(len(distinct_defect_failure.defect.failuredata_set.all()),failure_week_number)
                        
                        failure_week_count = (len(distinct_defect_failure.defect.failuredata_set.all())/failure_week_number)*52              
                        total_failures_count += math.ceil(failure_week_count)
                        # print(total_failures_count, math.ceil(failure_week_count))
                        #print(defect_start_date,latest_failure_date,len(distinct_defect_failure.defect.failuredata_set.all()),failure_week_number,failure_week_count, "NEW Calc")
                        new_defect_count = round(len(distinct_defect_failure.defect.failuredata_set.all())/failure_week_number, 2)
                        new_total_defect_count = new_total_defect_count + new_defect_count
                        failure_defects.append({'defect_id':distinct_defect_failure.defect.defect_id, 'count':math.ceil(failure_week_count), 'new_count':new_defect_count})
            print(total_failures_count,'total_failures_count')            
                        # print(new_defect_count, distinct_defect_failure.defect.defect_id, "Rate of defects")
            # print(new_total_defect_count, "New Total Defect Count")
            week_scale.append(str(0))
            actual_MTBF.append({'x':0, 'y':'null',})
            prediced_MTBF.append({'x':0, 'y':'null',})
            software_mode.append({'x':0, 'y': 'null','custome': []})
            asset_count = asset_data.count()
            print(asset_count,"count")
            NOOFDAY = 365 if number_of_days < 365 else number_of_days
            random_failure_count = round((24*NOOFDAY*asset_count)/pbs_mtbf_value,1)
            # print(random_failure_count,"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
            # print('---------befor-----')
            # print(total_failures_count,'total_failures_count')
            if random_failure_count != 0:
                total_failures_count += random_failure_count
                
            print(total_failures_count, random_failure_count,'random_failure_count')
            # print(new_total_defect_count,"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
            avg_failures_per_week = round(total_failures_count/(week_number-1),2)
            duplicate_avg_failures_per_week = avg_failures_per_week
            # print(total_failures_count, avg_failures_per_week, random_failure_count, total_failures_count)
            flag = False
            last_actual_values = []
            last_actual_weeks = []
            for week in range(1, week_number+1):
                print('-----------------------')

                # to get start/end dates of current week
                # if week == 1:
                #     week_start_date = defect_start_date
                # elif week == 2:
                #     week_start_date = second_week_start_date
                # else:
                #     week_start_date = week_end_date + timedelta(days=1)

                # if week ==1:
                #     week_end_date = first_week_sunday
                # else:
                #     week_end_date = week_start_date + timedelta(days=6)
                print(week,'week')
                print(avg_failures_per_week,'avg_failures_per_week')

                if week == 1:
                    week_start_date = defect_start_date
                else:
                    week_start_date = week_end_date + timedelta(days=1)

                week_end_date = week_start_date + timedelta(days=6)

                print(week_start_date,' to ',week_end_date)
                
                if lru_type and lru_type!="all":
                    defects = Defect.objects.filter(is_active=0,asset_type=lru_type, oem_target_date__range=[week_start_date,week_end_date])
                    failure_count = FailureData.objects.filter(is_active=0,asset_type=lru_type, date__range=[week_start_date,week_end_date]).exclude(failure_type='Other').count()
                else:
                    defects = Defect.objects.filter(is_active=0,asset_type__in=asset_types, oem_target_date__range=[week_start_date,week_end_date])
                    failure_count = FailureData.objects.filter(is_active=0,asset_type__in=asset_types, date__range=[week_start_date,week_end_date]).exclude(failure_type='Other').count()
                oem_references = []
                # print(week_start_date, week_end_date, defects, len(defects))
                print(failure_count,'failure_count')
                predicted_avg_failures_per_week = predicted_avg_failures_per_week+avg_failures_per_week
                print(predicted_avg_failures_per_week,'predicted_avg_failures_per_week')
                i = i+1
                if FN_NAME == 'two':
                    lru_population_hours = (asset_count*24*7)*i
                else:
                    lru_population_hours = (24*7)*i
                print(lru_population_hours,'lru_population_hours')
                # print(week_start_date, defects, avg_failures_per_week, predicted_avg_failures_per_week)
                if week_end_date <= current_date:
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>')
                    if failure_count != 0:
                        cum_actual_failure_count = cum_actual_failure_count+failure_count
                        # print(lru_population_hours,cum_actual_failure_count,failure_count,actual_mtbf_value)
                    # print(failure_count, cum_actual_failure_count, "loooooooo")
                    if actual_mtbf_value == 0:
                        actual_mtbf_value = 'null'

                    if cum_actual_failure_count != 0:
                        actual_mtbf_value = round(lru_population_hours/cum_actual_failure_count,2)
                    else:
                        actual_mtbf_value = 'null'

                    findUnit = PBSUnit.objects.filter()
                    if findUnit[0].MTBFMTBSAF == 'days':
                        if actual_mtbf_value != 'null':
                            actual_mtbf_value = round(actual_mtbf_value/24,2)                        
                    elif findUnit[0].MTBFMTBSAF == 'mins':
                        if actual_mtbf_value != 'null':
                            actual_mtbf_value = actual_mtbf_value *60
                    else:
                        actual_mtbf_value = actual_mtbf_value

                    actual_MTBF.append({'x':week, 'y':actual_mtbf_value,})
                    prediced_MTBF.append({'x':week, 'y':'null',})
                    last_actual_values.append(actual_mtbf_value)
                    last_actual_weeks.append(week)
                else:
                    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                    if new_total_defect_count != 0:
                    # if avg_failures_per_week != 0:
                        actual_mtbf_value = 0

                        # new_total_defect_count = round((new_total_defect_count + (random_failure_count/52)),0)
                        # cum_actual_failure_count = cum_actual_failure_count+round((new_total_defect_count + (random_failure_count/52)),0)
                        if flag == False:
                            findUnit = PBSUnit.objects.filter()
                            if findUnit[0].MTBFMTBSAF == 'days':
                                if last_actual_values[-1] != 'null':
                                    last_actual_values[-1] = round(last_actual_values[-1]/24,2)                        
                            elif findUnit[0].MTBFMTBSAF == 'mins':
                                if last_actual_values[-1] != 'null':
                                    last_actual_values[-1] = last_actual_values[-1] *60
                            else:
                                last_actual_values[-1] = last_actual_values[-1]

                            prediced_MTBF.pop()
                            prediced_MTBF.append({'x':last_actual_weeks[-1], 'y':last_actual_values[-1],})
                            flag = True
                        cum_actual_failure_count = cum_actual_failure_count+new_total_defect_count+(random_failure_count/52)
                        prediced_mtbf_value = round(lru_population_hours/predicted_avg_failures_per_week, 2)
                        
                        findUnit = PBSUnit.objects.filter()
                        if findUnit[0].MTBFMTBSAF == 'days':
                            if prediced_mtbf_value != 'null':
                                prediced_mtbf_value = round(prediced_mtbf_value/24,2)                        
                        elif findUnit[0].MTBFMTBSAF == 'mins':
                            if prediced_mtbf_value != 'null':
                                prediced_mtbf_value = prediced_mtbf_value *60
                        else:
                            prediced_mtbf_value = prediced_mtbf_value

                        # prediced_mtbf_value = round(lru_population_hours/predicted_avg_failures_per_week, 2)
                        prediced_MTBF.append({'x':week, 'y':prediced_mtbf_value,})
                print(cum_actual_failure_count,'cum_actual_failure_count')   
                no_of_defect_failures = 0
                # print(prediced_MTBF)
                # print()
                if defects:
                    defects_week = week
                    cum_cta1 = 0
                    for defect in defects: 
                        print(defect,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                        if defect.defect_id in [d['defect_id'] for d in failure_defects]:
                            no_of_defect_failures = [d['count'] for d in failure_defects if d['defect_id']==defect.defect_id][0]
                            new_no_of_defect_failures = [d['new_count'] for d in failure_defects if d['defect_id']==defect.defect_id][0]
                        else:
                            new_no_of_defect_failures = 0
                        # cum_cta = (((defect.oem_target_date).month)/12)*no_of_defect_failures
                        print(new_no_of_defect_failures,'new_no_of_defect_failures')
                        remaining_week = (53-week)/52
                        # total_failures_count = total_failures_count-math.ceil(cum_cta)
                        new_total_defect_count = round((new_total_defect_count - (new_no_of_defect_failures*remaining_week)),2)
                        print(week,(53-week),remaining_week)
                        total_failures_count = total_failures_count - (no_of_defect_failures*remaining_week)
                        oem_references.append(defect.oem_defect_reference)
                    avg_failures_per_week = round(total_failures_count/52,2)
                # print(len(defects), lru_population_hours,avg_failures_per_week,round(predicted_avg_failures_per_week,2),prediced_mtbf_value)
                # print(avg_failures_per_week,predicted_avg_failures_per_week,cum_actual_failure_count,actual_mtbf_value,prediced_mtbf_value,'----',week,"looooooooo")
                MTBF_target.append({'x':week, 'y':pbs_mtbf_value,})
                soft_mode = 'null'
                print(actual_mtbf_value,'actual_mtbf_value')
                print('prediced_mtbf_value',prediced_mtbf_value)
                if len(oem_references) > 0 :
                    soft_mode = '0'
                software_mode.append({'x':week, 'y': soft_mode,'custome': oem_references})
                week_scale.append(str(week))
            updated_predicted_failure_count_list=[]
            lru_population_hours1_list=[]
            lru_population_hours1=0
            updated_predicted_failure_count=0

        response = {'actualMTBF' : actual_MTBF, 'predicedMTBF' : prediced_MTBF, 'MTBFtarget' : MTBF_target, 'softwareMode' : software_mode,'rangeScale' : week_scale, 'scale':scale}
        return JsonResponse(response)