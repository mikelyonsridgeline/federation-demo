#!/bin/bash

# Description: assumes the devops-deployment-role in the specified account

# Dependencies: apt-get install jq

if [ "$1" == "" ]; then
  echo "specify the profile where you would like to assume the role"
  exit 1
fi

profile=$1

while getopts ":h" opt; do
  case "${opt}" in
    h ) echo "Usage: [profile] [-h help]"
        exit 0
        ;;
  esac
done

# get deployment role arn from ssm
ssm_output=$(aws ssm get-parameter --name $profile-devops-deployment-role-arn)
echo $ssm_output
role_arn=$(echo $ssm_output | jq -r '.Parameter.Value')

# assume role and gather credentials
assume_role_output=$(aws sts assume-role --role-arn $role_arn --role-session-name $profile-session)
echo $assume_role_output
secret_access_key=$(echo $assume_role_output | jq -r '.Credentials.SecretAccessKey')
access_key_id=$(echo $assume_role_output | jq -r '.Credentials.AccessKeyId')
session_token=$(echo $assume_role_output | jq -r '.Credentials.SessionToken')

# configure aws with new credentials
aws configure set aws_access_key_id $access_key_id
aws configure set aws_secret_access_key $secret_access_key
aws configure set aws_session_token $session_token
aws configure set default.region us-east-1