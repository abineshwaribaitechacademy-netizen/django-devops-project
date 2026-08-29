variable "aws_region" {
  type        = string
  description = "AWS region where resources will be created"
  default     = "ap-south-1"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t3.micro"
}

variable "ssh_allowed_ip" {
  type        = string
  description = "Public IP address allowed to SSH into EC2"
}

variable "key_name" {
  type        = string
  description = "Existing EC2 key pair name"
}
