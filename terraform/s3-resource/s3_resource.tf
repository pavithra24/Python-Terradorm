#Variablize multiple buckets

variable "s3_bucket_names" {
  type = list
  default = ["qa-firstname-lastname-platform-challenge-67896", "staging-firstname-lastname-platform-challenge-67896"]
}

#create s3 buckets

resource "aws_s3_bucket" "qa_stage" {
  count         = length(var.s3_bucket_names)
  bucket        = var.s3_bucket_names[count.index]
  force_destroy = true
}


#apply the lifecycle rule for s3 keep the objects for 24h

resource "aws_s3_bucket_lifecycle_configuration" "qa" {
  bucket = "qa-firstname-lastname-platform-challenge-67896"

  rule {
        status = "Enabled"
      expiration {
        days = 1
      }

      id = "py"
    }
   depends_on = [
           "aws_s3_bucket.qa_stage",
       ]
 }

 resource "aws_s3_bucket_lifecycle_configuration" "stage" {
   bucket = "staging-firstname-lastname-platform-challenge-67896"

   rule {
         status = "Enabled"
       expiration {
         days = 1
       }

       id = "py"
     }
     depends_on = [
                "aws_s3_bucket.qa_stage",
            ]
  }
