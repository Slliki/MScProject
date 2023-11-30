# TASK 2: Cloud Deployment

Overview
--------
Word Frequency is a sample service built with AWS SDK for Go.
The service takes advantage of Amazon EC2 service, Amazon Simple Storage service, Amazon Simple Queue Service and Amazon DynamoDB to collect and report the top 10 most common words of a text file.
The original sample app released by AWS is here:
https://github.com/aws-samples/aws-go-wordfreq-sample

Setup guide
-----------
The rest of this document covers step by step setup of the standard application, ready for further work required in the LSDE coursework (see the separate coursework documentation).

Pre-requisites
--------------
- AWS Academy Foundation Learner Lab account, registered and activated
- SSH Terminal / PuTTy or similar on Windows
- Internet Browser - Google Chrome or Firefox are best


Task A - Launching the Development Instance
-------------------------------------------

1. Log in to AWS Academy and start up the Learner Lab

2. On the lab screen note the remaining credits, and check this as you start each session.
-- $100 should be more than enough for the coursework and all testing (you will need under $50)
-- If you are down to $20 or under shut down any EC2 instances and contact the instructor for advice.

3. Note the session time. You have 4 hours before you need to refresh this Lab page and reopen any AWS Console pages.
-- All resources you create will remain in your Learner Lab for as long as you have credit available, they are not destroyed at the end of a session!

4. Click the 'AWS' button with green status once the Lab has started, to open a new AWS Console page.

5. Go to the EC2 service and launch an instance with the following non-default settings:
-- AMI:
--- Select Ubuntu
--- Select the default AMI (Ubuntu Server 22.04 LTS(HVM), SSD Volume Type)
-- Name: wordfreq-dev
-- Instance Type: t2.micro
-- KeyPair: name: learnerlab-keypair  (create a new keypair then download the .pem file and keep it safe! If using PuTTy on Windows, please download the .ppk file)
-- Security Group: name: wordfreq-dev-sg rule: SSH (default rule)
-- Storage Volume: 30GB GP2
-- IAM instance profile (under Advanced Details): choose EMR_EC2_DefaultRole



Task B - Create the S3 Buckets
-----------------------------

1. Select S3 using the Services dropdown at the top left of the EC2 Console page (it can be helpful to open this in a new browser tab).

2. Create a new S3 Bucket with the following non-default settings. This is your uploading bucket:
-- Bucket name: a unique name, using alphanumeric characters or dashes, perhaps using your initials or date;
   e.g. zj-wordfreq-nov23-uploading

3. Create the second S3 Bucket with the following non-default settings. This is your processing bucket:
-- Bucket name: a unique name, using alphanumeric characters or dashes, perhaps using your initials or date;
   e.g. zj-wordfreq-nov23-processing

4. Make a note of your bucket names for later.

5. Note the bucket ARNs (Amazon Resource Names): on the Bucket list view, select a queue and click 'Copy ARN', then note each bucket ARN for later.

Note: The uploading S3 Bucket is used for uploading text files from your local machine and storing those files.
The files will be copied to your processing S3 bucket.
The bucket will have upload notifications enabled, such that when a file is uploaded, a message notification is automatically added to a wordfreq SQS queue and an email will be sent to you.



Task C - Create the SQS Queues
------------------------------

1. Select SQS using the Services dropdown, ideally opening in another new browser tab.

2. Create a new SQS queue (for file processing jobs) with the following non-default settings:
-- Queue type: Standard
-- Queue name: wordfreq-jobs
-- Access policy: Advanced
-- Change the JSON policy code section that looks like this...:

"Principal": {
        "AWS": "<12 digits>"
      },

-- ...to the following (this allows any AWS entity to write to the queue, not just the queue owner):

"Principal": {
        "AWS": "*"
      },

3. Once the queue is created, take a note of the queue URL ('https://sqs.us-east-1.amazonaws.com/....').

4. Create a second SQS queue (for file processing results) with the following non-default settings:
-- Queue name: wordfreq-results
-- Access policy: Advanced [configure as for the jobs queue]

5. Once again, make a note of the queue URL once it's created.


Task D - Create the Amazon SNS Topic
------------------------------------
1. Select Simple Notification Service (SNS) using the Services dropdown, ideally opening in another new browser tab.

2. Create a topic with the following non-default settings:
-- Type: Standard
-- Name: wordfreq-file-copied
-- Access Policy: Basic, Everyone can publish messages, Everyone can subscribe
-- Create topic and then make a note of your SNS ARN.

