from django.contrib import admin
from .models import (
    GrowSubSection,
    SubSectionDetails,
    GrowSection,
    ContectSections,
    ContectSubSections,
    SubContectDetails,
    SectionCategory,
    News,
    WelcomeLine

    )


admin.site.register(GrowSubSection)
admin.site.register(SectionCategory)
admin.site.register(SubSectionDetails)
admin.site.register(GrowSection)
admin.site.register(ContectSections)
admin.site.register(ContectSubSections)
admin.site.register(SubContectDetails)
admin.site.register(News)
admin.site.register(WelcomeLine)


