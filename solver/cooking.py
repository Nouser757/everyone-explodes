from ktools import Edge, rangify

def cooking(edge: Edge):
    
    meal = rangify((edge.batteryHolders - edge.indicatorCount + (edge.totalBatteries * edge.portCount) - edge.portPlates), 5, 1, 5) - 1
    oven = rangify((edge.litIndicatorCount - edge.unlitIndicatorCount + edge.serialLetterCount), 6, 1, 6) - 1
    light = (edge.serialVowel or "ps2" in edge.portsPresent)

    heats = [250, 160, 200, 180, 180]
    settings = ["Bottom Elem", "Bottom Elem + Grill", "Conv. Heat", "Fan", "Grill", "Fan + Grill"]

    if "lFRK" in edge.indicators or "serial" in edge.portsPresent: client = 3
    elif [] in edge.portsRaw or "lFRQ" in edge.indicators: client = 0
    elif edge.serialDigitCount > edge.serialLetterCount or "uSND" in edge.indicators: client = 4
    elif "BOB" in edge.indicatorLabels: client = 1
    else: client = 2

    times = [[10, 15, 20, 30, 50], [75, 70, 80, 65, 10], [55, 70, 65, 45, 60], [95, 90, 75, 70, 35], [25, 30, 35, 40, 10]]

    print(f"""    Temp: {heats[meal]}
    Setting: {settings[oven]}
    Light: {"on" if light else "off"}
    Time: {times[meal][client]}""")