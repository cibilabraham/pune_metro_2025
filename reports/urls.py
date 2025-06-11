from django.urls import path, include
from reports.views import *

urlpatterns = [
    path('defect_status/',defectStatus.as_view(),name='defect status'),
    path('review_board/',ReviewBoardView.as_view(),name='review_board'),
    path('review_details/',ReviewBoardDetailsView.as_view(),name='review_details'),
    path('rootcause_corrective_status/',RootCauseCorrectiveStatusView.as_view(),name='rootcause_corrective_status'),
    path('actual_mtbf/',MTBFvsTimeReportView.as_view(),name='Actual MTBF Report'),
    path('mtbf_growth/',LogPlotMtbfReportView.as_view(),name='Probabilistic Reliability Growth'),
    path('cum_actual_mtbf/',CumalativeMtbfReportView.as_view(),name='cum_actual_mtbf'),
    path('cum_actual_mtbf2/',CumalativeMtbfReportF2View.as_view(),name='cum_actual_mtbf2'),
    path('cum_actual_mtbf3/',CumalativeMtbfReportF3View.as_view(),name='cum_actual_mtbf3'),
    path('minuts/download/',ReviewBoardMinutesDownloadView.as_view(),name='minute_download'),
    path('system/',SystemSubsystem.as_view(),name='system'),
    path('product/',Products.as_view(),name='product'),
    path('asset_type/',AssetTypes.as_view(),name='asset_type'),
    path('defect/',DefectTypes.as_view(),name='defect_get'),
    path('project/',Project.as_view(),name='project'),
    path('availability/',AvailabilityView.as_view(),name='availability'),
    path('availability2/',Availability2View.as_view(),name='availability2'),
    
    path('review_details/PDF/',ReviewBoardDetailsToPDFView.as_view(),name='review_detailsPDF'),
]