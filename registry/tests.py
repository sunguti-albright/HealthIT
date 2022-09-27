from django.test import TestCase

# Create your tests here.

from .models import Profile,Report
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        user = User.objects.create()
        self.new_profile = Profile(user = user,bio = 'test_bio',created = '2022-09-27')
        self.new_profile.save()
        def test_instance(self):
            self.assertTrue(isinstance(self.new_profile,Profile)) 


class ReportTestClass(TestCase):
        def setUp(self):
            user = User.objects.create()


            self.new_report = Report(project_name ='test_report_name',description = 'test_description',created = '2022-09-27',author = user )

        def test_instance(self):
            self.assertTrue(isinstance(self.new_report,Report))   

        def test_save_method(self):
            self.new_project.save_project()
            project = Report.objects.all()
            self.assertTrue(len(project) > 0)    

        def tearDown(self):
            Report.objects.all().delete()
            Profile.objects.all().delete()

        def test_delete_method(self):
            self.new_project.save_project()
            self.new_project.delete_project()
            project = Report.objects.all()
            self.assertTrue(len(project) == 0)    

        def test_update_method(self):
            self.new_project.save_project()
            self.new_project.update_project()
            project = Report.objects.all()
            self.assertTrue(len(project) > 0) 

        def test_get_project_by_id(self):
            id = Report.get_project_by_id()
            self.assertTrue(len(id) == 0)    


