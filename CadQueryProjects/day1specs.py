import cadquery as cq

# Parameters for the cuboid
length = 21.0  # Length of the cuboid
width = 2.0     # Width of the cuboid
thickness = 2.0  # Thickness of the cuboid

# Create a 3D cuboid that represents a "line" with thickness and width
cuboid = (
    cq.Workplane("YZ")
    .rect(width, thickness)  # Create a rectangle with the desired width and thickness
    .extrude(length)  # Extrude the rectangle to give it the desired length
)

# Parameters for the semi-circular path
length = 20.0  # Length of the sweep path
width = 2.0    # Width of the rectangular profile
thickness = 2.0  # Thickness of the rectangular profile
arc_height = 10.0  # Height of the arc's midpoint, increase this for a larger diameter

start_point = (0,0)
peak_point = (length / 2, arc_height)
end_point = (length, 0)

# Create a semi-circular path using three points
path = cq.Workplane("XZ").moveTo(*start_point).threePointArc(peak_point, end_point)

# Create the profile to be swept - a rectangle in this case
profile = cq.Workplane("XY").rect(width, thickness)

# Perform the sweep
swept_semi_circular_rod = profile.sweep(path)


#show_object(cuboid)

