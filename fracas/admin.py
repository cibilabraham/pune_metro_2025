from django.contrib import admin
from django.forms import forms
from django.forms import ModelForm, CheckboxSelectMultiple, MultipleChoiceField, DateField, CharField
from django.forms.models import ModelChoiceIterator, ChoiceField, ModelMultipleChoiceField
from fracas.models import FailureData, Asset, FailureMode, Defect, CorrectiveAction, RootCause, ReviewBoard, Action, DefectDiscussion, EmployeeMaster, PBSMaster
from fracas.resources import AssetResource, FailureDataResource, FailureModeResource
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext as _, gettext_lazy
from nested_inline.admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget
from datetime import datetime
from fracas_site import settings
from fracas.forms import DefectForm, RootCauseForm, CorrectiveActionForm, ReviewBoardForm, DefectDiscussionForm, FailureModeForm, FailureDataForm
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count

from django.contrib.admin.utils import unquote
from django.contrib.admin import helpers
from django.utils.encoding import force_text
from django.views.decorators.csrf import csrf_protect

from django.utils.decorators import method_decorator
csrf_protect_m = method_decorator(csrf_protect)
from django.db import models, transaction
from django.contrib.admin import AdminSite



admin.site.index_template = "fracas_home.html"



# Register your models here.


# class CustomModelChoiceField(ModelMultipleChoiceField):
#     def label_from_instance(self, obj):
#         return '{assettype}'.format(assettype=obj.AssetConfigID.Type)

class AssetTypeListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('asset type')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'asset_type'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        if Asset.objects.all().exists():
            asset_type = [(i['asset_type'], i['asset_type']) for i in Asset.objects.values('asset_type').distinct()]
            return asset_type
        return None

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value():   
           return queryset.filter(failuredata__asset_config_id__asset_type=self.value()).distinct()


class CustomModelChoiceIterator(ModelChoiceIterator):
    def choice(self, obj):
        return (self.field.prepare_value(obj),
                self.field.label_from_instance(obj), obj)

class CustomModelChoiceField(ModelMultipleChoiceField):
    defect_queryset = Defect.objects.all()


class CustomNestedTabularInline(NestedTabularInline):
    save_on_top = True
    template = 'defect_discussion_tabular.html'
    extra = 0

class ActionInline(NestedTabularInline):
    model = Action
    fk_name = 'defect_discussion_id'
    extra = 0

class DefectDiscussionInline(CustomNestedTabularInline):
    model = DefectDiscussion
    form = DefectDiscussionForm
    save_on_top = True
    change_form_template = 'review_board_change_form.html'
    fk_name = 'review_board'
    extra = 0
    filter_horizontal = ['attendees', ]
    inlines = [
                ActionInline,
            ]


class FailureDataInline(NestedTabularInline):
    model = FailureData
    verbose_name = "Failure data attributed to this mode"
    fk_name = 'mode_id'
    extra = 0


class CorrectiveActionInline(admin.TabularInline):
    model = CorrectiveAction
    fk_name = 'defect'
    extra = 0

