
File = """
PointLightA;
{
Color:0,0,255;
Range:500;
};
PointLightB;
{
Color:0,255,0;
Dist:300;
Blabla:hello;
};
"""

def get_entities(file_):
    mode = "type"
    actual_ent_name = ""
    ents = {}
    for e in file_.split("\n"):
        if mode == "type" and e != "":
            actual_ent_name = e
            ents[ actual_ent_name ] = []
            mode = "inside"
        elif mode == "inside":
            if e != "{" and e != "};":
                ents[ actual_ent_name ].append(e)
            if e == "};":
                mode = "type"
    return ents

def get_arg(arg_):
    arg_splitted = arg_.split(":")
    arg_name = arg_splitted[0]
    arg_content = arg_splitted[1]
    if arg_content.endswith(";"):
        arg_content = arg_content[:-1]
    arg_content_splitted = arg_content.split(",")

    return {"name" : arg_name, "content" : arg_content_splitted}



if __name__ == "__main__":
    Ents = get_entities(File)

    for e in Ents:
        print(f"---> {e}")
        for a in Ents[e]:
            b = get_arg(a)
            print(f"{ b['name'] } ---> { b['content'] }")
