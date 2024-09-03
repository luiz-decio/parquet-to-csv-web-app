resource "aws_security_group" "allow_ssh_http" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 8501
    to_port = 8501
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}