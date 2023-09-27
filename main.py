import requests
import re
from bs4 import BeautifulSoup

URL = "https://www.start.gg/tournament/road-to-wololo/event/july-weekly-i/brackets/1125935/1757447"
REQUEST = requests.get(URL)
SOUP = BeautifulSoup(REQUEST.text, 'lxml')


def get_score(soup):
    l = soup.select('[class^="match-player-stocks"]')
    return_l = []
    for z in l:
        z = str(z)
        m = re.search('[0-9]', z)
        z = m.group(0)
        return_l.append(z)
    return return_l


def get_name(soup):
    l = soup.select('span[class^="match-player-name-container"]')
    return_l = []
    for item in l:
        item = str(item)
        item = item[:-7]
        if "</span>" in item:
            m = re.search('</span>.*', item)
            temp = m.group(0)
            temp = temp[7:]
            item = temp
        else:
            m = re.search('">.*', item)
            temp = m.group(0)
            temp = temp[2:]
            item = temp
        return_l.append(item)
    return return_l


def get_dqs(soup):
    l = soup.select('[class^="match has-identifier reportable"]')
    dq_l = []
    for item in l:
        if "match-player-stocks" in str(item):
            dq_l.append(-1)
            dq_l.append(-1)
        else:
            dq = re.search("text-dq", str(item))
            winner = re.search("fa fa-check text-success", str(item))
            if dq:
                if winner:
                    if dq.start() < winner.start():
                        dq_l.append(0)
                        dq_l.append(1)
                    else:
                        dq_l.append(1)
                        dq_l.append(0)
                else:
                    dq_l.append(0)
                    dq_l.append(0)
            else:
                secondary_check = re.search("match-section match-section-bottom", str(item))
                if secondary_check.start() < winner.start():
                    dq_l.append(0)
                    dq_l.append(1)
                else:
                    dq_l.append(1)
                    dq_l.append(0)
    return dq_l


def get_final_list(l1, l2):
    counter = 0
    final_list = []
    for i in range(len(l1)):
        if dq_l[i] == -1:
            final_list.append([l1[i], int(l2[i + counter])])
        else:
            final_list.append([l1[i], dq_l[i]])
            counter -= 1
    return final_list


def get_sheets_lists():
    l1_final = []
    l2_final = []
    for j in range(len(final_list)):
        if j % 2 == 0:
            if final_list[j][1] > final_list[j + 1][1]:
                l1_final.append(final_list[j][0])
                l2_final.append(final_list[j + 1][0])
                l1_final.append(final_list[j + 1][0])
                l2_final.append(final_list[j][0])
            elif final_list[j + 1][1] > final_list[j][1]:
                l1_final.append(final_list[j + 1][0])
                l2_final.append(final_list[j][0])
                l1_final.append(final_list[j][0])
                l2_final.append(final_list[j + 1][0])
    return l1_final, l2_final


def print_lists(l1, l2):
    for player in l1:
        print(player)
    print("/////////////////////////////////////////////////")
    for player in l2:
        print(player)


def write_to_file(l1, l2):
    f = open("target.txt", "w")
    for item in l1:
        f.write(item)
        f.write("\n")
    f.close()
    f = open("opponent.txt", "w")
    for item in l2:
        f.write(item)
        f.write("\n")
    f.close()


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


l1, l2 = get_name(SOUP), get_score(SOUP)
rename(l1)
dq_l = get_dqs(SOUP)
final_list = get_final_list(l1, l2)
l1_final, l2_final = get_sheets_lists()
print_lists(l1_final, l2_final)
write_to_file(l1_final, l2_final)
