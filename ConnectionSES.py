from xml.etree.ElementTree import tostring
import boto3, os
from dotenv import load_dotenv
from botocore.exceptions import ClientError
import pandas as pd
from sqlalchemy import create_engine
import pymysql

load_dotenv()
password = os.environ["password"]
region_name = os.environ["region_name"]
aws_access_key_id=os.environ["aws_access_key_id"]
aws_secret_access_key=os.environ["aws_secret_access_key"]

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "Sender Name <waelcodezilla@gmail.com>"

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.

# The subject line for the email.
SUBJECT = "Amazon SES Test (SDK for Python)"
# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the 
# ConfigurationSetName=CONFIGURATION_SET argument below.
#CONFIGURATION_SET = "ConfigSet"
# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )
            
# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>.</p>
</body>
</html>
            """            

# The character encoding for the email.
CHARSET = "UTF-8"

# Connection between Boto3 and AWS SES service. 
clientses = boto3.client('ses',region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
verifiedemails = clientses.list_verified_email_addresses()

# Connection between in email survey distribution dashboard and AWS RDS MySQL DB.
# Fetch the emails from the survey table. 
db = pymysql.connect(host="in-email-survey-db.ckwsrtisuili.eu-central-1.rds.amazonaws.com",user = "Admin",password = password, database='in_email_survey_db')
cursor = db.cursor()
cursor.execute("SELECT User_email FROM survey;")
emails = cursor.fetchall()

# Iteration and sending emails over the list of emails addresses tuples.
i=0
for i,tuple in enumerate(emails):
    RECIPIENT = tuple[0]
    if RECIPIENT in verifiedemails['VerifiedEmailAddresses']:
        try:
                #Provide the contents of the email.
                 response = clientses.send_email(Destination={'ToAddresses': [RECIPIENT,],},Message={
                'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,},
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,},},
                'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,},},Source=SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                 #ConfigurationSetName=CONFIGURATION_SET,
                 )
                # Display an error if something goes wrong.	
        except ClientError as e:
                              print(e.response['Error']['Message'])
        else :
                              print("Email sent! Message ID:"),
                              print(response['MessageId'])
    else:
        print(RECIPIENT + " Email is not Verified")

