from django.shortcuts import render, redirect

from fracas.models import *
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
# Create your views here.


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
            asset_distinct_review_board = ReviewBoard.objects.all().distinct('asset_type')
            asset_data = Asset.objects.all().distinct('asset_type')
        # print(url,'DDDDDD')

        return render(request, self.template_name, {'review_boards' : review_board, 'asset_datas':asset_data, 'asset_distinct_review_boards':asset_distinct_review_board})

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
        
        req = request.GET
        asset_type = unquote(req.get('asset_type'))
        start_date = req.get('start_date')
        end_date = req.get('end_date')
        review_board_id = req.get('r_id')
        review_board = ReviewBoard.objects.get(id=review_board_id)
        # defects = Defect.objects.filter(asset_type=asset_type, defect_open_date=start_date, defect_closed_date=end_date)
        defects = Defect.objects.filter(asset_type=asset_type)
        employees = EmployeeMaster.objects.all()
        print(review_board.meeting_status,'DDDDDD')
        return render(request, self.template_name, {'review_board' : review_board, 'defects':defects, 'employees':employees})

class ReviewBoardDefectDiscussionView(View):
    template_name = 'fracas_review_board_details.html'

    def get(self, request, *args, **kwargs):
        
        data=[]
        
        req = request.GET
        review_board_id = req.get('review_board_id')
        discussion_id = req.get('discussion_id')
        print(discussion_id,"VVVVVVVVVVVVVV")
        review_board = ReviewBoard.objects.get(id=req.get('review_board_id'))
        # defects = Defect.objects.filter(asset_type=asset_type, defect_open_date=start_date, defect_closed_date=end_date)
        
        defect_discussions = DefectDiscussion.objects.filter(review_board=review_board)
        for discussion in defect_discussions:
            employees = discussion.attendees.all()
            print(employees)
            attendees=[]
            for employee in employees:
                attendees.append({'employee_id':employee.employee_id, 'name':employee.name})
            data.append({'review_board_id':discussion.review_board.id,
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
        
        print(defect_id,"mmmmmmmmmmm")
        review_board = ReviewBoard.objects.get(id=review_board_id)
        # defects = Defect.objects.filter(asset_type=asset_type, defect_open_date=start_date, defect_closed_date=end_date)
        defect = Defect.objects.get(defect_id=defect_id)
        employees = EmployeeMaster.objects.filter(employee_id__in=attendees)
        defect_discussion = DefectDiscussion.objects.create(review_board=review_board, defect=defect)
        
        for employee in employees:
            defect_discussion.attendees.add(employee)

        return JsonResponse({'success':'success'})

class AdminReviewBoardUpdateView(View):
    template_name = 'fracas_review_board_details.html'

    def post(self, request, *args, **kwargs):
        
        req = request.POST
        review_board_id = req.get('review_board_id')
        delete_action = req.get('delete_action')
        meeting_status = req.get('meeting_status')
        meeting_outcome = req.get('meeting_outcome')
        review_board = ReviewBoard.objects.get(id=review_board_id)
        print(meeting_outcome,meeting_status,"loooooooo")
        if review_board_id and delete_action:
            print("loooooooo")
            discussions = DefectDiscussion.objects.filter(review_board=review_board)
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
        print(review_board,"SSSSSSSSSSSS")
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
            attendees.append({'employee_id':employee.employee_id, 'name':employee.name})
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
        defect_id = req.get('defect')
        attendees = req.getlist('attendees[]')
        discussion = DefectDiscussion.objects.get(defect_discussion_id=discussion_id)
        defect = ''
        if defect_id:
            defect = Defect.objects.get(defect_id=defect_id)
        employees = EmployeeMaster.objects.filter(employee_id__in=attendees)
        if discussion_id and delete_action:
            actions = Action.objects.filter(defect_discussion_id=discussion.defect_discussion_id)
            actions.delete()
            discussion.delete()
        else:
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
        print(discussion_id,"VVVVVVVVVVVVVV")      
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
        action_description = req.get('action_description')
        action_owner = req.get('action_owner')
        action_status = req.get('action_status')
        action_due_date = ''
        if req.get('action_due_dat'):
            action_due_date = datetime.strptime(req.get('action_due_dat'), "%d/%m/%Y").strftime("%Y-%m-%d") 
        progress_log = req.get('progress_log')

        action = Action.objects.get(action_id=action_id)
        if action_id and delete_action:
            action.delete()
        else:
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

        review_board=ReviewBoard.objects.filter(id=object_id)

        # Add graph to view
        
        if ReviewBoard.objects.filter(id=object_id).first().from_date and ReviewBoard.objects.filter(id=object_id).first().to_date:
            data = FailureData.objects.filter(asset_config_id__asset_type=ReviewBoard.objects.filter(id=object_id).first().asset_type, date__gte=ReviewBoard.objects.filter(id=object_id).first().from_date, date__lte=ReviewBoard.objects.filter(id=object_id).first().to_date).values("date").annotate(y=Count("id")).order_by("date")
        elif ReviewBoard.objects.filter(id=object_id).first().from_date and not ReviewBoard.objects.filter(id=object_id).first().to_date:
            data = FailureData.objects.filter(asset_config_id__asset_type=ReviewBoard.objects.filter(id=object_id).first().asset_type, date__gte=ReviewBoard.objects.filter(id=object_id).first().from_date).values("date").annotate(y=Count("id")).order_by("date")
        elif ReviewBoard.objects.filter(id=object_id).first().to_date and not ReviewBoard.objects.filter(id=object_id).first().from_date:
            data = FailureData.objects.filter(asset_config_id__asset_type=ReviewBoard.objects.filter(id=object_id).first().asset_type, date__lte=ReviewBoard.objects.filter(id=object_id).first().to_date).values("date").annotate(y=Count("id")).order_by("date")
        else:
            data = FailureData.objects.filter(asset_config_id__asset_type=ReviewBoard.objects.filter(id=object_id).first().asset_type).values("date").annotate(y=Count("id")).order_by("date")
        cumulative = 0
        data1=[]
        for d in data:
            data1.append({'x':d['date'], 'y':d['y']})
        for datum in data1:
            cumulative = cumulative + datum['y']
            datum['y'] = cumulative

        chart_data = (
            data1
        )
        asset_type = ReviewBoard.objects.filter(id=object_id).first().asset_type
        asset_data = PBSMaster.objects.filter(asset_type__icontains=asset_type).first()

        expected = []
        if(asset_data and FailureData.objects.all().exists()):
            MTBF = asset_data.MTBF

            if ReviewBoard.objects.filter(id=object_id).first().from_date:
                first_failure_date = ReviewBoard.objects.filter(id=object_id).first().from_date
            else:
                first_failure_date = FailureData.objects.filter(asset_config_id__asset_type=asset_type).order_by("date").first().date
            if ReviewBoard.objects.filter(id=object_id).first().to_date:
                last_failure_date = ReviewBoard.objects.filter(id=object_id).first().to_date
            else:            
                last_failure_date = FailureData.objects.filter(asset_config_id__asset_type=asset_type).order_by("date").last().date

            increment = (last_failure_date - first_failure_date)/10
            expected = []
            dates = [0]*11
            for i in range(11):
                dates[i] = first_failure_date + i*increment
                time_window = ((dates[i] - first_failure_date)*24).days
                expected_failure = time_window*asset_data.asset_quantity/MTBF
                expected.append({'x': dates[i], 'y': expected_failure})

        cumulative = 0
        for datum in expected:
            cumulative = cumulative + datum['y']
            datum['y'] = round(cumulative)

        expected_data = (
            expected
        )

        # Serialize and attach the chart data to the template context

        as_json_chart_data = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        as_json_expected_data = json.dumps(list(expected_data), cls=DjangoJSONEncoder)


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
            attendees.append({'name':employee.name})

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
            defects = Defect.objects.filter(defect_status_remarks=req.get('defect_status_remarks'))
        elif req.get('asset_type'):
            defects = Defect.objects.filter(defect_status_remarks=req.get('asset_type'))
        elif req.get('defect_open_date__gte') and req.get('defect_open_date__lt'):
            defects = Defect.objects.filter(defect_open_date__range=[req.get('defect_open_date__gte'),req.get('defect_open_date__lt')])
        elif req.get('defect_closed_date__gte') and req.get('defect_closed_date__lt'):
            defects = Defect.objects.filter(defect_closed_date__range=[req.get('defect_closed_date__gte'),req.get('defect_closed_date__lt')])
        else:
            defects = Defect.objects.all()
        asset_data = Asset.objects.all().distinct('asset_type')
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
        url_header = request.build_absolute_uri()[:-len(request.get_full_path())]
        formated_start_date = datetime.strptime(start_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        formated_end_date = datetime.strptime(end_date[:15], '%a %b %d %Y').strftime('%Y-%m-%d')
        defect = Defect.objects.create(asset_type=asset_type,start_date=formated_start_date,end_date=formated_end_date)
        return JsonResponse({'asset_type':asset_type.replace(" ","_"), 'start_date':formated_start_date,'end_date':formated_end_date, 'defect_id':defect.defect_id, 'url_header':url_header})

class AdminFailuresView(View):
    template_name = 'fracas_defect_identification_details.html'

    def get(self, request, *args, **kwargs):
        
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
        return render(request, self.template_name, {'defect_id' : defect_id, 'failure_datas':failure_data, 'defect':defect,'defect_failure_datas':defect_failure_data})

class AdminDefectsUpdateView(View):
    template_name = 'fracas_defect_identification_details.html'


    def get(self, request, *args, **kwargs):
        
        data=[]
        
        req = request.GET
        defect_id = req.get('defect_id')     
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
        failure_ids = req.getlist('idsArr[]')
        
        defect = Defect.objects.get(defect_id=defect_id)
        if not delete_defect:
            failure_datas = FailureData.objects.filter(failure_id__in=failure_ids)
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
            for failure_data in failure_datas:
                if not failure_data.defect == defect:
                    failure_data.defect = defect
                    failure_data.save()
        else:
            # corrective_action = CorrectiveAction.objects.get(defect=defect)
            # failure_data = FailureData.objects.get(defect=defect)
            # defect_discussion = DefectDiscussion.objects.get(defect=defect)
            defect.delete()

        return JsonResponse({'success':'success'})

class AdminDefectsFailureAddView(View):
    template_name = 'fracas_defect_identification_details.html'

    # def get(self, request, *args, **kwargs):
        
    #     data=[]
        
    #     req = request.GET
    #     defect_id = req.get('defect_id')

    #     defects = Defect.objects.get(defect_id=defect_id)

    #     failure_defect_data = FailureData.objects.filter(defect=defect)

    #     return render(request, self.template_name, {'defects' : defects, 'failure_defect_datas':failure_defect_data})


    def post(self, request, *args, **kwargs):
        
        req = request.POST
        defect_id = req.get('defect')
        failure_ids = req.getlist('idsArr[]')
        defect = Defect.objects.get(defect_id=defect_id)
        
        failure_datas = FailureData.objects.filter(failure_id__in=failure_ids)

        for failure_data in failure_datas:
            failure_data.defect = defect
            failure_data.save()

        return JsonResponse({'success':'success'})


class AdminDefectsCorrectiveActionAddView(View):
    template_name = 'fracas_defect_identification_details.html'


    def get(self, request, *args, **kwargs):
        
        data=[]
        
        req = request.GET
        defect_id = req.get('defect_id')      
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