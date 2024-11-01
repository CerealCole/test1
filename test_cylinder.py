import pytest
from cylinder import volume_cylinder, area_cylinder

def test_volume_cylinder():
    # Test case 1: Diameter = 1, Height = 2
    assert round(volume_cylinder(1, 2), 4) == 1.5708
    # Test case 2: Diameter = 0.1, Height = 4
    assert round(volume_cylinder(0.1, 4), 4) == 0.0314
    # Test case 3: Diameter = 2, Height = 1
    assert round(volume_cylinder(2, 1), 4) == 3.1416

def test_area_cylinder():
    # Test case 1: Diameter = 1, Height = 2
    assert round(area_cylinder(1, 2), 4) == 7.8540
    # Test case 2: Diameter = 0.1, Height = 4
    assert round(area_cylinder(0.1, 4), 4) == 1.2723
    # Test case 3: Diameter = 2, Height = 1
    assert round(area_cylinder(2, 1), 4) == 12.5664

# New tests to check ValueError for negative height
def test_volume_negative_height():
    with pytest.raises(ValueError, match="Height must be a positive value."):
        volume_cylinder(1, -1)  # Negative height

def test_area_negative_height():
    with pytest.raises(ValueError, match="Height must be a positive value."):
        area_cylinder(1, -1)  # Negative height
