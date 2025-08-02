from django.db import models
from django.forms import ModelForm, DateField, ChoiceField, CharField
from datetime import date
from fracas_site import settings
from django.contrib.admin.widgets import AdminDateWidget
import datetime
import uuid
from django.forms.models import ModelChoiceIterator, ModelMultipleChoiceField
from django.forms.widgets import MultipleHiddenInput
from django.contrib.postgres.fields import *

from django.contrib.auth.models import User,Group

# Create your models here.


class ModelArrowCharField(models.CharField):
    arrow = True
    
class CorrectiveAction(models.Model):
    defect = models.ForeignKey('Defect', on_delete=models.CASCADE)
    # root_cause = models.ForeignKey('RootCause', on_delete=models.CASCADE)
    corrective_action_id = models.AutoField(primary_key=True)
    corrective_action_owner = models.CharField(max_length=550, blank=True)
    corrective_action_description = models.TextField(blank=True)
    corrective_action_update = models.TextField(blank=True)
    corrective_action_status = models.CharField(max_length=550, blank=True)
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)

class FailureMode(models.Model):
    mode_id = models.CharField(max_length=550, unique=True)
    mode_description = models.CharField(max_length=550, null=True, blank=True)
    asset_type = ArrayField(models.CharField(max_length=255, blank=True),default=list)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    P_id = models.IntegerField(default=0)
    is_active = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Failure Mode Identification'


    def __str__(self):
        return self.mode_id

failureTypeChoices = (
    ('software', 'Software'),
    ('hardware', 'Hardware'),
    ('random', 'Random')
)
saftyFailureChoices = (
    ('yes', 'Yes'),
    ('no', 'No')
)
class FailureData(models.Model):
    asset_type = models.CharField(max_length=550, blank=True)
    failure_id = models.CharField(max_length=600, null=True, blank=True)
    asset_config_id = models.ForeignKey('Asset', on_delete=models.CASCADE, to_field='asset_config_id', null=True, blank=True)
    event_description = models.CharField(max_length=600 , null=True)
    mode_id = models.ForeignKey('FailureMode', on_delete=models.SET_NULL, null=True, blank=True)
    mode_description = models.CharField(max_length=600, null=True, blank=True)
    date = models.DateField(null=True)
    time = models.TimeField(max_length=15, null=True)
    detection = models.CharField(max_length=600 , null=True)
    service_delay = models.CharField(max_length=600, null=True, blank=True)
    immediate_investigation = models.TextField(null=True, blank=True)
    failure_type = models.CharField(max_length=600  , default='safety', choices=failureTypeChoices)
    safety_failure = models.CharField(max_length=550, default='yes', choices=saftyFailureChoices)
    hazard_id = models.CharField(max_length=550, null=True, blank=True)
    cm_description = models.TextField(null=True, blank=True)
    replaced_asset_config_id = models.CharField(max_length=500  , null=True)
    cm_start_date = models.DateField(null=True, blank=True)
    cm_start_time = models.TimeField(max_length=15, null=True) 
    cm_end_date = models.DateField(null=True, blank=True)
    cm_end_time = models.TimeField(null=True,blank=True)
    oem_failure_reference = models.TextField(null=True, blank=True)
    defect = models.ForeignKey('Defect', on_delete=models.SET_NULL, null=True, blank=True)
    P_id = models.IntegerField(default=0)
    is_active = models.IntegerField(default=0)
    # root_cause = models.ForeignKey('RootCause', on_delete=models.SET_NULL, null=True, blank=True)
    location_id = models.CharField(max_length=550, null=True, blank=True)
    kilometre_reading = models.CharField(max_length=550, null=True, blank=True)
    sel_car = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    equipment = models.TextField(null=True, blank=True)
    direction = models.TextField(null=True, blank=True)
    no_of_trip_cancel = models.IntegerField(default=0)
    department = models.CharField(max_length=550, null=True, blank=True)
    reported_to_PPIO = models.CharField(max_length=550, null=True, blank=True)
    TO_name = models.TextField(null=True, blank=True)
    incident = models.CharField(max_length=550, null=True, blank=True)
    deboarding = models.CharField(max_length=550, null=True, blank=True)
    def __str__(self):
        return ' '

    class Meta:
        verbose_name_plural = 'Failure data Collection Form'

