from math import sin, cos, pi, floor

def in_bounds(row, step, rows, steps, padding):
    if row < padding or row+padding >= rows:
        return False
    if step < padding or step+padding >= steps:
        return False
    return True


def coord_to_draw(row, step, padding):
    xoffset = (row-padding) % 4*23    
    x = -66+step*46+xoffset
    y = 560-row*39
    return (x, y)

def val_to_color(val, muted):
    color = [0, 0, 0]
    if val & 1:
        color[0] = 250
    if val & 4:
        color[1] = 250
    if val & 8:
        color[2] = 250
        
    if val & 2:
        if val & 1:
            color[0] = 250
            color[1] = 150
            color[2] = 60
        elif val & 4:
            color[0] = 150
            color[1] = 220
            color[2] = 30
        else:
            color[0] = 250
            color[1] = 250
    if muted:
        color[0] *= 0.4
        color[1] *= 0.4
        color[2] *= 0.4
    return color


def polygon_verts(vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    verts = []
    for i in range(n):
        deg = 2 * pi * i / n + 0.5*pi
        vx = x + r * cos(deg)
        vy = y + r * sin(deg)
        verts.append((round(vx), round(vy)))
    return verts

def polygon_outline(vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    verts = []
    for i in range(n):
        deg = 2 * pi * i / n + 0.5*pi
        verts.append((x + r * cos(deg), y + r * sin(deg)))
    return verts
