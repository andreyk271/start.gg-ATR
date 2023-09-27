f = open("prep_target.txt", "r", encoding="utf-8")
g = open("prep_opponent.txt", "r", encoding="utf-8")

target_lines = f.readlines()
opponent_lines = g.readlines()


def rename(l):
    for i in range(len(l)):
        if l[i] == "judgin_z":
            l[i] = "Judgin"
        elif l[i] == "Reina AntoCony":
            l[i] = "AntoCony"
        elif l[i] == "AGE 4":
            l[i] = "YUImetal"
        elif l[i] == "[NFR] Oblago":
            l[i] = "Oblago"
        elif l[i] == "Beastyqt":
            l[i] = "Beasty"
        elif l[i] == "GG.simtom":
            l[i] = "simtom"
        elif l[i] == "ingsok":
            l[i] = "ingsoc"
        elif l[i] == "OppaXoai":
            l[i] = "Xoai"
        elif l[i] == "Avely":
            l[i] = "IamAvely"
        elif l[i] == "DeMusliM":
            l[i] = "DeMu"
        elif l[i] == "Corvinus1":
            l[i] = "Corvinus"
        elif l[i] == "COINNU (aka PSiArc)":
            l[i] = "COINNU"
        elif l[i] == "Flash":
            l[i] = "Flash!"
        elif l[i] == "PCS.Tattoo":
            l[i] = "Tattoo"
        elif l[i] == "Viola./-":
            l[i] = "Viola"
        elif l[i] == "GhostKz_aoe":
            l[i] = "kz"
        elif l[i] == "General_Bai_qi":
            l[i] = "General Bai qi"
        elif l[i] == "OpDVlaM":
            l[i] = "OpDVIaM"
        elif l[i] == "1puppypaw":
            l[i] = "Puppypaw"
        elif l[i] == "Knusch":
            l[i] = "Knuschelbär"
        elif l[i] == "loueMT":
            l[i] = "IoueMT"
        elif l[i] == "SAS_":
            l[i] = "wntdSAS"
        elif l[i] == "SkWizZ_Wraith":
            l[i] = "Wraith"
        elif l[i] == "OmnissiaH":
            l[i] = "OmnissiahMaster"
        elif l[i] == "DarkPsicopata ESP":
            l[i] = "DarkPsicopata"
        elif l[i] == "mYi.Ourk":
            l[i] = "Ourk"
        elif l[i] == "stamminen":
            l[i] = "stamminen21"
        elif l[i] == "SBS | ClearMan":
            l[i] = "ClearMan"
        elif l[i] == "hosein81":
            l[i] = "hoseinm"
        elif l[i] == "Der_schöne_Klaus":
            l[i] = "Der schöne Klaus"
        elif l[i] == "imtoonoob_AoE":
            l[i] = "imtoonoob"
        elif l[i] == "Cory.costa22":
            l[i] = "Cory.Costa"
        elif l[i] == "General_Wang_Jian":
            l[i] = "General Wang Jian"
        elif l[i] == "HB`":
            l[i] = "HB"
        elif l[i] == "Keyrun22":
            l[i] = "Keyrun"
        elif l[i] == "AOE4":
            l[i] = "ORILIGHT"
        elif l[i] == "iamcoco2647":
            l[i] = "iamcoco"
        elif l[i] == "Hutster911":
            l[i] = "Hutster"
        elif l[i] == "StateSC2":
            l[i] = "State"
        elif l[i] == "aX | Matiz":
            l[i] = "Matiz"
        elif l[i] == "iTzGarry2555":
            l[i] = "iTzGarry"
        elif l[i] == "真 善 美 | Flash":
            l[i] = "Flash!"
        elif l[i] == "3D! | Garnath":
            l[i] = "Garnath"
        elif l[i] == "PSR.Draldrin":
            l[i] = "Draldrin"
        elif l[i] == "ICONIC | AceMcClyde":
            l[i] = "AceMcClyde"
        elif l[i] == "Szalami1":
            l[i] = "Corvinus"
        elif l[i] == "hoseinm1381":
            l[i] = "hoseinm"
        elif l[i] == "PSR.Tattoo":
            l[i] = "Tattoo"
        elif l[i] == "SBS | SBS | ClearMan":
            l[i] = "ClearMan"
        elif l[i] == "YUImetal | AGE 4":
            l[i] = "YUImetal"
        elif l[i] == "3D! | Bee":
            l[i] = "Bee"
        elif l[i] == "Liquid | DeMusliM":
            l[i] = "DeMu"
        elif l[i] == "GG | Chrysaor":
            l[i] = "Chrysaor"
    return l


target = []
opponent = []
for line in target_lines:
    line = line[:-1]
    target.append(line)
for line in opponent_lines:
    line = line[:-1]
    opponent.append(line)

f.close()
g.close()

target.reverse()
opponent.reverse()

t1 = target.copy()
o1 = opponent.copy()

counter = 0
for i in range(len(target)):
    t1.insert(i + 1 + counter, opponent[i])
    o1.insert(i + 1 + counter, target[i])
    counter += 1
    print(i+1+counter, len(t1))

t1 = rename(t1)
o1 = rename(o1)

target_file = open("target.txt", "w", encoding="utf-8")
opponent_file = open("opponent.txt", "w", encoding="utf-8")
for i in range(len(t1)):
    target_file.write(t1[i])
    target_file.write("\n")
    opponent_file.write(o1[i])
    opponent_file.write("\n")