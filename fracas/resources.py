from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from fracas.custom_widgets import AssetConfigIDForeignKeyWidget, ModeIDForeignKeyWidget, ModeDescriptionForeignKeyWidget
from fracas.models import Asset, FailureMode, Defect, FailureData
import logging
import tablib
import traceback
from import_export.utils import atomic_if_using_transaction
from import_export.results import Error, Result, RowResult


try:
    from django.db.transaction import atomic, savepoint, savepoint_rollback, savepoint_commit  # noqa
except ImportError:
    from .django_compat import atomic, savepoint, savepoint_rollback, savepoint_commit  # noqa

logger = logging.getLogger(__name__)
# Set default logging handler to avoid "No handler found" warnings.
logger.addHandler(logging.NullHandler())

class AssetResource(resources.ModelResource):
    def before_import(self, dataset, dry_run, *args, **kwargs):
        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: "", header='id')
            
    class Meta:
        model = Asset

class FailureModeResource(resources.ModelResource):
    
    def before_import(self, dataset, dry_run, *args, **kwargs):
        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: "", header='id')

            
    class Meta:
        model = FailureMode

class FailureDataResource(resources.ModelResource):

    asset_config_id = fields.Field(
                        column_name='asset_config_id',
                        attribute='asset_config_id',
                        widget=AssetConfigIDForeignKeyWidget(Asset, 'asset_config_id')
                    )

    mode_id = fields.Field(
                        column_name='mode_id',
                        attribute='mode_id',
                        widget=ModeIDForeignKeyWidget(FailureMode, 'mode_id')
                    )

    # mode_description = fields.Field(
    #                     column_name='mode_description',
    #                     attribute='mode_description',
    #                     widget=ModeDescriptionForeignKeyWidget(FailureMode, 'mode_description')
    #                 )

    def before_import(self, dataset, dry_run, *args, **kwargs):
        if 'id' not in dataset.headers: 
            dataset.insert_col(0, lambda row: "", header='id')
        return dataset


    def import_data_inner(self, dataset, dry_run, raise_errors, using_transactions, collect_failed_rows, **kwargs):
        result = self.get_result_class()()
        result.diff_headers = self.get_diff_headers()
        result.total_rows = len(dataset)
        print(len(dataset))
        print(dataset['failure_id'])
        failure_ids = []
        duplicate_failure_id = []
        for k in dataset['failure_id']:
            if k not in failure_ids:
                failure_ids.append(k)
            else:
                duplicate_failure_id.append(k)
        print(duplicate_failure_id)
        for failure_id in dataset['failure_id']:
            if FailureData.objects.filter(failure_id=failure_id).exists():
                failure_data = FailureData.objects.filter(failure_id=failure_id)
                failure_data.delete()
        if using_transactions:
            # when transactions are used we want to create/update/delete object
            # as transaction will be rolled back if dry_run is set
            sp1 = savepoint()

        try:
            with atomic_if_using_transaction(using_transactions):
                dataset = self.before_import(dataset, using_transactions, dry_run, **kwargs)
        except Exception as e:
            logger.debug(e, exc_info=e)
            tb_info = traceback.format_exc()
            result.append_base_error(self.get_error_result_class()(e, tb_info))
            if raise_errors:
                raise

        instance_loader = self._meta.instance_loader_class(self, dataset)

        # Update the total in case the dataset was altered by before_import()
        result = self.get_result_class()()
        result.diff_headers = self.get_diff_headers()
        result.total_rows = len(dataset)

        if collect_failed_rows:
            result.add_dataset_headers(dataset.headers)
            print("it's called", dataset.headers)

        for i, row in enumerate(dataset.dict, 1):
            with atomic_if_using_transaction(using_transactions):
                row_result = self.import_row(
                    row,
                    instance_loader,
                    using_transactions=using_transactions,
                    dry_run=dry_run,
                    **kwargs
                )
            result.increment_row_result_total(row_result)

            if row_result.errors:
                if collect_failed_rows:
                    result.append_failed_row(row, row_result.errors[0])
                if raise_errors:
                    raise row_result.errors[-1].error
            elif row_result.validation_error:
                result.append_invalid_row(i, row, row_result.validation_error)
                if collect_failed_rows:
                    result.append_failed_row(row, row_result.validation_error)
                if raise_errors:
                    raise row_result.validation_error
            if (row_result.import_type != RowResult.IMPORT_TYPE_SKIP or
                    self._meta.report_skipped):
                result.append_row_result(row_result)

        try:
            with atomic_if_using_transaction(using_transactions):
                self.after_import(dataset, result, using_transactions, dry_run, **kwargs)
        except Exception as e:
            logger.debug(e, exc_info=e)
            tb_info = traceback.format_exc()
            result.append_base_error(self.get_error_result_class()(e, tb_info))
            if raise_errors:
                raise

        if using_transactions:
            if dry_run or result.has_errors():
                savepoint_rollback(sp1)
            else:
                savepoint_commit(sp1)

        return result


    class Meta:
        model = FailureData
        exclude = ('Defect',)
