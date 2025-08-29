The goal of this project is to update a python notebook file to print and manipulate git file history for a single repo. The python notebook should:\n
 - Print all the files in a file tree\n
 - Print all the contributors in a list\n
 - Create a data structure to store associate contributors to each given file\n
   - The data structure should include information on how recently a contributor made changes to the file\n
   - This could be expensive to compute and update as changes are made to the repo, so alternatively we could have each query compute the result for a given query each time\n
   - We should benchmark these two methods\n

