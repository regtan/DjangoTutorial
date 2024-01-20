import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from polls.models import Question
from http import HTTPStatus

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text = question_text, pub_date = time)

class ResultViewTest(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future Question.", days=5)
        response = self.client.get(reverse("polls:results", args=(future_question.id,)))
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_past_question(self):
        past_question = create_question(question_text="Past Question.", days=-5)
        response = self.client.get(reverse("polls:results", args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)
