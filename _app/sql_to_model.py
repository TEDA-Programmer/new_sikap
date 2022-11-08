import os

main_resource = input("Masukan nama main folder (default: _app): ")
main_resource = "_app" if main_resource == "" else main_resource
fl = open("static/new_sikap.sql")
isi_file = fl.read()
fl.close()

per_baris = isi_file.split("\n")
mulai = False
list_tabel = []
for pb in per_baris:
    if "CREATE TABLE public." in pb:
        mulai = True
        list_tabel.append({
            "name": pb.replace("CREATE TABLE public.", "").replace(" (", ""),
            "isi": []
        })

    if ");" not in pb and mulai:
        if "CREATE TABLE" not in pb:
            pb = pb.replace("    ", "").replace(",", "")
            isi = pb.split(" ")
            list_tabel[-1]["isi"].append(isi)
    elif ");" in pb:
        mulai = False

if not os.path.exists("models"):
    os.mkdir("models")

for lt in list_tabel:
    md = open("models/" + lt['name'] + ".py", "w")
    md.write(f"import uuid\n")
    md.write(f"from datetime import datetime\n\n")
    md.write(f"from {main_resource} import db\n\n\n")
    md.write(f"class {lt['name'].title().replace('_', '')}Model(db.Model):\n")
    md.write(f"    __tablename__ = '{lt['name']}'\n")
    list_col, isi_init, col_init = [], [], []

    for i in lt['isi']:
        primary, default = "", ""

        list_col.append(i[0])
        if i[0] != "id" and i[0] != "add_time":
            col_init.append(i[0])
            isi_init.append(f"        self.{i[0]} = {i[0]}\n")
        if i[0] == 'id':
            primary = ", primary_key=True"
            if i[1] == 'character':
                data_type = "String"
                default = ", default=lambda: uuid.uuid4().hex"
            elif i[1] == 'integer':
                data_type = "Integer"
                default = ", autoincrement=True"
        elif i[0] == "add_time":
            data_type = "DateTime"
            default = ", default=lambda: datetime.now()"

        if i[1] == 'character':
            data_type = "String"
        elif i[1] == 'integer':
            data_type = "Integer"
        elif i[1] == 'timestamp':
            data_type = "DateTime"
        else:
            data_type = i[1].upper()

        for index, d in enumerate(i):
            if d == 'DEFAULT' and i[0] != "id" and i[0] != "add_time":
                if i[index + 1] == "CURRENT_DATE":
                    default = f", default=lambda: datetime.now().date()"
                else:
                    default = f", default={i[index + 1]}"

        md.write(f"    {i[0]} = db.Column(db.{data_type}{primary}{default})\n")

    md.write("\n")

    md.write(f"    def __init__(self, {', '.join(col_init)}):\n")
    md.write(f"".join(isi_init))

    md.write("\n")

    md.write(f"    def json(self):\n")
    md.write("        return {\n")
    for lc in list_col:
        if "password" not in lc:
            md.write(f"            '{lc}': self.{lc},\n")
    md.write("        }\n")

    md.close()

print("Models created succesfully!")