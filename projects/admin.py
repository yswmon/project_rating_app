from django.contrib import admin
from django.db.models import Avg, Count
from .models import Project, Vote

admin.site.register(Vote)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'average_score_display', 'vote_count_display')
    list_display_links = ('title',)
    search_fields = ('title', 'description')

    def average_score_display(self, obj):
        return round(obj.average_score, 2) if obj.average_score is not None else "평가 없음"
    average_score_display.short_description = '평균 점수'
    average_score_display.admin_order_field = 'average_score'

    def vote_count_display(self, obj):
        return obj.vote_count
    vote_count_display.short_description = '누적 투표 수'
    vote_count_display.admin_order_field = 'vote_count'

    def get_queryset(self, request):
        # annotate로 필드 추가
        qs = super().get_queryset(request).annotate(
            average_score=Avg('vote__score'),
            vote_count=Count('vote')
        )
        # 평균 점수 기준 내림차순 정렬
        return qs.order_by('-average_score')

    class Media:
        css = {
            'all': ('admin/css/custom_sort_button.css',)
        }
