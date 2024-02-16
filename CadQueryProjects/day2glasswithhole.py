import cadquery as cq

# Original shapes creation as before

# First shape with spline
s = cq.Workplane("XY")
sPnts = [(0.2, 0), (0.2, -1), (1, -2)]
r1 = s.moveTo(0.3, 0).lineTo(3, 0).spline(sPnts, includeCurrent=True).close().extrude(0.1)

# Second shape, a polygon
points = [(0.2, 0), (1, -2), (2, -2), (3, -2), (3, -1), (3, 0)]
r2 = cq.Workplane("XY").polyline(points).close().extrude(0.1)

# Combine the two shapes with union
combined_result = r1.union(r2)

# Cutting off parts above X-axis as before
cut_box = cq.Workplane("XY").box(10, 10, 0.2).translate((1.5, 5, 0.1))
result_with_cut = combined_result.cut(cut_box)

# Create a scaled-down outline for the hole
# Assuming the combined result's outline can be represented similarly
hole_outline = cq.Workplane("XY").polyline(points).close().offset2D(-0.05)  # Offset by a fraction to scale down

# Extrude the hole outline to make it a solid to use for cutting
hole_to_cut = hole_outline.extrude(0.1)

# Cut the hole from the original combined shape
final_result = result_with_cut.cut(hole_to_cut)

# Display the final result
show_object(final_result)
