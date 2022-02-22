# ZenJob-Assignment

Three different directories are created called K8s, Python and terrafom


**k8**

  |------>**cronjob.yml**
              -----> to schedule kubernetes pod job to run on every 5 minutes
              
  |------>**namespace.yml**
              -----> to create 2 different namesapces qa and staging
              
              
**python**

  |------>**Dockerfil**
              -----> containerize the python application
              
  |------>**secrets.py**
              -----> to pass the aws secret and access key
              
  |------>**write_s3.py**
              -----> python script that creates a new file on every execution with date and time as a prefix and uploads to s3 bucket on aws 
              
**terraform**

  |------>**eks-cluster**
              -----> terrafom snippet to create eks cluster with all supporting resources 
              
  |------>**s3-resource**
              -----> terrafom snippet to create s3 resource to upload python executed files
            
