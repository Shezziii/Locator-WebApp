from django.shortcuts import render
import folium
import geocoder
# Import the required library
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")



# Create your views here.
def home(request):
      my_location='INDIA'
      location = geolocator.geocode(my_location)
      map = folium.Map(location=[location.latitude, location.longitude],width=1000, height=500,zoom_start=2)
      folium.Marker([location.latitude, location.longitude], popup=location).add_to(map)
      from_=[location.latitude, location.longitude]
      if request.method=='POST':
            search=request.POST['search']
            location2 = geolocator.geocode(search)
            to_=[location2.latitude, location2.longitude]
            try:
                  folium.Marker([location2.latitude, location2.longitude],icon=folium.Icon(color='green' , icon="home"),popup=location2).add_to(map)
                  folium.PolyLine(locations=[from_,to_],color='light blue').add_to(map)
                  
            except :
                  print('Error')
            
      #location = geocoder(search)
      
      
      #print("The latitude of the location is: ", location.latitude)
      #print("The longitude of the location is: ", location.longitude)
      #lat = location.latitude
      #Ing =location.longitude
      #con=location.country
      # Create Map Obje abc lng
      # Get HTML Representation of Map Object
      
      
      map =map._repr_html_()
      context={ 'map' : map}
      return render(request,'home.html',context)