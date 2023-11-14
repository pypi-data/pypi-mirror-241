# Filename:       | meraki_api_library_v1.py
# Author:         | Marco Caspers
# Version:        | 9.1.1
# Description:
#
# Version 8.0.3, rewrite for Macal.
#
# Version 9.0.0, detached from MacalLibrary class for Macal version 3.5 which supports external libraries.
# Use this file in conjunction with meraki.mcl
#
# Rewrite to remove dependancy on meraki_api_interface.py
#
# Version 9.1.0, Macal 4.0.3 release
#
# Version 9.1.1, fixes for Macal 4.0.75
#
# Version 9.1.2, fixes for Macal 4.0.82
#
# Version 9.1.4
#
# Moved ERROR_TRAFFIC_AND_VISIBILITY and ERROR_NOT_FOUND_TRAFFIC constants from ../utilities.py into this file.
# This is to fix failing imports. The other functions that were imported from utilities where just shims for imports from os.path and inspect
# So i moved those imports directly here.
#
# This was needed because the new method of installing the Meraki Agent on Check Mk v2.0 would cause the import to fail.
#

# Version 9.1.5
#
# Added GetApplianceVpnStats Meraki API call.
#

# Version 10.0.0
#
# Upgraded for Macal version 5.0
#
# Using new library interface of Macal, aka no interface at all :)
#

from typing import Any
import meraki
from meraki.exceptions import APIError
from os.path import dirname, exists
from inspect import getframeinfo, currentframe
from datetime import datetime
import time
import json


Dapi = None
LastErrorMessage = ''

LAST_REQUEST = datetime.now()
EXEC_DELAY = 0.21
DEFAULT_REQUEST_COUNT = 1
API_CALL_THROTTLE_DELAY = 3
API_CALL_THROTTLE_PORT_STATUS_DELAY = 6

ERROR_TRAFFIC_AND_VISIBILITY   = "Traffic Analysis with Hostname Visibility must be enabled on this network to retrieve traffic data."
ERROR_NOT_FOUND_TRAFFIC        = "ERROR 0x10: Traffic data for networkID {} was not found."



def loadJson(fileName):
	"""Loads the json file from a given filename/path it does check for the existence of the file, returns None if no file exists."""
	if (exists(fileName)):
		with open(fileName) as json_file:
			return json.load(json_file)
	return None


def RequestsThrottle(p_requestcount=DEFAULT_REQUEST_COUNT):
	"""Execution Throttler
		This is used to delay the execution of network requests so that the limit 
		for the total number of requests is not exceded.
		Exceeding the limit of requests per second will result in fatal error, 
		bad request responses by the API."""
	# taking this one away makes meraki_test.mcl about 2.3 times faster. 
	# From almost 1 second down to just shy of 0.4 seconds.
	global LAST_REQUEST
	timeElapsed = (datetime.now() - LAST_REQUEST).total_seconds()
	if (timeElapsed < (EXEC_DELAY * p_requestcount)):
		#time.sleep(EXEC_DELAY * p_requestcount - timeElapsed)
		pass
	LAST_REQUEST = datetime.now()


def FnInitDashboardApi(api_key):
	"""Implementation of FnInitDashboardapi function"""
	global Dapi
	global LastErrorMessage
	try:
		Dapi = meraki.DashboardAPI(api_key, suppress_logging = True)
		return True
	except APIError as error:
		LastErrorMessage = f"Init API: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Init API unhandled Exception: {ex}'
	return False

def GetApiVersion() -> Any:
	if Dapi:
		return Dapi._session._version
	return False



def GetLastErrorMessage() -> str:
	"""Implementation of GetLastErrorMessage function, just returns the last error message to the scripting engine."""
	global LastErrorMessage
	return LastErrorMessage


def GetOrganizations() -> None:
	"""get_app_Organizations()
		input
			Dapi 		- Dashboard API

		The API returns a list of organizations.

        https://developer.cisco.com/meraki/api-v1/#!get-organizations
	"""
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.organizations.getOrganizations()
	except APIError as error:
		if "errors" in error.response:
			emsg = ""
			for msg in error.response["errors"]:
				emsg = f"{emsg}\n{msg}"
			LastErrorMessage = f"Get Organizations: {emsg}"
		LastErrorMessage = f"Get Organizations: {error.response}"
	except Exception as ex:
		LastErrorMessage = f"Get Organizations: Unhandled exception: {ex}"
	return False



