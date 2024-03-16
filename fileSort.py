import os
"""
file9 = ["bed","chair","closet","curtain","desk","lamp","shelf","sofa","table"]
for _, file in enumerate(file9):
    directory = os.listdir('/Users/HYG/boj-solve/'+file)
    os.chdir('/Users/HYG/boj-solve/'+file)
    target_word = ' '
    new_word = '\n'

    for file in directory:
        new_text_content = ''
        with open(file, 'r',encoding='utf-8') as f:
            lines = f.readlines()
            for i, l in enumerate(lines):
                new_string = l.strip().replace(target_word, new_word)
                if new_string:
                    new_text_content += new_string + '\n'
                else:
                    new_text_content += '\n'

        with open(file,'w',encoding='utf-8') as f:
            f.write(new_text_content)


"""

coldSoft = {"Dreamy": [], "Charming": [], "Wholesome": [], "Tranqu": [], "Plain": [], "Fresh": [], "Emotional": [],
            "Fashionable": [], "Delicate": [], "Chic": [], "Agile": [], "Youthful": [], "Refreshing": [], "Clean": [],
            "Neat": []}
warmSoft = {"Colorful": [], "Casual": [], "Bright": [], "Enjoyable": [], "Pretty": [], "Childlike": [], "Sweet": [],
            "Soft": [], "Intimate": [], "Mild": [], "Graceful": []}
warmHard = {"Lively": [], "Bold": [], "Active": [], "Wild": [], "Extravagant": [], "Alluring": [], "Mellow": [],
            "Luxurious": [], "Trational": [], "Elaborate": [], "Heavy&Deep": [], "Calm": []}
coldHard = {"Modest": [], "Quite": [], "Dapper": [], "Dignified": [], "Noble": [], "Stylish": [], "Sporty": [],
            "Sharp": [], "Rational": [], "Masculine": [], "Metallic": []}
theme4 = [coldSoft,warmSoft,warmHard,coldHard]
backup = {"coldSoft": [],"warmSoft": [],"warmHard": [],"coldHard": []}
file9 = ["bed","chair","closet","curtain","desk","lamp","shelf","sofa","table"]
"""
for _, file in enumerate(file9):
    os.chdir('/Users/HYG/boj-solve/' + file)
    for _, theme in enumerate(theme4):
        with open(file + ".txt", 'r',encoding='utf-8') as f:
            lines = f.readlines()
            for tone in theme.keys():
                for i, l in enumerate(lines):
                    if str(tone) in l:
                        theme[tone].append(i)
                with open(file + "_" + tone + ".txt", 'w',encoding='utf-8') as g:
                    for i, index in enumerate(theme[tone]):
                        g.write(str(index) +"\n")
                    theme[tone] = []
"""
for _, file in enumerate(file9):
    os.chdir('/Users/HYG/boj-solve/' + file)
    for h, theme in enumerate(theme4):
        with open(file + ".txt", 'r',encoding='utf-8') as f:
            lines = f.readlines()
            for i, l in enumerate(lines):
                for tone in theme.keys():
                    if str(tone) in l:
                        list(backup.values())[h].append(i)
            with open(file + "_" + list(backup.keys())[h] + ".txt", 'w',encoding='utf-8') as g:
                for j, index in enumerate(list(backup.values())[h]):
                    g.write(str(index) +"\n")
        backup["coldSoft"] = []
        backup["warmSoft"] = []
        backup["warmHard"] = []
        backup["coldHard"] = []

