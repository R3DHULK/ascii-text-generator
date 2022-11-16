from pyfiglet import Figlet

print ('''
    ***************************************************   
    *    _   ___  ___ ___ ___   _____ _____  _______  *
    *   /_\ / __|/ __|_ _|_ _| |_   _| __\ \/ /_   _| *
    *  / _ \\__ \ (__ | | | |    | | | _| >  <  | |   *
    * /_/ \_\___/\___|___|___|   |_| |___/_/\_\ |_|   *
    *                                                 *
    *   ___ ___ _  _ ___ ___    _ _____ ___  ___      *
    *  / __| __| \| | __| _ \  /_\_   _/ _ \| _ \     *
    * | (_ | _|| .` | _||   / / _ \| || (_) |   /     *
    *  \___|___|_|\_|___|_|_\/_/ \_\_| \___/|_|_\     *
    *                                                 *
    *              coded by R3dHULK                   *
    *                                                 *
    ***************************************************   
    *   popular ascii text are shown below :          *
    *                                                 *
    *   1. Graffiti                                   *
    *   2. Small                                      *
    *   3. Big                                        *
    *   4. Bulbhead                                   *
    *   5. Alphabet                                   *
    *   6. Avatar                                     *
    *   7. Banner 3-d                                 *
    *   8. Acrobatic                                  *
    *   9. Doh                                        *
    *  10. Babyface lame                              *
    *  11. Isometric1                                 *
    *  12. Letters                                    *
    *  13. Alligator                                  *
    *  14. Dotmatrix                                  *
    *  15. Block                                      *
    *  16. Bubble                                     *
    *  17. Doom                                       *
    *  18. Digital                                    *
    *  19. Slant                                      *
    *  20. Graceful                                   *
    *  21. Doh                                        *
    *  22. Epic                                       *
    *  23. 5lineoblique                               *
    *  24. Standard                                   *  
    *                                                 *
    * 😊 Choose Your Favourite Font 😊               *
    *                                                 *
    ***************************************************
    ''')

custom_fig = Figlet(font=(input(" ==> Enter Your Choice 👉  ")))

print(custom_fig.renderText(input(" ==> Enter Your Text 👉  ")))

input ("Enter To Exit")