class Asset(models.Model):
    asset_config_id = models.CharField(max_length=550, unique=True)
    asset_serial_number = models.CharField(max_length=550)
    location_id = models.TextField()
    location_description = models.TextField()
    asset_type = models.IntegerField(default=0)
    software_version = models.CharField(max_length=550)
    asset_description = models.TextField()
    software_description = models.TextField()
    asset_status = models.CharField(max_length=550)
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)
    sub_location = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Asset Register'

    def __str__(self):
        return self.asset_config_id

class Defect(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    asset_type = models.CharField(max_length=550, blank=True)
    defect_id = models.AutoField(primary_key=True)
    defect_description = models.TextField(blank=True)
    defect_open_date = models.DateField(null=True, blank=True)
    defect_closed_date = models.DateField(null=True, blank=True)
    investigation = models.TextField(blank=True)
    defect_status = models.CharField(max_length=550, blank=True)
    defect_status_remarks = models.TextField(blank=True)
    oem_defect_reference = models.TextField(blank=True)
    oem_target_date = models.DateField(null=True, blank=True)
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = '(4) FRACAS Defect Identification'

    def start_date_to_string(self):
        if self.start_date is None:
            return ''
        else:
            return self.start_date.value_to_string(self.start_date, '%d-%m-%y') + '-'

    def end_date_to_string(self):
        if self.end_date is None:
            return ''
        else:
            return self.end_date.value_to_string(self.start_date ,'%d-%m-%y')

    def __str__(self):
        return (str(self.defect_id) + ': ' + str(self.defect_description))

class RootCause(models.Model):
    root_cause_id = models.AutoField(primary_key=True)
    asset_type = models.CharField(max_length=550, blank=True)
    rca_workshop_date = models.DateField(null=True, blank=True)
    root_cause_status = models.CharField(max_length=550, blank=True)
    defect = models.ForeignKey('Defect', on_delete=models.CASCADE, null=True, blank=True)
    immediate_cause = models.TextField(blank=True)
    leading_reasons = models.TextField(blank=True)
    root_cause_description = models.TextField()
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)
    systemic_cause = models.TextField(blank=True)
    organistaional_management_cause = models.TextField(blank=True)
    material_is_damaged = models.CharField(max_length=550, blank=True)
    assembly_no = models.TextField( blank=True)
    

    class Meta:
        verbose_name_plural = 'Root Cause Analysis'


class DefectDiscussion(models.Model):
    defect_discussion_id = models.AutoField(primary_key=True)
    meeting_date = models.DateField(null=True, blank=True, auto_now_add=True)
    attendees = models.ManyToManyField('UserProfile', blank=True)
    review_board = models.ForeignKey('ReviewBoard', on_delete=models.CASCADE)
    defect = models.ForeignKey('Defect', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=550, blank=True)

    def get_asset_type(self):
        if hasattr(self, 'review_board'):
            return self.review_board.asset_type
    
    def __str__(self):
        return ''
        


class Action(models.Model):
    action_id = models.AutoField(primary_key=True)
    action_description = models.CharField(max_length=550, blank=True)
    action_owner = models.CharField(max_length=550, blank=True)
    action_status = models.CharField(max_length=550, blank=True)
    action_due_date = models.DateField(null=True, blank=True)
    progress_log = models.TextField()
    defect_discussion_id = models.ForeignKey('DefectDiscussion', on_delete=models.CASCADE, to_field='defect_discussion_id', null=True, blank=True)
    
    def __str__(self):
        return ''


