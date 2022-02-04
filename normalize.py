from pprint import pprint

main2alts = {
    "California Institute of Technology (Caltech)": [
        "California Institute of Technology",
    ],
    "ETH Zurich": ["ETH Zurich - Swiss Federal Institute of Technology"],
    "Karlsruhe Institute of Technology (KIT)": [
        "KIT, Karlsruhe Institute of Technology",
        "Karlsruhe Institute of Technology",
    ],
    "King Abdulaziz University (KAU)": ["King Abdulaziz University",],
    "Korea Advanced Institute of Science and Technology (KAIST)": [
        "Korea Advanced Institute of Science and Technology",
        "KAIST - Korea Advanced Institute of Science & Technology",
    ],
    "Ludwig Maximilian University of Munich (LMU)": [
        "LMU Munich",
        "Ludwig-Maximilians-Universität München",
    ],
    "Massachusetts Institute of Technology (MIT)": [
        "Massachusetts Institute of Technology",
    ],
    "Nanyang Technological University (NTU)": [
        "Nanyang Technological University",
        "Nanyang Technological University, Singapore",
        "Nanyang Technological University, Singapore (NTU)",
    ],
    "National University of Singapore (NUS)": ["National University of Singapore",],
    "New York University (NYU)": ["New York University",],
    "Paris Sciences et Lettres (PSL University)": [
        "Paris Sciences et Lettres – PSL Research University Paris",
        "PSL University",
        "Université PSL",
    ],
    "Penn State": ["Penn State (Main campus)",],
    "Purdue University": ["Purdue University - West Lafayette",],
    "Swiss Federal Institute of Technology Lausanne (EPFL)": [
        "Swiss Federal Institute of Technology Lausanne",
        "EPFL",
        "École Polytechnique Fédérale de Lausanne",
    ],
    "TU Wien": ["Technische Universität Wien",],
    "Technical University of Berlin": ["Technische Universität Berlin (TU Berlin)",],
    "Chinese University of Hong Kong (CUHK)": [
        "Chinese University of Hong Kong",
    ],
    "University of New South Wales (UNSW Sydney)": [
        "University of New South Wales",
        "UNSW Sydney",
    ],
    "Tokyo Institute of Technology (Tokyo Tech)": ["Tokyo Institute of Technology"],
    "University College London (UCL)": ["University College London", "UCL",],
    "Universidad Nacional Autónoma de México (UNAM)": [
        "Universidad Nacional Autónoma de México  (UNAM)",
    ],
    "University of California, Berkeley": ["University of California, Berkeley (UCB)",],
    "University of California, Los Angeles (UCLA)": [
        "University of California, Los Angeles",
    ],
    "University of California, San Diego (UCSD)": [
        "University of California, San Diego",
    ],
    "University of Massachusetts (UMass)": [
        "University of Massachusetts",
        "University of Massachusetts Amherst",
    ],
    "University of North Carolina at Chapel Hill": [
        "University of North Carolina, Chapel Hill",
    ],
    "University of Wisconsin–Madison": [
        "University of Wisconsin - Madison",
        "University of Wisconsin-Madison",
    ],
    "Paris-Saclay University": ["Université Paris-Saclay",],
    "Université catholique de Louvain (UCL)": [
        "Université catholique de Louvain (UCLouvain)",
    ],
    "University of Montreal": ["Université de Montréal",],
    "Georgia Institute of Technology (Georgia Tech)": ["Georgia Institute of Technology",],
}

alt2main = dict()

for main, alts in main2alts.items():
    for alt in alts:
        alt2main[alt] = main

#pprint(alt2main)