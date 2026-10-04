APPLIANCE_FAULTS = {
    "Refrigerator": {
        "Not Cooling": {
            "possible_fault": "Compressor or thermostat problem",
            "solution": "Check the thermostat setting and ensure the refrigerator has proper ventilation.",
            "rule": "IF appliance = Refrigerator AND fault = Not Cooling THEN check compressor/thermostat."
        },

        "Water Leaking": {
            "possible_fault": "Blocked drain pipe or damaged water line",
            "solution": "Check and clean the drain pipe and inspect the water line.",
            "rule": "IF appliance = Refrigerator AND fault = Water Leaking THEN check drain pipe/water line."
        },

        "Excessive Ice / Frost": {
            "possible_fault": "Defrost system problem",
            "solution": "Check the defrost heater and thermostat.",
            "rule": "IF appliance = Refrigerator AND fault = Excessive Ice / Frost THEN check defrost system."
        },

        "No Power": {
            "possible_fault": "Power supply or plug problem",
            "solution": "Check the power socket, plug and circuit breaker.",
            "rule": "IF appliance = Refrigerator AND fault = No Power THEN check power supply."
        }
    },

    "Washing Machine": {
        "Not Starting": {
            "possible_fault": "Power supply or door lock problem",
            "solution": "Check the power connection and make sure the door is properly closed.",
            "rule": "IF appliance = Washing Machine AND fault = Not Starting THEN check power/door lock."
        },

        "Not Draining": {
            "possible_fault": "Blocked drain hose or pump",
            "solution": "Clean the drain hose and check the drain pump.",
            "rule": "IF appliance = Washing Machine AND fault = Not Draining THEN check drain system."
        },

        "Excessive Vibration": {
            "possible_fault": "Unbalanced load or uneven surface",
            "solution": "Redistribute the clothes and place the machine on a level surface.",
            "rule": "IF appliance = Washing Machine AND fault = Excessive Vibration THEN balance the machine/load."
        },

        "Water Leaking": {
            "possible_fault": "Loose hose or damaged seal",
            "solution": "Check the inlet and drain hoses and inspect the door seal.",
            "rule": "IF appliance = Washing Machine AND fault = Water Leaking THEN check hoses/seals."
        }
    },

    "Air Conditioner": {
        "Not Cooling": {
            "possible_fault": "Dirty filter or low refrigerant",
            "solution": "Clean the air filter and contact a technician if refrigerant service is required.",
            "rule": "IF appliance = Air Conditioner AND fault = Not Cooling THEN check filter/refrigerant."
        },

        "Water Leaking": {
            "possible_fault": "Blocked drain pipe",
            "solution": "Clean the condensate drain pipe.",
            "rule": "IF appliance = Air Conditioner AND fault = Water Leaking THEN check drain pipe."
        },

        "Bad Smell": {
            "possible_fault": "Dirty filter or evaporator coil",
            "solution": "Clean or replace the filter and arrange professional cleaning if needed.",
            "rule": "IF appliance = Air Conditioner AND fault = Bad Smell THEN check filter/coil."
        },

        "Not Turning On": {
            "possible_fault": "Power supply or remote control problem",
            "solution": "Check the power supply and remote batteries.",
            "rule": "IF appliance = Air Conditioner AND fault = Not Turning On THEN check power/remote."
        }
    },

    "Microwave": {
        "Not Heating": {
            "possible_fault": "Magnetron or power circuit problem",
            "solution": "Stop using the appliance and have it inspected by a qualified technician.",
            "rule": "IF appliance = Microwave AND fault = Not Heating THEN inspect heating circuit."
        },

        "Sparking": {
            "possible_fault": "Metal object or damaged waveguide cover",
            "solution": "Stop the microwave immediately and remove any metal objects. Seek professional service if sparking continues.",
            "rule": "IF appliance = Microwave AND fault = Sparking THEN check for metal/damaged cover."
        },

        "Not Turning On": {
            "possible_fault": "Power supply or fuse problem",
            "solution": "Check the power socket and circuit. Do not open the microwave yourself.",
            "rule": "IF appliance = Microwave AND fault = Not Turning On THEN check power supply."
        },

        "Buttons Not Working": {
            "possible_fault": "Control panel problem",
            "solution": "Power cycle the appliance. If the buttons remain unresponsive, contact a technician.",
            "rule": "IF appliance = Microwave AND fault = Buttons Not Working THEN check control panel."
        }
    },

    "Television": {
        "No Display / Black Screen": {
            "possible_fault": "Input, cable or display problem",
            "solution": "Check the input source and HDMI/video cables.",
            "rule": "IF appliance = Television AND fault = No Display / Black Screen THEN check input/cables."
        },

        "No Sound": {
            "possible_fault": "Mute, audio setting or speaker problem",
            "solution": "Check volume, mute settings and audio output settings.",
            "rule": "IF appliance = Television AND fault = No Sound THEN check audio settings."
        },

        "Remote Not Working": {
            "possible_fault": "Weak batteries or remote sensor problem",
            "solution": "Replace the batteries and make sure the sensor is unobstructed.",
            "rule": "IF appliance = Television AND fault = Remote Not Working THEN check batteries/sensor."
        },

        "TV Not Turning On": {
            "possible_fault": "Power supply problem",
            "solution": "Check the power cable, socket and standby indicator.",
            "rule": "IF appliance = Television AND fault = TV Not Turning On THEN check power supply."
        }
    },

    "Fan": {
        "Not Rotating": {
            "possible_fault": "Motor or capacitor problem",
            "solution": "Switch off the fan and have the motor/capacitor inspected.",
            "rule": "IF appliance = Fan AND fault = Not Rotating THEN check motor/capacitor."
        },

        "Rotating Slowly": {
            "possible_fault": "Weak capacitor or motor issue",
            "solution": "Have the capacitor and motor checked by a technician.",
            "rule": "IF appliance = Fan AND fault = Rotating Slowly THEN check capacitor/motor."
        },

        "Making Noise": {
            "possible_fault": "Loose parts or bearing problem",
            "solution": "Switch off the fan and inspect for loose parts or arrange servicing.",
            "rule": "IF appliance = Fan AND fault = Making Noise THEN check mechanical parts."
        },

        "Not Turning On": {
            "possible_fault": "Power supply or switch problem",
            "solution": "Check the switch and power connection.",
            "rule": "IF appliance = Fan AND fault = Not Turning On THEN check power/switch."
        }
    },

    "Water Heater": {
        "Not Heating": {
            "possible_fault": "Heating element or thermostat problem",
            "solution": "Switch off the heater and have the heating element/thermostat inspected.",
            "rule": "IF appliance = Water Heater AND fault = Not Heating THEN check heating element/thermostat."
        },

        "Water Leaking": {
            "possible_fault": "Loose connection or damaged tank",
            "solution": "Switch off the power and water supply and contact a technician.",
            "rule": "IF appliance = Water Heater AND fault = Water Leaking THEN check connections/tank."
        },

        "No Power": {
            "possible_fault": "Electrical supply or circuit breaker problem",
            "solution": "Check the circuit breaker and power supply.",
            "rule": "IF appliance = Water Heater AND fault = No Power THEN check electrical supply."
        },

        "Temperature Too High": {
            "possible_fault": "Thermostat malfunction",
            "solution": "Switch off the heater and have the thermostat checked.",
            "rule": "IF appliance = Water Heater AND fault = Temperature Too High THEN check thermostat."
        }
    }
}