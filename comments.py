paths = {
    "node1": {
        "node2": [
            [],
            [],
            []
        ],
        "node3": [
            [],
            [],
            []
        ]
    },

    "node2": {
        "node1": [
            [],
            [],
            []
        ],
        "node3": [
            [],
            [],
            []
        ]
    }
}

routing_scheme = {
    ("node1", "node2"): {
        "paths": [["node1", "node3", "node2"], [], []],
        "allocations": ["path1_allocation", "path2_allocation", "path3_allocation", [], []],
    }
}





{
    'Palo Alto':
        {'Los Angeles': [['Palo Alto', 'Los Angeles'], ['Palo Alto', 'Vienna', 'Atlanta', 'Los Angeles']],
         'Denver': [['Palo Alto', 'Denver'], ['Palo Alto', 'Vienna', 'Chicago', 'Denver']],
         'Chicago': [['Palo Alto', 'Denver', 'Chicago'], ['Palo Alto', 'Vienna', 'Chicago']],
         'Vienna': [['Palo Alto', 'Vienna'], ['Palo Alto', 'Los Angeles', 'Atlanta', 'Vienna']],
         'Atlanta': [['Palo Alto', 'Los Angeles', 'Atlanta'], ['Palo Alto', 'Vienna', 'Atlanta']]},

    'Los Angeles':
        {'Palo Alto': [['Los Angeles', 'Palo Alto'], ['Los Angeles', 'Atlanta', 'Vienna', 'Palo Alto']],
        'Denver': [['Los Angeles', 'Palo Alto', 'Denver'], ['Los Angeles', 'Atlanta', 'Vienna', 'Palo Alto', 'Denver']],
        'Chicago': [['Los Angeles', 'Palo Alto', 'Denver', 'Chicago'], ['Los Angeles', 'Atlanta', 'Vienna', 'Chicago']],
        'Vienna': [['Los Angeles', 'Palo Alto', 'Vienna'], ['Los Angeles', 'Atlanta', 'Vienna']],
        'Atlanta': [['Los Angeles', 'Atlanta'], ['Los Angeles', 'Palo Alto', 'Vienna', 'Atlanta']]},

    'Denver': {'Palo Alto': [['Denver', 'Palo Alto'], ['Denver', 'Chicago', 'Vienna', 'Palo Alto']],
           'Los Angeles': [['Denver', 'Palo Alto', 'Los Angeles'], ['Denver', 'Chicago', 'Vienna', 'Palo Alto', 'Los Angeles']],
           'Chicago': [['Denver', 'Chicago'], ['Denver', 'Palo Alto', 'Vienna', 'Chicago']],
           'Vienna': [['Denver', 'Palo Alto', 'Vienna'], ['Denver', 'Chicago', 'Vienna']],
           'Atlanta': [['Denver', 'Palo Alto', 'Los Angeles', 'Atlanta'], ['Denver', 'Chicago', 'Vienna', 'Atlanta']]},

    'Chicago': {'Palo Alto': [['Chicago', 'Denver', 'Palo Alto'], ['Chicago', 'Vienna', 'Palo Alto']],
                'Los Angeles': [['Chicago', 'Denver', 'Palo Alto', 'Los Angeles'], ['Chicago', 'Vienna', 'Palo Alto', 'Los Angeles']],
                'Denver': [['Chicago', 'Denver'], ['Chicago', 'Vienna', 'Palo Alto', 'Denver']],
                'Vienna': [['Chicago', 'Vienna'], ['Chicago', 'Denver', 'Palo Alto', 'Vienna']],
                'Atlanta': [['Chicago', 'Vienna', 'Atlanta'], ['Chicago', 'Denver', 'Palo Alto', 'Los Angeles', 'Atlanta']]},
    'Vienna': {'Palo Alto': [['Vienna', 'Palo Alto'], ['Vienna', 'Chicago', 'Denver', 'Palo Alto']],
               'Los Angeles': [['Vienna', 'Palo Alto', 'Los Angeles'], ['Vienna', 'Atlanta', 'Los Angeles']],
               'Denver': [['Vienna', 'Palo Alto', 'Denver'], ['Vienna', 'Chicago', 'Denver']],
               'Chicago': [['Vienna', 'Chicago'], ['Vienna', 'Palo Alto', 'Denver', 'Chicago']],
               'Atlanta': [['Vienna', 'Atlanta'], ['Vienna', 'Palo Alto', 'Los Angeles', 'Atlanta']]},
    'Atlanta': {'Palo Alto': [['Atlanta', 'Los Angeles', 'Palo Alto'], ['Atlanta', 'Vienna', 'Palo Alto']],
                'Los Angeles': [['Atlanta', 'Los Angeles'], ['Atlanta', 'Vienna', 'Palo Alto', 'Los Angeles']],
                'Denver': [['Atlanta', 'Los Angeles', 'Palo Alto', 'Denver'], ['Atlanta', 'Vienna', 'Palo Alto', 'Denver']],
                'Chicago': [['Atlanta', 'Vienna', 'Chicago'], ['Atlanta', 'Los Angeles', 'Palo Alto', 'Denver', 'Chicago']],
                'Vienna': [['Atlanta', 'Vienna'], ['Atlanta', 'Los Angeles', 'Palo Alto', 'Vienna']]}}
