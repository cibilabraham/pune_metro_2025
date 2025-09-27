from django.urls import path
from forms.views import *
from . import views

urlpatterns = [
    path('asset_register/', assetRegister.as_view(), name='asset_register'),
    path('asset_register/addasset/',AddAsset.as_view(),name='add_asset'),
    path('asset_register/importasset/',ImportAssetForm.as_view(),name='import_asset'),
    path('asset_register/addimportasset/',AddImportAssetReg.as_view(),name='import_asset'),
    path('asset_register/importfailuredata/',ImportFailureData.as_view(),name='import_failure_data'),
    path('asset_register/addfailuredata/',AddImportFailureData.as_view(),name='import_addfailure_data'),
    path('asset_register/addasset/<int:id>/',AddAsset.as_view(),name='add_asset'),
    path('asset_register/delete/',DeleteAsset.as_view(),name='delete_asset'),
    path('asset_register/deleteAll/',DeleteAllAsset.as_view(),name='deleteAll_asset'),

    path('asset_register/get_serial_no/',GetSerialNumber.as_view(),name='get_serial_no'),
    path('asset_register/get_serial_no/<int:id>/',GetSerialNumber.as_view(),name='get_serial_no'),
    
    path('failuredata/',Failuredata.as_view(),name='failuredata'),
    path('failuredata/delete/',DeleteFailureData.as_view(),name='delete_failuredata'),
    path('failuredata/deleteAll/',DeleteAllFailureData.as_view(),name='deleteAll_failuredata'),
    path('failuredata/addfailuredata/',AddFailureData.as_view(),name='add_failuredata'),
    path('failuredata/addfailuredata/<int:id>/',AddFailureData.as_view(),name='add_failuredata'),
    path('failuredata/importfailuredata/',ImportFailureData.as_view(),name='import_failure_data'),
    path('failuredata/addimportfailuredata/',AddImportFailureData.as_view(),name='import_addfailure_data'),
    path('system/',SystemAssetconfig.as_view(),name='system'),
    path('location_id/',SystemLocationId.as_view(),name='location_id'),
    path('km_location_id/',KmSystemLocationId.as_view(),name='location_id'),
    
    path('failuremode/', Failuremode.as_view(), name='failuremode'),
    path('failuremode/import/',ImportFailuremode.as_view(),name='import_failuremode'),
    path('failuremode/addimport/',AddImportFailuremode.as_view(),name='addimport_failuremode'),
    path('failuremode/delete/',DeleteFailuremode.as_view(),name='delete_failuremode'),
    path('failuremode/deleteAll/',DeleteAllFailuremode.as_view(),name='deleteAll_failuremode'),
    path('failuremode/addfailuremode/',AddFailuremode.as_view(),name='add_failuremode'),
    path('failuremode/addfailuremode/<int:id>/',AddFailuremode.as_view(),name='add_failuremode'),
    path('failuremode/listfailuredata/',Listfailuredata.as_view(),name='listfailuredata'),
    path('failuremode/getmodedata/',Listgetmodedata.as_view(),name='listgetmodedata'),
    path('failuremode/getasset_type/',GetAssetType.as_view(),name='getasset_type'),
    path('failuremode/addfailuredata/',AddTempFailureData.as_view(),name='failuremode_add_failuredata'),
    path('failuremode/findmodeid/',FindModeId.as_view(),name='findmodeid'),
    
    path('defect/',DefectsView.as_view(),name='defect'),
    path('defect/<int:add>/',DefectsView.as_view(),name='defect'),
    path('defect/delete/',DeleteDefectsView.as_view(),name='delete_defect'),
    path('defect/deleteAll/',DeleteAllDefectsView.as_view(),name='deleteAll_defect'),
    path('defect/add/',AddDefectsView.as_view(),name='add_defect'),
    
    path('defect/update/',UpdateDefect.as_view(),name='update_defect'),
    path('defect/update/<int:id>/',UpdateDefect.as_view(),name='update_defect'),
    path('failuremode/getdefectdata/',Listgetdefectdata.as_view(),name='getdefectdata'),
    path('defect/listfailuredata/',Listfailuredata1.as_view(),name='listfailuredata'),
    
    path('rootcause/',RootcauseView.as_view(),name='rootcause'),
    path('rootcause/delete/',DeleteRootcauseView.as_view(),name='delete_rootcause'),
    path('rootcause/deleteAll/',DeleteAllRootcauseView.as_view(),name='deleteAll_rootcause'),
    path('rootcause/add/',AddRootcauseView.as_view(),name='add_rootcause'),
    path('rootcause/add/<int:id>/',AddRootcauseView.as_view(),name='add_rootcause'),
    path('rootcause/listfailuredata/',ListfailuredataRootcauseView.as_view(),name='listfailuredata_rootcause'),
    path('rootcause/Correctivedata/',ListgetCorrectivedatas.as_view(),name='Correctivedata'),
    path('rootcause/checkdefect/',Checkdefect.as_view(),name='checkdefect'),
    path('rootcause/GETdefect/',GETdefect.as_view(),name='GETdefect'),
    path('rootcause/CheckCorrectivedata/',CheckCorrectivedata.as_view(),name='CheckCorrectivedata'),
    
    path('review_board/',ReviewBoardView.as_view(),name='review_board'),
    path('review_board/<int:add>/',ReviewBoardView.as_view(),name='review_board'),
    path('review_board/delete/',DeleteReviewBoardView.as_view(),name='delete_review_board'),
    path('review_board/deleteAll/',DeleteAllReviewBoardView.as_view(),name='deleteAll_review_board'),
    path('review_board/add/',AddReviewBoardView.as_view(),name='add_review_board'),


    path('jobcard_register/', jobcardRegister.as_view(), name='job_register'),
    path('jobcard_register/addjobcard/',AddJobcard.as_view(),name='add_jobcard'),
    path('jobcard_register/viewjobcard/',ViewJobcard.as_view(),name='view_jobcard'),
    path('jobcard_register/addjobcard/<int:id>/',AddJobcard.as_view(),name='add_jobcard'),
    path('jobcard_register/viewjobcard/<int:id>/',ViewJobcard.as_view(),name='view_jobcard'),
    path('jobcard_register/dwdjobcard/',DwdJobcard.as_view(),name='dwd_jobcard'),
    path('jobcard_register/dwdjobcard/<int:id>/',DwdJobcard.as_view(),name='dwd_jobcard'),

    path('eir_register/', EIRRegister.as_view(), name='eir_register'),
    path('eir_register/addeir/',AddEIR.as_view(),name='add_eir'),
    path('eir_register/vieweir/',ViewEIR.as_view(),name='view_eir'),
    path('eir_register/addeir/<int:id>/',AddEIR.as_view(),name='add_eir'),
    path('eir_register/vieweir/<int:id>/',ViewEIR.as_view(),name='view_eir'),
    path('eir_register/dwd_eir/',DwdEIR.as_view(),name='dwd_eir'),
    path('eir_register/dwd_eir/<int:id>/',DwdEIR.as_view(),name='dwd_eir'),


    path('kilometre_reading/', KilometreReadingReg.as_view(), name='kilometre_reading'),
    path('kilometre_reading/add_kilometre_reading/',AddKilometreReading.as_view(),name='add_kilometre_reading'),
    path('kilometre_reading/add_kilometre_reading/<int:id>/',AddKilometreReading.as_view(),name='add_kilometre_reading'),
    path('kilometre_reading/importkilometre_reading/',ImportKilometreReadingForm.as_view(),name='importkilometre_reading'),
    path('kilometre_reading/addimportkilometre_reading/',AddImportKilometreReading.as_view(),name='addimportkilometre_reading'),

    path('ncr_register/', NCRRegister.as_view(), name='ncr_register'),
    path('ncr_register/addncr/',AddNCR.as_view(),name='add_ncr'),
    path('ncr_register/addncr/<int:id>/',AddNCR.as_view(),name='add_ncr'),
    path('ncr_register/viewncr/',ViewNCR.as_view(),name='view_ncr'),
    path('ncr_register/viewncr/<int:id>/',ViewNCR.as_view(),name='view_ncr'),
    path('ncr_register/dwd_ncr/',DwdNCR.as_view(),name='dwd_ncr'),
    path('ncr_register/dwd_ncr/<int:id>/',DwdNCR.as_view(),name='dwd_ncr'),


    path('location_id_from_asset_type/',LocatioIDFromAssetType.as_view(),name='location_id_from_asset_type'),
    path('get_all_Serialnumber/',GetAllSerialNumber.as_view(),name='get_all_Serialnumber'),
    path('location_id_from_asset_type_ncr/',LocatioIDFromAssetTypeNcr.as_view(),name='location_id_from_asset_type_ncr'),
    path('get_all_Serialnumber_ncr/',GetAllSerialNumberNcr.as_view(),name='get_all_Serialnumber_ncr'),

    path('downtime_maintenance_log/', ViewDowntimeMaintenanceLog.as_view(), name='downtime_maintenance_log'),
    path('downtime_maintenance_log/add_downtime_maintenance_log/',AddDowntimeMaintenanceLog.as_view(),name='add_downtime_maintenance_log'),
    path('downtime_maintenance_log/add_downtime_maintenance_log/<int:id>/',AddDowntimeMaintenanceLog.as_view(),name='add_downtime_maintenance_log'),
    path('downtime_maintenance_log/delete/',DeleteDowntimeMaintenanceLog.as_view(),name='delete_downtime_maintenance_log'),
    
]
