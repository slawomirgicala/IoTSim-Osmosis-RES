from scripts import wind_energy_coordinates, iot_devices_coordinates
import json
import copy

infrastructure_configuration = {}

edge_datacenter_template = {
    "name": None,
    "type": "edge",
    "schedulingInterval": 1.0,
    "vmAllocationPolicy": {
        "className": "VmAllocationPolicyCombinedLeastFullFirst"
    },
    "characteristics": {
        "costPerMem": 0.05,
        "cost": 1.0,
        "os": "Linux",
        "costPerSec": 0.0,
        "vmm": "Xen",
        "timeZone": 10.0,
        "costPerBw": 0.0,
        "costPerStorage": 0.001,
        "architecture": "x86"
    },
    "hosts": [
        {
            "name": None,
            "pes": 4,
            "ramSize": 10000,
            "bwSize": 100,
            "storage": 10000,
            "mips": 10000
        }
    ],
    "MELEntities": [
        {
            "name": None,
            "bw": 100,
            "mips": 250,
            "ram": 10000,
            "pesNumber": 1,
            "vmm": "xxx",
            "cloudletSchedulerClassName": "org.cloudbus.cloudsim.CloudletSchedulerTimeShared"
        }
    ],
    "controllers": [
        {
            "name": None,
            "trafficPolicy": "FairShare",
            "routingPolicy": "ShortestPathBw"
        }
    ],
    "switches": [
        {
            "type": "gateway",
            "name": None,
            "controller": None,
            "iops": 1000000000
        },
        {
            "type": "core",
            "name": None,
            "controller": None,
            "iops": 1000000000
        },
        {
            "type": "edge",
            "name": None,
            "controller": None,
            "iops": 1000000000
        }
    ],
    "links":
        [
            {"source": None, "destination": None, "bw": 100},
            {"source": None, "destination": None, "bw": 100},
            {"source": None, "destination": None, "bw": 100}
        ],
    "ioTDevices": []
}

iot_device_template = {
    "name": None,
    "bw": 100,
    "max_battery_capacity": 100.0,
    "battery_sensing_rate": 0.0001,
    "battery_sending_rate": 0.0001,
    "ioTClassName": "org.cloudbus.cloudsim.edge.iot.TemperatureSensor",
    "mobilityEntity": {
        "movable": False,
        "location": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0
        }
    },
    "networkModelEntity": {
        "communicationProtocol": "xmpp",
        "networkType": "wifi"
    },
    "latitude": None,
    "longitude": None
}

edge_datacenters = []
for station in wind_energy_coordinates.wind_stations:
    edge_datacenter = copy.deepcopy(edge_datacenter_template)
    station_id = str(station[0])
    edge_datacenter['name'] = 'Edge_' + station_id
    edge_datacenter['hosts'][0]['name'] = 'Edge_Device_' + station_id
    edge_datacenter['MELEntities'][0]['name'] = 'MEL.' + station_id
    edge_datacenter['controllers'][0]['name'] = 'edge_sdn_controller_' + station_id
    edge_datacenter['switches'][0]['name'] = 'edge_' + station_id + '_gateway'
    edge_datacenter['switches'][0]['controller'] = 'edge_sdn_controller_' + station_id
    edge_datacenter['switches'][1]['name'] = 'edge_' + station_id + '_core'
    edge_datacenter['switches'][1]['controller'] = 'edge_sdn_controller_' + station_id
    edge_datacenter['switches'][2]['name'] = 'edge_' + station_id + '_device'
    edge_datacenter['switches'][2]['controller'] = 'edge_sdn_controller_' + station_id
    edge_datacenter['links'][0]['source'] = 'edge_' + station_id + '_gateway'
    edge_datacenter['links'][0]['destination'] = 'edge_' + station_id + '_core'
    edge_datacenter['links'][1]['source'] = 'edge_' + station_id + '_core'
    edge_datacenter['links'][1]['destination'] = 'edge_' + station_id + '_device'
    edge_datacenter['links'][2]['source'] = 'edge_' + station_id + '_device'
    edge_datacenter['links'][2]['destination'] = 'Edge_Device_' + station_id
    edge_datacenters.append(edge_datacenter)

iot_devices = []
for iot_device_config in iot_devices_coordinates.iot_devices_config:
    iot_device = copy.deepcopy(iot_device_template)
    iot_device['name'] = 'iot_device_' + str(iot_device_config[0])
    iot_device['latitude'] = iot_device_config[1]
    iot_device['longitude'] = iot_device_config[2]
    iot_devices.append(iot_device)

edge_datacenters[0]['ioTDevices'] = iot_devices

infrastructure_configuration['edgeDatacenter'] = edge_datacenters

infrastructure_configuration['logEntity'] = {
    "logLevel": "debug",
    "saveLogToFile": True,
    "logFilePath": "log.txt",
    "append": False
}
infrastructure_configuration['trace_flag'] = False