def GetOrganization(org_id) -> None:
	"""get_app_Organizations()
		input
			Dapi 		- Dashboard API
			org_id      - Organization ID

		The API returns the information of the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization
	"""
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.organizations.getOrganization(org_id)
	except APIError as error:
		if "errors" in error.response:
			emsg = ""
			for msg in error.response["errors"]:
				emsg = f"{emsg}\n{msg}"
			LastErrorMessage = f"Get Organization: {emsg}"
		LastErrorMessage = f"Get Organization: {error.response}"
	except Exception as ex:
		LastErrorMessage = f"Get Organization: Unhandled exception: {ex}"
	return False



def GetInventory(org_id) -> None:
	"""get_org_Inventory(Dapi, org_id)

		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of organizations inventory
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.organizations.getOrganizationInventoryDevices(org_id, total_pages = -1)
	except APIError as error:
		LastErrorMessage = f"Get Inventory: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Inventory: Unhandled Exception: {ex}'
	return False

def GetDevices(org_id) -> None:
	"""get_org_Devices(Dapi, org_id)

		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of organizations devices
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-devices"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.organizations.getOrganizationDevices(org_id, total_pages = -1)
	except APIError as error:
		LastErrorMessage = f"Get Devices: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Devices: Unhandled Exception: {ex}'
	return False


def GetDevice(serial) -> None:
	"""get_dev_Device(Dapi, serial)

		Input:
	   		Dapi      - Dashboard API
	   		serial    - Device serial number

	   	Output:
	   		Get a device from the list of devices.
	   		https://developer.cisco.com/meraki/api-v1/#!get-device"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.devices.getDevice(serial)
	except APIError as error:
		LastErrorMessage = f"Get Device: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Device: Unhandled Exception: {ex}'
	return False



def GetDevicesStatuses(org_id) -> None:
	"""get_org_DevicesStatuses(Dapi, org_id)

		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of statuses of organizations devices
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.organizations.getOrganizationDevicesStatuses(org_id, total_pages = -1)
	except APIError as error:
		LastErrorMessage = f"Get Devices Statusses: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Devices Statusses: Unhandled Exception: {ex}'
	return False



def GetDevicesLatency(org_id) -> None:
	"""get_org_DevicesUplinksLossAndLatency(Dapi, org_id)

		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of Uplink, packet loss and latency data for organizations devices
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.organizations.getOrganizationDevicesUplinksLossAndLatency(org_id, total_pages = -1)
	except APIError as error:
		LastErrorMessage = f"Get Device Uplink Loss and Latency: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Device Uplink Loss and Latency: Unhandled Exception: {ex}'
	return False


def GetDevicesLatencyEx(org_id) -> None:
	"""get_org_DevicesUplinksLossAndLatency(Dapi, org_id)

		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of Uplink, packet loss and latency data for organizations devices
	   		This is the enhanced version that calculates the averages this is to reduce the clunk in the macal script.
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	#try:
	result = Dapi.organizations.getOrganizationDevicesUplinksLossAndLatency(org_id, total_pages = -1)
	#{'networkId': 'N_645140646620848439', 'serial': 'Q2JN-94W8-MN69', 'uplink': 'wan2', 'ip': '8.8.8.8', 'timeSeries': [{'ts': '2022-09-05T13:10:37Z', 'lossPercent': 0.0, 'latencyMs': 3.1}, {'ts': '2022-09-05T13:11:37Z', 'lossPercent': 0.0, 'latencyMs': 3.0}, {'ts': '2022-09-05T13:12:36Z', 'lossPercent': 0.0, 'latencyMs': 2.9}, {'ts': '2022-09-05T13:13:37Z', 'lossPercent': 0.0, 'latencyMs': 3.1}, {'ts': '2022-09-05T13:14:37Z', 'lossPercent': 0.0, 'latencyMs': 3.2}]}
	ret = []
	for item in result:
		rec = {}
		rec['networkId'] = item['networkId']
		rec['serial'] = item['serial']
		rec['uplink'] = item['uplink']
		rec['ip'] = item['ip']
		rec['lossPercent'] = 0.0
		rec['latencyMs'] = 0.0
		rec['timeSeries'] = item['timeSeries']
		countLoss    = len(item['timeSeries'])
		countLatency = len(item['timeSeries'])
		for ts in item['timeSeries']:
			if ts['lossPercent'] is None:
				countLoss -= 1
			else:
				rec['lossPercent'] += ts['lossPercent']
			if ts['latencyMs'] is None:
				countLatency -= 1
			else:
				rec['latencyMs'] += ts['latencyMs']
		if countLoss > 0:
			rec['lossPercent'] = rec['lossPercent'] / countLoss
		if countLatency > 0:
			rec['latencyMs'] = rec['latencyMs'] / countLatency
		ret.append(rec)
	return ret



