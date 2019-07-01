from flask import Flask, jsonify  # for working with RESTful API
from redminelib import Redmine  # for working with Redmine API

app = Flask(__name__)

redmine = Redmine('https://my.redmine.jp/mulodo',
                  username='<your-username>', password='<your-password>')
project = redmine.project.get('bts-inspection')

@app.route("/")
def hello():
    return "BTS Due Date Inspection"

# get a list of tickets that have not been set due
@app.route("/api/issues/without-due-date")
def getIssuesWithoutDueDate():
    issuesWithoutDueDate = []
    for issue in project.issues:
        issueDueDate = getattr(issue, 'due_date', None)
    if issueDueDate is None:
        issuesWithoutDueDate.append(issue.subject)
    return jsonify(issuesWithoutDueDate)

if __name__ == '__main__':
    app.run(debug=True)
