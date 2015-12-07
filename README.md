# auditd-sudo-logger
Log all sudo commands captured by auditd and get them in a nifty daily report.
I want a report that's easier than rummaging through OSSEC alerts or user
.bash_history.

Written in python2.7

ADD: Example auditd conf file
ADD: Cron Entry for automation

This can either be run as a standalone script or run as a firstaction command in
in logrotate.