def GetDeviceManagementInterface(serial) -> None:
	"""
		get_devices_managementInterface(Dapi, serial)

		Input:
			Dapi   - Dashboard API
	   		serial - Serial number of the device.

		Output:
			Return the management interface settings for a device
			https://developer.cisco.com/meraki/api-v1/#!get-device-management-interface

	"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.devices.getDeviceManagementInterface(serial)
	except APIError as error:
		LastErrorMessage = f"Get Device Management Interface Settings: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Device Management Interface Settings: Unhandled Exception: {ex}'
	return False



def GetConfigTemplates(org_id) -> None:
	"""get_org_ConfigTemplates(Dapi, org_id)

		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of configuration templates of this organization
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.organizations.getOrganizationConfigTemplates(org_id)
	except APIError as error:
		LastErrorMessage = f"Get Config Templates: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Config Templates: Unhandled Exception: {ex}'
	return False

def GetNetworks(org_id) -> None:
	"""get_org_Networks(Dapi, org_id)
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of networks in the organization
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-networks"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.organizations.getOrganizationNetworks(org_id)
	except APIError as error:
		LastErrorMessage = f"Get Networks: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Networks: Unhandled Exception: {ex}'
	return False

def GetNetwork(network_id) -> None:
	"""get_org_Network(Dapi, network_id)
		Input:
	   		Dapi   - Dashboard API
	   		network_id - Network ID

	   	Output:
	   		Get a single network
	   		https://developer.cisco.com/meraki/api-v1/#!get-network"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.networks.getNetwork(network_id)
	except APIError as error:
		LastErrorMessage = f"Get Network: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Network: Unhandled Exception: {ex}'
	return False

def GetApplianceUplinkStatuses(org_id) -> None:
	"""get_app_UplinkStatuses(Dapi, org_id)
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID
		Output:
		List the uplink status of every Meraki MX and Z series appliances in the organization
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplink-statuses"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.appliance.getOrganizationApplianceUplinkStatuses(org_id, total_pages = -1)
	except APIError as error:
		LastErrorMessage = f"Get Organization Appliance Uplink Statuses: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Organization Appliance Uplink Statuses: Unhandled Exception: {ex}'
	return False

def GetApplianceUplinkStatus(org_id, serials = None) -> None:
	"""get_app_UplinkStatuses(Dapi, org_id, serials)
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID
		Output:
		List the uplink status of every Meraki MX and Z series appliances in the organization
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplink-statuses"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.appliance.getOrganizationApplianceUplinkStatuses(org_id, serials = serials)
	except APIError as error:
		LastErrorMessage = f"Get Organization Appliance Uplink Statuses: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Organization Appliance Uplink Statuses: Unhandled Exception: {ex}'
	return False


