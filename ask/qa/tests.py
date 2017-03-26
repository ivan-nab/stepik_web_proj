from django.test import TestCase

# Create your tests here.
def question_add(*args, **kwargs):
    print args.get(0)
    print kwargs.get('name')
question_add("peter",name="michael")
question_add(name="michael")
