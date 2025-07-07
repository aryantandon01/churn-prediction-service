variable "aws_region" {
  default = "ap-south-1" # e.g., Mumbai
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "Name of your existing AWS key pair for SSH"
}

variable "docker_image" {
  description = "Docker Hub image name"
}
