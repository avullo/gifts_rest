import pprint

# from restui.serializers.ensembl import EnsemblTranscriptSerializer
# from restui.serializers.uniprot import UniprotEntrySerializer

from rest_framework import serializers

class TaxonomySerializer(serializers.Serializer):
    """
    For nested serialization of taxonomy in call to mapping/<id> endpoint.
    """

    species = serializers.CharField()
    ensemblTaxId = serializers.IntegerField()
    uniprotTaxId = serializers.IntegerField()

class UniprotEntrySerializer(serializers.Serializer):
    uniprotAccession = serializers.CharField()
    entryType = serializers.CharField()
    entryVersion = serializers.IntegerField()
    sequenceVersion = serializers.IntegerField()
    upi = serializers.CharField()
    md5 = serializers.CharField()
    ensemblDerived = serializers.NullBooleanField()
    isoform = serializers.NullBooleanField()

class EnsemblTranscriptSerializer(serializers.Serializer):
    enstId = serializers.CharField()
    enstVersion = serializers.IntegerField()
    upi = serializers.CharField()
    biotype = serializers.CharField()
    deleted = serializers.NullBooleanField()
    seqRegionStart = serializers.IntegerField()
    seqRegionEnd = serializers.IntegerField()
    ensgId = serializers.CharField()
    sequence = serializers.CharField()

class EnsemblUniprotMappingSerializer(serializers.Serializer):
    """
    For nested serialization of Ensembl-Uniprot mapping in call to mapping/<id> endpoint.
    """

    mappingId = serializers.IntegerField()
    timeMapped = serializers.DateTimeField()
    uniprotRelease = serializers.CharField()
    ensemblRelease = serializers.CharField()
    uniprotEntry = UniprotEntrySerializer()
    ensemblTranscript = EnsemblTranscriptSerializer()
    status = serializers.CharField()

class MappingSerializer(serializers.Serializer):
    """
    Serialize data in call to mapping/<id> endpoint.

    JSON specs derived from:
    https://github.com/ebi-uniprot/gifts-mock/blob/master/data/mapping.json
    """
    
    taxonomy = TaxonomySerializer()
    mapping = EnsemblUniprotMappingSerializer()
    relatedMappings = EnsemblUniprotMappingSerializer(many=True)

class CommentSerializer(serializers.Serializer):
    """
    For nested serialization of user comment in call to mapping/comments/<mapping_id> endpoint.
    """

    text = serializers.CharField()
    timeAdded = serializers.DateTimeField()
    user = serializers.CharField()

class LabelSerializer(serializers.Serializer):
    """
    For nested serialization of mapping label in call to mapping/comments/<mapping_id> endpoint.
    """

    text = serializers.CharField()
    timeAdded = serializers.DateTimeField()
    user = serializers.CharField()
    
class MappingCommentsSerializer(serializers.Serializer):
    """
    Serialize data in call to mapping/comments/<mapping_id> endpoint.
    """

    mappingId = serializers.IntegerField()
    status = serializers.CharField()
    user = serializers.CharField()
    comments = CommentSerializer(many=True)
    labels = LabelSerializer(many=True)
