import os
import logging

def lambda_handler(event, context):
    submissions = get_submissions()