cloud_datacenter_template = {
    "name": "Cloud_1",
    "type": "cloud",
    "vmAllocationPolicy": "VmAllocationPolicyCombinedLeastFullFirst",
    "hosts":
        [
            {
                "name": "host1",
                "pes": 4,
                "mips": 1250,
                "ram": 32750,
                "bw": 10000,
                "storage": 6400000000000
            },
            {
                "name": "host2",
                "pes": 4,
                "mips": 1250,
                "ram": 32750,
                "bw": 10000,
                "storage": 6400000000000
            }
        ],
    "VMs":
        [
            {
                "name": "VM_1",
                "pes": 2,
                "mips": 250,
                "ram": 512,
                "storage": 10000,
                "bw": 1000,
                "cloudletPolicy": "TimeShared"
            },
            {
                "name": "VM_2",
                "pes": 2,
                "mips": 250,
                "ram": 512,
                "storage": 10000,
                "bw": 1000,
                "cloudletPolicy": "TimeShared"
            },
            {
                "name": "VM_3",
                "pes": 2,
                "mips": 250,
                "ram": 512,
                "storage": 10000,
                "bw": 1000,
                "cloudletPolicy": "TimeShared"
            }
        ],
    "controllers":
        [
            {
                "name": "dc1_sdn1",
                "trafficPolicy": "FairShare",
                "routingPolicy": "ShortestPathBw"
            }
        ],
    "switches":
        [
            {
                "type": "gateway",
                "name": "dc1_gateway",
                "controller": "dc1_sdn1",
                "iops": 1000000000
            },
            {
                "type": "core",
                "name": "core1",
                "controller": "dc1_sdn1",
                "iops": 1000000000
            },
            {
                "type": "aggregate",
                "name": "aggregate1",
                "controller": "dc1_sdn1",
                "iops": 1000000000
            }
        ],
    "links":
        [
            {"source": "core1", "destination": "dc1_gateway", "bw": 1000},
            {"source": "core1", "destination": "aggregate1", "bw": 1000},
            {"source": "aggregate1", "destination": "host1", "bw": 1000},
            {"source": "aggregate1", "destination": "host2", "bw": 1000}
        ]
}

infrastructure_configuration['cloudDatacenter'] = [cloud_datacenter_template]

infrastructure_configuration['sdwan'] = [
    {
        "controllers": {
            "name": "wan_sdn",
            "trafficPolicy": "FairShare",
            "routingPolicy": "ShortestPathBw"
        },
        "switches": [
            {
                "type": "gateway",
                "name": "sdwan_router_1",
                "controller": "wan_sdn",
                "iops": 1000000000
            }
        ],
        "links": [{"source": "edge_" + str(x[0]) + "_gateway", "destination": "sdwan_router_1", "bw": 1000} for x in
                  wind_energy_coordinates.wind_stations]
                 + [{"source": "dc1_gateway", "destination": "sdwan_router_1", "bw": 1000}]
    }
]

energy_configuration = {
    "simulationDate": "20160101:0000"
}

edge_datacenter_energy_template = {
    "name": None,
    "type": "edge",
    "energyManagementPolicy": {
        "className": "OnGridPolicy"
    },
    "utilization": "50",
    "energyStorage": [
        {
            "type": "BATTERY",
            "capacity": "100",
            "currentEnergy": "20"
        }
    ],
    "powerGrid": [
        {
            "country": "Poland",
            "priceForEnergy": "0.148",
            "emissionCO2": "303",
            "lowEmission": "65",
            "renewable": "48"
        }
    ],
    "energySources": [
        {
            "name": None,
            "type": "PV_PANELS",
            "technology": "crystSi",
            "angle": 50,
            "peakPower": 50,
            "loss": 14,
            "location": {
                "latitude": None,
                "longitude": None,
                "elevation": 0.0
            }
        }
    ]
}

edge_datacenter_energies = []
for station in wind_energy_coordinates.wind_stations:
    edge_datacenter_energy = copy.deepcopy(edge_datacenter_energy_template)
    station_id = str(station[0])
    edge_datacenter_energy['name'] = 'Edge_' + station_id
    edge_datacenter_energy['energySources'][0]['name'] = 'Photovoltaic_panels_' + station_id
    edge_datacenter_energy['energySources'][0]['location']['latitude'] = station[2]
    edge_datacenter_energy['energySources'][0]['location']['longitude'] = station[3]
    edge_datacenter_energies.append(edge_datacenter_energy)
energy_configuration['edgeDatacenters'] = edge_datacenter_energies

cloud_datacenter_energy_template = {
    "name": "Cloud_1",
    "type": "cloud",
    "energyManagementPolicy": {
        "className": "OnGridPolicy"
    },
    "utilization": "30",
    "energyStorage": [
        {
            "type": "BATTERY",
            "capacity": "500",
            "currentEnergy": "10"
        }
    ],
    "powerGrid": [
        {
            "country": "Ireland",
            "priceForEnergy": "0.196",
            "emissionCO2": "252",
            "lowEmission": "62",
            "renewable": "60"
        }
    ],
    "energySources": [
        {
            "name": "Photovoltaic_panels_1",
            "type": "PV_PANELS",
            "technology": "crystSi",
            "peakPower": 1000,
            "loss": "14",
            "angle": "40",
            "location": {
                "latitude": 53.35,
                "longitude": -6.30,
                "elevation": 0.0
            }
        }
    ]
}

energy_configuration['cloudDatacenters'] = [cloud_datacenter_energy_template]

if __name__ == "__main__":
    print("================ INFRA CONFIGS ====================")
    print(infrastructure_configuration)
    print(json.dumps(infrastructure_configuration, indent=4, sort_keys=True))
    with open("../inputFiles/doubleRES/RES_example_solar_power_only_infrastructure.json", "w") as infra_config_file:
        infra_config_file.write(json.dumps(infrastructure_configuration, indent=4, sort_keys=True))
    print("================ ENERGY CONFIGS ====================")
    print(energy_configuration)
    print(json.dumps(energy_configuration, indent=4, sort_keys=True))
    with open("../inputFiles/doubleRES/RES_example_solar_power_only_energy_config.json", "w") as energy_config_file:
        energy_config_file.write(json.dumps(energy_configuration, indent=4, sort_keys=True))
