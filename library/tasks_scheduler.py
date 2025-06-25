from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "daily_overdue_book_loans": {
        "task": "library.tasks.check_overdue_loans",
        "schedule": crontab(hour=9, minute=0),  # This runs 9am everyday
    }
}
