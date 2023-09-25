from django.test import TestCase, Client
from django.urls import reverse
from .models import Task
from .forms import Taskform

# Create your tests here.
class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")

    def test_task_form_valid(self):
        data = {"title": "Test Task"}
        form = Taskform(data=data)
        self.assertTrue(form.is_valid())


class TaskIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(title="Test Task")

    def test_task_list_view(self):
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_edit_view(self):
        response = self.client.get(reverse("edit_task", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edit Task")