class FailureDataDefectInline(admin.TabularInline):
    model = FailureData
    fk_name = 'defect'
    verbose_name = "Failure data attributed to this defect"
    verbose_name_plural = "Failure data attributed to this defect"
    extra = 0
    max_num = 0
    fields = (
                    'failure_id',
                    'asset_type',
                    'asset_config_id', 
                    'event_description', 
                    'mode_id', 
                    'mode_description',
                    'date', 
                    'time', 
                    'detection', 
                    'service_delay', 
                    'immediate_investigation', 
                    'failure_type', 
                    'safety_failure', 
                    'hazard_id', 
                    'cm_description', 
                    'replaced_asset_config_id', 
                    'cm_start_date', 
                    'cm_start_time', 
                    'cm_end_date', 
                    'cm_end_time', 
                    'oem_failure_reference'
                )
    readonly_fields = (
                    'failure_id',
                    'asset_type',
                    'asset_config_id', 
                    'event_description', 
                    'mode_id', 
                    'date', 
                    'time', 
                    'detection', 
                    'service_delay', 
                    'immediate_investigation', 
                    'failure_type', 
                    'safety_failure', 
                    'hazard_id', 
                    'cm_description', 
                    'replaced_asset_config_id', 
                    'cm_start_date', 
                    'cm_start_time', 
                    'cm_end_date', 
                    'cm_end_time', 
                    'oem_failure_reference'
                ) 
    list_display = (
                    'failure_id',
                    'asset_type',
                    'asset_config_id', 
                    'event_description', 
                    'mode_id', 
                    'mode_description', 
                    'date', 
                    'time', 
                    'detection', 
                    'service_delay', 
                    'immediate_investigation', 
                    'failure_type', 
                    'safety_failure', 
                    'hazard_id', 
                    'cm_description', 
                    'replaced_asset_config_id', 
                    'cm_start_date', 
                    'cm_start_time', 
                    'cm_end_date', 
                    'cm_end_time', 
                    'oem_failure_reference'
                )
    fields = (
                    'failure_id',
                    'asset_type',
                    'asset_config_id', 
                    'event_description', 
                    'mode_id', 
                    'mode_description',
                    'date', 
                    'time', 
                    'detection', 
                    'service_delay', 
                    'immediate_investigation', 
                    'failure_type', 
                    'safety_failure', 
                    'hazard_id', 
                    'cm_description', 
                    'replaced_asset_config_id', 
                    'cm_start_date', 
                    'cm_start_time', 
                    'cm_end_date', 
                    'cm_end_time', 
                    'oem_failure_reference'
                )
    readonly_fields = (
                    'failure_id',
                    'asset_type',
                    'asset_config_id', 
                    'event_description', 
                    'mode_id', 
                    'date', 
                    'time', 
                    'detection', 
                    'service_delay', 
                    'immediate_investigation', 
                    'failure_type', 
                    'safety_failure', 
                    'hazard_id', 
                    'cm_description', 
                    'replaced_asset_config_id', 
                    'cm_start_date', 
                    'cm_start_time', 
                    'cm_end_date', 
                    'cm_end_time', 
                    'oem_failure_reference'
                ) 
    list_display = (
                    'failure_id',
                    'asset_type',
                    'asset_config_id', 
                    'event_description', 
                    'mode_id', 
                    'mode_description', 
                    'date', 
                    'time', 
                    'detection', 
                    'service_delay', 
                    'immediate_investigation', 
                    'failure_type', 
                    'safety_failure', 
                    'hazard_id', 
                    'cm_description', 
                    'replaced_asset_config_id', 
                    'cm_start_date', 
                    'cm_start_time', 
                    'cm_end_date', 
                    'cm_end_time', 
                    'oem_failure_reference'
                )
    list_filter = ( 
                    'date', 
                    'mode_id', 
                    'asset_config_id__asset_type'
                )

class FailureDataAdmin(ImportExportModelAdmin, NestedModelAdmin):
    resource_class = FailureDataResource
    form = FailureDataForm
    list_display = (
                    'failure_id',
                    'asset_type',
                    'asset_config_id', 
                    'event_description', 
                    'mode_id',
                    'date', 
                    'time', 
                    'detection', 
                    'service_delay', 
                    'immediate_investigation', 
                    'failure_type', 
                    'safety_failure', 
                    'hazard_id', 
                    'cm_description', 
                    'replaced_asset_config_id', 
                    'cm_start_date', 
                    'cm_start_time', 
                    'cm_end_date', 
                    'cm_end_time', 
                    'oem_failure_reference'
                )
    search_fields  = [
                    'failure_id',
                    'asset_type',
                    'asset_config_id__asset_config_id', 
                    'asset_config_id__asset_type', 
                    'event_description', 
                    'mode_id__mode_id',
                    'mode_id__mode_description', 
                    'date', 
                    'time', 
                    'detection', 
                    'service_delay', 
                    'immediate_investigation', 
                    'failure_type', 
                    'safety_failure', 
                    'hazard_id', 
                    'cm_description', 
                    'replaced_asset_config_id', 
                    'cm_start_date', 
                    'cm_start_time', 
                    'cm_end_date', 
                    'cm_end_time', 
                    'oem_failure_reference'
                ]  
    list_filter = ( 
                    'asset_type',
                    'date', 
                    'failure_type', 
                    'safety_failure',
                    'mode_id', 
                )
    readonly_fields = ('mode_description',)


class AssetAdmin(ImportExportModelAdmin):
    resource_class = AssetResource
    list_display = (
                    'asset_config_id',
                    'location_id',
                    'location_description',
                    'asset_serial_number',
                    'asset_type',
                    'asset_description',
                    'software_version',
                    'software_description',
                    'asset_status',
                )
    search_fields  = [
                    'asset_config_id',
                    'location_id',
                    'location_description',
                    'asset_serial_number',
                    'asset_type',
                    'asset_description',
                    'software_version',
                    'software_description',
                    'asset_status',
                ] 
    list_filter = [ 
                    'location_id',
                    'asset_serial_number',
                    'asset_type',
                    'asset_description',
                    'software_version',
                    'software_description',
                    'asset_status',
                ]