3. In the left navigation pane, choose Subscriptions.

4. Create a subscription for the Jobs queue:
-- Topic: wordfreq-file-copied (select)
-- Protocol: Amazon SQS
-- Endpoint: wordfreq-jobs (select)
-- Tick enable raw message delivery

5. Create a second subscription to send an email:
 -- Topic: wordfreq-file-copied (select)
 -- Protocol: Email
 -- Endpoint: your email address (please use a personal address such as a GMail account)
You will receive an email to confirm this subscription, click on the link in the email. Please check your spam folder if you didn't receive the link.



Task E - Configure the File Copied notification from Bucket to SNS
--------------------------------------------------------------------

1. Return to the S3 Console page and click on your processing S3 Bucket (e.g. zj-wordfreq-nov23-processing) > Properties.

2. Scroll down to 'Event notifications', click 'Create event notification'.

3. Configure the following non-default settings:
-- Event name: file-copied-ev
-- Event types: [Select 'All object create events']
-- Destination: SNS topic
-- SNS topic: [Select 'wordfreq-file-copied']

You will receive an email if you've successfully created event notification.

4. Return to the SQS Console page and you are expected to see 1 (test) message available in the Queue wordfreq-jobs. Select wordfreq-jobs and click Actions -> Purge.



Task F - Log in to the Dev Instance and Setup the Environments
--------------------------------------------------------------

1. Return to the EC2 Console and select the wordfreq-dev instance (select the checkbox).

2. Click the Connect button above and select the 'SSH client' tab.

3. The connection instructions are correct if your PC is running Linux or MacOS (in a Terminal window):
-- If you are connecting from a Windows PC, following instructions in sections 'Prerequisites' and 'Connecting to your Linux instance' on the following page:
   https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html
   (This is for PuTTy - other SSH clients are available)
   There is also a helpful 4-min video available from Linux Academy (ensure you use the 'ubuntu' username when logging in):
   https://www.youtube.com/watch?v=bi7ow5NGC-U&lc=Ugh4DAc2SqJj3HgCoAEC

   NOTE: If using PuTTy, pasting text from the system clipboard onto the command line is often achieved using a mouse right-click only.

4. When logging in for the first time, you may need to confirm the connection is valid by typing 'yes'.

5. You should see a command line prompt of the form: 'ubuntu@ip-172-XXX-XXX-XXX' OR ':~ $' (it may take 30 seconds to finally display) - this confirms you have logged in successfully.

6. In your SSH CLI window and run the following command to update the system (it may take a minute or two):

sudo apt update

7. Install AWS CLI and unzip

sudo apt  install awscli
sudo apt install unzip

8. Install and Configure go language

8a. Download the package: 
	wget https://go.dev/dl/go1.20.1.linux-amd64.tar.gz
8b. Unzip the file and move it to the directory
	sudo tar -C /usr/local -xzf go1.20.1.linux-amd64.tar.gz
8c. Add to the $PATH environment variable:
	vi ~/.bash_profile
-- Press 'i' to enter Insert mode in Vi, then paste or type the following:
	export PATH=$PATH:/usr/local/go/bin
-- Now exit Insert mode by pressing the Escape key (Esc)
-- Enter the following key strokes to write updates and quit: colon, lower case 'w' and lower case 'q', then press ENTER, i.e.

:wq

8d. Reload the profile and Check if Go is installed and its version:
	source ~/.bash_profile
	go version

If you see the similar output 'go version go1.20.1 linux/amd64', which indicates that go has successfully been installed.
 

NOTE: To quit the SSH session later, type: exit


Task G - Copy the Application Code zip onto the Dev Instance
------------------------------------------------------------

1. Return to the S3 Console page and click on your uploading Bucket name, e.g. zj-wordfreq-nov23-uploading

2. Click 'Upload' on the 'Objects' tab and select the coursework zip file ('lsde-wordfreq-app.zip'), OR drag the coursework zip file directly onto this webpage and confirm.

3. Once uploaded, click on the blue zip filename link now present in the 'Files and Folders' section.

4. On the file details page that opens, find the S3 URI and click the copy button next to it (or click the 'Copy S3 URI' button) and note it down - we will use this to access the file from the CLI later;
e.g. s3://zj-wordfreq-nov23-uploading/lsde-wordfreq-app.zip