def GetLicenseOverview(org_id) -> None:
	"""get_org_LicensesOverview(Dapi, org_id)

		Input:
	   		Dapi       - Dashboard API
	   		org_id     - Organization ID

		Output:
			LicensesOverview for the organization.
			https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.organizations.getOrganizationLicensesOverview(org_id)
	except APIError as error:
		LastErrorMessage = f"Get License Overview: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get License Overview: Unhandled Exception: {ex}'
	return False



def GetAppPerformance(serial) -> None:
	"""get_app_Performance(Dapi, serial)
		Input:
	   		Dapi   - Dashboard API
	   		serial - Device Serial Number
		Output:
		Return the performance score for a single device. Only primary MX devices supported. If no data is available, a 204 error code is returned.
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-performance"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.appliance.getDeviceAppliancePerformance(serial)
	except APIError as error:
		if error.status == 400:
			LastErrorMessage = f'Get device appliance performance: {error.operation}: {error.status}, {serial} {error.message["errors"][0]}'
		elif error.status != 404:
			LastErrorMessage = f"Get device appliance performance: {error.operation}: {error.status}, {error.message}, {error.reason}"
		LastErrorMessage = f"Get device appliance performance Unknown error for {serial}: {error.status}, {error.response}"
	except Exception as ex:
		LastErrorMessage = f'Get device appliance performance Unhandled Exception: {ex}'
	return False



def GetNetworkTraffic(network_id, timespan=7200) -> None:
	"""get_app_NetworkTraffic(Dapi, network_id, T_timepsan=7200)

		Input:
	   		Dapi       - Dashboard API
	   		network_id - Network ID
	   		timespan   - Timespan in which to measure data, default 2 hours.

		Output:
			The traffic analysis data for this network.
            https://documentation.meraki.com/MR/Monitoring_and_Reporting/Hostname_Visibility
            ->Traffic Analysis with Hostname Visibility must be enabled on the network.
	        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic"""
	global Dapi
	global LastErrorMessage
	print("@ This function is obsolete please use get_app_NetworkApplianceUplinkUsageHistory")
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	result = None
	try:
		return Dapi.networks.getNetworkTraffic(network_id, timespan = timespan)
	except APIError as error:
		if error.status == 400:
			if "errors" in error.message:
				if (len(error.message["errors"]) > 0):
					if (error.message["errors"][0] == ERROR_TRAFFIC_AND_VISIBILITY):
						LastErrorMessage = f"{ERROR_TRAFFIC_AND_VISIBILITY} (NetworkID: {network_id}"
			else:
				LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
		elif error.status == 404:
			LastErrorMessage = ERROR_NOT_FOUND_TRAFFIC.format(network_id)
		else:
			LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	return False



def GetNetworkEvents(network_id, product_type, start_after = -1) -> None:
	"""get_net_NetworkEvents()
		input:
			Dapi 		 - Dashboard API
			network_id   - Network ID
			product_Type - Product Type of the appliance
							  Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway

			start_After  - The date/time from where to start collecting the data
							use -1 if you want to list all the events, regardless of the start date/time

		output:
			Gets a list of all network events that happened after the given date/time, for the specified product type, on the given network_id.
			https://developer.cisco.com/meraki/api-v1/#!get-network-events"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		if (start_after == -1):
			result = Dapi.networks.getNetworkEvents(network_id, productType = product_type, total_pages = 10)
		else:
			result = Dapi.networks.getNetworkEvents(network_id, productType = product_type, startingAfter = start_after)
		return result
	except APIError as error:
		LastErrorMessage = f"Get Network Events: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Network Events: Unhandled Exception: {ex}'
	return False


def GetOrgSecurityEvents(org_id, time_span = -1) -> None:
	"""get_app_OrganizationSecurityEvents()
		input
			Dapi 		- Dashboard API
			org_id 		- Organization ID
			time_span 	- Timespan over which to collect the data.
							Default is 5 minutes (300 seconds),
							Use -1 to list all data.

		List the security events for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-events
	"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		if (time_span == -1):
			result = Dapi.appliance.getOrganizationApplianceSecurityEvents(org_id, total_pages = -1)
		else:
			result = Dapi.appliance.getOrganizationApplianceSecurityEvents(org_id, timespan = time_span)
		return result
	except APIError as error:
		LastErrorMessage = f"Get Security Events: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Security Events: Unhandled Exception: {ex}'
	return False