class CorrectiveActionAdmin(NestedModelAdmin):
        form = CorrectiveActionForm
        extra = 0
        list_display = (
                    'corrective_action_id',
                    'corrective_action_owner',
                    'corrective_action_description',
                    'corrective_action_update',
                    'corrective_action_status',
                )

        search_fields = (
                    'corrective_action_id',
                    'corrective_action_owner',
                    'corrective_action_description',
                    'corrective_action_update',
                    'corrective_action_status',
                )
        list_filter = (
                    'corrective_action_id',
                    'corrective_action_owner',
                    'corrective_action_description',
                    'corrective_action_update',
                    'corrective_action_status',
                )

    
class FailureModeAdmin(ImportExportModelAdmin, NestedModelAdmin):
    change_form_template = 'failure_mode_change_form.html'
    save_on_top = True
    form = FailureModeForm
    inlines =   [
                    FailureDataInline,
                ]

    resource_class = FailureModeResource
    list_display = [
                    'mode_id',
                    'mode_description',
                    'asset_type',
                ]

    search_fields = [
                    'mode_id',
                    'mode_description',
                    'asset_type',
                ]

    list_filter = [
                    AssetTypeListFilter,
                ]


class DefectAdmin(admin.ModelAdmin):
    change_form_template = 'defect_change_form.html'
    form = DefectForm
    save_on_top = True
    inlines = [
                FailureDataDefectInline,
                CorrectiveActionInline,
            ]
    list_display = [
                    'defect_id',
                    'defect_description',
                    'defect_open_date',
                    'defect_closed_date',
                    'investigation',
                    'defect_status',
                    'defect_status_remarks',
                    'oem_defect_reference',
                    'asset_type'
                ]
    search_fields = [
                    'defect_description',
                    'defect_open_date',
                    'defect_closed_date',
                    'investigation',
                    'defect_status',
                    'defect_status_remarks',
                    'oem_defect_reference',
                    'asset_type'
                ]
    list_filter = [
                    'defect_description',
                    'defect_open_date',
                    'defect_closed_date',
                    'investigation',
                    'defect_status',
                    'defect_status_remarks',
                    'oem_defect_reference',
                    'asset_type'
                ]
    blank=True

    def get_mode_id(self, obj):
        return obj.mode_id

    def get_mode_description(self, obj):
        return obj.mode_id.mode_description


class RootCauseAdmin(admin.ModelAdmin):
    form = RootCauseForm
    save_on_top = True
    change_form_template = 'root_cause_change_form.html'
    fields = [
                ('asset_type'),
                ('defect','rca_workshop_date','root_cause_status'),
                # ('rca_workshop_date', 'root_cause_description', 'root_cause_id'),
                ('immediate_cause','leading_reasons','root_cause_description'),
                'defect_failures','corrective_actions',
    ]
    
    list_display = ('root_cause_id', 'asset_type', 'defect', 'rca_workshop_date', 'immediate_cause', 'leading_reasons', 'root_cause_description', 'root_cause_status',)


