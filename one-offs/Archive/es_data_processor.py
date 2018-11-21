import pandas as pd
import numpy as np

class ESDataProcessor:
    
    def __init__(self, data):
        self.data=data
    
    def get_item_recur(self, key, obj):
        if key in obj:
            return obj[key]
        for k, v in obj.items():
            if isinstance(v,dict):
                item = self.get_item_recur(key, v)
                if item is not None:
                    return item
                
    def format_df(self):
        
        unique_id = [self.get_item_recur('_id',dat) for dat in self.data]
        text = [self.get_item_recur('body',dat) for dat in self.data]
        date = [self.get_item_recur('timestamp',dat) for dat in self.data]
        
        #lons = []
        #lats = []
        #locs = []

        """
        for loc in self.data:
            if self.get_item_recur('geo',loc) != None:
                locs.append(self.get_item_recur('geo',loc))
            else:
                locs.append(self.get_item_recur('place',loc))
                
        for loc in locs:
            if type(loc) == dict:
                if 'bounding_box' in loc.keys():
                    corners = loc['bounding_box']['coordinates'][0]
                    corner_lons = [corner[0] for corner in corners]
                    corner_lats = [corner[1] for corner in corners]
                    mean_lon = np.mean(corner_lons)
                    mean_lat = np.mean(corner_lats)
                    lons.append(mean_lon)
                    lats.append(mean_lat)
                elif loc['type'] == 'Point':
                    lons.append(loc['coordinates'][1])
                    lats.append(loc['coordinates'][0])
                    
                    """                    
        df_frame = pd.DataFrame({'tweet_id': unique_id,
                               'text': text,
                               'date':date})
                               #'lon': lons,
                               #'lat': lats})
        
        return df_frame