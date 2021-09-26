import pytest

from polls.models import Choice, Question
from django.utils import timezone


@pytest.mark.django_db
def test_one():
    # Make sure our __str__() addition worked.
    Question.objects.all()

    # Django provides a rich database lookup API that's entirely driven by
    # keyword arguments.
    Question.objects.filter(id=1)
    Question.objects.filter(question_text__startswith='What')

    # Get the question that was published this year.
    current_year = timezone.now().year
    # Question.objects.get(pub_date__year=current_year)