5. Type the following 'S3 list' command to ensure you can see your S3 Bucket name, which shows you have correct permissions. You should be able to see two S3 buckets

aws s3 ls

6. Run the following command, entering your noted down 'S3 URI' instead of S3_URI (don't forget the final dot, with a space before it, indicating to copy to the current directory):

aws s3 cp S3_URI .

7. Check you now have the zip file downloaded on your Dev Instance, then unzip the package:

ls
unzip lsde-wordfreq-app.zip

8. Run the 'ls' command again - you should now see you have a new 'lsde-wordfreq-app' directory.

NOTE: We will leave the zip file in case you need to completely delete the directory AND all its files and start again.
      You can do this with the following command in the home directory: rm -rf lsde-wordfreq-app; unzip lsde-wordfreq-app.zip


Task H - Set up and Configure the WordFreq App
----------------------------------------------

1. Change directory to the app folder and ensure all shell scripts have correct execution permissions:

cd lsde-wordfreq-app
chmod +x *.sh

2. Run the 'setup.sh' script, which will install the GO language runtime and any dependencies, as well as creating the DynamoDB 'wordfreq' database table:

./setup.sh

NOTE: This script should take a couple of minutes to run, and end with 'Setup complete.'. If errors are shown, run it again.
      If there are still other errors (ignore the 'table already exists' error), and you don't get 'Setup complete', please add a post on the BB forum or book an Office Hours session.

3. Optional: In another browser tab, open the DynamoDB Console, click Tables, select wordfreq and click View Items, which will display items (rows) added to the table. Initially the table is empty.

4. You will now need to manually edit the 'run_worker.sh' and 'run_upload.sh' scripts to refer to the correct SQS queue URLs.
-- These instructions assume you will use the 'Vi' editor, but you can install and use any other one, such as GEdit or EMACS, as required.
-- Type the following to open and edit the run_worker.sh script in Vi:

vi run_worker.sh

-- Using the arrow keys, move the cursor down to the following line:

export WORKER_QUEUE_URL="https://sqs.us-east-1.amazonaws.com/12345678/wordfreq-jobs"

-- Press 'i' to enter Insert mode in Vi, then delete the URL and paste or type in your noted URL for the SQS jobs queue between the quotes.
-- Similarly edit the following line, updating the URL value for the results queue with your own:

export WORKER_RESULT_QUEUE_URL="https://sqs.us-east-1.amazonaws.com/12345678/wordfreq-results"

-- Now exit Insert mode by pressing the Escape key (Esc)
-- Enter the following key strokes to write updates and quit: colon, lower case 'w' and lower case 'q', then press ENTER, i.e.

:wq




Task I - Test the Worker and Upload functionality
-------------------------------------------------

1. We will now try to test the basic app functionality. We first need to empty the jobs queue of any spurious messages.
-- Return to the SQS Console window and select the 'wordfreq-jobs' queue (click on the radio button on the left)
-- Click on the 'Purge' button and type in 'purge' where required to confirm you want to delete all messages.


2. SSH Window: Worker
-- Ensure you are in the correct directory and start the worker process. If there are errors, check your SQS URLs in the run_worker.sh file.

cd ~/lsde-wordfreq-app
./run_worker.sh

-- You should see some lines of log output, which will increase when the worker finds jobs to process.

NOTE: The main WordFreq process is this 'worker' application, which runs continuously, checking for jobs on the queue and processing them.

3. Upload any text file (You could use any text file from data.zip on BB) to your to your 'processing' S3 bucket, e.g. zj-wordfreq-nov23-processing


-- You should see after a few moments that the worker retrieves the job and successfully processes the job. You could check the results in your DynamoDB table.
-- You should also have received an email to the address you set up in the SNS topic, which simply contains the job message that has been processed. Notice the S3 information including the object key (file path).

NOTE: The worker performance has been deliberately crippled by adding an extra 'wait' of between 10-20 seconds during processing, which you must not modify.
This makes it much easier to ensure the scaling operation is effective without requiring hundreds of input files.

-- If you observed the output described above, the basic application is working. We now just need to set it up as a Linux service.


Task J - Setting up the Worker Service
--------------------------------------

1. In your SSH Window:
-- Press CTRL+c to exit the worker.sh process.
-- Set up the WordFreq Worker service by running the shell script:

./configure-service.sh

NOTE 1: This command installs the Worker.sh command as a service, which runs in the background and will auto-start on boot.
        It's important that any auto-scaling EC2 worker instances have this service configured in this way.

NOTE 2: If you do NOT get a 'Service started successfully' message, run again, or run through the setup process again.
        If you still experience issues, please post on the BlackBoard Discussion Forum for LSDE, or book an Office Hours session.

-- To view the output logs from the running wordfreq worker service, enter the following (CTRL+c to exit):

sudo journalctl -f -u wordfreq

NOTE: To stop or start the wordfreq worker service, run the following commands, respectively:

sudo systemctl stop wordfreq
sudo systemctl start wordfreq

2. In your processing S3 bucket:
-- We need to upload the test file again to check our new service processes it correctly
-- Upload any text file (You could use any text file from data.zip on BB) to your to your 'processing' S3 bucket, e.g. zj-wordfreq-nov23-processing


3. Check again that SSH Window shows the worker output in the log entries. Again, you should receive a job email.

4. At this point, press CTRL+c in your SSH Window if you don't need it anymore, and pat yourself on the back, we're done!
-- BUT ... make an AMI backup of this EC2 instance - see 'strong recommendation' below - THEN you can relax. ;-)


