"""
********************************************************************************
* Project Name:  Pixela API Habit Tracker 
* Description:   It is a Python-based application that integrates with the Pixela API to help you track daily activities such as reading, exercising, or any other task. 
* Author:        ziqkimi308
* Created:       2024-12-18
* Updated:       2024-12-18
* Version:       1.0
********************************************************************************
"""

import requests
import datetime as dt

# ------------------- CONSTANT ------------------- #
# Create your own token, username, and graph id
TOKEN = ""
USERNAME = ""
GRAPH_ID = ""
PIXELA_API_ENDPOINT = " https://pixe.la//v1/users"
GRAPH_API_ENDPOINT = f"{PIXELA_API_ENDPOINT}/{USERNAME}/graphs"
PIXEL_API_ENDPOINT = f"{GRAPH_API_ENDPOINT}/{GRAPH_ID}"

# --------------------------------------------➡️ USER SETUP ⬅️-------------------------------------------------------- #
# pixela_parameters = {
# 	"token": TOKEN,
# 	"username": USERNAME,
# 	"agreeTermsOfService": "yes",
# 	"notMinor": "yes"
# }

# pixela_response = requests.post(url=PIXELA_API_ENDPOINT, json=pixela_parameters)
# print(pixela_response.text)

# -------------------------------------------➡️ GRAPH SETUP ⬅️--------------------------------------------------------- #
# Change the parameters suit your activity
# graph_parameters = {
# 	"id": GRAPH_ID,
# 	"name": "Reading Graph",
# 	"unit": "pages",
# 	"type": "int",
# 	"color": "ajisai",
# }

graph_headers = {
	"X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=GRAPH_API_ENDPOINT, json=graph_parameters, headers=graph_headers)
# print(graph_response.text)

# --------------------------------------------➡️ PIXEL SETUP ⬅️⬅-------------------------------------------------------- #
# Uncomment to use either date today or specific date
# date_today = dt.datetime.now().strftime("%Y%m%d")
# date_target = dt.datetime(year=2024, month=12, day=17).strftime("%Y%m%d")

# Change the quantity input text which suit your chosen activity
# pixel_parameters = {
# 	"date": date_target,
# 	"quantity": input("How many book pages did you read today? : "),
# }

# # We going to use graph_headers for headers
# pixel_response = requests.post(url=PIXEL_API_ENDPOINT, json=pixel_parameters, headers=graph_headers)
# print(pixel_response.text)

# ----------------------------------------➡️ UPDATE PIXEL HERE ⬅️------------------------------------------------------ #
# date_target = dt.datetime(year=2024, month=12, day=17).strftime("%Y%m%d")

# pixel_update_parameters = {
# 	"quantity": "3",
# }

# PIXEL_UPDATE_API_ENDPOINT = f"{PIXEL_API_ENDPOINT}/{date_target}"

# # We will use graph_headers for headers
# # Use put() instead of post() here
# pixel_update_response = requests.put(url=PIXEL_UPDATE_API_ENDPOINT, json=pixel_update_parameters, headers=graph_headers)
# print(pixel_update_response)

# ----------------------------------------➡️ DELETE PIXEL HERE ⬅️------------------------------------------------------ #
# date_target = dt.datetime(year=2024, month=12, day=17).strftime("%Y%m%d")

# PIXEL_DELETE_API_ENDPOINT = f"{PIXEL_API_ENDPOINT}/{date_target}"

# pixel_delete_response = requests.delete(url=PIXEL_DELETE_API_ENDPOINT, headers=graph_headers)
# print(pixel_delete_response.text)
