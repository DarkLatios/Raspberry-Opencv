
n=raw_input("Enter The points")
y=raw_input("Enter The points")
lat=n.split(',')
lon=y.split(',')
dlat=int(lat[0])+(int(lat[1])/60.0)+(int(lat[2])/3600.0)
dlon=int(lon[0])+(int(lon[1])/60.0)+(int(lon[2])/3600.0)
print dlat,dlon