Task K - Upload files to your S3 uploading bucket
-------------------------------------------------

We will use the two S3 buckets to simplify the uploading of files for processing by the application

1. Download data.zip from BB.

2. Unzip the downloaded file and review the files in the folder. You should have about 120 text files in the folder.
Ensure:
•	Files are in text (.txt) format only, no binary files should be used.
•	Filenames have no spaces or non-alphanumeric characters (hypens, underscores are ok).

3. Upload these files to your 'uploading' S3 bucket, e.g. zj-wordfreq-nov23-uploading


Task L - Copy files to your S3 processing bucket to start processing them
-------------------------------------------------------------------------

1. To start processing these files with your worker application service, we simply copy the text files (only) from the uploading bucket to the processing bucket.
-- NOTE: This operation may take around 20 minutes and will generate 120 emails to your email address if successful! You will only need the screenshot of one email. If you wish to stop receiving emails, delete the SNS Topic's email subscription in AWS, or click on the unsubscribe link in each email.
-- Run the following S3 copy command in SSH

aws s3 cp s3://<name of uploading bucket> s3://<name of processing bucket> --exclude "*" --include "*.txt" --recursive

e.g.
  aws s3 cp s3://zj-wordfreq-nov23-uploading s3://zj-wordfreq-nov23-processing --exclude "*" --include "*.txt" --recursive

2. Observe the processing log as the application begins to process the files:
sudo journalctl -f -u wordfreq



Task M - Consult the Coursework Doc for tasks
---------------------------------------------

- When implementing and testing autoscaling, you will be mainly using the following operations of those we have learned here:
-- Copying files from the uploading bucket to the processing bucket to start processing them (Task L)
-- Purging (emptying) messages from the queues (Use the 'purge' button in the SQS console - Task E(4))
-- Reviewing the worker logs on an EC2 instance (Task J/L)
-- Stopping or starting the workfreq worker service if necessary on an EC2 instance (Task J)
-- Running the run_upload.sh script on the Dev Instance for initial testing (Task I)

NOTE: The infrastructure configuration we have performed is functional, but not necessarily optimal or best practice...






IMPORTANT NOTES
===============
- When you have finished a coursework session, ensure that any EC2 instances are stopped to minimise cost.
NOTE 1: The approximate cost for a running EC2 t2.micro instance is about 2 cents (US) per hour, but it adds up if never stopped.
NOTE 2: You do not pay for stopped EC2 instances, but you still pay for their EBS storage volumes, however this is a fraction of the EC2 cost.
- When you restart an EC2 instance, the free Public IP changes, so if you are accessing SSH via the IP address only, you will need to copy the new one.

------------------------------------------------------------------------
STRONG Recommendation: Create an AMI Backup before ending this session!!
------------------------------------------------------------------------
- Create an AMI image from the running EC2 instance (Instances > select wordfreq-dev > Actions > 'Image and templates' > Create image).
- If you lose your configured EC2 instance, check with the instructors on how to retrieve your configuration from the AMI, or rebuild a new EC2 instance as above.
- EBS Snapshots can also be used to store incremental backups of an EBS disk volume used by an instance.


SUPPORT
=======
For any general or technical issues with this setup, please start a new post on the BlackBoard Coursework Discussion Forum
Alternatively, for one-to-one support, please book an Office Hours Session with the instructor or a TA.