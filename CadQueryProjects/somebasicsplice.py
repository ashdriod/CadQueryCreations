import cadquery as cq

# Define the workplane
s = cq.Workplane("XY")

# Define the points for the spline, excluding the first and last point which are part of the line
sPnts = [(0.2,-1), (1,-2), (2,-2), (3,-2), (3,-1), (3,0)]

# Move to the starting point (0,0)
r = s.moveTo(0.3, 0)

# Draw a straight line to the point (3,0)


# Continue with a spline through the rest of the points
r = r.spline(sPnts, includeCurrent=True)

# Close the wire to form a face and extrude
result = r.close().extrude(0.1)
