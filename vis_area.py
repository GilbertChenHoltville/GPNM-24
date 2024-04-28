'''
version control
    v1: 
        lat1, lat2, lon1, lon2, in ascending order
        visulize scattered points, only binary, not heatmap
        coordinate resolution: 0.00001, approx 38m
        brute force for loop
'''
import googlemaps
import matplotlib.pyplot as plt
import numpy as np
def VisArea(lat1, lat2, lon1, lon2, min_ele, res):
    # res 0.001 100m
    API_KEY = 'YOUR_API_KEY'
    map_client = googlemaps.Client(key=API_KEY)
    lat_steps = np.arange(lat1, lat2, res)
    lon_steps = np.arange(lon1, lon2, res)
    coord_list = [(lat, lon) for lat in lat_steps for lon in lon_steps]
    batch_size = 512
    elevation_matrix = np.zeros((len(lat_steps), len(lon_steps)))
    for i in range(0, len(coord_list), batch_size):
        batch = coord_list[i:i+batch_size]
        print("requesting", coord_list[i])
        elevations = map_client.elevation(batch)
        for j, elevation in enumerate(elevations):
            lat_idx = int((batch[j][0] - lat1) / res)
            lon_idx = int((batch[j][1] - lon1) / res)
            elevation_matrix[lat_idx, lon_idx] = elevation['elevation']
    #initialize a plot
    plt.figure(figsize=(10, 10))
    # Normalize the data to 0 or 1 based on the elevation threshold
    elevation_binary = (elevation_matrix > min_ele).astype(int)
    plt.imshow(elevation_binary, cmap='coolwarm', origin='lower', extent=[lon1, lon2, lat1, lat2])
    plt.colorbar(label='Elevation > {} m'.format(min_ele))
    plt.title('Elevation Map')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()
    return