def GetSwitchPortStatuses(serial, time_span = -1) -> None:
	"""get_switch_DeviceSwitchPortsStatuses(Dapi, org_id)

		Input:
	   		Dapi     - Dashboard API
	   		serial   - Serial of the device
	   		timespan - timespan in seconds (300 = 5m default.)

	   	Output:
	   		list of statuses for ports for a specific switch.
	   		https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_PORT_STATUS_DELAY)
	try:
		return Dapi.switch.getDeviceSwitchPortsStatuses(serial=serial, timespan = time_span)
	except APIError as error:
		LastErrorMessage = f"Get Switch Port Statuses: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Switch Port Statuses: Unhandled Exception: {ex}'
	return False



def GetSwitchPortStatusT0(serial, t0) -> None:
	"""get_switch_DeviceSwitchPortsStatuses(Dapi, org_id)

		Input:
	   		Dapi     - Dashboard API
	   		serial   - Serial of the device
	   		t0 - The beginning of the timespan for the data. The maximum lookback period is 31 days from today.

	   	Output:
	   		list of statuses for ports for a specific switch.
	   		https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses"""
	global Dapi
	global LastErrorMessage	
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.switch.getDeviceSwitchPortsStatuses(serial=serial, t0=t0)
	except APIError as error:
		LastErrorMessage = f"Get Switch Port Statuses T0: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Switch Port Statuses T0: Unhandled Exception: {ex}'
	return False


def GetApplianceUplinkUsageHistory(network_id) -> None:
	"""
		getNetworkApplianceUplinksUsageHistory.

		by default timespan   is 10 minutes.
		by default resolution is 1 minute.

		so by default a query returns 10 results per interface.

		The dimension is bytes.

		https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-uplinks-usage-history
	"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	timespan = 600 # The timespan is 10 minutes, we can set the default here 
	               # because we don't allow changing of the default in this function call.
	try:
		upl = Dapi.appliance.getNetworkApplianceUplinksUsageHistory(network_id)
		nr = upl[0]['byInterface']
		for i, pt in enumerate(upl):
			if i > 0:
				inf = pt['byInterface']
				for f, intf in enumerate(inf):
					if nr[f]["sent"] is None:
						nr[f]["sent"] = 0
					if nr[f]["received"] is None:
						nr[f]["received"] = 0
					if intf is not None:
						if intf["sent"] is not None:
							nr[f]['sent'] += intf["sent"]
						if intf["received"] is not None:
							nr[f]['received'] += intf["received"]
		# Recalculate to bytes per second by deviding by the timespan
		for f in nr:
			f["total"] = (f["sent"] + f["received"]) / timespan
			f["sent"] = f["sent"] / timespan
			f["received"] = f["received"] / timespan
		return nr
	except APIError as error:
		LastErrorMessage = f"Get Appliance Uplink Usage History: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Appliance Uplink Usage History: Unhandled Exception: {ex}'
	return False



def GetApplianceTrafficShapingUplinkBandwidth(network_id) -> None:
	"""
    		**Returns the uplink bandwidth settings for your MX network.**
    		https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-bandwidth
    		- networkId (string): (required)
    """
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.appliance.getNetworkApplianceTrafficShapingUplinkBandwidth(network_id)
	except APIError as error:
		LastErrorMessage = f"Get Appliance Traffic Shaping Uplink Bandwidth: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Appliance Traffic Shaping Uplink Bandwidth: Unhandled Exception: {ex}'
	return False

def GetWirelessStatus(serial) -> None:
	"""https://developer.cisco.com/meraki/api/#!get-network-device-wireless-status"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.wireless.getDeviceWirelessStatus(serial)
	except APIError as error:
		LastErrorMessage = f"Get Wireless Status: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Wireless Status: Unhandled Exception: {ex}'
	return False


def GetApplianceVpnStats(org_id) -> None:
	"""https://developer.cisco.com/meraki/api-latest/#!get-organization-appliance-vpn-stats"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.appliance.getOrganizationApplianceVpnStats(org_id, total_pages='all')
	except APIError as error:
		LastErrorMessage = f"Get VPN stats: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get VPN stats: Unhandled Exception: {ex}'
	return False

