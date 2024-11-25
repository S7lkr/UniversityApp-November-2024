from django.db import models


class CourseChoices(models.TextChoices):
    WEB_DESIGN = "Web Design", "Web Design"
    GRAPHIC_DESIGN = "Graphic Design", "Graphic Design"
    VIDEO_EDITING = "Video Editing", "Video Editing"
    ONLINE_MARKETING = "Online Marketing", "Online Marketing"
    SOFTWARE_DEVELOPMENT = "Software Development", "Software Development"
    OTHER = "Other", "Other"
