import cadquery as cq

# First shape with spline
s = cq.Workplane("XY")
sPnts = [(0.2, 0), (0.2, -1), (1, -2)]
r1 = s.moveTo(0.3, 0).lineTo(3, 0).spline(sPnts, includeCurrent=True).close().extrude(0.1)

# Second shape, a polygon
points = [(0.2, 0), (1, -2), (2, -2), (3, -2), (3, -1), (3, 0)]
r2 = cq.Workplane("XY").polyline(points).close().extrude(0.1)

# Combine the two shapes with union
combined_result = r1.union(r2)

# Define a large box that covers the area above the X-axis
# The box dimensions and position should be adjusted based on the expected size and location of your shapes
cut_box = cq.Workplane("XY").box(10, 10, 0.2).translate((1.5, 5, 0.1))

# Cut the part of the combined shape that extends above the X-axis using the box
result = combined_result.cut(cut_box)

# Display the result
show_object(result)
