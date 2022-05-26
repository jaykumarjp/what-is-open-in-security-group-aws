import logging, boto3, json, sys, csv
from botocore.exceptions import ClientError
from urllib3.exceptions import InsecureRequestWarning

#Ask user for which profile to use, if there are multiple account in cli.
#profile = str(input("Please enter for which profile you are running this script = \n"))
profile = sys.argv[1]
file = sys.argv[2]
i = 1
highriskports = ["22","6379","3389","5432","1433","3306","8080"]

session = boto3.Session(profile_name=profile) #Set session in boto3 according profile.
ec2 = session.resource('ec2')
ec3 = session.client('ec2')
myarray = [["sgname","sgid","open_ports","risky_ports","ec2"]]

try:
    response = ec3.describe_security_groups()
    for sg in response['SecurityGroups']:
        openport = []
        risk = []
        ec2instance []
        myarray.append([sg['GroupName'],sg['GroupId']])
        sg = sg['GroupId']
        try:
            response = ec3.describe_security_groups(GroupIds=[sg])
            for public in response['SecurityGroups'][0]['IpPermissions']:
                if "'CidrIp': '0.0.0.0/0'" in str(public) :
                    try:
                        openport.append(public['FromPort'])
                        if str(public['FromPort']) in highriskports:
                            risk.append(public['FromPort'])
                   # print(openport)
                    except:
                        openport.append(public['IpProtocol'])             
        except ClientError as e:
            print(e)
        #list ec2 and their sg(id), match with sg, if matched add to ec2 array
 
        myarray[i].append(openport)
        myarray[i].append(risk)
        myarray[i].append(ec2instance)
        i=i+1
except ClientError as e:
    print(e)
with open(file+".tsv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter='\t')
        csvWriter.writerows(myarray)
