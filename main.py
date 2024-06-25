from HaeufigeWoerter.CreatingTable import create_combined_table
from HaeufigeWoerter.HW import main
from partei import Partei

cduCsu = Partei(
    name="cduCsu",
    wahlprogrammLoc="Data/Wahlprogramme/CDUCSU.txt"
)
afd = Partei(
    name="afd",
    wahlprogrammLoc="Data/Wahlprogramme/AFD.txt"
)
spd = Partei(
    name="spd",
    wahlprogrammLoc="Data/Wahlprogramme/SPD.txt"
)
volt = Partei(
    name="volt",
    wahlprogrammLoc="Data/Wahlprogramme/Volt.txt"
)

main(cduCsu)
main(afd)
main(spd)
main(volt)

json_files = ['HaeufigeWoerter/Results/afd.json', 'HaeufigeWoerter/Results/cduCsu.json', 'HaeufigeWoerter/Results/spd.json', 'HaeufigeWoerter/Results/volt.json']
output_file = 'HaeufigeWoerter/Results/combined_table.json'
create_combined_table(json_files, output_file)