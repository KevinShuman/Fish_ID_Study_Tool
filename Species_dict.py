import pandas as pd
import numpy as np
import os

def species_dict(name, size, position, group_size, appearance, distinguishing_features, occurence):
    return {"Scientific Name":name, "Size":size, "Position":position, "Group Size":group_size, "Appearance":appearance, "Distinguishing Features":distinguishing_features, "Occurence":occurence}

def species_dict_int(name, size, position, group_size, appearance, distinguishing_features, occurence, interest):
    return {"Scientific Name":name, "Size":size, "Position":position, "Group Size":group_size, "Appearance":appearance, "Distinguishing Features":distinguishing_features, "Occurence":occurence, "Interest":interest}

def rv_rp_strings(string):
    new_string = string
    new_string = new_string.replace('Group Size: ','","')
    new_string = new_string.replace('Size: ','"')
    new_string = new_string.replace('Position: ','","')
    new_string = new_string.replace('Appearance: ','","')
    new_string = new_string.replace('Distinguishing Feature: ','","')
    new_string = new_string.replace('Occurrence: ','","')
    front = "species_dict("
    back = '")'
    return front + new_string + back

def rv_rp_int_strings(string):
    new_string = string
    new_string = new_string.replace('Group Size: ','","')
    new_string = new_string.replace('Size: ','"')
    new_string = new_string.replace('Position: ','","')
    new_string = new_string.replace('Appearance: ','","')
    new_string = new_string.replace('Distinguishing Feature: ','","')
    new_string = new_string.replace('Occurrence: ','","')
    new_string = new_string.replace('Interest: ','","')
    front = "species_dict_int("
    back = '")'
    return front + new_string + back

sharks = [
        r"Grey Reef Shark",
        r"Blacktip Reef Shark",
        r"Whitetip Reef Shark",
        r"Silvertip Shark",
        r"Blacktip Shark",
        r"Sicklefin Lemon Shark",
        r"Tiger Shark",
        r"Oceanic Thresher Shark",
        r"Snaggletooth Shark",
        r"Scalloped Hammerhead Shark",
        r"Great Hammerhead Shark",
        r"Whale Shark",
        r"Indonesian Wobbegong Shark",
        r"Spotted Wobbegong Shark",
        r"Coral Catshark",
        r"Tawny Nurse Shark",
        r"Brownbanded Bamboo Shark"
        ]
rays = [
        r"Oceanic Manta Ray",
        r"Reef Manta Ray",
        r"Spinetail Devil Ray",
        r"Spotted Eagle Ray",
        r"Javanese Cownose Ray",
        r"Pink Whipray",
        r"Blue-Spotted Stingray",
        r"Blue-Spotted Ribbontail Ray",
        r"Marbled Stingray",
        r"Mangrove Whipray",
        r"Broad Cowtail Stingray",
        r"Bowmouth Guitarfish"
        ]
turtles = [
        r"Loggerhead Turtle",
        r"Green Sea Turtle",
        r"Hawksbill Turtle",
        r"Olive Ridely Turtle",
        r"Leatherback Turtle"
        ]
grouper = [
        r"Brown-Marbled Grouper",
        r"Malabar Grouper",
        r"Potato Grouper",
        r"Giant Grouper",
        r"Speckled Grouper",
        r"Blue-and-Yellow Grouper",
        r"Black-Saddled Coral Grouper",
        r"Leopard Coral Grouper",
        r"Spotted Coral Grouper",
        r"Roving Coral Grouper",
        r"Yellow-Edged Lyretail Grouper",
        r"Dusktail Grouper",
        r"White-Spotted Grouper",
        r"Orange-Spotted Grouper",
        r"Blacktip Grouper",
        r"Highfin Grouper",
        r"One-Blotch Grouper",
        r"Netfin Grouper",
        r"Camoflague Grouper",
        r"Halfmoon Grouper",
        r"Redmouth Grouper",
        r"Slender Grouper",
        r"Peacock Grouper",
        r"Chocolate Grouper",
        r"Bluelined Grouper",
        r"Coral Grouper",
        r"Harlequin Grouper",
        r"Tomato Grouper",
        r"Masked Grouper",
        r"Squaretail Coral Grouper",
        r"White-Edged Lyretail Grouper",
        r"Barramundi"
        ]
snapper = [
        r"Red Snapper",
        r"Blubberlip Snapper",
        r"Red Emperor Snapper",
        r"Chinamanfish",
        r"Green Jobfish",
        r"Mangrove Snapper",
        r"Checkered Snapper",
        r"Blackspot Snapper",
        r"Longspot Snapper",
        r"Blacktail Snapper",
        r"Humpback Snapper",
        r"Humpback Snapper",
        r"Big Eye Snapper",
        r"Onespot Snapper",
        r"Brownstripe Snapper",
        r"Yellowfin Snapper",
        r"Midnight Snapper",
        r"Black Snapper",
        r"Smalltooth Jobfish",
        r"Pinjalo Snapper",
        r"Slender Pinjalo"
        ]
emperors = [
        r"Yellowtail Emperor",
        r"Yellowfin Emperor",
        r"Longfin Emperor",
        r"Thumbprint Emperor",
        r"Pinkear Emperor",
        r"Smalltooth Emperor",
        r"Spangled Emperor",
        r"Orange-Striped Emperor",
        r"Longface Emperor",
        r"Ornate Emperor",
        r"Spotcheek Emperor",
        r"Yellowlip Emperor",
        r"Humpnose Bigeye Bream"
    ]
parrotfish = [
        r"Bumphead Parrotfish",
        r"Bleeker's Parrotfish",
        r"Steephead Parrotfish",
        r"Bridled Parrotfish",
        r"Blue-Barred Parrotfish",
        r"Redlip Parrotfish",
        r"Red Parrotfish",
        r"Tricolor Parrotfish"
    ]
jacks_trevally= [
        r"Giant Trevally",
        r"Black Jack",
        r"Bluefin Trevally",
        r"Bigeye Trevally",
        r"Gold-Spotted Trevally",
        r"Bludger Trevally",
        r"Rainbow Runner",
        r"Almaco Amberjack",
        r"African Pompano",
        r"Orange-Spotted Trevally",
        r"Blue Trevally",
        r"Barcheek Trevally",
        r"Brassy Trevally",
        r"Longraked Trevally",
        r"Double-Spotted Queenfish"
    ]
tuna_mackerel= [
        r"Dogtooth Tuna",
        r"Yellowfin Tuna",
        r"Wahoo",
        r"Narrow-Barred Spanish Mackerel",
        r"Double-Lined Mackerel",
        r"Slingjaw Mackerel"
        ]
barracuda= [
        r"Great Barracuda",
        r"Pickhandle Barracuda",
        r"Chevron Barracuda",
        r"Yellowtail Barracuda",
        r"Bigeye Barracuda"
        ]
species_of_interest= [
        r"Napoleon Wrasse",
        r"Bumphead Parrotfish",
        r"Bumphead Mola",
        r"Java Rabbitfish",
        r"Oriental Sweetlips",
        r"Topsail Drummer Chub",
        r"Giant Moray Eel",
        r"Honeycomb Moray Eel",
        r"Big Blue Octopus",
        r"Broadclub Cuttlefish",
        r"Bigfin Reef Squid",
        r"Triton Trumpetshell",
        r"Crown-of-Thorns Starfish",
        r"Ornate Spiny Lobster",
        r"Short-Finned Pilot Whale",
        r"Common Bottlenose Dolphin",
        r"Spinner Dolphin"
]

#species_groups = [sharks, rays, turtles, grouper, snapper, emperors, parrotfish, jacks_trevally, tuna_mackerel, barracuda, species_of_interest]

