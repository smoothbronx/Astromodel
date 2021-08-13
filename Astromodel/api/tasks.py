from celery import shared_task
from .models import Query, WeekActivity

@shared_task
def get_week_activity(date):
    current_year, current_week, _ = date
    list(map(lambda protocol_type: WeekActivity(year=current_year, week=current_week, activity=len(Query.objects.filter(datetime__week=current_week, datetime__year=current_year, protocol=protocol_type, debug=False)), protocol=protocol_type).save(), ("websocket", "http")))
    return f"Collection of analytical data for the period of {current_week} weeks of {current_year} completed successfully."