class ReviewBoard(models.Model):
    asset_type = models.CharField(max_length=550, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    meeting_date = models.DateField(null=True, blank=True, auto_now_add=True)
    meeting_id = models.CharField(max_length=550, blank=True, null=True)
    meeting_status = models.CharField(max_length=550, blank=True)
    meeting_outcome = models.CharField(max_length=550, blank=True)
    is_active = models.IntegerField(default=0)
    P_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = '(6) FRACAS Review'

    def save(self, *args, **kwargs):
        if not self.meeting_id:
            self.meeting_id = self.id
        super(ReviewBoard, self).save(*args, **kwargs)

class EmployeeMaster(models.Model):
    employee_id =  models.CharField(max_length=550, blank=True, null=True)
    name = models.CharField(max_length=550, blank=True)
    designation = models.CharField(max_length=550, blank=True)
   
    def __str__(self):
        if self.employee_id and self.name:
            return self.employee_id + ': ' + self.name
        elif self.employee_id and not self.name:
            return self.employee_id
        elif self.name and not self.employee_id:
            return self.name
        else:
            return ''


    class Meta:
        verbose_name_plural = 'Employee Master'

class PBSMaster(models.Model):
    system = models.CharField(max_length=550, blank=True)
    subsystem = models.CharField(max_length=550, blank=True)
    project = models.ForeignKey('Product', on_delete=models.CASCADE,null=True, blank=True)
    product_id = models.CharField(max_length=550, blank=True)
    product_description = models.CharField(max_length=550, blank=True)
    asset_type = models.CharField(max_length=550, blank=True)
    asset_description = models.CharField(max_length=550, blank=True)
    MTBF = models.FloatField(default=0)
    MTBSAF = models.FloatField(default=0,blank=True)
    MTTR = models.FloatField(default=0,blank=True)
    MART = models.FloatField(default=0,blank=True)
    asset_quantity = models.IntegerField(default=0)
    is_active = models.IntegerField(default=0)
    availability_target = models.FloatField(default=0,blank=True)

    class Meta:
        verbose_name_plural = 'PBS Master'
        
    def __str__(self):
        return self.asset_type

class UserProfile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE,null=True, blank=True)
    user_role = models.ForeignKey(Group, on_delete=models.CASCADE,null=True, blank=True,)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.IntegerField(default=0)
    is_disable = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class UserResetKey(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    key = models.CharField(max_length=255, db_index=True)
    # key_type = models.CharField(choices=keyChoices, max_length=20, null=True, blank=True)
    expires_on = models.DateTimeField(null=True, blank=True)
    otp_expires_on = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class assetRegister(models.Model):
    
    class Meta:
        verbose_name_plural = 'Asset Register'
        
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    MTBF = models.FloatField(default=0)
    MTBSAF = models.FloatField(default=0)
    MTTR = models.FloatField(default=0)
    availability_target = models.FloatField(default=0)
    is_active = models.IntegerField(default=0)
    num_of_trains = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

class temp_table_import_file(models.Model):
    # id = models.TextField()
    system = models.TextField()
    subsystem = models.TextField()
    subsystem_id = models.IntegerField()
    product_id = models.CharField(max_length=550, blank=True)
    product_description = models.TextField()
    asset_type = models.TextField()
    asset_description = models.TextField()
    MTBF = models.TextField()
    MTBSAF = models.TextField()
    MTTR = models.TextField()
    MART = models.TextField()
    asset_quantity = models.TextField()
    error_list = models.TextField()
    updated_by = models.TextField()

    
class temp_table_asset_register(models.Model):
    asset_config_id = models.CharField(max_length=550)
    asset_serial_number = models.CharField(max_length=550)
    location_id = models.TextField()
    location_description = models.TextField()
    asset_type = models.TextField()
    asset_type_id = models.TextField()
    software_version = models.CharField(max_length=550)
    asset_description = models.TextField()
    software_description = models.TextField()
    asset_status = models.CharField(max_length=550)
    is_active = models.IntegerField(default=0)
    P_id = models.TextField()
    error_list = models.TextField()
    updated_by = models.TextField()
    
class temp_table_FailureData(models.Model):
    failure_id = models.TextField()
    asset_type = models.TextField()
    asset_config_id = models.TextField()
    event_description = models.TextField()
    mode_id = models.TextField()
    mode_description = models.TextField()
    date = models.TextField()
    time = models.TextField()
    detection = models.TextField()
    service_delay = models.TextField()
    immediate_investigation = models.TextField()
    failure_type = models.TextField()
    safety_failure = models.TextField()
    hazard_id = models.TextField()
    cm_description = models.TextField()
    replaced_asset_config_id = models.TextField()
    cm_start_date = models.TextField()
    cm_start_time = models.TextField()
    cm_end_date = models.TextField()
    cm_end_time = models.TextField()
    oem_failure_reference = models.TextField()
    defect = models.TextField()
    P_id = models.TextField()
    is_active = models.TextField()
    updated_by = models.TextField()


class temp_table_failure_mode(models.Model):
    mode_id = models.TextField()
    mode_description = models.TextField()
    asset_type = models.TextField()
    asset_type_id = models.TextField()
    error_list = models.TextField()
    P_id = models.TextField()
    updated_by = models.TextField()

class temp_table_failure_data(models.Model):
    failure_id= models.BigIntegerField(null=True)
    asset_type= models.TextField()
    asset_config_id= models.TextField()
    asset_type_id= models.TextField()
    event_description= models.TextField()
    mode_id= models.TextField()
    date= models.TextField()
    time= models.TextField()
    detection= models.TextField()
    service_delay= models.TextField()
    immediate_investigation= models.TextField()
    failure_type= models.TextField()
    safety_failure= models.TextField()
    hazard_id= models.TextField()
    cm_description= models.TextField()
    replaced_asset_config_id= models.TextField()
    cm_start_date= models.TextField()
    cm_start_time= models.TextField()
    cm_end_date= models.TextField()
    cm_end_time= models.TextField()
    oem_failure_reference= models.TextField()
    defect= models.TextField()
    error_list = models.TextField()
    P_id = models.TextField()
    updated_by = models.TextField()
    
class history(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    P_id = models.IntegerField(default=0)
    date = models.DateField(null=True, blank=True)
    message = models.TextField()
    time = models.TimeField(max_length=15, null=True)
    function_name = models.CharField(max_length=50,null=True, blank=True)
    
   
class PBSUnit(models.Model):
    MTBFMTBSAF= models.TextField()
    MTTR = models.TextField()
    average_speed = models.FloatField(default=0)
    chk_average_speed = models.FloatField(default=0)
    running_time = models.IntegerField(default=18)
    num_of_days = models.IntegerField(default=7)

class Systems(models.Model):
    project = models.ForeignKey('Product', on_delete=models.CASCADE,null=True, blank=True)
    System = models.CharField(max_length=550, blank=True)
    MTBF = models.FloatField(default=0)
    MTBSAF = models.FloatField(default=0)
    MTTR = models.FloatField(default=0)
    availability_target = models.FloatField(default=0)
    is_active = models.IntegerField(default=0)

    def __str__(self):
        return self.System

class JobCardIDs(models.Model):
    uid_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=550, null=True, blank=True)
    month = models.CharField(max_length=550, null=True, blank=True)
    last_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Job Card IDs'

    def __str__(self):
        return ''

class JobCard(models.Model):
    job_id = models.AutoField(primary_key=True)
    train_set_no = models.CharField(max_length=550, null=True, blank=True)
    date = models.DateField(null=True)
    time = models.TimeField(max_length=15, null=True)
    department = models.CharField(max_length=550, null=True, blank=True)
    subsystem = models.CharField(max_length=550, blank=True)
    equipment = models.TextField(null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    nature_of_job = models.TextField(null=True, blank=True)
    sic_required = models.TextField(null=True, blank=True)
    assigned_to = models.TextField(null=True, blank=True)
    last_update = models.DateField(auto_now=True, null=True, blank=True)
    status = models.IntegerField(default=0)
    job_card_no = models.CharField(max_length=550, blank=True)
    failure_id = models.ForeignKey('FailureData', on_delete=models.SET_NULL, null=True, blank=True)
    run_status = models.IntegerField(default=0)
    ohe_required = models.CharField(max_length=550, blank=True)
    issued_to = models.TextField(null=True, blank=True)
    completion_time = models.CharField(max_length=550, blank=True)
    from_revenue_service = models.CharField(max_length=550, blank=True)
    delay_to_service = models.CharField(max_length=550, blank=True)
    trip_no = models.CharField(max_length=550, blank=True)
    event_date = models.DateField(null=True)
    event_time = models.TimeField(max_length=15, null=True)
    sic_no = models.CharField(max_length=550, blank=True)
    l1_date = models.DateField(null=True)
    l1_time = models.TimeField(max_length=15, null=True)
    issued_by = models.CharField(max_length=550, blank=True)
    signature_img = models.TextField(null=True, blank=True)
    l2_date = models.DateField(null=True)
    l2_time = models.TimeField(max_length=15, null=True)
    received_by = models.CharField(max_length=550, blank=True)
    signature_img2 = models.TextField(null=True, blank=True)
    signature_img3 = models.TextField(null=True, blank=True)
    follow_up_details = models.TextField(null=True, blank=True)
    details_of_the_activitues = models.TextField(null=True, blank=True)
    handed_over = models.CharField(max_length=550, blank=True)
    new_supervisor = models.CharField(max_length=550, blank=True)

    train_can_be_energized = models.CharField(max_length=550, blank=True)
    completion_name = models.CharField(max_length=550, blank=True)
    down_time = models.CharField(max_length=550, blank=True)
    train_can_be_moved = models.CharField(max_length=550, blank=True)
    completion_date = models.DateField(null=True)
    completion_date_time = models.TimeField(max_length=15, null=True)
    signature_img4 = models.TextField(null=True, blank=True)

    train_can_be_energized2 = models.CharField(max_length=550, blank=True)
    completion_name2 = models.CharField(max_length=550, blank=True)
    down_time2 = models.CharField(max_length=550, blank=True)
    train_can_be_moved2 = models.CharField(max_length=550, blank=True)
    completion_date2 = models.DateField(null=True)
    completion_date_time2 = models.TimeField(max_length=15, null=True)
    signature_img5 = models.TextField(null=True, blank=True)

    corrective_action = models.TextField(null=True, blank=True)
    sic_start_time = models.CharField(max_length=550, blank=True)
    sic_has_performed = models.CharField(max_length=550, blank=True)

    close_name = models.CharField(max_length=550, blank=True)
    close_date = models.DateField(null=True)
    close_time = models.TimeField(max_length=15, null=True)
    signature_img6 = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Job Card'

    def __str__(self):
        return ''


class JobDetails(models.Model):
    job_details_id = models.AutoField(primary_key=True)
    job_card_id = models.ForeignKey('JobCard', on_delete=models.SET_NULL, null=True, blank=True)
    s_no = models.CharField(max_length=550, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    is_active = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Job details'

    def __str__(self):
        return ''
    
class JobWorkToMaintainers(models.Model):
    job_work_id = models.AutoField(primary_key=True)
    job_card_id = models.ForeignKey('JobCard', on_delete=models.SET_NULL, null=True, blank=True)
    jobwork_name = models.CharField(max_length=550, null=True, blank=True)
    jobwork_work = models.TextField(null=True, blank=True)
    jobwork_signature = models.TextField(null=True, blank=True)
    is_active = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Job work'

    def __str__(self):
        return ''

class JobReplacedEquipment(models.Model):
    job_equipment_id = models.AutoField(primary_key=True)
    job_card_id = models.ForeignKey('JobCard', on_delete=models.SET_NULL, null=True, blank=True)
    jobequipment_name = models.CharField(max_length=550, null=True, blank=True)
    jobequipment_new_no = models.CharField(max_length=550, null=True, blank=True)
    jobequipment_old_no = models.CharField(max_length=550, null=True, blank=True)
    is_active = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Job Replaced Equipment'

    def __str__(self):
        return ''
    

class FailureDataIDs(models.Model):
    uid_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=550, null=True, blank=True)
    month = models.CharField(max_length=550, null=True, blank=True)
    last_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Failure Data IDs'

    def __str__(self):
        return ''

class EIRIDs(models.Model):
    uid_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=550, null=True, blank=True)
    last_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'EIR IDs'

    def __str__(self):
        return ''


class EIRGeneration(models.Model):
    eir_id = models.AutoField(primary_key=True)
    eir_gen_id = models.CharField(max_length=550, null=True, blank=True)
    failure_id = models.ForeignKey('FailureData', on_delete=models.SET_NULL, null=True, blank=True)
    depot = models.CharField(max_length=550, null=True, blank=True)
    addressed_by = models.TextField(null=True, blank=True)
    incident_details = models.TextField(null=True, blank=True)
    repercussion = models.TextField(null=True, blank=True)
    incident_location = models.CharField(max_length=550, null=True, blank=True)
    incident_time = models.CharField(max_length=550, null=True, blank=True)
    component = models.TextField(null=True, blank=True)
    action_taken_in_depot = models.TextField(null=True, blank=True)
    concern = models.TextField(null=True, blank=True)
    further_action = models.TextField(null=True, blank=True)
    TRSL = models.CharField(max_length=550, null=True, blank=True)
    signature_img2 = models.TextField(null=True, blank=True)
    signature_img3 = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'EIR'

    def __str__(self):
        return ''

class InvestigationDetails(models.Model):
    details_id = models.AutoField(primary_key=True)
    eir_dt_id = models.ForeignKey('EIRGeneration', on_delete=models.SET_NULL, null=True, blank=True)
    non_compliance_details = models.TextField(null=True, blank=True)
    onvestigation_details = models.TextField(null=True, blank=True)
    relevant_ERTS_clause = models.TextField(null=True, blank=True)
    is_active = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Job details'

    def __str__(self):
        return ''

class EIRImages(models.Model):
    img_id = models.AutoField(primary_key=True)
    eir_dt_id = models.ForeignKey('EIRGeneration', on_delete=models.SET_NULL, null=True, blank=True)
    file_path = models.TextField(null=True, blank=True)
    is_active = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'EIR Images'

    def __str__(self):
        return ''

class KilometreReading(models.Model):
    km_id = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    ts01_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts02_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts03_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts04_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts05_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts06_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts07_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts08_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts09_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts10_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts11_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts12_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts13_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts14_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts15_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts16_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts17_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts18_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts19_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts20_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts21_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts22_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts23_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts24_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts25_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts26_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts27_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts28_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts29_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts30_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts31_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts32_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts33_tkm = models.CharField(max_length=550, null=True, blank=True)
    ts34_tkm = models.CharField(max_length=550, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Kilometre Reading'

    def __str__(self):
        return ''


class NCRGeneration(models.Model):
    rec_id = models.AutoField(primary_key=True)
    ncr_gen_id = models.CharField(max_length=550, null=True, blank=True)
    rootcause_id = models.ForeignKey('RootCause', on_delete=models.SET_NULL, null=True, blank=True)
    date= models.TextField()
    time= models.TextField()
    is_active = models.IntegerField(default=0)

    defect_date = models.CharField(max_length=550, null=True, blank=True)
    corrective_action_date = models.CharField(max_length=550, null=True, blank=True)
    approved_date = models.CharField(max_length=550, null=True, blank=True)
    action_date = models.CharField(max_length=550, null=True, blank=True)
    verification_date = models.CharField(max_length=550, null=True, blank=True)
    fnl_date = models.CharField(max_length=550, null=True, blank=True)

    defect_time = models.CharField(max_length=550, null=True, blank=True)
    defect_description = models.TextField(null=True, blank=True)

    inspector_name = models.TextField(blank=True)
    asset_type = models.CharField(max_length=550, blank=True)
    assembly_name = models.TextField( blank=True)
    assembly_no = models.TextField( blank=True)
    drawing_no = models.TextField(blank=True)
    detection_workstation = models.TextField(blank=True)
    location_id = models.TextField( blank=True)
    sel_car = models.TextField( blank=True)
    serial_no = models.TextField( blank=True)
    green_red_channel = models.TextField( blank=True)

    chkMinor = models.IntegerField(default=0)
    chkMajor = models.IntegerField(default=0)
    chkCritical = models.IntegerField(default=0)

    specification = models.TextField(blank=True)
    defect_source = models.TextField( blank=True)
    supplier_name = models.TextField(blank=True)
    defect_location = models.TextField(blank=True)
    defect_detected_by = models.TextField( blank=True)
    defect_detected_workstation = models.TextField( blank=True)
    no_of_parts_deloverd = models.TextField( blank=True)
    no_of_defective_parts = models.TextField( blank=True)

    active_deviations = models.TextField( blank=True)
    chk_Internal = models.IntegerField(default=0)
    chk_Supplier = models.IntegerField(default=0)
    chk_TWL = models.IntegerField(default=0)
    chk_Transportation = models.IntegerField(default=0)

    ok_img = models.TextField(null=True, blank=True)
    notok_img = models.TextField(null=True, blank=True)
    signature_img = models.TextField(null=True, blank=True)
    signature_img2 = models.TextField(null=True, blank=True)
    signature_img3 = models.TextField(null=True, blank=True)
    signature_img4 = models.TextField(null=True, blank=True)
    signature_img5 = models.TextField(null=True, blank=True)


    initial_analysis = models.TextField(blank=True)
    attachments_files = models.CharField(max_length=550, null=True, blank=True)
    responsibility = models.TextField(blank=True)
    invoice_number = models.TextField(blank=True)
    non_conforming_part_disposition = models.TextField( blank=True)
    responsible_for_execution = models.TextField( blank=True)
    containment_action = models.TextField( blank=True)
    corrective_action_by = models.TextField( blank=True)
    corrective_action_designation = models.TextField( blank=True)
    approved_by = models.TextField( blank=True)
    approved_designation = models.TextField( blank=True)
    action_name = models.TextField( blank=True)
    verification_name = models.TextField( blank=True)
    inp_root_cause = models.TextField( blank=True)
    occurrence = models.TextField( blank=True)
    detection = models.TextField( blank=True)
    effectiveness = models.TextField( blank=True)

    cost_1 = models.CharField(max_length=550, default=0)
    cost_2 = models.CharField(max_length=550, default=0)
    cost_3 = models.CharField(max_length=550, default=0)
    cost_4 = models.CharField(max_length=550, default=0)
    cost_5 = models.CharField(max_length=550, default=0)
    cost_6 = models.CharField(max_length=550, default=0)
    total_cost = models.CharField(max_length=550, default=0)

    no_of_day_open = models.TextField( blank=True)
    physical_closure = models.TextField( blank=True)
    physical_closure_rca_capa = models.TextField( blank=True)
    fnl_name = models.TextField( blank=True)
    fnl_designation = models.TextField( blank=True)

    ncr_status = models.IntegerField(default=0)
    root_cause_analysis = models.CharField(max_length=550, default=0)

    rev_no = models.CharField(max_length=550, default=0)

    remark = models.TextField(blank=True)
    rejection_status = models.IntegerField(default=0)
    accept_status = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'NCR'

    def __str__(self):
        return ''

class NCRIDs(models.Model):
    uid_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=550, null=True, blank=True)
    last_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'NCR IDs'

    def __str__(self):
        return ''

class AssetSerialNumberIDs(models.Model):
    uid_id = models.AutoField(primary_key=True)
    asset_type = models.CharField(max_length=550, null=True, blank=True)
    location_id = models.CharField(max_length=550, null=True, blank=True)
    sub_location = models.CharField(max_length=550, null=True, blank=True)
    last_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Asset Serial Number IDs'

    def __str__(self):
        return ''

class NCRImagesList(models.Model):
    img_id = models.AutoField(primary_key=True)
    ncr_gen_id = models.CharField(max_length=550, null=True, blank=True)
    file_path = models.TextField(null=True, blank=True)
    is_active = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'NCR Images List'

    def __str__(self):
        return ''