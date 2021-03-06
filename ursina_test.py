from ursina import *
from ent_parser import *

App = Ursina()

Map = Entity(model = "map.x", collider = "mesh", double_sided = True)
EditorCamera()

Entities = """
PointLight;
{
Position:-48,48,-64;
Color:255,255,255;
Range:500;
};
PointLight;
{
Position:48,48,-64;
Color:255,255,255;
Range:500;
};
PointLight;
{
Position:-48,48,48;
Color:255,255,255;
Range:500;
};
PointLight;
{
Position:64,48,48;
Color:255,255,255;
Range:500;
};
"""

Ents = get_entities(Entities)

for e in Ents:
    print(e)

App.run()
