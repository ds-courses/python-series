import requests
import time
from datetime import datetime
import reverse_geocode
from typing import List

def get_astro_names() -> List:
    ''' Provide the names of the astronauts on board the ISS
    
        Returns
        -------
        astro_names
            The list of the astronaut names
    '''
    # Get the names of astronauts on board the ISS 
    astros_json = requests.get('http://api.open-notify.org/astros.json').json()
    astro_names = []
    for astro_info in astros_json['people']:
        astro_names.append(astro_info['name'])
    # Note: equivalent to astro_names = [astro_info['name'] for astro_info in astros_json['people']]
    return astro_names

def get_iss_positions(n_trials: int, trial_pause_seconds: float) -> List[str]:
    ''' Provide the positions of the ISS at K time intervals
    
        Parameters
        ----------
        n_trials
            The number of trials to get the ISS positions
        trial_pause_seconds
            The number of seconds between each trial

        Returns
        -------
        iss_positions
            A list of description of the ISS position at each trial
    '''
    iss_info_alltrials = []
    for i_trial in range(n_trials):
        # Get date and time
        date_time_now = datetime.now()
        time_str = date_time_now.strftime("%d-%b-%Y %H:%M:%S")
        # ISS position
        issnow_json = requests.get('http://api.open-notify.org/iss-now.json').json()
        if issnow_json['message']  == 'success':
            iss_latlong = (issnow_json['iss_position']['latitude'], 
                        issnow_json['iss_position']['longitude'])
            # The search method expects a list and returns a list.
            # Hence we need to coerce a single value latlong to a list with [latlong]
            # Afterwards we need to extract the result, itself a single-item list, with result_list[0]
            iss_pos_list = reverse_geocode.search([iss_latlong])
            iss_pos = iss_pos_list[0]
            iss_info = 'At {}, the ISS was above {} in {}'.format(time_str, iss_pos['city'], iss_pos['country'])
            iss_info_alltrials.append(iss_info)
            time.sleep(trial_pause_seconds)
        else:
            raise requests.exceptions.RequestException
    return iss_info_alltrials

def test_get_astro_names():
    names = get_astro_names()
    assert (len(names) >=3 and len(names) <=6)

def test_get_iss_positions():
    info_alltrials = get_iss_positions(n_trials=3, trial_pause_seconds=0.5)
    assert len(info_alltrials) == 3

if __name__ == '__main__':
    print(f'The astronauts on board ISS are now: {get_astro_names()}')
    print(f'Position: {get_iss_positions(n_trials=1, trial_pause_seconds=0)}')