species = {
    "Sharks": {
        "Grey Reef Shark":species_dict("Carcharhinus amblyrhynchos","Up to 2.65m, commonly around 1.6m.","Coastal, lagoon and outer slopes.","Solitary or form schools.","Grey with white underside. Second dorsal, anal and underside of pectoral fins usually black. Can have white margin on dorsal posterior edge. Broad black tail margin.","Black tail margin.","Rare (Penida, Bunaken), Common (Bira)."),
        "Blacktip Reef Shark":species_dict("Carcharhinus melanopterus","Up to 2.3m, commonly around 1.2m.","Coastal, lagoon and outer slopes.","Solitary or small groups.","Brownish grey with underside. Black tip on 1st and 2nd dorsal, pectoral, anal and lower lobe of tail fins.", "Black and white stripe dorsal.","Rare (Penida), Common (Bira, Bunaken)."),
        "Whitetip Reef Shark":species_dict("Triaenodon obesus","Up to 2m, commonly 1.4m.","Coastal, lagoon and outer slopes.","Solitary or small groups.","Grey body. Occasional dark spots on sides/ White tips on 1st dorsal fin and upper tail lobe. Often found resting in day on reef flats and under ledges. Blunt nose.","White tips & blunt nose.","Common (Bira, Bunaken), Uncommon (Penida)."),
        "Silvertip Shark":species_dict("Carcharhinus albimarginatus","Up to 3 m.","Coastal, lagoon and outer slopes.","Solitary or small groups.","Grey with pale underside. White-silvery continuous tips on 1st, pectoral and caudal fin lobes. Very fast moving shark.","Silver edges on all fins.","Extremely Rare (Penida, Bunaken), Rare (Bira)."),
        "Blacktip Shark":species_dict("Carcharhinus limbatus","Up to 2.8 m.","Lagoons, inshore water and reef channel.","Solitary or small groups.","Grey with white underside. Anal fin pale tip white. Black tips on 2nd dorsal, pectoral and ventral fins and lower tail lobe. Silver-white streak on flank.","Black tips on pectorals.","Rare (Penida, Bira, Bunaken)."),
        "Sicklefin Lemon Shark":species_dict("Negaprion acuntidens","Up to 3.1m.","Bottom of bays, estuaries and offshore reefs.","Solitary or small groups.","Pale yellow-brown with white underside. Pair of widely spaced dorsal fins of nearly equal height.","Open mouth 'smile' and dorsal fin spacing.","Extremely Rare (Penida, Bira, Bunaken)."),
        "Tiger Shark":species_dict("Galeocerdo cuvier","Up to 7.4m, commonly 5m.","Oceanic, coastal and offshore reef.","Solitary.","Grey with dusky bars on body. Long slender caudal fin with pointed tip. Robust body shape with blunt nose.","Tiger stripes, robust body.","Extremely Rare (Penida, Bira, Bunaken)."),
        "Oceanic Thresher Shark":species_dict("Alopias pelagicus","Up to 4.2m, commonly 2m.","Oceanic, occasionally near reef drop-offs.","Solitary or small groups.","Dark blue to bluish gray with silvery burnish and white underside. Long upper lobe of tail almost length of entire body. Long pectoral fins with nearly straight leading edge has a rounded tip","Black scutes & edges.","Uncommon (Penida, Bira), Rare (Bunaken)."),
        "Snaggletooth Shark":species_dict("Hemipristis elongata","Up to 2.3m.","Oceanic, sandy, reef area.","Solitary.","Grey to brown without marking. Rounded snout. Gill slits long. Fins strongly curved: pectoral, pelvic, anal and caudal fins separated almost in a similar distance through the whole-body size.","Bump shaped head.","Uncommon (Penida), Extremely Rare (Bira, Bunaken)."),
        "Scalloped Hammerhead Shark":species_dict("Sphyrna lewini","Up to 4.3m, commonly 3m.","Open water of seaward reef.","Can be solitary but commonly in schools.","Grey with white underside. Head flattened and extended to either side resembles to hammer, prominent central indentation on front edge and “scalloped”.","Regular size dorsal fin.","Uncommon (Penida, Bira), Extremely Rare (Bunaken)"),
        "Great Hammerhead Shark":species_dict("Sphyrna mokarran","Up to 6.1m, commonly 4.5m.","Oceanic, rarely on the reef.","Solitary.","Grey with white underside. Head resembles hammer shape, front edge slightly curved. Lesser prominent indentation on the front head. Rear edge of the ventral fin curved.","Large dorsal fin.","Extremely Rare (Penida, Bira, Bunaken)."),
        "Whale Shark":species_dict("Rhincodon typus","Up to 17m, juvenile males mostly seen (10m).","Oceanic, occasionally around reefs.","Solitary.","Huge, dark grey with white underside. Numerous white spots scattered on head and arranged in rows and bars on body. Broad mouth, ridges on side of body.","Size and shape.","Uncommon (Penida), Rare (Bira, Bunaken)."),
        "Indonesian Wobbegong Shark":species_dict("Orectolobus leptolineatus","Up to 1.2m.","Benthic; ambush predator.","Solitary.","Striking colour pattern of fine vermiculations, with alternating dark brownish bars and saddles. Nasal barbel with branch with 2-3 simple lobes.","Pattern on dorsal Side.","Common - seasonal (Penida), Rare (Bira, Bunaken)."),
        "Spotted Wobbegong Shark":species_dict("Orectolobus maculatus","Up to 1.7m.","Benthic; ambush predator.","Solitary.","Brown with dark saddles and pale irregular circular markings with pale white border. Unbranched barbel in clusters.", "Pattern on dorsal side.","Uncommon - seasonal (Penida), Rare (Bira, Bunaken)."),
        "Coral Catshark":species_dict("Atelomycterus marmoratus","Up to 70cm.","Benthic; Inshore, reef-associated.","Solitary.","Slender body, short head and tail, dorsal fins angled backwards. Numerous black and white spots, which often merge to form horizontal bars. Reclusive in daylight hours.","Spot markings.","Uncommon (Bira), Rare (Penida, Bunaken)."),
        "Tawny Nurse Shark":species_dict("Nebrius ferrugineus","Up to 3.2m.","Benthopelagic and Benthic; rests on bottom.","Solitary or small groups.","Brown to greyish brown without marking. Pair of short nasal barbell. Close-set dorsal fins of nearly same height. Wide face and small eyes.","Wide face. Dorsal fin position.","Rare (Penida, Bira, Bunaken)."),
        "Brownbanded Bamboo Shark":species_dict("Chiloscyllium punctatum","Up to 1.4m.","Benthopelagic and Benthic; rests on bottom.","Solitary.","Brown to greyish brown. May retain hint of juvenile banded pattern. Pectoral and ventral fins forward of dorsal fins. Narrow face.","Narrow face, hint of bands.","Common (Penida), Uncommon (Bira, Bunaken).")
    },
    "Rays":{
        "Oceanic Manta Ray":species_dict("Mobula birostris","Up to 7m.","Outer reef to open ocean.","Mainly solitary or in small groups.","White shoulder patches that form the “T”. Black band between eyes and forebody. Additional dark patches along the trailing edge of individual gill slit.","Spine remnant at base of tail.","Extremely Rare (Penida, Bira, Bunaken)."),
        "Reef Manta Ray":species_dict("Mobula alfredi","Up to 5m, juveniles from 1.5m.","Shallow shelf and reef habitats.","Solitary or in group.","White shoulder patches that form the “Y”. Terminal mouth with cephalic fins. Underside with black spots to be unique pattern of each individual.","Lack of spine remnant.","Very Common (Penida), Rare (Bira, Bunaken)."),
        "Spinetail Devil Ray":species_dict("Mobula mobular","Up to 3.2m.","Outer reef to open ocean.","Can be solitary but commonly in schools.","Dorsal side has wide slightly curving black band between eyes and forebody. Single spines on base of tail.","'Mini manta', cephalic fins.","Uncommon (Penida, Bira, Bunaken).") ,
        "Spotted Eagle Ray":species_dict("Aetobatus ocellatus","Up to 1.5m.","Outer reef to open ocean.","Solitary.","Grey-brown, numerous white spots and white underside. Triangular wings, protruding head. Multiple spines.","Spotted dorsal side.","Common (Penida, Bira, Bunaken)."),
        "Javanese Cownose Ray":species_dict("Rhinoptera javanica","Up to 1.5m.","Outer reef to open ocean.","Solitary.","Brown, white underside. Protruding head, short slender tail. Single spines.","Body shape.","Extremely Rare (Penida, Bira, Bunaken)."),
        "Pink Whipray":species_dict("Pateobatis fai","Up to 1.8m.","Benthic; reef-associated, sand bottoms.","Solitary or form schools. Known to 'piggyback' other ray species.","Light grey to pinkish brown, ocassionally blotched or mottled. Snout blunty pointed. Rounded 'wings' and long tapered tail.","Long tail. No spines along the back (if present - Jenkins Whipray).","Uncommon (Penida, Bira, Bunaken)."),
        "Blue-Spotted Stingray":species_dict("Neotrygon kuhlii","Up to 70cm, commonly 40cm.","Benthic; lagoon and outer slopes.","Solitary or form schools (pancake).","Brown to olive with blue spots and small black spots. Sharply rounded “wing”. Tail marked with white bars, longer than diameter of disc. Mask-like marking around eyes.","Shape, mask-like marking.","Common (Penida), Uncommon (Bira, Bunaken)."),
        "Blue-Spotted Ribbontail Ray":species_dict("Taeniura lymma","Up to 35cm.","Benthic; sand bottoms, under ledges, lagoon and outer slopes.","Solitary or form schools","Yellow-brown with numerous blue spots. Flattened blue ribbon like tail about 1.5 times of disc width. Have 2 spines.","Blue ribbon tail.","Common (Bira, Bunaken), Rare (Penida)."),
        "Marbled Stringray":species_dict("Taeniura meyeni","Up to 3.2m.","Benthic and Benthopelagic; reef-associated.","Solitary.","Grey with variable pattern of dense black spots, blotches. Short tail, about the same length as disc. Single spine.","Shape and dorsal pattern.","Common (Penida, Bira, Bunaken)."),
        "Mangrove Whipray":species_dict("Urogymnus granulates","Up to 1.4m.","Benthic; reef and mangrove-associated.","Solitary.","Dark slate grey with scattered white spots and pale borders on disc. Stingers (usually 2) and white tail behind. Found near mangrove areas.","White tail.","Rare (Penida), Extremely Rare (Bira, Bunaken)."),
        "Broad Cowtail Stingray":species_dict("Pastinachus ater","Up to 2m.","Benthic; marine and brackish; reef-associated.","Solitary or form schools","Large, uniformly dark stingray with a dense band of blunt denticles over the central disc, very broad tail and flattened anteriorly.","Broad tail.","Uncommon (Penida), Rare (Bira, Bunaken)."),
        "Bowmouth Guitarfish":species_dict("Rhina ancylostoma","Up to 3m.","Benthic and Bethopelagic; coastal seas, reef-associated.","Solitary.","Large grey shark-like ray; broad rounded head with body ridges above eyes and along centerline. Large broad-based pectoral fins; white spotting on body and fins.","Body shape.","Extremely Rare (Penida, Bira, Bunaken).")
    },
    "Turtles": {
        "Loggerhead Turtle":species_dict("Caretta caretta","Up to 1.2m, carapace length. ","Coastal reefs, rocky areas and lagoons. ","Solitary. ","Adults have a constant dorsal pattern, easily recognisable by the reddish-brown coloration. Head and neck both large and broad. Fore flippers relatively short and thick, each with 2 visible claws on anterior margin; rear flippers with 2 or 3 claws. ","Fat neck, scutes. ","Rare (Penida, Bira, Bunaken)."),
        "Green Sea Turtle":species_dict("Chelonia mydas","Up to 1.5m carapace length. ","Coastal reefs, rocky areas, sea grass, estuaries and lagoons. ","Solitary. ","Single pair of prefrontal scales. Carapace is bony without ridges and has large, non-overlapping scutes. Flippers with 1 visible claw. ","Scutes. Round head. ","Very Common (Penida, Bira, Bunaken)."),
        "Hawksbill Turtle":species_dict("Eretmochelys imbricata","Up to 1.15m carapace length. ","Coastal reefs, rocky areas and lagoons. ","Solitary. ","Elongated, tapered head ends in a beak-like mouth. Two pairs of prefrontal scales (scales in front of eyes). Carapace is elliptical, bony without ridges, posterior scutes overlap to give a rear margin of its carapace a serrated look. Flippers have 2 claws ","Scutes. Beak-like mouth.","Very Common (Penida, Bira, Bunaken)."),
        "Olive Ridely Turtle":species_dict("Lepidochelys olivacea","Up to 80cm, carapace length. ","Coastal reefs, rocky areas and lagoons. ","Solitary. ","Olive coloured carapace, bony without ridges. Variable and asymmetrical lateral scutes 6 to 8 counts. 12-14 marginal scutes. ","Scutes. ","Rare (Penida, Bira, Bunaken)."),
        "Leatherback Turtle":species_dict("Dermochelys coriacea","Up to 2.4m, carapace length. ","Pelagic; open ocean. ","Solitary. ","Primarily black rubbery skin with pinkish-white underside. The only species that lack scales and a hard shell and are named for their tough rubbery skin. ","Carapace and size. ","Extremely Rare (Penida, Bira, Bunaken).")
    },
    "Grouper": {
        "Brown-Marbled Grouper" : species_dict("Epinephelus fuscoguttatus","Up to 120cm, commonly 50cm. ","Benthopelagic; lagoon pinnacles, channels, and outer reef slopes. ","Solitary. ","Pale yellowish brown with numerous close-set small brown spots of variable intensity. Five vertical series of irregular brown blotches. Small black saddle tail base. Deep bodied. ","Size, distinct robust shape. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Malabar Grouper" : species_dict("Epinephelus malabaricus","Up to 234cm, commonly 100cm. ","Benthopelagic; variety of habitats. ","Solitary. ","Large. Barred or mottled shades of grey to brown to olive with small whitish spots. Covered with numerous small dark spots. ","Size, distinct robust shape. ","Rare (Penida, Bira, Bunaken).") ,
        "Potato Grouper" : species_dict("Epinephelus tukula","Up to 200cm. ","Coastal reefs, lagoons and seaward reefs. ","Solitary. ","Pale greyish. Large round to ovate dark grey or blackish blotches on body. Spoke-like markings radiating from eye. ","Eye markings and size. ","Rare (Penida, Bira, Bunaken).") ,
        "Giant Grouper" : species_dict("Epinephelus lanceolatus","Up to 270cm. ","Coastal reefs, lagoons and outer slopes. ","Solitary. ","Yellowish shades around the tip of fins. Mottled shades of dark grey to dark brown with small whitish spots and blotches. ","Size, distinct robust shape. ","Extremely Rare (Penida, Bira, Bunaken).") ,
        "Speckled Grouper" : species_dict("Epinephelus cyanopodus","Up to 122cm. ","Benthopelagic to pelagic; lagoons and outer reefs over mud, rock or cobble bottom. ","Solitary. ","Pale bluish grey colour. Profuse small black spots on head, body and fins. Juveniles and sub-adults have black margin on tail and black ventral fin tips. ","Bluish colour and spots. ","Rare (Penida, Bira, Bunaken).") ,
        "Blue-and-Yellow Grouper" : species_dict("Epinephelus flavocaeruleus","Up to 90cm, commonly 45cm. ","Bethopelagic; shallow to deeper reefs. ","Solitary. ","Dark bluish violet to dark greyish blue head. Fins and jaws are bright yellow. Yellow colour fades as the fish grows. ","Yellow fins and jaws. ","Uncommon (Penida), Rare (Bira, Bunaken)") ,
        "Black-Saddled Coral Grouper" : species_dict("Plectropomus laevis","Up to 125cm, commonly 85cm. ","Benthopelagic; lagoons and seaward reefs. ","Solitary. ","2 color variations - Pale and Dark, with 3- 5 dark saddles on body and head and scattered dark-edged blue spots. Pale variation - whitish body, yellow fins. Dark variation - grey / olive body, dark fins. ","Saddles on body. ","Rare (Penida, Bira, Bunaken).") ,
        "Leopard Coral Grouper" : species_dict("Plectropomus leopardus","Up to 120cm. ","Benthopelagic; coastal and lagoon reefs. ","Solitary. ","Red, pale grey or olive to dark brown with numerous dark-edged blue spots on head, body (except ventrally) and median fins. Narrow white/blue posterior margin on caudal fin. Blue Ring around eye. ","Blue ring around eye. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Spotted Coral Grouper" : species_dict("Plectropomus maculatus","Up to 125 cm. ","Benthopelagic; silty coastal reefs. ","Solitary. ","Red, pale grey or olive to dark brown. Numerous small blue spots, elongated towards the anterior end. ","Elongated spots. ","Rare (Penida, Bira, Bunaken).") ,
        "Roving Coral Grouper" : species_dict("Plectropomus pessuliferus","Up to 120cm. ","Benthopelagic; lagoons and seaward reefs. ","Solitary.","Brown to orange-red with numerous small, dark-edged blue spots on head, body and fins (only basally on pectorals). Some spots on side of body are vertically elongate. ","Bars/Spots. truncate tail. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Yellow-Edged Lyretail Grouper" : species_dict("Variola louti","Up to 83cm, commonly 60cm. ","Benthopelagic; clear-waters of lagoons and outer reefs. ","Solitary. ","Violet to orange-red to brown with violet to blue spots on head, body and fins. Pectoral, dorsal and anal fins and lyre-shaped tail with yellow margins. ","Yellow margin lyretail. ","Common (Penida, Bira, Bunaken).") ,
        "Dusktail Grouper" : species_dict("Epinephelus bleekeri","Up to 76cm. ","Benthic; silty coastal reef. ","Solitary. ","Whiteish with numerous orange to dark brown spots. Often display several faint dark bars. Last 2/3 of tail purplish and without spots. ","Purplish tail. ","Rare (Penida, Bira) Uncommon (Bunaken)") ,
        "White-Spotted Grouper" : species_dict("Epinephelus coeruleopunctatus","Up to 76cm. ","Benthic; inside or near caves. ","Solitary. ","Brownish grey to charcoal with white spots and scattered, larger whitish blotches. Series of dark blotches along back. Pectoral, anal and convex caudal fins black. ","Black fins, white blotches. ","Rare (Penida, Bira, Bunaken).") ,
        "Orange-Spotted Grouper" : species_dict("Epinephelus coioides","Up to 120cm. ","Benthopelagic; turbid coastal reefs and estuaries. ","Solitary. ","Tan to dark grey-brown with numerous orangish spots on head, body and fins. Four irregular H-shaped dark bars and 3-4 blackish saddles on back. ","Orange spots. black saddles. ","Rare (Penida, Bira, Bunaken).") ,
        "Blacktip Grouper" : species_dict("Epinephelus fasciatus","Up to 40cm. ","Benthic; coastal lagoon and seaward reef. ","Solitary. ","Highly variable from pale to medium greenish gray. Often with 5-6 straight dark bars of variable intensity. ","Dorsal fin, eyes. ","Common (Penida, Bira, Bunaken).") ,
        "Highfin Grouper" : species_dict("Epinephelus maculatus","Up to 60cm. ","Benthic; open sand and base of reefs in coastal, lagoon and outer reefs. ","Solitary. ","Brownish grey to brown covered with dark brown polygonal spots. Pair of prominent white saddles on forehead and middle of dorsal fin/back. ","Prominent first dorsal. ","Rare (Penida, Bira) Uncommon (Bunaken).") ,
        "One-Blotch Grouper" : species_dict("Epinephelus melanostigma","Up to 35cm. ","Benthic; lagoons, reef flats and outward slopes. ","Solitary. ","Bluish white undercolour with closely packed polygonal spots in varying shades of brown; merging spots on back form blotch under mid-dorsal. ","Blotch under mid-dorsal. ","Common (Penida), Uncommon (Bira, Bunaken).") ,
        "Netfin Grouper" : species_dict("Epinephelus miliaris","Up to 53cm. ","Benthic; young inhabit mangroves and seagrass beds, adults move to deeper waters. ","Solitary. ","Undercolor white with irregular grey blotches and covered with closely packed polygonal brown spots. ","Uniform polygonal blotches. ","Rare (Penida, Bira, Bunaken).") ,
        "Camoflague Grouper" : species_dict("Epinephelus polyphekadion","Up to 90cm. ","Benthopelagic; clear oceanic waters. ","Solitary or form schools. ","Silvery grey to brown to nearly black. Black scutes and black edges. Black spot on upper end of gill cover. Concave slope boxy head & big eyes. ","Black scutes & edges. ","Rare (Penida, Bira, Bunaken).") ,
        "Halfmoon Grouper" : species_dict("Epinephelus rivulatus","Up to 45cm. ","Benthic; coastal reefs. ","Solitary. ","Reddish brown body, 5-6 irregular dark brown bars. ","Reddish brown body. ","Common (Penida, Bira, Bunaken).") ,
        "Redmouth Grouper" : species_dict("Aethaloperca rogaa","Up to 60cm. ","Benthopelagic to pelagic; near caves or under ledges in coral rich areas of seaward reefs. ","Solitary. ","Dark gray to black, occasionally with orangish cast. Frequently with pale bar across abdomen. Reddish inside the mouth. ","Oblong body shape. ","Common (Penida, Bira, Bunaken).") ,
        "Slender Grouper" : species_dict("Anyperodon leucogrammicus","Up to 65cm. ","Benthopelagic; coastal and outer reefs. ","Solitary. ","Slender, greenish to brownish grey with red orange spots. Usually with 3-4 pale stripes. ","Slender body shape. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Peacock Grouper" : species_dict("Cephalopholis argus","Up to 60cm, commonly 40cm. ","Benthic to benthopelagic. ","Solitary or form groups of up to 12. ","Brown / green covered with small dark-edged blue spots. Broad blue borders on rear dorsal, anal, pectoral and tail fins. May display 5-6 pale bars on rear body. Can be dark or pale and transition rapidly. ","Starry night appearance. ","Very Common (Penida, Bira, Bunaken).") ,
        "Chocolate Grouper" : species_dict("Cephalopholis boenak","Up to 30cm. ","Benthic; lagoons, reef flats and outward slopes to 10m. ","Solitary. ","Usually display 7-8 dark bars on side. Tail with dark corners edged in blue. Dark spot under upper rear gill cover. ","Dark spot. ","Common (Penida, Bira, Bunaken).") ,
        "Bluelined Grouper" : species_dict("Cephalopholis formosa","Up to 34cm. ","Benthic; dead silty reefs in sheltered waters. ","Solitary. ","Dark brown to yellowish brown with dark blue, primarily horizontal lines on head body and fins. ","Blue stripes. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Coral Grouper" : species_dict("Cephalopholis miniata","Up to 50cm. ","Benthopelagic; coastal and lagoon reefs. ","Solitary. ","Orange-reddish with numerous of dark-edged spots. Narrow blue margin on all fins expect pectorals. Purplish coloration towards posterior. ","Purple posterior colouration. ","Very Common (Penida, Bira, Bunaken).") ,
        "Harlequin Grouper" : species_dict("Cephalopholis polleni","Up to 43cm. ","Benthopelagic; outer caves, steep slopes. ","Solitary. ","Yellow to greenish yellow, bright blue or violet stripes on head, body and fins. ","Violet stripes. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Tomato Grouper" : species_dict("Cephalopholis sonnerati","Up to 57cm. ","Benthopelagic; coastal reefs and sandy areas. ","Solitary. ","Orange to red with dense covering of red spots on head, more scattered to body. Variation with blotchy shades of red-oranges, forming 6-7 bars with scattered white spots on fins. ","Purple posterior colouration. ","Rare (Penida, Bira, Bunaken).") ,
        "Masked Grouper" : species_dict("Gracila albomarginata","Up to 40cm. ","Benthopelagic; outer slopes. ","Solitary. ","Brown head. Large white square on midbody, midlateral row of short narrow dark bars. Dot in pre-caudal area. Subadult: Purple to brown with bright red margins on rear dorsal, anal and tail fins. ","Pre-caudal dot. ","Common (Bira, Bunaken), Uncommon (Penida).") ,
        "Squaretail Coral Grouper" : species_dict("Plectropomus areolatus","Up to 80cm. ","Benthopelagic; coastal and lagoon reefs. ","Solitary. ","Whiteish to pale grey with numerous small dark-edged blue spots on head, body and fins. Dark fins and dark margin on the edge of caudal fin. Often forming saddles (see left below). ","Dark margin on caudal fin. ","Common (Bira, Bunaken), Uncommon (Penida).") ,
        "White-Edged Lyretail Grouper" : species_dict("Variola albimarginata","Up to 65cm. ","Benthopelagic; coastal reefs, lagoons and outer reefs. ","Solitary. ","Brownish orange to pink or red with violet spots on head, body and fins. Lyre-shaped tail with white margin. ","White margin lyretail. ","Common (Penida, Bira, Bunaken).") ,
        "Barramundi" : species_dict("Cromileptes altivelis","Up to 70cm. ","Benthic; inhabit lagoon and seaward reef and are typically found in dead or silty area. ","Solitary. ","Pale greenish white with large widely paced black spots. Concave profile above eyes. ","Unique body shape. ","Extremely Rare (Penida, Bira, Bunaken).")
    },
    "Snapper": {
        "Red Snapper" : species_dict("Lutjanus bohar","Up to 90cm. ","Pelagic; sheltered lagoons and outer reefs. ","Either solitary or form groups. ","Red to reddish grey. Dark reddish fins, notably upper edge of pectoral fins. Pronounced groove in front of eyes. Juveniles and small adults have 1/2 silvery-white spots on back. ","Groove before eyes. ","Very Common (Penida, Bira, Bunaken).") ,
        "Blubberlip Snapper" : species_dict("Lutjanus rivulatus","Up to 80cm, commonly 60cm. ","Bethopelagic; near shore and outer reefs. ","Solitary or form small groups. ","Greyish green with wavy yellow lines on head. Yellow fins and outer edge of tail. Slightly upturned snout with large mouth. ","Size and 'lips'. ","Common (Penida, Bira, Bunaken).") ,
        "Red Emperor Snapper" : species_dict("Lutjanus sebae","Up to 80cm. ","Benthopelagic; sandy bottom and reef. ","Solitary. ","Red to reddish grey. Subadult with band from lip nape. Juveniles and small adults have 1/2 silvery-white spots on back. ","Band from lip nape. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Chinamanfish" : species_dict("Symphorus nematophorus","Up to 100cm. ","Benthopelagic; coastal reefs. ","Solitary or form large schools. ","Reddish to yellowish with faint to distinct irregular bars. Numerous faint bluish stripes on head and body. Occasionally filaments extend from upper rear of dorsal fins. Pronounced groove in front of eyes. ","Dorsal fin shape. ","Rare (Penida, Bira, Bunaken).") ,
        "Green Jobfish" : species_dict("Aprion virescens","Up to 112cm, commonly 90cm. ","Pelagic and Benthopelagic; lagoons, reef passes or outer slopes. ","Usually solitary. ","Dark green to bluish grey. Slender cylindrical body with strongly forked tail. Pectoral fins short. No distinctive markings. ","Looks exactly like the photo. ","Common (Penida, Bira, Bunaken).") ,
        "Mangrove Snapper" : species_dict("Lutjanus argentimacuatus","Up to 150cm. ","Benthopelagic; mangroves, estuarine to steep outer reef. ","Solitary or form loose groups. ","Grey with tints of red, green and brown. Darkish fins and scale centers. No groove in front of eye. ","No groove before eyes. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Checkered Snapper" : species_dict("Lutjanus decussatus","Up to 35cm. ","Bethopelagic; coastal reefs, lagoons and outer slopes. ","Solitary or form small groups. ","White with six brown stripes on body. Five or six bars across back forming netted pattern on upper body. Black spot on base of caudal fin. ","Netted pattern and spot. ","Common (Penida, Bira, Bunaken).") ,
        "Blackspot Snapper" : species_dict("Lutjanus ehrenbergii","Up to 35cm. ","Benthopelagic; coastal reefs and estuaries. ","Form groups. ","Large round black spot on lateral line below 2nd dorsal fin. Five thin yellow stripes below lateral line. ","Dot and stripes. ","Common (Bira, Bunaken), Uncommon (Penida).") ,
        "Longspot Snapper" : species_dict("Lutjanus fulviflamma","Up to 35cm. ","Benthopelagic; coastal reef to outer slope. ","Form groups. ","Long oval to rectangular spot on lateral line below dorsal. Bold yellow stripes of equal width below lateral line. ","'Long' spot. ","Common (Penida, Bira, Bunaken).") ,
        "Blacktail Snapper" : species_dict("Lutjanus fulvus","Up to 40cm. ","Benthopelagic; lagoons, passages and outer reef slopes. ","Solitary or loose aggreation. ","Silvery white to yellow with dark tail. Dark dorsal fin. Yellow pectoral, ventral and anal fins. ","Black tail. ","Common (Penida, Bira, Bunaken).") ,
        "Humpback Snapper" : species_dict("Lutjanus gibbus","Up to 50cm, commonly 45cm. ","Benthopelagic; lagoons, passages and outer reef slopes. ","Solitary or form schools. ","Greyish red to red and sometimes with a yellow tinge. Maroon forked tail with rounded lobes. Orange around base of pectoral fin. Concave slope above eye and hump on forehead ","Slope of the head. ","Very Common (Penida, Bira, Bunaken).") ,
        "Bluestripe Snapper" : species_dict("Lutjanus kasmira","Up to 40cm. ","Benthopelagic; coastal reefs to outer slopes. ","Form groups. ","Yellow upper body with four blue stripes. White belly with thin grey to yellow stripes. ","Four blue stripes. ","Common (Penida, Bira, Bunaken).") ,
        "Big Eye Snapper" : species_dict("Lutjanus lutjanus","Up to 35cm. ","Bethopelagic; coastal reefs to outer slopes. ","Form groups. ","Yellow upper body with four blue stripes. Wavy diagonal line on back above lateral line (to differ with yellowfin snapper). ","Wavy line on back. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Onespot Snapper" : species_dict("Lutjanus monostigma","Up to 60cm, commonly 50cm. ","Benthopelagic; outer reef areas. ","Solitary or form small groups. ","Adults grey or yellowish grey to brown with yellow fins. May display a horizontally elongate black spot on rear. ","Plain other than the spot. ","Common (Penida, Bira, Bunaken).") ,
        "Brownstripe Snapper" : species_dict("Lutjanus vitta","Up to 35cm. ","Benthopelagic; coastal to offshore reefs. ","Solitary or form groups. ","Yellow to brown or black stripe from eye to base of caudal fin. Diagonal brownish lines above lateral line. ","Line through eye. ","Common (Penida, Bira, Bunaken).") ,
        "Yellowfin Snapper" : species_dict("Lutjanus xanthopinnis","Up to 30cm. ","Benthopelagic; coastal reef and outer slope. ","Form groups. ","Silver body with thin yellow stripe from eye to caudal fin. Nearly straight diagonal lines on back above lateral line. ","Stripes and lines. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Midnight Snapper" : species_dict("Macolor macularis","Up to 60cm. ","Pelagic; edge of steep slopes of lagoons, passes and outer reefs. ","Solitary or form groups. ","Black with pale line markings in scales. Blue line and spot markings on head. Large eye with bright gold iris. ","Golden eye, faint markings. ","Common (Penida, Bira, Bunaken).") ,
        "Black Snapper" : species_dict("Macolor niger","Up to 75cm, commonly 40cm. ","Pelagic; steep slopes of lagoons, passes and outer reefs. ","Solitary or form schools. ","Grey to grey-brown with numerous indistinct blotches. No blue lines or spots on head. Large eye with dull gold iris. ","Rounder head than midnight. ","Common (Penida, Bira, Bunaken).") ,
        "Smalltooth Jobfish" : species_dict("Aphareus furca","Up to 70cm, commonly 40cm. ","Pelagic and Benthopelagic; inshore coral and rocky reefs and in clear waters of lagoons. ","Solitary or in small groups. ","Blue-grey coloration. Slender body with large mouth and strongly forked tail. Long pectoral fins. Dark outline on rear edge and bar on gill cover. ","Downturned mouth. ","Common (Penida, Bira, Bunaken).") ,
        "Pinjalo Snapper" : species_dict("Pinjalo pinjalo","Up to 80cm. ","Benthopelagic; costal reefs and outer slopes. "," Form schools. ","Variable shades from reddish gray to red that can quickly intensify or pale. Yellow ventral fins. ","Body, yellow ventral fins. ","Rare (Penida, Bira, Bunaken).") ,
        "Slender Pinjalo" : species_dict("Pinjalo lewisi","Up to 50cm. ","Benthopelagic; costal reefs and outer slopes. ","Form schools. ","Variable shades from greyish red to bright red. No ventral yellow fins. ","Similar to Pinjalo Snapper, distinguished by no yellow ventral fins. ","Rare (Penida, Bira, Bunaken).")
    },
    "Emperors": {
        "Yellowtail Emperor" : species_dict("Lethrinus atkinsoni","Up to 50cm. ","Benthopelagic; sand, rubble, seagrass area adjacent to coral reefs. ","Solitary or form small groups. ","Blue grey to yellowish tan. Yellow caudal fin. Variation displaying yellowish head, broad yellow midlateral stripe on side. ","Yellow caudal fin. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Yellowfin Emperor" : species_dict("Lethrinus erythracanthus","Up to 70cm. ","Benthopelagic; deep lagoons and outer reef slopes. ","Solitary or form small groups. ","Dark bluish head and dark gray body with yellow or occasionally reddish fin. Easily distinguished from most emperor by large size. ","Size, yellow/red fins. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Longfin Emperor" : species_dict("Lethrinus erythropterus","Up to 50cm. ","Benthopelagic; coastal reefs, lagoons and outer slopes. ","Solitary or form small groups. ","Red to yellow brown, often with faint bars. Red fins, pair of pale to bright white bars on base of caudal fins. ","Pale white bars. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Thumbprint Emperor" : species_dict("Lethrinus harak","Up to 50cm. ","Benthopelagic; sand and rubbles ares of coastal reefs, lagoons and outer slopes. ","Solitary or form small groups. ","Pale grey. Dark elongate blotch on middle of side (thumbprint-like). ","Thumprint. ","Common (Penida, Bira, Bunaken).") ,
        "Pinkear Emperor" : species_dict("Lethrinus lenjan","Up to 50cm. ","Benthopelagic; sand and rubbles ares of coastal reefs, lagoons and outer slopes. ","Solitary or form small groups. ","Bright red streak on rear edge of gill cover. Pale silvery grey. ","Bright red streak. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Smalltooth Emperor" : species_dict("Lethrinus microdon","Up to 70cm. ","Benthopelagic; coastal reefs, lagoons and outer slopes. ","Solitary or form groups. ","Long pointed snout. Silvery grey. Dark streaks radiate from fore lower quarter of eye. ","Dark streaks around eye. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Spangled Emperor" : species_dict("Lethrinus nebulosus","Up to 80cm. ","Benthopelagic; flat sand bottoms close to reefs; Seagrass beds and mangrove areas. ","Solitary to large groups. ","Elongate pointed snout. Pale grey with blue to white scale centers. Blue streak on cheek. ","Blue streak on cheek. ","Common (Penida, Bira), Rare (Bunaken).") ,
        "Orange-Striped Emperor" : species_dict("Lethrinus obsoletus","Up to 50cm. ","Benthopelagic; sand and rubbles ares of coastal reefs, lagoons and outer slopes. ","Solitary or form small group. ","Pale gray. Yellow-Orange stripe from base of pectoral fin to tail. ","Orange stripe. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Longface Emperor" : species_dict("Lethrinus olivaceus","Up to 100cm, commonly 70cm. ","Benthopelagic; sand bottoms of lagoons and outer slopes. ","Solitary or form schools. ","Elongate body with long pointed snout. Grey to olive with no distinct markings; often display mottled pattern (see insert). Highly active and fast swimming. ","Elongated face. ","Common (Penida, Bira, Bunaken).") ,
        "Ornate Emperor" : species_dict("Lethrinus ornatus","Up to 45cm. ","Benthopelagic; seagrass beds, sand and rubble area of coastal reefs and lagoons. ","Solitary or form small groups. ","Narrow red bar on cheek and gill cover. Four to five broad yellowish stripes on sides. ","Narrow red bar on cheek. ","Common (Penida, Bira, Bunaken).") ,
        "Spotcheek Emperor" : species_dict("Lethrinus rubrioperculatus","Up to 50cm. ","Benthopelagic; sand, rubbles bottoms of coastal reefs and outer slopes. ","Solitary or form small group. ","Diffuse stripe and bar marking on lower body, making white blotch pattern. Red dot on upper of the gill cover. Pale silvery grey. ","Spot on cheek. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Yellowlip Emperor" : species_dict("Lethrinus xanthochilus","Up to 70cm. ","Benthopelagic; sand or rubble bottoms. ","Elongate body, unmarked silvery pale grey to olive, also mottled and blotched pattern. Yellow upper lip. Yellow to orange spot on base of pectoral fin. ","Solitary or form small groups. ","Face shape, yellow upper lip. ","Common (Penida), Uncommon (Bira, Bunaken).") ,
        "Humpnose Bigeye Bream" : species_dict("Monotaxis grandoculis","Up to 60cm, commonly 40cm. ","Benthopelagic; found in sand and rubble areas near coral reefs. ","Solitary or form groups. ","Black to grey, silver or brown back gradating to pale underside, often yellowish tints on head and lips. Black spot on base of pectoral fin. May display four broad dark bars on body. ","Big eye and roundish face. ","Common (Penida, Bira, Bunaken).")
    },
    "Parrotfish": {
        "Bumphead Parrotfish" : species_dict("Bolbometopon muricatum","Up to 130cm; commonly 70cm. ","Benthopelagic; reef-associated. ","Solitary or form schools. ","Bump on forehead of adult. Deep body. The primary phase is a dull gray with scattered white spots, gradually becoming uniformly dark green. ","Bumphead and beak. ","Common (Bira, Bunaken), Rare (Penida).") ,
        "Bleeker's Parrotfish" : species_dict("Chlorurus bleekeri","Up to 49cm. ","Benthopelagic; reef-associated. ","Females (small groups), males (solitary). ","TP - Green with pink to lavender scale edges; large pale yellowish to greenish patch on cheek with green border, dark green margin on tail. IP - Dark brown with 3-4 faint pale whitish bars. ","Patch on cheek. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Steephead Parrotfish" : species_dict("Chlorurus microrhinos","Up to 70cm. ","Benthopelagic; sheltered reefs. ","TP - Blunt forehead profile; shades of green to blue-green with lavender-pink scale edges. Pale lower head. Can also be reddish in TP. IP - Black-dark brown with 3-4 yellow to pale stripes. ","Solitary. ","Blunt forehead profile. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Bridled Parrotfish" : species_dict("Scarus frenatus","Up to 47cm. ","Benthopelagic; seaward slopes, reef crests. ","Usually solitary. ","TP - Shades of green, abrubt transition from dark to light green on tail base; pale green bands around mouth. IP - Grey to red with broad blackish stripes on sides; dorsal, anal and ventral fins can be bright red. ","Dark to light green tail base. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Blue-Barred Parrotfish" : species_dict("Scarus ghobban","Up to 49cm. ","Benthopelagic; inshore reefs, sand/rubble. ","Solitary. ","TP - Yellow to yellowish brown underfloor with large blue-green scale markings; blue-green band markings around mouth and tail borders. IP - Yellow-brown with 4-5 diffuse blue bars on side. ","Blue-green scale markings. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Redlip Parrotfish" : species_dict("Scarus rubroviolaceus","Up to 70cm. ","Benthopelagic; outer reef slopes. ","Solitary or in pairs. ","TP - Shades of green, often bicolour with darker forebody; double bands on chin, numerous blue-green stripes on tail. IP - Shades of reddish brown with small black spots and irregular lines on scales,often bicolour with darker forebody, fins and usually red lips. ","None","Uncommon (Penida, Bira, Bunaken).") ,
        "Red Parrotfish" : species_dict("Scarus xanthopleura","Up to 54cm. ","Benthopelagic; lagoons and seaward reefs. ","Solitary. ","TP - Green with pink scale margins; dark green lips; irregular dark green patch on lower cheek and chin. faint banding or spotting on head. IP - Bright red with 3-4 faint pale bars on side. Rare. ","None","Uncommon (Penida, Bira, Bunaken).") ,
        "Tricolor Parrotfish" : species_dict("Scarus tricolor","Up to 55cm. ","Benthopelagic; outer slopes. ","Solitary. ","TP - Shades of green, often with strong tints of pink or yellow on sides. Long pointed lobes of tail lavender-pink with dark margins. IP - Dark gray to blackish head, red tail, yellow-orange anal fin, dusky orange ventral fins. ","None","Common (Penida, Bira, Bunaken).")
    },
    "Jacks & Trevally": {
        "Giant Trevally" : species_dict("Caranx ignobilis","Up to 170cm, commonly 100cm. ","Pelagic; coastal and oceanic. ","Solitary or form schools. ","Silvery with numerous scattered small black spots, can also be black/dark grey with silvery spots. Small black area on upper base of pectoral fin. Steep forehead profile. ","Size, distinct robust shape. ","Common (Penida, Bira), Rare (Bunaken).") ,
        "Black Jack" : species_dict("Caranx lugubris","Up to 100cm. ","Benthopelagic; clear oceanic waters. ","Solitary or form schools. ","Silvery grey to brown to nearly black. Black scutes and black edges. Black spot on upper end of gill cover. Concave slope boxy head & big eyes. ","Black scutes & edges. ","Rare (Penida, Bira, Bunaken).") ,
        "Bluefin Trevally" : species_dict("Caranx melampygus","Up to 117cm, commonly 60cm. ","Pelagic and Benthopelagic; coastal and oceanic. ","Solitary or form small schools. Also hunts with other species, eg. groupers, eels. ","Iridescent silvery blue to dark green with dense spotting on upper body. Sloped forehead profile. Blue fins. ","Electric blue fins. ","Common (Penida, Bira, Bunaken).") ,
        "Bigeye Trevally" : species_dict("Caranx sexfasciatus","Up to 120cm. ","Pelagic; clear outer reefs. ","Form large schools ","Silver color - Males turn black when courting. Small black spot on upper end of gill cover. White tip on fore lobe of rear dorsal fin. Relatively large eye and mouth. ","White-tipped second dorsal. ","Rare (Penida, Bira, Bunaken).") ,
        "Gold-Spotted Trevally" : species_dict("Carangoides fulvoguttatus","Up to 120cm. ","Pelagic; lagoons and outer slopes. ","Solitary or form school. ","Silvery with many small golden or brassy spots. Often with five faint darkish bars. Adults have four or five dark blotches along the side. ","Golden bars. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Bludger Trevally" : species_dict("Carangoides gymnostethus","Up to 90cm. ","Pelagic; sheltered coasts and deeper offshore reefs. ","Solitary, juveniles form schools. ","Blunt shape of the snout. Body shape is more oval, do not have breast scales. ","Snout shape. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Rainbow Runner" : species_dict("Elagatis bipinnulata","Up to 120cm, commonly 90cm. ","Pelagic; oceanic and coastal waters. ","May form large schools. ","Elongated body shape. Two bright blue stripes with a yellow margin in the middle, hence the 'rainbow'. Large caudal fin. ","Two stripes. ","Rare (Penida), Common (Bira, Bunaken).") ,
        "Almaco Amberjack" : species_dict("Seriola rivoliana","Up to 120cm. ","Pelagic; occasionally over reefs. ","Form schools. ","Silvery; high back profile. Dark band runs from lip across eye to front of first dorsal fin. ","Body shape and eye band. ","Rare (Penida, Bira, Bunaken).") ,
        "African Pompano" : species_dict("Alectis ciliaris","Up to 150cm, subadult up to 90 cm. ","Pelagic; near dropoffs. ","Young form schools, large adults solitary. ","Silver, often with bluish or greenish tints. Scales not obvious. Subadult - Front lobes of dorsal and anal fins trail long filamentous rays (see insert photo). ","Smooth appearance. ","Uncommon (Penida), Rare (Bira, Bunaken).") ,
        "Orange-Spotted Trevally" : species_dict("Carangoides bajad","Up to 55cm. ","Pelagic; coastal reefs and outer slopes. ","Solitary or form large schools. ","Brassy silver to yellow-orange. Orange spots on side. Variation - Silver head and body with scattered orange spots on side. ","Orange spots. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Blue Trevally" : species_dict("Carangoides ferdau","Up to 70cm. ","Pelagic; near reefs and lagoons. ","Solitary or form small schools. ","Silvery, rear dorsal, anal and caudal fin tinted yellowish green, usually display five to seven bars. Bars more pronounced in juveniles. ","Vertical bars. ","Common (Penida), Uncommon (Bira, Bunaken).") ,
        "Barcheek Trevally" : species_dict("Carangoides plagiotaenia","Up to 50cm. ","Benthopelagic; around reef slopes. ","Solitary or form small schools. ","Silvery, narrow dark bar on gill cover. ","Narrow dark bar. ","Common (Bunaken), Uncommon (Penida, Bira).") ,
        "Brassy Trevally" : species_dict("Caranx papuensis","Up to 88cm. ","Pelagic; lagoon, seaward reef. ","Solitary or form schools. ","Lower caudal fin lobe yellowish with white margin. Dark speckles above laterl line. White spot above gill. ","White spot above gill. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Longraked Trevally" : species_dict("Ulua mentalis","Up to 100cm. ","Benthopelagic; shallow coastal waters. ","Form schools. ","Dusky to blackish 1st dorsal. Large protruding under-jaw. ","Dusky dorsal. ","Rare (Penida, Bira, Bunaken).") ,
        "Double-Spotted Queenfish" : species_dict("Scomberoides lysan","Up to 110cm. ","Benthopelagic; coastal reefs, lagoons and outer slopes. ","Solitary or form small schools. ","Silver with double row of 6-8 dusky round blotches on side; black spot fore lobe of rear dorsal fin. Often dark to black dorsal. ","Dark dorsal and spots. ","Common (Penida), Uncommon (Bira, Bunaken).")
    },
    "Tuna & Mackerel": {
        "Dogtooth Tuna" : species_dict("Gymnosarda unicolor","Up to 200cm ","Pelagic; deeper lagoons, passes and outer reef slopes. ","Solitary or in small groups ","Silvery. Pale tips on rear dorsal and anal fins. Single lateral line. ","Pale tips (2nd dorsal/anal). ","Common (Penida, Bira, Bunaken).") ,
        "Yellowfin Tuna" : species_dict("Thunnus albacares","Up to 240cm, commonly 150cm. ","Pelagic; Open water and reef drop-offs. ","Form large schools. ","Very long 2nd dorsal and anal fins; long pectoral fin. Black metallic dark blue color on back, yellow to silver on belly. Yellow 2nd dorsal, anal fins and finlet. Deep bodied. ","Long yellow fins. ","Extremely Rare (Penida, Bira, Bunaken).") ,
        "Wahoo" : species_dict("Acanthocybium solandri","Up to 210cm. ","Pelagic. "," Solitary or in small groups. ","Silvery. Elongate pointed snout. May display wavy bars on body. ","Elongate body shape. ","Extremely Rare (Penida, Bira, Bunaken).") ,
        "Narrow-Barred Spanish Mackerel" : species_dict("Scomberomorus commerson","Up to 240cm, commonly 120cm. ","Pelagic; outer reefs. ","Solitary. ","Silvery. Display numerous thin, wavy bars on body. Whitish 2nd dorsal and anal fins. ","Clear narrow bars. ","Uncommon (Penida, Bira, Bunaken).") ,
        "Double-Lined Mackerel" : species_dict("Grammatorcynus bilineatus","Up to 100cm. ","Pelagic; lagoon, outer reefs, drop-offs and pinnacles. ","Solitary or form schools. ","Silvery. Double lateral line; one on upper side, one on lower side. ","Double lateral lines. ","Common (Penida, Bira, Bunaken).") ,
        "Slingjaw Mackerel" : species_dict("Rastreliger kanagurta","Up to 42cm. ","Benthopelagic; coastal, lagoons and seaward reefs. "," Form schools. ","Silvery, faint spotting on upper back with arrow stripes below. Black spot under pectoral fins. Often seen with widely opened mouth feeding on plankton whilst swimming. ","Open mouth feeding. ","Uncommon (Penida, Bira, Bunaken).")
    },
    "Barracuda": {
        "Great Barracuda" : species_dict("Sphyraena barracuda","Up to 200cm. ","Pelagic; reefs and relatively shallow water. ","Solitary or form small groups. ","Silvery, with few scattered dark blotches. Can display barred or mottled pattern. ","Blotches, solitary nature. ","Common (Penida, Bira, Bunaken).") ,
        "Pickhandle Barracuda" : species_dict("Sphyraena jello","Up to 150cm. ","Pelagic and Bethopelagic; coastal, lagoons and outer reef slopes. ","Small or large schools. ","Silvery with yellowish tail. About 20 oblique bars on upper half of body. ","Yellowish tail. ","Rare (Penida, Bira, Bunaken).") ,
        "Chevron Barracuda" : species_dict("Sphyraena qenie","Up to 170cm, commonly 80cm. ","Pelagic and Bethopelagic; seaward reefs. ","Form large schools. ","Silvery with dusky to dark tail with dark margin. 18-22 chevron-shaped dark markings on sides. ","Dark tail with dark margin. ","Rare (Penida, Bira, Bunaken).") ,
        "Yellowtail Barracuda" : species_dict("Sphyraena flavicauda","Up to 60cm. ","Pelagic and Bethopelagic; coastal reefs, lagoons and outer reefs. ","Form schools. ","Silvery, yellowish to yellow tail. Possible pair of diffuse brownish stripes on side. May display short blackish bars on upper back. ","Yellow caudal fin in schools. ","Rare (Penida, Bira, Bunaken).") ,
        "Bigeye Barracuda" : species_dict("Sphyraena forsteri","Up to 75cm. ","Pelagic and Bethopelagic; reefs and outer slopes. ","Form schools. ","Silvery, median fins dusky. Blackish blotch behind base of pectoral fin. White tips on 2nd dorsal and anal fins. Large eyes for body size. ","All eyes, no barracuda! ","Common (Penida, Bira, Bunaken).")
    },
    "Species of Interest": {
        "Napoleon Wrasse" : species_dict_int("Cheilinus undulatus","Up to 229cm. ","Benthopelagic; slopes and lagoons. ","Solitary or in pairs (male, female). ","Terminal Phase (TP): Blue head with maze-like markings, pronounced hump above eyes. Initial Phase (IP): Olive to bluish/greenish grey body, dark diagonal streaks extend from lower eye. ","Dorsal / caudal fin shape. ","Common (Penida, Bunaken, Bira). ","Endangered fish, trophy catch.") ,
        "Bumphead Parrotfish" : species_dict_int("Bolbometopon muricatum","Up to 130cm; commonly 70cm. ","Benthopelagic; reef-associated. ","Solitary or form schools. ","Bump on forehead of adult. Deep body. The primary phase is a dull gray with scattered white spots, gradually becoming uniformly dark green. ","Bumphead and beak. ","Common (Bira, Bunaken), Rare (Penida). ","Vulnerable fish, trophy catch.") ,
        "Bumphead Mola" : species_dict_int("Mola alexandrini","Up to 300cm. ","Pelagic; Coastal and oceanic. ","Solitary, congregate at cleaning stations. ","Rounded clavus, dinner plate with wings. ","It's a mola! ","Common (Penida), Rare (Bira, Bunaken). ","Charismatic 'iconic' species, economically important for Penida (tourism).") ,
        "Java Rabbitfish" : species_dict_int("Siganus javus","Up to 53cm. ","Benthopelagic; coastal reefs and mangroves. ","Solitary or form small schools. ","Pale grey with numerous bluish white spots, yellowish head, dorsal and anal fins; large black blotch on tail. ","Body shape, black tail blotch. ","Common (Penida, Bira, Bunaken). ","Known local consumption.") ,
        "Oriental Sweetlips" : species_dict_int("Plectorhinchus vittatus","Up to 72cm. ","Benthopelagic; coastal reefs and lagoons. ","Solitary or small schools. ","White with black stripes, lips and fins yellow; spotted dorsal, anal and tail fins. ","Stripes/spots combination. ","Uncommon (Penida, Bira, Bunaken). ","Known local consumption.") ,
        "Topsail Drummer Chub" : species_dict_int("Kyphosus cinerascens","Up to 51cm. ","Benthopelagic; rocky shores, reef flats, lagoons and outer reefs. ","Form small to large schools. ","Silvery grey with thin dark horizontal lines on side; rear dorsal fin distinctly elevated (higher than tallest dorsal spines). ","Elevated rear dorsal fin. ","Common (Penida, Bira, Bunaken). ","Known local consumption.") ,
        "Giant Moray Eel" : species_dict_int("Gymnothorax javanicus","Up to 300cm. ","Benthic; inhabit reef holes of lagoon and outer reefs. ","Solitary. ","Brown with irregular dark brown spots on head, body and fins. Black blotch on gill opening. ","Black blotch on gill opening. ","Common (Penida, Bira, Bunaken). ","High trophic level.") ,
        "Honeycomb Moray Eel" : species_dict_int("Gymnothorax favagineus","Up to 300cm. ","Benthic; inhabit reef holes of lagoon and outer reefs. ","Solitary. ","White to yellow with black leopard-like spots that form honeycomb pattern. ","Honeycomb pattern. ","Uncommon (Penida, Bira, Bunaken). ","High trophic level.") ,
        "Big Blue Octopus" : species_dict_int("Octopus cyanea","Up to 22cm, arms extend to 80cm. ","Benthic; inhabit reef holes. ","Solitary or in pairs. ","Typically brown in colour but have the ability to rapidly change color and skin texture. Dark brown coloring on the tips of their arms along with 2 rows of lighter spots. ","Large day octopus. ","Common (Penida, Bira, Bunaken). ","Known local consumption.") ,
        "Broadclub Cuttlefish" : species_dict_int("Sepia latimanus","Up to 50cm. ","Benthopelagic; reef-associated. ","Solitary. ","Commonly light brown or yellowish with white mottled markings, ability to rapidly change markings. ","Large cuttlefish species. ","Uncommon (Penida, Bira, Bunaken). ","Known local consumption.") ,
        "Bigfin Reef Squid" : species_dict_int("Sepioteuthis lessoniana","Up to 36cm. ","Benthopelagic; reef-associated. ","Solitary or form small groups. ","Long and sturdy tentacles. Fin very long and flat covering mantle. Translucent body that change colour with the environment. ","Long fin. ","Uncommon (Penida, Bira, Bunaken). ","Known local consumption.") ,
        "Triton Trumpetshell" : species_dict_int("Charonia tritonis","Up to 50cm. ","Benthic; shallow reefs and sand areas. ","Solitary. ","Distinctive shell, pointed spire and a large body whorl. Exterior creamy with darker brown dashes and chevrons. Aperture large, orange, and with banded lip. ","Distinctive shell. ","Rare (Penida, Bira, Bunaken). ","Crown-of-thorns predator.") ,
        "Crown-of-Thorns Starfish" : species_dict_int("Acanthaster planci","Up to 80cm. ","Benthic. ","Solitary or form aggregations. ","Between 8 and 21 arms radiating from central disc. Colour variable. Large venomous spines. Often hides in the reef during daylight hours. ","Horrible spines! ","Rare (Penida), Common (Bira, Bunaken). ","Voracious coral predator, can damage reefs.") ,
        "Ornate Spiny Lobster" : species_dict_int("Panulirus ornatus","Up to 50cm. ","Benthic; coral reefs, sand/mud substrates. ","Solitary or form small groups. ","Bluish green, with a white spot on each of the spurs which project from the abdomen (two spurs on each abdominal segment). ","Colourful appearance. ","Uncommon (Penida, Bira, Bunaken). ","Known local consumption.") ,
        "Short-Finned Pilot Whale" : species_dict_int("Globicephala macrorhynchus","Up to 610cm. ","Pelagic; deep offshore areas. ","Form pods, rarely solitary. ","Round head, small beak, up-curved mouthline. Dark gray to black colour with lighter colored patch on the ventral surface. Small black area on upper base of pectoral fin. Steep forehead profile. ","Round head. ","Rare (Penida, Bira, Bunaken). ","High trophic level.") ,
        "Common Bottlenose Dolphin" : species_dict_int("Tursiops truncatus","Up to 380cm. ","Pelagic; coastal waters. ","Form pods, rarely solitary. ","Dark to light grey back that fades to white on underside; dark stripe from eye to flipper. Dorsal fin is tall and backward-curving. Short, well-defined snout or beak. ","Short snout. ","Uncommon (Penida, Bira, Bunaken).", "Dope AF") ,
        "Spinner Dolphin" : species_dict_int("Stenella longirostris","Up to 240cm. ","Pelagic; coastal waters, islands or banks. ","Form pods, rarely solitary. ","Slim build, elongated rostrum. Tripartite colour pattern; dorsal dark grey, sides light grey, underside pale grey. ","Slim build, elongated rostrum. ","Uncommon (Penida, Bira, Bunaken). ","High trophic level.") 
    }
    
}
