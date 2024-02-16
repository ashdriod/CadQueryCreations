import cadquery as cq

# Define the points for the zigzag path
points = [(0, 0, 0), (10, 0, 0), (10, 0,10), (00, 0, 10), (0, 0, 0)]

# Create the path using the points
path = cq.Workplane("XY").polyline(points)

# Define the size of the rectangle profile
width = 2.0
height = 2.0

# Create the profile to be extruded
profile = cq.Workplane("YZ").rect(width, height)

# Extrude the profile along the path
extruded_shape = profile.sweep(path, makeSolid=True)

# Show the result
show_object(extruded_shape)
