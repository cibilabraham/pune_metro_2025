from django.urls import path, include
from fracas_admin.views import *
from . import views

urlpatterns = [
    path('review_board/',AdminReviewBoardView.as_view(),name='review_board'),
    # path('review_board/add/',AddAdminReviewBoardView.as_view(),name='add_review_board'),
    # path('review_board/details/',AdminReviewBoardDetailsView.as_view(),name='review_board_details'),
    path('review_board/update/',AdminReviewBoardUpdateView.as_view(),name='review_board_update'),
    path('review_board/defect_discussion/',ReviewBoardDefectDiscussionView.as_view(),name='review_defect_discussion'),
    path('review_board/defect_discussion/update/',ReviewBoardDefectDiscussionUpdateView.as_view(),name='review_defect_discussion_update'),
    path('review_board/defect_discussion/attendees/',ReviewBoardDiscussionActionAttendeesView.as_view(),name='review_defect_discussion_attendees'),
    path('review_board/defect_discussion/action/',ReviewBoardDiscussionActionView.as_view(),name='review_defect_discussion_action'),
    path('review_board/defect_discussion/action/update/',ReviewBoardDiscussionActionUpdateView.as_view(),name='review_defect_discussion_action_update'),
    path('review_board/graph/view/',ReviewBoardGraphView.as_view(),name='review_board_graph_view'),

    
    path('defect/failures/details/',AdminFailuresView.as_view(),name='asset_failures_details'),
    path('defect/add/',AdminDefectsAddView.as_view(),name='asset_failures'),
    path('defect/',AdminDefectsView.as_view(),name='fracs_defect'),
    path('defect/update/',AdminDefectsUpdateView.as_view(),name='fracs_defect_add'),
    # path('defect/add/failure/',AdminDefectsFailureAddView.as_view(),name='fracs_defect_add_failure'),
    path('defect/add/c_action/',AdminDefectsCorrectiveActionAddView.as_view(),name='fracs_defect_add_corrective_action'),
    path('defect/add/c_action/update/',AdminDefectsCorrectiveActionUpdateView.as_view(),name='fracs_defect_update_corrective_action'),
    path('defect/remove/failure/',AdminDefectsFailureRemoveView.as_view(),name='fracs_defect_update_corrective_action'),
    
    path('user/list/',ListUsers.as_view(),name='list_user'),
    path('user/add/',AddUsers.as_view(),name='add_user'),
    path('user/add/<int:id>/',AddUsers.as_view(),name='add_user'),
    path('user/delete/',DeleteUsers.as_view(),name='delete_user'),
    path('user/disable/',DisableUsers.as_view(),name='disable_user'),

    # path('rootcause_corrective_status/',RootCauseCorrectiveStatusView.as_view(),name='rootcause_corrective_status'),
    # path('actual_mtbf/',MTBFvsTimeReportView.as_view(),name='Actual MTBF Report'),
    # path('mtbf_growth/',LogPlotMtbfReportView.as_view(),name='Probabilistic Reliability Growth'),
    # path('cum_actual_mtbf/',CumalativeMtbfReportView.as_view(),name='cum_actual_mtbf')
]