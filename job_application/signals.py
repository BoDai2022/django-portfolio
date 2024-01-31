# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JobApplication,Feedback
# from django.core.mail import send_mail
import uuid
import boto3
from botocore.exceptions import ClientError
from django.db import transaction

"""
These functions will be executed in a trasaction as save()
or using this code
if created:
    transaction.on_commit(lambda: some_function(instance))
"""
@receiver(post_save, sender=JobApplication)
def create_feedback_link_uuid(sender, instance, created, **kwargs):
    if created and not instance.feedback_link_uuid:
        instance.feedback_link_uuid = str(uuid.uuid4())
        instance.save()
        print("feedback uuid generated! ")
@receiver(post_save, sender=Feedback)
def send_notification_email(sender, instance, created, **kwargs):
    if created:  
        subject = 'God blesses you, Bo. New JobApplication Feedback Received'
        # to do: append link here to view the feedback
        message = f'detailed_feedback: {instance.detailed_feedback}'
        recipient_list = ['dbo837035@gmail.com']  # Replace with the recipient's email
        # send_mail(subject, message, 'dbo837035@gmail.com', recipient_list)
        send_email('dbo837035@gmail.com', recipient_list, subject, message)
        print("email sent! ")

def send_email(from_email, to_emails, subject, body):
    client = boto3.client('ses', region_name='ap-southeast-2')  # Choose the appropriate AWS region
    try:
        response = client.send_email(
            Source=from_email,
            Destination={'ToAddresses': to_emails},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body}}
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])