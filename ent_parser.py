
File = """
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

def get_entities(file_):
    mode = "type"
    actual_ent_name = ""
    ent = {}
    ents = []

    for e in file_.split("\n"):
        if mode == "type" and e != "":
            actual_ent_name = e
            if actual_ent_name.endswith(";"):
                actual_ent_name = actual_ent_name[:-1]
            ent[ actual_ent_name ] = []
            mode = "inside"
        elif mode == "inside":
            if e != "{" and e != "};":
                ent[ actual_ent_name ].append(e)
            if e == "};":
                ents.append({"name" : actual_ent_name, "content" : ent[ actual_ent_name ] } )
                mode = "type"
    return ents

def get_arg(arg_):
    arg_content = arg_["content"]
    ret = {}
    rets = []
    for e in arg_content:
        arg_s = e.split(":")
        arg_name = arg_s[0]
        arg_content = arg_s[1]
        ret[arg_name] = []
        for c in arg_content.split(","):
            if c.endswith(";"):
                c = c[:-1]
            ret[arg_name].append(c)

        return ret

if __name__ == "__main__":
    Ents = get_entities(File)
    for e in Ents:
        print(f"------> {e['name']}")
        print(f"---> {get_arg(e)['Position']}")
