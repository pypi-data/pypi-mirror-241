from django.db import models

class VideoImportMeta(models.Model):
    processor = models.ForeignKey('EndoscopyProcessor', on_delete=models.CASCADE)
    center = models.ForeignKey('Center', on_delete=models.CASCADE)
    video_anonymized = models.BooleanField(default=False)
    video_patient_data_detected = models.BooleanField(default=False)
    outside_detected = models.BooleanField(default=False)
    patient_data_removed = models.BooleanField(default=False)
    outside_removed = models.BooleanField(default=False)
    
