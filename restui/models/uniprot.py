from django.db import models

class Domain(models.Model):
    domain_id = models.BigAutoField(primary_key=True)
    isoform = models.ForeignKey('Isoform', models.DO_NOTHING, blank=True, null=True)
    start = models.BigIntegerField(blank=True, null=True)
    end = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domain'

class Ptm(models.Model):
    ptm_id = models.BigAutoField(primary_key=True)
    domain = models.ForeignKey(Domain, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    start = models.BigIntegerField(blank=True, null=True)
    end = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ptm'

class Uniprot(models.Model):
    uniprot_id = models.BigAutoField(primary_key=True)
    uniprot_acc = models.CharField(max_length=30, blank=True, null=True)
    protein_existence_id = models.BigIntegerField(blank=True, null=True)
    species = models.CharField(max_length=30, blank=True, null=True)
    uniprot_tax_id = models.BigIntegerField(blank=True, null=True)
    ensembl_derived = models.NullBooleanField()
    is_isoform = models.NullBooleanField()
    entry_type = models.CharField(max_length=30, blank=True, null=True)
    release_version = models.CharField(max_length=30, blank=True, null=True)
    userstamp = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    entry_version = models.BigIntegerField(blank=True, null=True)
    mapping_history_id = models.BigIntegerField(blank=True, null=True)
    sequence_version = models.SmallIntegerField(blank=True, null=True)
    is_canonical = models.BigIntegerField(blank=True, null=True)
    upi = models.CharField(max_length=13, blank=True, null=True)
    md5 = models.CharField(max_length=32, blank=True, null=True)
    canonical_accession = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uniprot'


class UniprotEntry(models.Model):
    uniprot_id = models.BigAutoField(primary_key=True)
    uniprot_acc = models.CharField(max_length=30, blank=True, null=True)
    uniprot_tax_id = models.BigIntegerField(blank=True, null=True)
    userstamp = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    sequence_version = models.SmallIntegerField(blank=True, null=True)
    upi = models.CharField(max_length=13, blank=True, null=True)
    md5 = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uniprot_entry'


class UniprotEntryHistory(models.Model):
    uniprot_entry_version_id = models.BigAutoField(primary_key=True)
    release_version = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'uniprot_entry_history'
        unique_together = (('uniprot_entry_version_id', 'release_version'),)


class UniprotEntryVersion(models.Model):
    uniprot_entry_version_id = models.BigAutoField(primary_key=True)
    protein_existence_id = models.BigIntegerField(blank=True, null=True)
    ensembl_derived = models.NullBooleanField()
    is_isoform = models.NullBooleanField()
    entry_type = models.CharField(max_length=30, blank=True, null=True)
    userstamp = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    entry_version = models.BigIntegerField(blank=True, null=True)
    is_canonical = models.BigIntegerField(blank=True, null=True)
    canonical_accession = models.CharField(max_length=30, blank=True, null=True)
    uniprot_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uniprot_entry_version'
