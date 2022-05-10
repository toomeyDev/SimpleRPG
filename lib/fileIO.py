from world.map import Map
from world.cell import Cell
"""
Module containing functions for interacting with 
various files during runtime (save files, configurations, mapfiles)
"""

def load_map(mapfile):
    """
    Parse a provided .txt mapfile into a valid map to be used during gameplay.
    """
    reference_map = open(mapfile)
    dim_x = 0
    dim_y = 0
    for line in reference_map:
        line.strip()
        if line[0] == '/':
            continue
        elif 'MAPSIZE' in line:
            dim_x = line[9]
            dim_y = line[12]
    print(f"X: {dim_x} | Y: {dim_y}")
