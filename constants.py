# Username for authentication
USERNAME1 = ""
USERNAME2 = ""
USERNAME3 = ""

# Token from GitHub for user1
TOKEN = ""

# Token from GitHub for user1
TOKEN1 = ""

# Token from GitHub for user1
TOKEN2 = ""

# Token from GitHub for user2
TOKEN6 = ""

# Token from GitHub for user2
TOKEN7 = ""

# Token from GitHub for user3
TOKEN8 = ""

# Token from GitHub for user3
TOKEN9 = ""

# Token from SonarQube
TOKEN10 = ""

REPOSCHARACTERISTICS = [
    "index",
    "repo_name",
    "bug_issues_count",
    "bug-fix_commits_count",
    "commits_count",
    "code_smells",
    "cognitive_complexity",
    "ncloc",
]

METRICS = [
    "index",
    "repo_name",
    "avg_bug-issue_time",
    "bug-fix-commits_ratio",
    "code-smells_ncloc",
    "cognitive-complexity_ncloc",
]

CALCULATEDVALS = [
    "",
    "react",
    "angular",
    "vue",
    "others",
]
URLCREATEPROJECT = "http://localhost:9000/api/projects/create"
URLGENERATETOKEN = "http://localhost:9000/api/user_tokens/generate"
URLISSUES = "http://localhost:9000/api/issues/search"
URLCOMPONENTREE = "http://localhost:9000/api/measures/component_tree"