def GetApplianceVpnStatuses(org_id) -> None:
	"""https://developer.cisco.com/meraki/api-latest/#!get-organization-appliance-vpn-statuses"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.appliance.getOrganizationApplianceVpnStatuses(org_id, total_pages='all')
	except APIError as error:
		LastErrorMessage = f"Get VPN stats: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get VPN stats: Unhandled Exception: {ex}'
	return False

def Output(*params) -> None:
	"""Implementation of Output function. output => (params args)"""
	if len(params) != 2:
		raise Exception(f"Output requires 2 arguments got ({len(params)}).")
	v = params[1]
	if (v is not None and v != '' and v != {} and v != [] and v != "nil"):
		print(params[0])
		print(v)



def OutputOnCondition(*params) -> None:
	"""Implementation of OutputOnCondition function"""
	if params[0] is False: return
	if len(params) != 3:
		raise Exception(f"OutputOnCondition requires 3 arguments got ({len(params)}).")
	params = params[1:]
	v = params[1]
	if (v is not None and v != '' and v != {} and v != [] and v != "nil"):
		print(params[0])
		print(v)

def Header(*params) -> None:
	"""Implementation of Header function"""
	print("<<<meraki_devices>>>")
	v = params[1]
	if (params[0] == True):
		print(f"[{v}_demo]")
	else:
		print(f"[{v}]")
	model = params[2]
	serial = params[3]
	template = params[4]
	if model is None or model ==  "nil": model = ""
	if serial is None or serial == "nil": serial = ""
	if template is None or template == "nil": template = ""
	print(f"{model} - {serial} - {template}")


def ProductInfo(*params) -> None:
	"""Implementation of Header function"""
	print("<<<meraki_product_info>>>")
	model = params[0]
	serial = params[1]
	template = params[2]
	if model is None or model == "nil": model = ""
	if serial is None or serial == "nil": serial = ""
	if template is None or template == "nil": template = ""
	print(f"{model} - {serial} - {template}")

def DeviceHeader(*params) -> None:
	"""Implementation of DeviceHeader function"""
	if params[0] == True:
		print(f"<<<<{params[1]}_demo>>>>")
	else:
		print(f"<<<<{params[1]}>>>>")

def ReadFilters(customer) -> None:
	"""Implementation of DeviceHeader function"""
	if not customer:
		print("@customer did not exist")
		return None
	# Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway
	filters = {}
	filters_base = customer["network_event_filters"][0]
	filename  = getframeinfo(currentframe()).filename   # get the filename/path where this script is located.
	filepath  = dirname(filename)			        # get the path of this file.
	# if we get the externals subfolder back, cut it off!
	if filepath.endswith("/external"):
		filepath = filepath[0:-9]
	if "switch" in filters_base:
		filename =  f"""{filepath}{filters_base["switch"]}"""
		filters["switch"] = loadJson(filename)
	if "wireless" in filters_base:
		filename =  f"""{filepath}{filters_base["wireless"]}"""
		filters["wireless"] = loadJson(filename)
	if "appliance" in filters_base:
		filename =  f"""{filepath}{filters_base["appliance"]}"""
		filters["appliance"] = loadJson(filename)
	if "systemsManager" in filters_base:
		filename =  f"""{filepath}{filters_base["systemsManager"]}"""
		filters["systemsManager"] = loadJson(filename)
	if "camera" in filters_base:
		filename =  f"""{filepath}{filters_base["camera"]}"""
		filters["camera"] = loadJson(filename)
	if "cellularGateway" in filters_base:
		filename =  f"""{filepath}{filters_base["cellularGateway"]}"""
		filters["cellularGateway"] = loadJson(filename)
	return filters

def FlattenRecord(rec) -> None:
	"""Implementation of FlattenRecord function"""
	result = ""
	for (key, value) in rec.items():
		result = "{},'{}','{}'".format(result, key, value)
	return result[1:]


def FlattenTuple(tup) -> None:
	"""Implementation of FlattenTuple function"""
	result = []
	for item in tup:
		if isinstance(item, str):
			result.append(f"'{item}'")
		else:
			result.append(item)
	return result


def GetSensorReadingsHistory(org_id) -> None:
	"""https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history"""
	global Dapi
	global LastErrorMessage
	RequestsThrottle(API_CALL_THROTTLE_DELAY)
	try:
		return Dapi.sensor.getOrganizationSensorReadingsHistory(org_id)
	except APIError as error:
		LastErrorMessage = f"Get Sensor Readings History: {error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Get Sensor Readings History: Unhandled Exception: {ex}'
	return False


def StrToInt(str) -> None:
	"""https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history"""
	global LastErrorMessage
	try:
		return int(str)
	except Exception as ex:
		LastErrorMessage = f"StrToInt(): {ex}"

