import cadquery as cq

# Parameters for the cuboid
length = 50.0  # Length of the cuboid
width = 2.0     # Width of the cuboid
thickness = 2.0  # Thickness of the cuboid

# Create a 3D cuboid that represents a "line" with thickness and width
cuboid = (
    cq.Workplane("XY")
    .rect(width, thickness)  # Create a rectangle with the desired width and thickness
    .extrude(length)  # Extrude the rectangle to give it the desired length
)

# Assuming you're using CQ-editor or a similar environment to visualize
# Replace `show_object` with the appropriate function call if using a different environment
show_object(cuboid)

