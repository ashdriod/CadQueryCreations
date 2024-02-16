import cadquery as cq

# Parameters for the semi-circular path
length = 20.0  # Length of the sweep path
width = 2.0    # Width of the rectangular profile
thickness = 2.0  # Thickness of the rectangular profile
arc_height = 10.0  # Height of the arc's midpoint, increase this for a larger diameter

# Assuming we want to define the semi-circular path with points,
# we can manually define points or calculate them to approximate a semi-circle.
# Here's a simple approximation using three points (start, peak, end) for the semi-circle:
start_point = (0, 0)
peak_point = (length / 2, arc_height)
end_point = (length, 0)

# Create a semi-circular path using three points
path = cq.Workplane("XZ").moveTo(*start_point).threePointArc(peak_point, end_point)

# Create the profile to be swept - a rectangle in this case
profile = cq.Workplane("XY").rect(width, thickness)

# Perform the sweep
swept_semi_circular_rod = profile.sweep(path)

