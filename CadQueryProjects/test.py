import cadquery as cq

# Parameters for the eyeglasses
lens_diameter = 50.0  # Diameter of each lens
bridge_length = 20.0  # Length of the bridge between the lenses
frame_thickness = 5.0  # Thickness of the eyeglasses frame
rim_thickness = 2.0   # Thickness of the rim around each lens

# Create the left lens
left_lens = (
    cq.Workplane("XY")
    .circle(lens_diameter / 2)
    .circle((lens_diameter / 2) - rim_thickness)
    .extrude(frame_thickness)
)

# Create the right lens by mirroring the left
right_lens = left_lens.mirror("Y")

# Create the bridge between the lenses
bridge = (
    cq.Workplane("XY")
    .workplane(offset=-bridge_length / 2, invert=True)
    .moveTo(0, lens_diameter / 2 - rim_thickness / 2)
    .lineTo(0, lens_diameter / 2 + rim_thickness / 2)
    .line(bridge_length, 0)
    .lineTo(0, lens_diameter / 2 - rim_thickness / 2)
    .close()
    .extrude(frame_thickness)
)

# Combine the lenses and the bridge to form the eyeglasses
eyeglasses = left_lens.union(right_lens).union(bridge)

# Render the solid
show_object(eyeglasses)

