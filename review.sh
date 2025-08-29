current_branch="$(git branch --show-current)"

# split on "/" into array
IFS='/' read -ra arr <<< "$current_branch"

# print last element
project_name="${arr[@]: -1}"
echo "$project_name"



file_path="./projects/$project_name.md"
project_prompt="$(cat $file_path)"

echo $project_prompt
