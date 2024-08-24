variable "ami" {}

provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "app_instance" {
  ami = var.ami
}