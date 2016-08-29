from django.contrib import admin
from django.contrib.auth.models import Group

from brochure_app.models import Brochure, Questionnaire


class BrochureAdmin(admin.ModelAdmin):
    class Meta:
        model = Brochure
        verbose_name = 'Brochure'


class QuestionnaireAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'email',
        'answer1',
        'answer2',
        'answer3',
        'comments',
    )

    class Meta:
        model = Questionnaire
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'

    def has_add_permission(self, request):
        return False


admin.site.register(Brochure, BrochureAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.unregister(Group)
