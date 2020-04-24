#!/bin/sh
# Prepends commit message with JIRA derived from current branch name

# Colors!
RED='\033[0;31m'
NC='\033[0m' # No color

# Set branch name prefix regex. This will need to change as new JIRA
# projects get added.
BRANCH_JIRA_PREFIX_REGEX="(^(RLA)-[0-9]+-)"

# Get current branch name
CURRENT_BRANCH_NAME="$(git symbolic-ref --short HEAD)"
echo Your current branch is $CURRENT_BRANCH_NAME

# Derive JIRA from branch name
if [[ $CURRENT_BRANCH_NAME =~ $BRANCH_JIRA_PREFIX_REGEX ]]
then
  JIRA="${BASH_REMATCH[1]%?}"
  echo "Your JIRA is" $JIRA
else
  echo ${RED}
  echo "Branch name invalid:"
  echo "    Your branch name must conform to this regex:" $BRANCH_JIRA_PREFIX_REGEX
  echo "    Example of a good branch name is 'DEV-123-test-branch'"
  echo "    To rename current branch, do: 'git branch -m <new_branch_name>'"
  echo ${NC}
  exit 1
fi

# Prepend JIRA to commit message
echo $JIRA: $(cat $1) > $1
exit 0