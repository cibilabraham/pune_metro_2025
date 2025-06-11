from import_export.widgets import ForeignKeyWidget
from fracas.models import Asset, FailureMode, FailureData

class AssetConfigIDForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        val = super(ForeignKeyWidget, self).clean(value)
        if val:
            if not Asset.objects.filter(asset_config_id=value).exists():
                Asset.objects.create(asset_config_id=value)
            return self.get_queryset(value, row, *args, **kwargs).get(**{self.field: val})
        else:
            return None

class ModeIDForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        val = super(ForeignKeyWidget, self).clean(value)
        if val:
            if not FailureMode.objects.filter(mode_id=value).exists():
                if FailureMode.objects.filter(mode_id='default id').exists():
                    FailureMode.objects.filter(mode_id='default id').update(mode_id=val)
                else:    
                    FailureMode.objects.create(mode_id=value)
            return self.get_queryset(value, row, *args, **kwargs).get(**{self.field: val})
        else:
            return None

class ModeDescriptionForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        val = super(ForeignKeyWidget, self).clean(value)
        if val:
            if not FailureMode.objects.filter(mode_description=val).exists():
                if FailureMode.objects.filter(mode_description='default description').exists():
                    FailureMode.objects.filter(mode_description='default description').update(mode_description=val)
                else:
                    FailureMode.objects.create(mode_id='default id', mode_description=val)
            return self.get_queryset(value, row, *args, **kwargs).get(**{self.field: val})
        else:
            return None
