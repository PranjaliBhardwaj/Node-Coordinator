
contractABI = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_modelHash",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_rounds",
				"type": "uint256"
			}
		],
		"name": "createTask",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_coordinatorAddress",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "_user",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "_fileHash",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			}
		],
		"name": "fileAdded",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "taskID",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "_modelHash",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			}
		],
		"name": "modelUpdated",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "taskID",
				"type": "uint256"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "_user",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "_modelHash",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_amt",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			}
		],
		"name": "newTaskCreated",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_fileHash",
				"type": "string"
			}
		],
		"name": "storeFile",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_coordinatorAddress",
				"type": "address"
			}
		],
		"name": "updateCoordinator",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_taskID",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_modelHash",
				"type": "string"
			},
			{
				"internalType": "address payable",
				"name": "computer",
				"type": "address"
			}
		],
		"name": "updateModelForTask",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "coordinatorAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getFiles",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTaskCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_taskID",
				"type": "uint256"
			}
		],
		"name": "getTaskHashes",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTasksOfUser",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "SentinelTasks",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "taskID",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "currentRound",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "totalRounds",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "cost",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "UserFiles",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "UserTaskIDs",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
contractAddress = "0x6d81122f119d2893C2Ab91F3F1cBc771bBBfBA26"
