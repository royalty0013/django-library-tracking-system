from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from .models import Loan


@shared_task
def send_loan_notification(loan_id, message_type="send_loan"):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title

        if message_type == "send_loan":
            subject = "Book Loaned Successfully"
            message = (
                f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            )
        elif message_type == "overdue_loan":
            subject = "Book loan with is overdue"
            message = f"The book you loaned with title {loan.title} is overdue"

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass


@shared_task()
def check_overdue_loans():
    today = timezone.now().date
    overdue_loans = Loan.objects.filter(due_date__lt=today, is_returned=False)
    for loan in overdue_loans:
        send_loan_notification.delay(loan.id, message_type="overdue_loan")
