# what-is-open-in-security-group-aws:
Here are the main characteristics:
*List all security groups in aws account.
*Find attached instances in that security group.
*Find public open ports in related security group.
*Get highlighted list of dangereous open ports to public.

# prerequisite:
1. python
2. boto3 (pip install boto3)
3. aws cli profile
4. requests module (pip install requests)

# usage: 
Type command in terminal<br>
``` sgfast.py default output ``` [If aws-cli profile is default else change "default" with profile name]

# Future Update
1. Remove false-positive by checking condition as well
2. Add - role based access
