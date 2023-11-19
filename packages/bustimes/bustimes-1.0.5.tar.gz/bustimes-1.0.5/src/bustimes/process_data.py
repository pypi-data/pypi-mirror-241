import string
import re

def process_bus_stop(bus_data: dict):
    StopNumber = int(bus_data['StopNo'])
    StopName: str = bus_data['Name']
    if StopName.startswith('NB'):
        StopName = StopName.replace('NB', 'Northbound')
    if StopName.startswith('SB'):
        StopName = StopName.replace('SB', 'Southbound')
    if StopName.startswith('EB'):
        StopName = StopName.replace('EB', 'Eastbound')
    if StopName.startswith('WB'):
        StopName = StopName.replace('WB', 'Westbound')
    StopName = StopName.replace('FS', '@')
    StopName = StopName.replace('NS', '@')
    StopName = StopName.replace('STN', 'Station')
    StopName = string.capwords(StopName, sep=' ')
    BayNumber: str = bus_data['BayNo']
    if BayNumber == 'N':
        BayNumber = None
    else:
        BayNumber = int(BayNumber)
    AtStreet: str = bus_data['AtStreet']
    if re.match(r'BAY \d+', AtStreet):
        AtStreet = None
    else:
        AtStreet = string.capwords(AtStreet, sep=' ')
    Routes: str = bus_data['Routes'].lstrip('0')
    return {'StopNumber': StopNumber,'StopName': StopName, 'BayNumber': BayNumber, 'AtStreet': AtStreet, 'Routes': Routes}

def process_multiple_bus_stops(bus_data: dict):
    bus_stops = []
    for bus_stop in bus_data:
        bus_stop_data = process_bus_stop(bus_stop)
        if 'Platform' in bus_stop_data['StopName'] or bus_stop_data['StopName'].endswith('New'):
            continue
        bus_stops.append(bus_stop_data)
    return bus_stops

def process_bus_departure_times(bus_data: dict):
    departure_times = {}
    for routes in bus_data:
        route_number_without_leading_zero = routes['RouteNo'].lstrip('0')
        departure_times.update({route_number_without_leading_zero:[]})
        for departure in routes['Schedules']:
            RealTime: bool = False
            IsDelayed: bool = False
            IsEarly: bool = False
            destination: str = departure['Destination']
            destination = destination.replace('STN', 'Station')
            destination = re.sub(r'\bEXP\b', 'Express', destination)
            destination = re.sub(r'\bEXCH\b', 'Exchange', destination)
            destination = destination.replace('CTRL', 'Central')
            destination = destination.replace('CTR', 'Centre')
            destination = string.capwords(destination, sep=' ')
            LeaveTime: str = departure['ExpectedLeaveTime']
            LeaveTime = LeaveTime.split(' ')[0]
            status: str = departure['ScheduleStatus']
            if status == ' ':
                RealTime = True
            if status == '-':
                RealTime = True
                IsDelayed = True
            if status == '+':
                RealTime = True
                IsEarly = True
            if departure['CancelledTrip'] == 'true' or departure['CancelledStop'] == 'true':
                CancelledTrip = True
            else:
                CancelledTrip = False
            CountdownTime: int = departure['ExpectedCountdown']
            departure_times[route_number_without_leading_zero].append({"RouteNumber": route_number_without_leading_zero, "Destination": destination, "LeaveTime": LeaveTime, "CountdownTime": CountdownTime, "RealTime": RealTime, "IsDelayed": IsDelayed, "IsEarly": IsEarly, "CancelledTrip": CancelledTrip})
    return departure_times

