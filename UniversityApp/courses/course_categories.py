from django.db import models


class CourseChoices(models.TextChoices):
    WEB_DESIGN = "WD", "Web Design"
    GRAPHIC_DESIGN = "GD", "Graphic Design"
    VIDEO_EDITING = "VE", "Video Editing"
    ONLINE_MARKETING = "OM", "Online Marketing"
    SOFTWARE_DEVELOPMENT = "SD", "Software Development"
    OTHER = "OTH", "Other"
