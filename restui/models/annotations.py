from django.db import models
from django.conf import settings

class CvEntryType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_entry_type'


class CvUeLabel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'cv_ue_label'


class CvUeStatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cv_ue_status'

# schema supporing editing comments/status for mapped entries

class UeMappingComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    time_stamp = models.DateTimeField()
    user_stamp = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_stamp')
    comment = models.TextField()
    mapping = models.ForeignKey('Mapping', models.DO_NOTHING, related_name='comments', blank=True, null=True)
    deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ue_mapping_comment'


class UeMappingLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    time_stamp = models.DateTimeField()
    user_stamp = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_stamp')
    label = models.ForeignKey('CvUeLabel', models.DO_NOTHING, db_column='label')
    mapping = models.ForeignKey('Mapping', models.DO_NOTHING, related_name='labels', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ue_mapping_label'


class UeMappingStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    time_stamp = models.DateTimeField()
    user_stamp = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, db_column='user_stamp')
    status = models.ForeignKey('CvUeStatus', db_column='status', to_field='id', on_delete=models.CASCADE)
    mapping = models.ForeignKey('Mapping', related_name='status_history', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ue_mapping_status'

# and the same for unmapped entries

class UeUnmappedEntryComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    time_stamp = models.DateTimeField()
    user_stamp = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_stamp')
    comment = models.TextField()
    uniprot = models.ForeignKey('UniprotEntry', models.DO_NOTHING, related_name='comments', blank=True, null=True)
    deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ue_unmapped_entry_comment'


class UeUnmappedEntryLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    time_stamp = models.DateTimeField()
    user_stamp = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_stamp')
    label = models.ForeignKey('CvUeLabel', models.DO_NOTHING, db_column='label')
    uniprot = models.ForeignKey('UniprotEntry', models.DO_NOTHING, related_name='labels', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ue_unmapped_entry_label'


class UeUnMappedEntryStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    time_stamp = models.DateTimeField()
    user_stamp = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, db_column='user_stamp')
    status = models.ForeignKey('CvUeStatus', db_column='status', to_field='id', on_delete=models.CASCADE)
    uniprot = models.ForeignKey('UniprotEntry', related_name='status_history', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ue_unmapped_entry_status'
