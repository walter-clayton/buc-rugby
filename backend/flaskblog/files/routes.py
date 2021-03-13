from flask import render_template, Blueprint
import boto3 


files = Blueprint('files', __name__)

@files.route("/file")
def file():
    s3_resource = boto3.resource('s3',
        aws_access_key_id='AKIAT2SZHIJOKKFNYTGO',
        aws_secret_access_key='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'
    )
    my_bucket = s3_resource.Bucket('afitpilot-stage')
    summaries = my_bucket.objects.all()
    return render_template('files.html', my_bucket=my_bucket, files=summaries)