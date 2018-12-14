"""-------------------------------------------------------------------------------
Name:       Groups_Users.py
Purpose:    Python 3x - Python API Examples for Sedaru Interfacing with Groups/Members

Version: 1.0 Base version
Author:     Alexander J Brown - Solution Engineer Esri (alexander_brown@esri.com)
-------------------------------------------------------------------------------"""
# Import Libraries
from arcgis.gis import *
import time


# Report User Attributes (not comprehensive)
# Full list: https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html?highlight=gis%20user#user
def report_attributes(user_acct):
    user_info = gis.users.get(username=user_acct)
    print('*************')
    print("Username: ", user_info.username)
    print("Description: ", user_info.description, " Email: ", user_info.email,
          "First Name: ", user_info.firstName, " Last Name:", user_info.lastName, " Full Name:", user_info.fullName)
    print(user_info.level, " ", user_info.mfaEnabled, " ", user_info.provider, " ", user_info.userType)
    # convert Unix epoch time to local time
    created_time = time.localtime(user_info.created / 1000)
    print("Created: {}/{}/{}".format(created_time[0], created_time[1], created_time[2]))
    last_accessed = time.localtime(user_info.lastLogin / 1000)
    print("Last active: {}/{}/{}".format(last_accessed[0], last_accessed[1], last_accessed[2]))


if __name__ == "__main__":
    # Establish Connection to ArcGIS Online or ArcGIS Enterprise
    # gis = GIS('http://www.arcgis.com', '<username>', '<password>')
    gis = GIS('https://<portal dns>:<port>/arcgis', '<username>', '<password>')

    # Search for Group Sedaru
    sedaru_group = gis.groups.search('title:Sedaru', max_groups=1)
    print(sedaru_group)

    # Return all users of the group
    group_members = sedaru_group[0].get_members()
    print(group_members)
    print(type(group_members))

    # Loop through groups dictionary and identify all users to pass to function
    for key, values in group_members.items():
        if key == 'admins':
            for value in values:
                report_attributes(value)
        elif key == 'users':
            for value in values:
                report_attributes(value)




