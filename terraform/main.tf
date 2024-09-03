variable "ami" {}

provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "app_instance" {
  ami = var.ami
  instance_type = "t2.micro"
  subnet_id = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.allow_ssh_http.id]

  user_data = <<-EOF
            !#/bin/bash
            sudo apt-get update
            sudo apt-get install -y docker.io git
            sudo systemctl start docker
            sudo systemctl enable socker

            # Clone GitHub repo
            git clone https://github.com/luiz-decio/parquet-to-csv-web-app.git
            
}