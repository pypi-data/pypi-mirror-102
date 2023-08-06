====================
FEMAP neutral Parser
====================


FEMAP neutral file parser


* Free software: MIT license


Features and limitations
------------------------

Parse and render FEMAP neutral files. For now, three blocks are interpreted:

* Block 100 "Neutral File Header"
* Block 450 "Output Sets"
* Block 451 "Output Data Vectors"

Additionally, MYSTRAN outputs (which makes use of different titles than FEMAP)
are harmonized: access to total translation is done using the same title as
FEMAP ("Total Translation" *vs* "RSS translations").

Basic example
-------------

        >>> from femap_neutral_parser import Parser
        >>> neutral = Parser("fea.NEU")
        >>> arr = neutral.output_vectors["Total Translation"][2]["record"]
        >>> type(arr)
        numpy.ndarray
        >>> arr
        array([(   1, 0.        ), (   2, 0.        ), (   3, 0.00923191), ...,
               (1363, 0.00986211), (1364, 0.1818963 ), (1365, 0.2173212 )],
              dtype=[('nodeID', '<i8'), ('disp', '<f8')])
        >>> import pandas as pd
        >>> pd.DataFrame(arr).set_index("nodeID")
                    disp
        nodeID          
        1       0.000000
        2       0.204539
        3       0.000000
        4       0.014683
        5       0.000092
        6       0.627640
        7       2.578386
        8       0.102510
        9       2.578363
        10      1.916094
        11      1.100510
        12      2.389742

Requirements
------------

Beside Python>=3.8, only `numpy` is required. `numpy` arrays are released as
<https://numpy.org/doc/stable/user/basics.rec.html>`_, which makes conversions
to Pandas a breeze.

Testing
-------

For testing, making docs or coding, all the dev requirements are provided in `requirements_dev.txt`. 

From a blank virtual environment, clone this repo:

        git clone https://framagit.org/numenic/femap_neutral_parser.git


Create a Python virtual environment:
        python3 -m venv fnp

Activate this environment:
        source fnp/bin/activate

Install requirements:
        cd femap_neutral_parser
        pip install -r requirements.txt  # install numpy
        pip install -r requirements_dev.txt
        pip install -e .  # install femap-neutral-parser in new venv

Now testing:
        make test  # or make coverage

Building docs:
        make docs


        
