from django.core.management.base import BaseCommand,CommandError
from core.models import Course,Module

class Command(BaseCommand):
    help = "load data for Test Use"
    
    def handle(self, *args, **options):
        Module.objects.all().delete()
        Course.objects.all().delete()

        courses = ['Artificial Intelligence','Computer Graphics','Robotics']
        for course in courses:
            Course.objects.create(name=course)
        
        intelligent_module = ['CIS 430/530 - Artificial Intelligence','CIS 431/531 - Machine Learning','CIS 432/532 - Deep Learning']
        
        graphics_module = ['CIS 460/560 - Interactive Computer Graphics','CIS 461/561 - Advanced Computer Graphics',
                           'CIS 462/562 - Virtual Reality','CIS 463/563 - Game Development']
        
        robotics_module = ['CIS 490/590 - Robotics','CIS 491/591 - Robot Vision','CIS 492/592 - Robot Motion Planning']
        
        for module in intelligent_module:
            Module.objects.create(name=module,course=Course.objects.get(name='Artificial Intelligence'))
            
        for module in graphics_module:
            Module.objects.create(name=module,course=Course.objects.get(name='Computer Graphics'))
            
        for module in robotics_module:
            Module.objects.create(name=module,course=Course.objects.get(name='Robotics'))
        
        return "Data Loaded Successfully"
        