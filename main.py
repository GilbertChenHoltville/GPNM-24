import vis_area
def DrawElevation(lat1, lat2, lon1, lon2, api_key):
    terrain_png_img = vis_area.get_terrain_img(lat1, lat2, lon1, lon2, api_key)
    positive_elevation_png_img = vis_area.get_positive_elevation_img(lat1, lat2, lon1, lon2, api_key)
    return

if __name__ == '__main__':
    API_KEY = 'YOUR_API_KEY'
