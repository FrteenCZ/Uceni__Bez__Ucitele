import os
from urllib.parse import quote


question_names = """1. Verzovací systém Git
2. Kybernetika, definice, základní principy a terminologie
3. Booleova Algebra
4. Karnaughovy mapy
5. Základní principy umělé inteligence
6. Učení s učitelem
7. Učení bez učitele
8. Základní principy neuronových sítí
9. Typy neuronových sítí
10. Computer vision
11. Algorytmizace - řízení programu
12. Objektově orientované programování
13. Pasivní elektronické prvky
14. Aktivní elektronické prvky
15. Kombinační a sekvenční logika
16. Elektronické senzory a aktuátory
17. Jednočipové mikropočítače a mikrokontrolery
18. Čítače a časové přerušení
19. A/D a D/A převodníky
20. Pulzně šířková modulace (PWM)
21. Komunikační protokol MQTT a jeho využití
22. Komunikační sběrnice I2C a SPI
23. Regulátory - P, PI, PID
24. Návrh a stabilita regulátorů""".split("\n")

teacher_folders = ["jedle", "svihlus"]
for teacher_folder in teacher_folders:

    questions = os.listdir(teacher_folder)


    for question in questions:
        if question == "README.md":
            continue

        files = os.listdir(os.path.join(teacher_folder, question))
        print(question, files)
        content = ""
        for file in files:
            if file[0] == "." or file == "README.md":
                continue
            

            content += f"- [{file}]({teacher_folder}/{question}/{quote(file)})\n"

        
        question_number = int(question[-2:]) - 1
        question_title = question_names[question_number]
        content += f"\n# {question_title}\n"
        with open(os.path.join(teacher_folder, question, "README.md"), "w", encoding="utf-8") as f:
            f.write(content)