class ReviewBoardAdmin(NestedModelAdmin):
    save_on_top = True
    change_form_template = 'review_board_change_form.html'
    form = ReviewBoardForm

    fields = [('asset_type', 'from_date', 'to_date',), 'meeting_id', 'meeting_date', 'defect_data',]
    readonly_fields = ['meeting_date',]
    inlines = [
                DefectDiscussionInline,
            ]
    list_display = [
                    'meeting_date',
                    'asset_type',
                    'meeting_id',
                ]
    list_filter = ['asset_type',]

    @csrf_protect_m
    @transaction.atomic
    def change_view(self, request, object_id, form_url='', extra_context=None):

        # Original change_view for inline model admin

        "The 'change' admin view for this model."
        model = self.model
        opts = model._meta

        obj = self.get_object(request, unquote(object_id))

        if not self.has_change_permission(request, obj):
            raise PermissionDenied

        if obj is None:
            raise Http404(_('%(name)s object with primary key %(key)r does not exist.') % {
                          'name': force_text(opts.verbose_name), 'key': escape(object_id)})

        if request.method == 'POST' and "_saveasnew" in request.POST:
            return self.add_view(request, form_url=reverse('admin:%s_%s_add' %
                                                           (opts.app_label,
                                                            opts.module_name),
                                                           current_app=self.admin_site.name))

        ModelForm = self.get_form(request, obj)
        formsets = []
        inline_instances = self.get_inline_instances(request, obj)
        if request.method == 'POST':
            form = ModelForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form_validated = True
                new_object = self.save_form(request, form, change=True)
            else:
                form_validated = False
                new_object = obj
            prefixes = {}
            for FormSet, inline in self.get_formsets_with_inlines(request, new_object):
                prefix = FormSet.get_default_prefix()
                prefixes[prefix] = prefixes.get(prefix, 0) + 1
                if prefixes[prefix] != 1 or not prefix:
                    prefix = "%s-%s" % (prefix, prefixes[prefix])
                formset = FormSet(
                    request.POST, request.FILES, instance=new_object,
                    prefix=prefix, queryset=inline.get_queryset(request),
                )
                formsets.append(formset)
                if hasattr(inline, 'inlines') and inline.inlines:
                    self.add_nested_inline_formsets(request, inline, formset)

            if self.all_valid_with_nesting(formsets) and form_validated:
                self.save_model(request, new_object, form, True)
                self.save_related(request, form, formsets, True)
                change_message = self.construct_change_message(request, form, formsets)
                self.log_change(request, new_object, change_message)
                return self.response_change(request, new_object)

        else:
            form = ModelForm(instance=obj)
            prefixes = {}
            for FormSet, inline in self.get_formsets_with_inlines(request, obj):
                prefix = FormSet.get_default_prefix()
                prefixes[prefix] = prefixes.get(prefix, 0) + 1
                if prefixes[prefix] != 1 or not prefix:
                    prefix = "%s-%s" % (prefix, prefixes[prefix])
                formset = FormSet(instance=obj, prefix=prefix, queryset=inline.get_queryset(request))
                formsets.append(formset)
                if hasattr(inline, 'inlines') and inline.inlines:
                    self.add_nested_inline_formsets(request, inline, formset)

        adminForm = helpers.AdminForm(
            form, self.get_fieldsets(request, obj),
            self.get_prepopulated_fields(request, obj),
            self.get_readonly_fields(request, obj),
            model_admin=self,
        )
        media = self.media + adminForm.media

        inline_admin_formsets = []
        for inline, formset in zip(inline_instances, formsets):
            fieldsets = list(inline.get_fieldsets(request, obj))
            readonly = list(inline.get_readonly_fields(request, obj))
            prepopulated = dict(inline.get_prepopulated_fields(request, obj))
            inline_admin_formset = helpers.InlineAdminFormSet(
                inline, formset, fieldsets, prepopulated, readonly, model_admin=self,
            )
            inline_admin_formsets.append(inline_admin_formset)
            media = media + inline_admin_formset.media
            if hasattr(inline, 'inlines') and inline.inlines:
                extra_media = self.wrap_nested_inline_formsets(request, inline, formset)
                if extra_media:
                    media += extra_media

        context = {
            'title': _('Change %s') % force_text(opts.verbose_name),
            'adminform': adminForm,
            'object_id': object_id,
            'original': obj,
            'is_popup': "_popup" in request.GET,
            'media': media,
            'inline_admin_formsets': inline_admin_formsets,
            'errors': helpers.AdminErrorList(form, formsets),
            'app_label': opts.app_label,
        } 

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
        for datum in data:
            cumulative = cumulative + datum['y']
            datum['y'] = cumulative

        chart_data = (
            data
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
                print(dates[i])
                time_window = ((dates[i] - first_failure_date)*24).days
                expected_failure = time_window*asset_data.asset_quantity/MTBF
                print(time_window, 'x', asset_data.asset_quantity, '/', MTBF, '=', expected_failure )
                expected.append({'date': dates[i], 'y': expected_failure})

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


        extra_context = extra_context or {"expected_data":as_json_expected_data, "chart_data": as_json_chart_data}


        context.update(self.admin_site.each_context(request))
        context.update(extra_context or {})

        # Call the superclass changelist_view to render the page
        return self.render_change_form(request, context, change=True, obj=obj, form_url=form_url)

    
class EmployeeMasterAdmin(ImportExportModelAdmin):
    model = EmployeeMaster

class PBSMasterAdmin(ImportExportModelAdmin):
    model = PBSMaster
    list_display = (
                    'id',
                    'system',
                    'subsystem',
                    'product_id',
                    'product_description',
                    'asset_type',
                    'asset_description',
                    'MTBF',
                    'MTBSAF',
                    'MART',
                    'asset_quantity',
                )

admin.site.site_title = gettext_lazy('Asset Optima site')
admin.site.site_header = gettext_lazy('Asset Optima') 
admin.site.index_title = gettext_lazy('')
admin.site.register(FailureData, FailureDataAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(FailureMode, FailureModeAdmin)
admin.site.register(Defect, DefectAdmin)
admin.site.register(RootCause, RootCauseAdmin)
admin.site.register(ReviewBoard, ReviewBoardAdmin)
admin.site.register(EmployeeMaster, EmployeeMasterAdmin)
admin.site.register(PBSMaster, PBSMasterAdmin)