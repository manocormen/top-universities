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
    "Pennsylvania State University": [
        "Penn State",
        "Penn State (Main campus)",
    ],
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
    "Humboldt University of Berlin": [
        "Humboldt-Universität zu Berlin",
    ],
    "King's College London": [
        "King’s College London",
    ],
    "Moscow Institute of Physics and Technology (MIPT)": [
        "Moscow Institute of Physics and Technology (MIPT / Moscow Phystech)",
    ],
    "Ohio State University": [
        "Ohio State University - Columbus",
    ],
    "University of Bonn": [
        "Rheinische Friedrich-Wilhelms-Universität Bonn",
    ],
    "University of Paris": [
        "Université de Paris",
    ],
    "Rutgers University": [
        "Rutgers, The State University of New Jersey - New Brunswick",
    ],
}

alt2main = dict()

for main, alts in main2alts.items():
    for alt in alts:
        alt2main[alt] = main

#pprint(alt2main)

main2id = {
    "Massachusetts Institute of Technology (MIT)": 39,
    "Stanford University": 1,
    "Carnegie Mellon University": 40,
    "University of California, Berkeley": 3,
    "University of Oxford": 1092,
    "ETH Zurich": 288,
    "Harvard University": 38,
    "National University of Singapore (NUS)": 72,
    "Tsinghua University": 168,
    "Nanyang Technological University (NTU)": 170,
    "Princeton University": 6,
    "University of California, Los Angeles (UCLA)": 692,
    "University of Toronto": 8,
    "Cornell University": 225,
    "Peking University": 159,
    "University of Cambridge": 978,
    "Imperial College London": 1043,
    "University of Washington": 15,
    "Shanghai Jiao Tong University": 238,
    "University College London (UCL)": 384,
    "University of Edinburgh": 14,
    "Columbia University": 33,
    "New York University (NYU)": 483,
    "Georgia Institute of Technology (Georgia Tech)": 12,
    "Swiss Federal Institute of Technology Lausanne (EPFL)": 16,
    "University of Texas at Austin": 86,
    "Chinese University of Hong Kong (CUHK)": 48,
    "University of Michigan-Ann Arbor": 2,
    "Hong Kong University of Science and Technology": 31,
    "Zhejiang University": 2027,
    "Technical University of Munich": 74,
    "University of Illinois at Urbana-Champaign": 17,
    "University of Waterloo": 2444,
    "California Institute of Technology (Caltech)": 11,
    "University of British Columbia": 4,
    "University of Montreal": 1458,
    "University of California, San Diego (UCSD)": 49,
    "University of Pennsylvania": 5,
    "University of Technology Sydney": 813,
    "Korea Advanced Institute of Science and Technology (KAIST)": 399,
    "University of Science and Technology of China": 930,
    "University of Sydney": 977,
    "Yale University": 99,
    "University of Maryland, College Park": 22,
    "University of Tokyo": 69,
    "Paris Sciences et Lettres (PSL University)": 888,
    "Australian National University": 292,
    "University of Hong Kong": 405,
    "University of Wisconsin–Madison": 56,
    "University of North Carolina at Chapel Hill": 70,
    "University of Melbourne": 24,
    "Johns Hopkins University": 9,
    "Seoul National University": 327,
    "University of Chicago": 119,
    "University of New South Wales (UNSW Sydney)": 233,
    "City University of Hong Kong": 1016,
    "McGill University": 268,
    "Hong Kong Polytechnic University": 663,
    "KU Leuven": 632,
    "Sorbonne University": 355,
    "Fudan University": 322,
    "Paris-Saclay University": 794,
    "Kyoto University": 266,
    "Northwestern University": 62,
    "University of Warwick": 187,
    "Brown University": 29,
    "University of Paris": 1248,
    "KTH Royal Institute of Technology": 976,
    "Duke University": 7,
    "University of Manchester": 227,
}